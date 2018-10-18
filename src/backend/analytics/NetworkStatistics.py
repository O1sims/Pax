import os

import numpy as np
import pandas as pd
import pymongo as pm
import networkx as nx
import random as random
import plotly.plotly as py
import datetime as datetime

import numpy.random as nprnd

from random import randint
from plotly.graph_objs import *


_author_ = 'Owen Sims (sims.owen@gmail.com)'


"""
A set of functions that generate, analyse, and visualise graph-based data.
In particular we develop a new centrality measure `contagion centrality`
that is used as an equilibrium heuristic in the game theory component.
"""


class DegreeCentrality:
    def __init__(self, network_data):
        """
        Initialise the class by assigning the network data to some object.
        """
        self.node_list_df = pd.DataFrame(network_data['nodes'], columns = ['id'])
        self.arc_list_df = pd.DataFrame(network_data['edges'], columns = ['source', 'target'])
        self.node_population = len(self.node_list_df)


    def degree_centrality(self):
        degree_cent = []

        for i in self.node_list_df['id']:
            normalized_centrality = 100 * float(len(self.arc_list_df[(self.arc_list_df['source'] == i) | (self.arc_list_df['target'] == i)]))/float(self.node_population)
            degree_cent.append("{0:.2f}".format(round(normalized_centrality, 2)))

        return degree_cent


    def in_degree_centrality(self):
        in_degree_cent = []

        for i in self.node_list_df['id']:
            nromalized_centrality = 100 * float(len(self.arc_list_df[self.arc_list_df['target'] == i]))/float(self.node_population)
            degree_cent.append("{0:.2f}".format(round(normalized_centrality, 2)))

        return in_degree_cent


    def out_degree_centrality(self):
        out_degree_cent = []

        for i in self.node_list_df['id']:
            nromalized_centrality = 100 * float(len(self.arc_list_df[self.arc_list_df['source'] == i]))/float(self.node_population)
            degree_cent.append("{0:.2f}".format(round(normalized_centrality, 2)))

        return out_degree_cent



class ContagionCentrality:
    def __init__(self, network_data):
        """
        Initialise the class by assigning the network data to some object.
        """
        self.node_list_df = pd.DataFrame(network_data['nodes'], columns = ['id', 'name', 'type', 'likelihood', 'sensitivity'])
        self.arc_list_df = pd.DataFrame(network_data['edges'], columns = ['id', 'source', 'target', 'type'])


    def get_direct_successors(self, arc_list_df):
        """
        A function that creates a dictionary of direct successors for each node.

        :param arc_list_df: A data-frame containing a sources, targets, and weights
                            of relationship.
        """
        # Instantiate the dictionary for direct successors
        direct_successors = {}

        for i in arc_list_df['source'].unique():
            # Extract the subgraph containing all direct successors of node i
            subgraph = arc_list_df[arc_list_df['source'] == i]

            # Parse direct successors from the subgraph
            successors = subgraph['target'].tolist()
            direct_successor_set = { i : successors }

            # Append to the `direct_successors` dictionary
            direct_successors.update(direct_successor_set)

        return direct_successors


    def get_direct_predecessors(self, arc_list_df):
        """
        A function that creates a dictionary of direct predecessors for each node.

        :param arc_list_df: A data-frame containing a sources, targets, and weights
                            of relationship.
        """
        # Instantiate the dictionary for direct predecessors
        direct_predecessors = {}

        for i in arc_list_df['target'].unique():
            # Extract the subgraph containing all direct predecessors of node i
            subgraph = arc_list_df[arc_list_df['target'] == i]

            # Parse direct predecessors from the subgraph
            predecessors = subgraph['source'].tolist()
            direct_predecessor_set = { i: predecessors }

            # Append to the `direct_predecessors` dictionary
            direct_predecessors.update(direct_predecessor_set)

        return direct_predecessors


    def contagion_centrality(self):
        """
        A function that measures the `contagion centrality` of each node in the
        weighted graph.

        :param node_list_df: A data-frame containing all nodes within a network and
                             the thresholds of each node.
        :param arc_list_df: A data-frame containing sources, targets, and weights
                            of relationship.
        """
        # Instantiate a list to record each nodes contagion centrality
        contagion_cent = []

        # Get all direct successors
        direct_successors = self.get_direct_successors(self.arc_list_df)

        # Repeat the contagion process for each individual node
        for i in self.node_list_df['id']:
            # Remove node i from the network
            impact_network = self.arc_list_df[(self.arc_list_df['source'] != i) & (self.arc_list_df['target'] != i)]

            total_successors = len(impact_network['target'].unique())

            nodes_to_remove = []

            # Check whether i's direct successors will fail
            if i in direct_successors:
                for j in direct_successors[i]:
                    # New incoming weight
                    w_j_impact_network = impact_network[impact_network['target'] == j]['weight'].sum()

                    threshold_j = self.node_list_df[self.node_list_df['id'] == j]['threshold'].tolist()[0]

                    # Some qualifier regarding incoming weight and threshold
                    if threshold_j > w_j_impact_network:
                        nodes_to_remove.append(j)

                while len(nodes_to_remove) > 0:
                    # Recursively remove nodes that have dropped below their threshold
                    for j in nodes_to_remove:
                        impact_network = impact_network[(impact_network['source'] != j) & (impact_network['target'] != j)]

                    subequent_removals = []
                    for j in nodes_to_remove:
                        if j in direct_successors:
                            for k in direct_successors[j]:
                                if k in impact_network['target'].unique():
                                    # New incoming weight
                                    w_k_impact_network = impact_network[impact_network['target'] == k]['weight'].sum()

                                    threshold_k = self.node_list_df[self.node_list_df['id'] == k]['threshold'].tolist()[0]

                                    # Some qualifier regarding incoming weight and threshold
                                    if threshold_k > w_k_impact_network:
                                        subequent_removals.append(k)

                    # Equate nodes_to_remove and subsequent_removals
                    nodes_to_remove = subequent_removals

                contagion_score = total_successors - len(impact_network['target'].unique())

                normalized_contagion_score = float(contagion_score) / float(len(self.node_list_df['id'].unique()))

                # Record normalized contagion centrality
                contagion_cent.append(max(normalized_contagion_score, float(0.0001)))

            else:
                contagion_cent.append(float(0.0001))

        return contagion_cent



class NetworkStatistics:
    """
    A class that analyses the topology of a network. Can generate some risk score
    from the topology and vulnerabilities present.
    """
    def __init__(self, network_data, use_asset_graph = False):
        """
        Initialise the class by assigning the network data to some object.
        """
        # Get nodes and node properties
        self.node_list_df = pd.DataFrame(network_data['nodes'], columns = ['id', 'name', 'type', 'likelihood', 'sensitivity'])
        self.node_list_df['threshold'] = [0.5 for i in range(len(self.node_list_df))]

        # Get edges (arcs) and weights
        self.arc_list_df = pd.DataFrame(network_data['edges'], columns = ['id', 'source', 'target', 'type'])
        self.arc_list_df = self.generate_arc_weights(arc_list_df = self.arc_list_df)

        # Get a graph of the assets only
        if use_asset_graph == True:
            asset_graph = self.get_asset_graph(node_list_df = self.node_list_df, arc_list_df = self.arc_list_df)
            self.node_list_df = asset_graph[0]
            self.arc_list_df = asset_graph[1]


    def get_asset_graph(self, node_list_df, arc_list_df):
        """
        A function that ingests the entire network graph and takes the subgraph
        containing all `Software` and `Devices`.
        """
        asset_list_df = node_list_df[(node_list_df['type'] == 'Software') | (node_list_df['type'] == 'Device')]
        asset_arc_list_df = arc_list_df[(arc_list_df['source'].isin(asset_list_df['id'])) & (arc_list_df['target'].isin(asset_list_df['id']))]

        asset_graph = [asset_list_df, asset_arc_list_df]

        return asset_graph


    def generate_arc_weights(self, arc_list_df):
        """
        Generate weighted arcs.
        """
        weights = {}
        for i in arc_list_df['source'].unique():
            weights.update({ i : float(1) / float(len(arc_list_df[arc_list_df.source == i])) })

        arc_weight = []
        for i in range(len(arc_list_df)):
            arc_weight.append(weights[arc_list_df['source'][i]])

        arc_list_df['weight'] = arc_weight

        return arc_list_df


    def ra_network_data(mongo_host = os.environ.get('DB_HOSTNAME'), mongo_port = int(os.environ.get('DB_PORT')), mongo_database = "",
                        mongo_collecton = "", path_to_JSON = "", from_JSON = True):
        """
        A function used to collect network data from Mongo sent from Risk Aware and
        extract the most important elements.

        :param mongo_host: String providing the name of the Host that Mongo sits on.
        :param mongo_port: String or integer containing the post number that Mongo sits on.
        :param mongo_database: String indicating the Mongo database name that the data is contained in.
        :param mongo_collecton: String indicating the Mongo collection name that the data is contained in.
        :param path_to_JSON: String indicating the directory path to the relevant JSON data.
            Example: path_to_JSON = '/home/owen/Code/Pax/analytics/exampledata/RA-sample-scenario.json'
        :param from_JSON: `True` or `False` statement indicating whether data is being
            loaded from a JSON or not.
        """
        if from_JSON == True:
            # Load network data from JSON (used primarily for static data analysis)
            with open(path_to_JSON) as data_file:
                networkData = json.load(data_file)

        else:
            # Extract network data from Mongo (used for both static and dynamic analysis)
            mongoConnection = pm.MongoClient('mongodb://' + mongoHost + ':' + str(mongoPort) + '/')[mongo_database][mongo_collecton]
            networkData = mongoConnection.find_one()

        # Create some separation between nodes and edges/arcs
        # Return only the data that is relevant right now
        node_list_df = pd.DataFrame(networkData['nodes'], columns = ['id', 'name', 'type', 'likelihood', 'sensitivity'])
        arc_list_df = pd.DataFrame(networkData['edges'], columns = ['id', 'source', 'target', 'type'])

        sanitizers = [":", "#"]

        for i in sanitizers:
            node_list_df['id'] = [re.sub(i, "", x) for x in node_list_df['id']]
            arc_list_df['id'] = [re.sub(i, "", x) for x in arc_list_df['id']]
            arc_list_df['source'] = [re.sub(i, "", x) for x in arc_list_df['source']]
            arc_list_df['target'] = [re.sub(i, "", x) for x in arc_list_df['target']]

        node_list_df['colour'] = node_list_df['type']
        unique_types = node_list_df['type'].unique()

        # Generate a colour dictionary for all types of node
        node_colour_dict = {}
        colour_list = ['#FF8A65', '#FFB74D', '#FFD54F', '#FFF176', '#DCE775', '#AED581', '#81C784', '#4DB6AC', '#4DD0E1', '#4FC3F7', '#64B5F6']
        for i in range(len(unique_types)):
            node_colour = { unique_types[i] : colour_list[i] }
            node_colour_dict.update(node_colour)

        for i in range(len(unique_types)):
            node_list_df['colour'] = node_list_df['colour'].replace(to_replace = unique_types[i],
                                                                    value = node_colour_dict[unique_types[i]])

        return [node_list_df, arc_list_df]


    def dataframe_to_networkx(self, arc_list_df):
        """
        Convert a (weighted) edge- or arc-list into a networkx object.

        :param arc_list_df: A data-frame containing a sources, targets, and weights
                           of relationship.
        """
        G = nx.from_pandas_dataframe(df = arc_list_df,
                                     source = 'source',
                                     target = 'target',
                                     edge_attr = 'type',
                                     create_using = nx.DiGraph())

        return G


    def plot_networkx(node_list_df, arc_list_df):
        """
        Plots network using networkX package.

        :param node_list_df: A data-frame containing all nodes within a network and
                             the thresholds of each node.
        :param arc_list_df: A data-frame containing sources, targets, and weights
                            of relationship.
        """
        G = dataframe_to_networkx(arc_list_df = arc_list_df)

        graph_plot = nx.draw(G = G,
                             pos = nx.spring_layout(G),
                             node_size = 50,
                             node_color = node_list_df['colour'],
                             edge_color = '#616161',
                             figsize = (120,120),
                             linewidths = 1,
                             with_labels = False)

        return graph_plot


    def generate_synthetic_network_data(n, m):
        """
        Function that generates a dataset of nodes and arcs with weights associated.
        The result is a weighted directed network.
        Nodes are characterised by their `label` and `threshold`. Arcs are characterised
        by their `direction` and `weight`.

        :param n: Number of nodes
        :param m: Number of arcs
        """
        # Sanity check that m is below a certain threshold
        if m >= n * (n - 1):
            return "Too many arcs involved here! Make sure m < n * (n - 1)."

        # Generate node list
        node_list = []
        threshold = []

        for i in range(n):
            node_list.append(i + 1)
            threshold.append(random.uniform(0, 1))

        # Generate arc list and corresponding weights
        weights = []
        target_list = []
        source_list = []
        arc_type = []

        for i in range(m):
            source = randint(1, n)
            target = randint(1, n)
            while source == target:
                target = randint(1, n)
            source_list.append(source)
            target_list.append(target)
            weights.append(random.uniform(0, 1))
            arc_type.append("Directed")

        # Convert data lists to DataFrame
        node_list_df = pd.DataFrame({"node" : node_list,
                                     "threshold" : threshold})
        arc_list_df = pd.DataFrame({"source" : source_list,
                                    "target" : target_list,
                                    "weight" : weights,
                                    "type" : arc_type})

        # Remove any duplicated arcs
        arc_list_df = arc_list_df.drop_duplicates(['source', 'target'],
                                                  keep = 'first')

        # Return with a list of data
        return [node_list_df, arc_list_df]


    def normalise_weights(arc_list_df):
        """
        A function that normalises the weights attached to each node such that they
        possess the characteristic of being row-stochastic.

        :param arc_list_df: A data-frame containing a sources, targets, and weights
                            of relationship.
        """
        for i in arc_list_df['target'].unique():
            subgraph = arc_list_df.query('target == ' + str(i))

            if subgraph.shape[0] > 0:
                norm = round(sum(subgraph['weight']), 3)
                row_names = list(subgraph.index)

                if len(row_names) == 1:
                    l = 1
                else:
                    l = len(row_names)

                for j in range(0, l):
                    arc_list_df['weight'][row_names[j]] = round(arc_list_df.xs(row_names[j], copy = False)['weight']/norm, 3)

        return arc_list_df


    def scatter_nodes(pos, labels = None, color = None, size = 20, opacity = 1):
        """
        Function to create the node trace used for graph plotting.

        :param pos: The dict of node positions
        :param labels: A list of labels of len(pos), to be displayed when
                      hovering the mouse over the nodes
        :param color: The color for nodes. When it is set as None the Plotly
                     default color is used
        :param size: The size of the dots representing the nodes
        :param opacity: A value between [0,1] defining the node color opacity
        """
        L = len(pos)
        trace = Scatter(x = [], y = [],  mode = 'markers', marker = Marker(size = []))
        for k in range(L):
            trace['x'].append(pos[k][0])
            trace['y'].append(pos[k][1])
        attrib = dict(name = '', text = labels , hoverinfo = 'text', opacity = opacity)
        trace = dict(trace, **attrib)
        trace['marker']['size'] = size

        return trace


    def scatter_edges(G, pos, line_color = None, line_width = 1):
        """
        Function to create the edge trace used for graph plotting.

        :param G: A networkx object representing the structure of the graph;
        :param pos: The dict of node positions;
        :param line-color: The color for edges. When it is set as None the Plotly
                          default color is used;
        :param line-width: The width of the edges.
        """
        trace = Scatter(x=[], y=[], mode='lines')
        for edge in G.edges():
            trace['x'] += [pos[edge[0]][0],pos[edge[1]][0], None]
            trace['y'] += [pos[edge[0]][1],pos[edge[1]][1], None]
            trace['hoverinfo'] = 'none'
            trace['line']['width'] = line_width
            if line_color is not None:
                trace['line']['color'] = line_color

        return trace


    def make_annotations(pos, text, font_size = 14, font_color = 'rgb(25,25,25)'):
        """
        An function that creates annotations on nodes.

        :param pos: The position of nodes
        :param text: Text body used for annotations
        :param font_size: Font size given by an integer
        :param font_color: Font colour can be either in a HEX or RGB format.
        :return: An array of annotations
        """
        L = len(pos)
        if len(text) != L:
            raise ValueError('The lists pos and text must have the same len')
        annotations = Annotations()
        for k in range(L):
            annotations.append(
                Annotation(
                    text = text[k],
                    x = pos[k][0], y = pos[k][1],
                    xref = 'x1', yref = 'y1',
                    font = dict(color = font_color, size = font_size),
                    showarrow = False
                )
            )

        return annotations


    def plot_networkx_plotly(G, width = 500, height = 500):
        """
        A function that plots a networkx graph in a Plotly representation.

        :param G: A networkx network object.
        """
        pos = nx.fruchterman_reingold_layout(G)

        labels = [str(k)  for k in range(len(pos))]

        trace1 = scatter_edges(G = G,
                               pos = pos)

        trace2 = scatter_nodes(pos = pos,
                               labels = labels)

        axis = dict(showline = False,
                    zeroline = False,
                    showgrid = False,
                    showticklabels = False,
                    title = '')

        layout = Layout(title = 'Fruchterman Reingold layout',
                        font = Font(),
                        showlegend = False,
                        autosize = False,
                        width = width,
                        height = height,
                        xaxis = XAxis(axis),
                        yaxis = YAxis(axis),
                        margin = Margin(l = 40,
                                        r = 40,
                                        b = 85,
                                        t = 100,
                                        pad = 0),
                        hovermode = 'closest',
                        plot_bgcolor = '#EFECEA')


        data = Data([trace1, trace2])

        fig = Figure(data = data, layout = layout)

        fig['layout'].update(annotations = make_annotations(pos, [str(k) for k in range(len(pos))]))

        py.iplot([{"x": [1, 2, 3], "y": [3, 1, 6]}])


    def get_network_statistics(self):
        """
        A function that generates summary statistics of the network as a whole
        under analysis.

        :param arc_list_df: A data-frame containing a sources, targets, and weights
                            of relationship.

        :Note: NetworkX does not work well with directed graphs.
        """
        G = nx.from_pandas_dataframe(df = self.arc_list_df,
                                     source = 'source',
                                     target = 'target',
                                     edge_attr = 'type')

        degree = nx.degree(G)
        total_degree = sum(degree.values())
        number_of_nodes = nx.number_of_nodes(G)
        average_degree = total_degree / number_of_nodes

        edge_population = len(self.arc_list_df['id'])

        summary_statistics = {}
        summary_statistics.update({ 'number_connected_components' : nx.number_connected_components(G) })
        summary_statistics.update({ 'average_node_connectivity' : nx.average_node_connectivity(G) })
        summary_statistics.update({ 'average_clustering' : nx.average_clustering(G) })
        summary_statistics.update({ 'diameter' : 12 })
        summary_statistics.update({ 'density' : nx.density(G) })
        summary_statistics.update({ 'number_of_nodes' : number_of_nodes })
        summary_statistics.update({ 'number_of_edges' : nx.number_of_edges(G) })
        summary_statistics.update({ 'total_degree' : total_degree })
        summary_statistics.update({ 'average_degree' : average_degree })


        return summary_statistics


    def get_centrality_measures(node_list_df, arc_list_df):
        """
        A function that generates a range of centrality measures for a generated
        DiGraph from the Pandas dataframe

        :param arc_list_df: A data-frame containing a sources, targets, and weights
                            of relationship.
        """
        G = dataframe_to_networkx(arc_list_df)

        centrality_measures = {}

        # Degree-based centrality measure
        centrality_measures.update({'degree' : nx.degree_centrality(G)})
        centrality_measures.update({'in_degree' : nx.in_degree_centrality(G)})
        centrality_measures.update({'out_degree' : nx.out_degree_centrality(G)})

        # Flow-based centrality measure
        centrality_measures.update({'closeness' : nx.closeness_centrality(G)})
        centrality_measures.update({'betweenness' : nx.betweenness_centrality(G)})
        centrality_measures.update({'contagion' : contagion_centrality(node_list_df, arc_list_df)})

        return centrality_measures


    def adjacency_matrix(node_list_df, arc_list_df):
        """
        Generates an n-by-n adjacency matrix representing the tupled network.

        :param node_list_df: A data-frame containing all nodes within a network and
                             the thresholds of each node.
        :param arc_list_df: A data-frame containing sources, targets, and weights
                            of relationship.
        """
        # Generate a matrix representing the network
        n = len(node_list_df['node'].unique())
        network_matrix = [[0 for x in range(n)] for y in range(n)]

        for i in list(arc_list_df.index):
            # I can't believe how terrible Python is.
            network_matrix[arc_list_df['source'][i] - 1][arc_list_df['target'][i] - 1] = network_matrix[arc_list_df['source'][i] - 1][arc_list_df['target'][i] - 1] + 1

        network_matrix = np.asmatrix(network_matrix)

        return network_matrix


    def network_connectivity(node_list_df, arc_list_df, network_matrix = None):
        """
        Calculates the connectivity of some sparse matrix.

        :param node_list_df: A data-frame containing all nodes within a network and
                             the thresholds of each node.
        :param arc_list_df: A data-frame containing sources, targets, and weights
                            of relationship.
        """
        if network_matrix == None:
            network_matrix = adjacency_matrix(node_list_df = node_list_df,
                                              arc_list_df = arc_list_df)

        # Binarize matrix
        network_matrix = np.where(network_matrix > 0, 1, 0)

        for i in range(int(len(node_list_df['node'].unique())/2)):
            network_matrix = network_matrix + np.linalg.matrix_power(network_matrix, i)
            network_matrix = np.where(network_matrix > 0, 1, 0)

        for i in range(network_matrix.shape[0]):
            network_matrix[i, i] = 0

        connectivity = np.sum(network_matrix)

        return connectivity


    def middleman_centrality(node_list_df, arc_list_df):
        """
        A function that measures the `middleman centrality` of each nodes in the
        graph.

        :param node_list_df: A data-frame containing all nodes within a network and
                             the thresholds of each node.
        :param arc_list_df: A data-frame containing sources, targets, and weights
                            of relationship.
        """
        brokerage = {}

        original_adjacency_matrix = adjacency_matrix(node_list_df = node_list_df,
                                                    arc_list_df = arc_list_df)

        kappa = network_connectivity(node_list_df = node_list_df,
                                     arc_list_df = arc_list_df)

        adjacency_matrix = original_adjacency_matrix

        for i in range(len(original_adjacency_matrix)):
            adjacency_matrix = original_adjacency_matrix
            network_matrix[:,i] = network_matrix[i,:] = 0
            kappa_new = network_connectivity()
            brokerage.update({ i : kappa - kappa_new })

        return brokerage


    def contagion_centrality(self):
        """
        A function that measures the `contagion centrality` of each node in the
        weighted graph.

        :param node_list_df: A data-frame containing all nodes within a network and
                             the thresholds of each node.
        :param arc_list_df: A data-frame containing sources, targets, and weights
                            of relationship.
        """
        # Instantiate a list to record each nodes contagion centrality
        contagion_cent = []

        # Get all direct successors
        direct_successors = self.get_direct_successors(self.arc_list_df)

        # Repeat the contagion process for each individual node
        for i in self.node_list_df['id']:
            # Remove node i from the network
            impact_network = self.arc_list_df[(self.arc_list_df['source'] != i) & (self.arc_list_df['target'] != i)]

            total_successors = len(impact_network['target'].unique())

            nodes_to_remove = []

            # Check whether i's direct successors will fail
            if i in direct_successors:
                for j in direct_successors[i]:
                    # New incoming weight
                    w_j_impact_network = impact_network[impact_network['target'] == j]['weight'].sum()

                    threshold_j = self.node_list_df[self.node_list_df['id'] == j]['threshold'].tolist()[0]

                    # Some qualifier regarding incoming weight and threshold
                    if threshold_j > w_j_impact_network:
                        nodes_to_remove.append(j)

                while len(nodes_to_remove) > 0:
                    # Recursively remove nodes that have dropped below their threshold
                    for j in nodes_to_remove:
                        impact_network = impact_network[(impact_network['source'] != j) & (impact_network['target'] != j)]

                    subequent_removals = []
                    for j in nodes_to_remove:
                        if j in direct_successors:
                            for k in direct_successors[j]:
                                if k in impact_network['target'].unique():
                                    # New incoming weight
                                    w_k_impact_network = impact_network[impact_network['target'] == k]['weight'].sum()

                                    threshold_k = self.node_list_df[self.node_list_df['id'] == k]['threshold'].tolist()[0]

                                    # Some qualifier regarding incoming weight and threshold
                                    if threshold_k > w_k_impact_network:
                                        subequent_removals.append(k)

                    # Equate nodes_to_remove and subsequent_removals
                    nodes_to_remove = subequent_removals

                contagion_score = total_successors - len(impact_network['target'].unique())

                normalized_contagion_score = float(contagion_score) / float(len(self.node_list_df['id'].unique()))

                # Record normalized contagion centrality
                contagion_cent.append(max(normalized_contagion_score, float(0.0001)))

            else:
                contagion_cent.append(float(0.0001))

        return contagion_cent

    def what_attacker_type(self, attacker_types):
        """
        Probability distribution over set of attacker types.
        """
        number_of_attacker_types = len(attacker_types)
        self.attacker_type = random.randomint(1, 0, len(attacker_types))

        return self.attacker_type



class TopologicalRisk:
    def __init__(self, network_data = list(), asset_data = list(), from_mongo = False):
        if from_mongo == False and network_data != list():
            self.node_list_df = pd.DataFrame(network_data['nodes'], columns = ['id', 'name', 'type', 'likelihood', 'sensitivity'])
            self.arc_list_df = pd.DataFrame(network_data['edges'], columns = ['id', 'source', 'target', 'type'])

        elif asset_data != list():
            self.node_list_df = pd.DataFrame(asset_data['assets'])

        elif from_mongo == True:
            mongo_client = pm.MongoClient(host = os.environ.get('DB_HOSTNAME'), port = int(os.environ.get('DB_PORT')))
            node_data_collection = mongo_client[os.environ.get('DB_NAME')]['node_data']
            node_data_cursor = node_data_collection.find({})
            self.node_list_df = pd.DataFrame(list(node_data_cursor))

            edge_data_collection = mongo_client[os.environ.get('DB_NAME')]['edge_data']
            edge_data_cursor = edge_data_collection.find({})
            self.arc_list_df = pd.DataFrame(list(edge_data_cursor))


    def asset_vulnerability_risk(self):
        if 'quantumState' in list(self.node_list_df) or 'exists' in list(self.node_list_df):
            remove_nodes = []
            if 'quantumState' in list(self.node_list_df):
                remove_nodes.extend(list(self.node_list_df[self.node_list_df['quantumState'] == 1]['id']))
            if 'exists' in list(self.node_list_df):
                remove_nodes.extend(list(self.node_list_df[self.node_list_df['exists'] == 0]['id']))

            for i in range(self.arc_list_df.shape[0]):
                if self.arc_list_df['source'][i] in remove_nodes or self.arc_list_df['target'][i] in remove_nodes:
                    self.arc_list_df = self.arc_list_df.drop([i])

            for i in range(self.node_list_df.shape[0]):
                if self.node_list_df['id'][i] in remove_nodes:
                    self.node_list_df = self.node_list_df.drop([i])

        G = nx.from_pandas_dataframe(df = self.arc_list_df, source = 'source', target = 'target')

        asset_nodes = self.node_list_df[(self.node_list_df['type'] == 'Software') | (self.node_list_df['type'] == 'Device')]
        vulnerability_nodes = self.node_list_df[self.node_list_df['type'] == 'SoftwareVulnerability']

        normalizer = len(vulnerability_nodes['id'])

        asset_vulnerability_closeness = {}
        for i in asset_nodes['id']:
            path_length = []
            for j in vulnerability_nodes['id']:
                path_length.append(len(nx.shortest_path(G, source = i, target = j)))

            asset_vulnerability_closeness.update({
            i : (((min(path_length)-1)**-1)**0.5) * 100
            })

        return asset_vulnerability_closeness


    def generate_node_risk_scores(self):
        """
        Generate risk scores and attach them to `Devices` and `Software`.
        """
        risk_scores = []

        for i in range(len(self.node_list_df)):
            if (self.node_list_df['type'][i] == "Device") or (self.node_list_df['type'][i] == "Software"):
                risk_scores.append(randint(1,100))
            else:
                risk_scores.append(0)

        return risk_scores


    def get_risk_labels(self, risk_scores):
        """
        Generate some risk labels from the risk scores.
        """
        risk_labels = []

        for i in range(len(risk_scores)):
            if risk_scores[i] == 0:
                risk_labels.append("Not applicable")
            elif risk_scores[i] >= 80:
                risk_labels.append("Critical")
            elif risk_scores[i] >= 60:
                risk_labels.append("High")
            elif risk_scores[i] >= 40:
                risk_labels.append("Medium")
            else:
                risk_labels.append("Low")

        return risk_labels


    def generate_historical_risk_scores(self, time_periods):
        """
        Generate risk scores and attach them to `Devices` and `Software`.
        """
        node_risk_scores = []

        asset_vulnerability_risk = self.asset_vulnerability_risk()

        for i in range(len(self.node_list_df)):
            historical_risk_scores = []
            if (self.node_list_df['type'][i] == "Device") or (self.node_list_df['type'][i] == "Software"):
                for j in range(time_periods):
                    if j == 0:
                        risk_score = asset_vulnerability_risk[self.node_list_df['id'][i]]
                    else:
                        risk_score = nprnd.randint(100, size = 1)[0]

                    historical_risk_scores.append({
                    'timestamp' : int(datetime.date.today().strftime("%s")) - (60 * 60 * 24 * (j)),
                    'risk_score' : risk_score
                    })

            else:
                for j in range(time_periods):
                    historical_risk_scores.append({
                    'time' : int(datetime.date.today().strftime("%s")) - (60 * 60 * 24 * (j)),
                    'risk_score' : 0
                    })

            node_risk_scores.append(historical_risk_scores)

        return node_risk_scores


    def generate_historical_asset_risk_scores(self, time_periods):
        """
        Generate risk scores and attach them to all assets.
        """
        asset_risk_scores = []

        for i in range(len(self.node_list_df)):
            historical_risk_scores = []
            for j in range(time_periods):
                risk_score = nprnd.randint(100, size = 1)[0]

                historical_risk_scores.append({
                'timestamp' : int(datetime.date.today().strftime("%s")) - (60 * 60 * 24 * (j)),
                'risk_score' : risk_score
                })

            asset_risk_scores.append(historical_risk_scores)

        return asset_risk_scores



class AssetNetworks:
    def __init__(self, network_data):
        self.node_list_df = pd.DataFrame(network_data['nodes'], columns = ['name', 'type'])


    def get_asset_networks(self):
        asset_networks = self.node_list_df[self.node_list_df['type'] == 'Network']['name'].values

        return asset_networks



class AssetImpact:
    def __init__(self, risk_scores):
        self.risk_scores = risk_scores


    def get_asset_impact(self):
        currentImpact = []
        for i in range(len(self.risk_scores)):
            if self.risk_scores[i][0]['risk_score'] == 0:
                impact = {
                'consequence': 0,
                'likelihood': 0
                }
            else:
                impact = {
                'consequence': int(round(float(self.risk_scores[i][0]['risk_score']) / float(10), 0)),
                'likelihood': float(random.randint(1,9)) / float(10)
                }

            currentImpact.append(impact)

        return currentImpact


class GetSubnets:
    def __init__(self, network_data):
        self.node_list_df = pd.DataFrame(network_data['nodes'], columns = ['id', 'name', 'type'])
        self.arc_list_df = pd.DataFrame(network_data['edges'], columns = ['source', 'target'])

    def get_subnet_data(self):
        devices = self.node_list_df[self.node_list_df['type'] == 'Device']['id']
        networks = self.node_list_df[self.node_list_df['type'] == 'Network']['id']

        subnets = {}
        for i in devices.values:
            subset = self.arc_list_df[self.arc_list_df['target'] == i]['source']
            for j in networks.values:
                if j in subset.values:
                    subnet = self.node_list_df[self.node_list_df['id'] == j]['name']
                    subnets.update({i : subnet.values[0]})

        return subnets
