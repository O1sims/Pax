System.register(["@angular/core", "@angular/http", "ng2-nvd3", "angular2-modal", "angular2-modal/plugins/bootstrap", "./courses.service"], function (exports_1, context_1) {
    "use strict";
    var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __metadata = (this && this.__metadata) || function (k, v) {
        if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
    };
    var __moduleName = context_1 && context_1.id;
    var core_1, http_1, ng2_nvd3_1, angular2_modal_1, bootstrap_1, courses_service_1, ActionWindowData, ActionWindow;
    return {
        setters: [
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (http_1_1) {
                http_1 = http_1_1;
            },
            function (ng2_nvd3_1_1) {
                ng2_nvd3_1 = ng2_nvd3_1_1;
            },
            function (angular2_modal_1_1) {
                angular2_modal_1 = angular2_modal_1_1;
            },
            function (bootstrap_1_1) {
                bootstrap_1 = bootstrap_1_1;
            },
            function (courses_service_1_1) {
                courses_service_1 = courses_service_1_1;
            }
        ],
        execute: function () {
            ActionWindowData = class ActionWindowData extends bootstrap_1.BSModalContext {
                constructor(systemId, actionData, objectiveData, actorData, parentTasks, riskScore) {
                    super();
                    this.systemId = systemId;
                    this.actionData = actionData;
                    this.objectiveData = objectiveData;
                    this.actorData = actorData;
                    this.parentTasks = parentTasks;
                    this.riskScore = riskScore;
                }
            };
            exports_1("ActionWindowData", ActionWindowData);
            ;
            ActionWindow = class ActionWindow {
                constructor(dialog, actionModalService) {
                    this.dialog = dialog;
                    this.actionModalService = actionModalService;
                    this.timeTaken = {
                        'expected': '0 minutes',
                        'stdev': '0 minutes'
                    };
                    this.probabilityOfSuccess = {
                        'score': 0,
                        'label': 'Very low'
                    };
                    this.taskView = 1;
                    this.actionNavView = 0;
                    this.dependencyView = 0;
                    this.actorData = {};
                    this.objectiveData = {};
                    this.actionList = [];
                    dialog.context.size = 'lg';
                    this.systemId = dialog.context['systemId'];
                    this.actionData = dialog.context['actionData'];
                    this.parentTasks = dialog.context['parentTasks'];
                    this.riskScore = dialog.context['riskScore'];
                    this.actorData = dialog.context['actorData'];
                    this.objectiveData = dialog.context['objectiveData'];
                    this.taskId = this.actionData['taskId'];
                }
                ;
                taskInformationView() {
                    this.dependencyView = 0;
                    this.actionNavView = 0;
                    this.taskView = 1;
                    setTimeout(() => {
                        this.generateHeatMap({
                            'likelihood': 9,
                            'riskScore': Math.round(this.riskScore / 10)
                        }, {
                            'likelihood': Math.round(this.probabilityOfSuccess['score'] / 10),
                            'riskScore': Math.round(this.newRiskScore / 10)
                        });
                    }, 1);
                }
                ;
                actionsView() {
                    this.actionNavView = 1;
                    this.dependencyView = 0;
                    this.taskView = 0;
                    this.actionModalService.getTaskActions('hostile', this.actionData['effect'], this.objectiveData['assetType']).subscribe(actions => {
                        this.actionList = actions[0]['actions'];
                    });
                }
                ;
                dependencyTreeView() {
                    this.dependencyView = 1;
                    this.actionNavView = 0;
                    this.taskView = 0;
                    setTimeout(() => {
                        this.generateDependencyGraph(this.allTasks);
                    }, 1);
                }
                ;
                prepareTasks(taskData, parentTaskData) {
                    var allTasks = [];
                    var allRawTasks = [taskData].concat(parentTaskData);
                    for (let i = 0; i < allRawTasks.length; i++) {
                        var task = {
                            'taskId': allRawTasks[i]['name'],
                            'objective': allRawTasks[i]['objective']['entityId'],
                            'effect': allRawTasks[i]['effect'],
                            'actor': allRawTasks[i]['assignee']['entityId'],
                            'timeFrame': allRawTasks[i]['timeFrame'],
                            'dependencies': allRawTasks[i]['dependencies']
                        };
                        allTasks.push(task);
                    }
                    ;
                    return allTasks;
                }
                ;
                ngOnInit() {
                    this.heatmapSpinner = 1;
                    this.allTasks = this.prepareTasks(this.actionData, this.parentTasks);
                    this.actionModalService.postEffects(this.systemId, this.allTasks)
                        .subscribe(riskData => {
                        var objectiveId = this.actionData['objective']['entityId'];
                        this.newRiskScore = riskData['assetRisk'][objectiveId]['risks'][0]['riskScore'];
                        this.probabilityOfSuccess['score'] = 100 - riskData['assetRisk'][objectiveId]['risks'][0]['likelihoodScore'];
                        ;
                        this.probabilityOfSuccess['label'] = this.probabilityLabel(this.probabilityOfSuccess['score']);
                        this.generateHeatMap({
                            'likelihood': 9,
                            'riskScore': Math.round(this.riskScore / 10)
                        }, {
                            'likelihood': Math.round(this.probabilityOfSuccess['score'] / 10),
                            'riskScore': Math.round(this.newRiskScore / 10)
                        });
                    });
                }
                ;
                probabilityLabel(likelihoodScore) {
                    if (likelihoodScore >= 80) {
                        return 'Very high';
                    }
                    else if (likelihoodScore >= 60) {
                        return 'High';
                    }
                    else if (likelihoodScore >= 40) {
                        return 'Medium';
                    }
                    else if (likelihoodScore >= 20) {
                        return 'Low';
                    }
                    else {
                        return 'Very low';
                    }
                    ;
                }
                ;
                findDirectChildren(taskId, taskData) {
                    var taskChildren = [];
                    for (let i = 0; i < taskData.length; i++) {
                        if (taskData[i]['taskId'] == taskId) {
                            for (let j = 0; j < taskData.length; j++) {
                                if (taskData[j]['dependencies'].includes(taskId)) {
                                    taskChildren.push(taskData[j]['taskId']);
                                }
                                ;
                            }
                            ;
                        }
                        ;
                    }
                    ;
                    return taskChildren;
                }
                ;
                findAllChildren(taskId, taskData) {
                    var childTasks = [];
                    var allChildren = [taskId];
                    for (let j = 0; j < taskData.length; j++) {
                        var toAdd = [];
                        for (let i = 0; i < taskData.length; i++) {
                            var dependencies = taskData[i]['dependencies'];
                            if (dependencies.length > 0 &&
                                !dependencies.some(val => allChildren.indexOf(val) === -1)) {
                                toAdd.push(taskData[i]['taskId']);
                            }
                            ;
                        }
                        ;
                        if (toAdd.length > 0) {
                            allChildren = allChildren.concat(toAdd.filter(function (item) {
                                return allChildren.indexOf(item) < 0;
                            }));
                        }
                        ;
                        ;
                    }
                    ;
                    allChildren = allChildren.filter(e => e !== taskId);
                    for (let i = 0; i < allChildren.length; i++) {
                        for (let j = 0; j < taskData.length; j++) {
                            if (taskData[j]['taskId'] == allChildren[i]) {
                                childTasks.push(taskData[j]);
                            }
                            ;
                        }
                        ;
                    }
                    ;
                    return childTasks;
                }
                ;
                findAllParents(initialParent, taskData) {
                    var parentTasks = [];
                    var allParents = [initialParent];
                    for (let j = 0; j < taskData.length; j++) {
                        for (let i = 0; i < taskData.length; i++) {
                            if (allParents.includes(taskData[i]['taskId'])) {
                                if (taskData[i]['dependencies'].length > 0) {
                                    allParents.push(taskData[i]['dependencies'][0]);
                                }
                                ;
                                break;
                            }
                            ;
                        }
                        ;
                    }
                    ;
                    var allParents = allParents.filter((v, i, a) => a.indexOf(v) === i);
                    for (let i = 0; i < allParents.length; i++) {
                        for (let j = 0; j < taskData.length; j++) {
                            if (taskData[j]['taskId'] == allParents[i]) {
                                parentTasks.push(taskData[j]);
                            }
                            ;
                        }
                        ;
                    }
                    ;
                    return parentTasks;
                }
                ;
                findParent(taskId, taskData, rootNodeName) {
                    for (let i = 0; i < taskData.length; i++) {
                        if (taskData[i]['taskId'] == taskId) {
                            if (taskData[i]['dependencies'].length == 0) {
                                var dependencyName = rootNodeName;
                            }
                            else {
                                var dependencyName = taskData[i]['dependencies'][0];
                            }
                            ;
                            return dependencyName;
                        }
                        ;
                    }
                    ;
                }
                ;
                getChildren(directChildren, taskDetails) {
                    var children = [];
                    for (let i = 0; i < directChildren.length; i++) {
                        children.push(taskDetails[directChildren[i]]);
                    }
                    ;
                    return children;
                }
                ;
                getUnitName(unitId, unitData) {
                    for (let i = 0; i < unitData.length; i++) {
                        if (unitData[i]['id'] == unitId) {
                            return unitData[i]['name'];
                        }
                        ;
                    }
                    ;
                }
                ;
                findTaskDetails(taskId, taskData) {
                    for (let i = 0; i < taskData.length; i++) {
                        if (taskData[i]['taskId'] == taskId) {
                            return {
                                'objective': taskData[i]['objective'],
                                'unit': taskData[i]['unit'],
                                'effect': taskData[i]['effect']
                            };
                        }
                        ;
                    }
                    ;
                }
                ;
                convertTaskData(taskData, rootNodeName) {
                    var layer = [];
                    var taskDetails = {};
                    var rootChildren = [];
                    for (let i = 0; i < taskData.length; i++) {
                        if (taskData[i]['dependencies'].length == 0) {
                            layer.push(taskData[i]['taskId']);
                        }
                        ;
                    }
                    ;
                    var graphLayers = {
                        0: layer
                    };
                    for (let i = 0; i < Object.keys(graphLayers).length; i++) {
                        layer = [];
                        for (let j = 0; j < taskData.length; j++) {
                            if (graphLayers[i].includes(taskData[j]['dependencies'][0])) {
                                layer.push(taskData[j]['taskId']);
                            }
                            ;
                        }
                        ;
                        if (layer.length > 0) {
                            var k = i + 1;
                            graphLayers[k] = layer;
                        }
                        ;
                    }
                    ;
                    for (let i = Object.keys(graphLayers).length - 1; i >= 0; i--) {
                        for (let j = 0; j < graphLayers[i].length; j++) {
                            var directChildren = this.findDirectChildren(graphLayers[i][j], taskData);
                            var parent = this.findParent(graphLayers[i][j], taskData, rootNodeName);
                            var details = this.findTaskDetails(graphLayers[i][j], taskData);
                            if (directChildren.length > 0) {
                                taskDetails[graphLayers[i][j]] = {
                                    "name": graphLayers[i][j],
                                    "parent": parent,
                                    "objective": details['objective'],
                                    "effect": details['effect'],
                                    "unit": details['unit'],
                                    "children": this.getChildren(directChildren, taskDetails)
                                };
                            }
                            else {
                                taskDetails[graphLayers[i][j]] = {
                                    "name": graphLayers[i][j],
                                    "parent": parent,
                                    "objective": details['objective'],
                                    "effect": details['effect'],
                                    "unit": details['unit']
                                };
                            }
                            ;
                        }
                        ;
                    }
                    ;
                    var taskIds = Object.keys(taskDetails);
                    for (let i = 0; i < taskIds.length; i++) {
                        if (taskDetails[taskIds[i]]['parent'] == rootNodeName) {
                            rootChildren.push(taskDetails[taskIds[i]]);
                        }
                        ;
                    }
                    ;
                    return [
                        {
                            "name": rootNodeName,
                            "parent": "null",
                            "children": rootChildren
                        }
                    ];
                }
                ;
                generateDependencyGraph(taskData) {
                    d3.select('#dependencyTreeModal').selectAll("*").remove();
                    var margin = { top: 20, right: 120, bottom: 20, left: 120 }, width = 960 - margin.right - margin.left, height = 500 - margin.top - margin.bottom;
                    var i = 0, duration = 750, root;
                    var tree = d3.layout.tree()
                        .size([height, width]);
                    var diagonal = d3.svg.diagonal()
                        .projection(function (d) { return [d.y, d.x]; });
                    var svg = d3.select("#dependencyTreeModal").append("svg")
                        .attr("width", width + margin.right + margin.left)
                        .attr("height", height + margin.top + margin.bottom)
                        .append("g")
                        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
                    var div = d3.select("body").append("div")
                        .attr("class", "tooltip")
                        .style("opacity", 1e-6);
                    var treeData = this.convertTaskData(taskData, "DP");
                    root = treeData[0];
                    root.x0 = width / 2;
                    root.y0 = 0;
                    update(root);
                    d3.select(self.frameElement).style("width", "500px");
                    function update(source) {
                        // Compute the new tree layout.
                        var nodes = tree.nodes(root).reverse(), links = tree.links(nodes);
                        // Normalize for fixed-depth.
                        nodes.forEach(function (d) { d.x = d.depth * 180; });
                        // Update the nodes…
                        var node = svg.selectAll("g.node")
                            .data(nodes, function (d) { return d.id || (d.id = ++i); });
                        // Enter any new nodes at the parent's previous position.
                        var nodeEnter = node.enter().append("g")
                            .attr("class", "node")
                            .attr("transform", function (d) { return "translate(" + source.y0 + "," + source.x0 + ")"; })
                            .on("click", click);
                        nodeEnter.append("circle")
                            .attr("r", 1e-6)
                            .style("fill", function (d) {
                            return d._children ? "#008bde" : "#fff";
                        })
                            .style("stroke", function (d) {
                            if (d.name == this.taskId) {
                                return d ? "#45b766" : "#fff";
                            }
                            ;
                        })
                            .on("mouseover", showNodeName)
                            .on("mousemove", function (d) {
                            moveNodeName(d);
                        })
                            .on("mouseout", hideNodeName);
                        nodeEnter.append("text")
                            .attr("x", function (d) { return d.children || d._children ? -13 : 13; })
                            .attr("dy", ".35em")
                            .attr("text-anchor", function (d) { return d.children || d._children ? "end" : "start"; })
                            .text(function (d) { return d.name; })
                            .style("fill-opacity", 1e-6);
                        // Transition nodes to their new position.
                        var nodeUpdate = node.transition()
                            .duration(duration)
                            .attr("transform", function (d) { return "translate(" + d.y + "," + d.x + ")"; });
                        nodeUpdate.select("circle")
                            .attr("r", 10)
                            .style("fill", function (d) { return d._children ? "#008bde" : "#fff"; });
                        function showNodeName() {
                            div.transition()
                                .duration(300)
                                .style("opacity", 1);
                        }
                        ;
                        function moveNodeName(d) {
                            var nodeName = getNodeName(d);
                            div.text(nodeName)
                                .style("left", (d3.event.pageX) + "px")
                                .style("top", (d3.event.pageY) + "px");
                        }
                        ;
                        function hideNodeName() {
                            div.transition()
                                .duration(300)
                                .style("opacity", 0);
                        }
                        ;
                        function getNodeName(d) {
                            if (d['unit'] == undefined || d['effect'] == undefined || d['objective'] == undefined) {
                                var tooltipString = 'Decision point';
                            }
                            else {
                                var tooltipString = d['unit'] + ' ' + d['effect'] + ' ' + d['objective'];
                            }
                            ;
                            return tooltipString;
                        }
                        ;
                        nodeUpdate.select("text")
                            .style("fill-opacity", 1);
                        // Transition exiting nodes to the parent's new position.
                        var nodeExit = node.exit().transition()
                            .duration(duration)
                            .attr("transform", function (d) { return "translate(" + source.y + "," + source.x + ")"; })
                            .remove();
                        nodeExit.select("circle")
                            .attr("r", 1e-6);
                        nodeExit.select("text")
                            .style("fill-opacity", 1e-6);
                        // Update the links…
                        var link = svg.selectAll("path.link")
                            .data(links, function (d) { return d.target.id; });
                        // Enter any new links at the parent's previous position.
                        link.enter().insert("path", "g")
                            .attr("class", "link")
                            .attr("d", function (d) {
                            var o = { x: source.x0, y: source.y0 };
                            return diagonal({ source: o, target: o });
                        });
                        // Transition links to their new position.
                        link.transition()
                            .duration(duration)
                            .attr("d", diagonal);
                        // Transition exiting nodes to the parent's new position.
                        link.exit().transition()
                            .duration(duration)
                            .attr("d", function (d) {
                            var o = { x: source.x, y: source.y };
                            return diagonal({ source: o, target: o });
                        })
                            .remove();
                        // Stash the old positions for transition.
                        nodes.forEach(function (d) {
                            d.x0 = d.x;
                            d.y0 = d.y;
                        });
                    }
                    // Toggle children on click.
                    function click(d) {
                        if (d.children) {
                            d._children = d.children;
                            d.children = null;
                        }
                        else {
                            d.children = d._children;
                            d._children = null;
                        }
                        update(d);
                    }
                }
                ;
                generateHeatMap(currentRisk, predictedRisk) {
                    var margin = {
                        top: 0,
                        right: 0,
                        bottom: 30,
                        left: 50
                    };
                    var width = 960 - margin.left - margin.right;
                    var height = 450 - margin.top - margin.bottom;
                    var gridSize = Math.floor(900 / 25);
                    var legendWidth = (gridSize / 2 + 4);
                    var dim_1 = ["100%", "90%", "80%", "70%", "60%", "50%", "40%", "30%", "20%", "10%", ""];
                    var dim_2 = ["0", "10", "20", "30", "40", "50", "60", "70", "80", "90", "100"];
                    var buckets = 10;
                    var sigma = 5;
                    var lambda = 0.1;
                    var svg = d3.select("#courseOfActionHeatMap").append("svg")
                        .attr("width", width + margin.left + margin.right)
                        .attr("height", height + margin.top + margin.bottom)
                        .append("g")
                        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
                    function getRiskValue(dim1, dim2) {
                        var totalValue = (11 - dim1) * dim2;
                        if (totalValue > 70) {
                            return 4;
                        }
                        else if (totalValue > 50) {
                            return 3;
                        }
                        else if (totalValue > 25) {
                            return 2;
                        }
                        else {
                            return 1;
                        }
                        ;
                    }
                    ;
                    function getRiskLevel(v) {
                        if (v == 4) {
                            return "Critical";
                        }
                        else if (v == 3) {
                            return "High";
                        }
                        else if (v == 2) {
                            return "Medium";
                        }
                        else {
                            return "Low";
                        }
                        ;
                    }
                    ;
                    d3.tsv("app/risk-graph/modals/action-modal/data/heat.tsv", function (d, i) {
                        var v = getRiskValue(d.dim1, d.dim2);
                        var riskLevel = getRiskLevel(v);
                        var consequence = predictedRisk['riskScore'];
                        var likelihood = predictedRisk['likelihood'];
                        if (d.dim1 == (10 - likelihood) && d.dim2 == consequence) {
                            return {
                                dim1: d.dim1,
                                dim2: d.dim2,
                                value: v,
                                risk: riskLevel,
                                current: false,
                                opacity: 0.7
                            };
                        }
                        else if (d.dim1 == (10 - currentRisk['likelihood']) && d.dim2 == currentRisk['riskScore']) {
                            return {
                                dim1: d.dim1,
                                dim2: d.dim2,
                                value: v,
                                risk: riskLevel,
                                current: true,
                                opacity: 1
                            };
                        }
                        ;
                        return {
                            dim1: +d.dim1,
                            dim2: +d.dim2,
                            value: v,
                            risk: riskLevel,
                            current: false,
                            opacity: 0.2
                        };
                    }, function (error, data) {
                        var maxNum = Math.round(d3.max(data, function (d) {
                            return d.value;
                        }));
                        var colors = colorbrewer.RdYlGn[buckets];
                        var colorScale = d3.scale.quantile()
                            .domain([0, buckets - 1, maxNum])
                            .range(colors);
                        var tip = d3.tip()
                            .attr('class', 'd3-tip')
                            .style("visibility", "visible")
                            .offset([-20, 0])
                            .html(function (d) {
                            return "Risk level:  <b>" + d.risk;
                        });
                        tip(svg.append("g"));
                        var dim1Labels = svg.selectAll(".dim1Label")
                            .data(dim_1)
                            .enter().append("text")
                            .text(function (d) {
                            return d;
                        })
                            .attr("x", 0)
                            .attr("y", function (d, i) { return i * gridSize; })
                            .style("text-anchor", "end")
                            .attr("transform", "translate(-6," + gridSize / 3 + ")")
                            .attr("class", "mono");
                        var dim2Labels = svg.selectAll(".dim2Label")
                            .data(dim_2)
                            .enter().append("text")
                            .text(function (d) {
                            return d;
                        })
                            .attr("x", function (d, i) { return (i * gridSize) - (gridSize / 2); })
                            .attr("y", function (d, i) { return (10.5 * gridSize); })
                            .style("text-anchor", "middle")
                            .attr("transform", "translate(" + gridSize / 2 + ", -6)")
                            .attr("class", "mono");
                        var heatMap = svg.selectAll(".dim2")
                            .data(data)
                            .enter().append("rect")
                            .attr("x", function (d) {
                            return (d.dim2 - 1) * gridSize;
                        })
                            .attr("y", function (d) {
                            return (d.dim1 - 1) * gridSize;
                        })
                            .attr("rx", 4)
                            .attr("ry", 4)
                            .attr("class", "dim2 bordered")
                            .attr("width", gridSize - 2)
                            .attr("height", gridSize - 2)
                            .style("fill", colors[0])
                            .attr("class", "square")
                            .on('mouseover', tip.show)
                            .on('mouseout', tip.hide);
                        heatMap.transition()
                            .style("fill", function (d) {
                            if (d.current == true) {
                                return "#424242";
                            }
                            else {
                                return getRiskColour(d);
                            }
                        })
                            .style("opacity", function (d) {
                            return d.opacity;
                        });
                        function getRiskColour(d) {
                            if (d.value == 4) {
                                return "#d9534f";
                            }
                            else if (d.value == 3) {
                                return "#f4c583";
                            }
                            else if (d.value == 2) {
                                return "#5cb85c";
                            }
                            else if (d.value == 1) {
                                return "#5bc0de";
                            }
                            else {
                                return "#E0E0E0";
                            }
                            ;
                        }
                        ;
                        heatMap.append("title").text(function (d) {
                            return d.risk;
                        });
                        svg.append("svg:defs").selectAll("marker")
                            .data(["end"])
                            .enter().append("svg:marker")
                            .attr("id", String)
                            .attr("viewBox", "0 -5 10 10")
                            .attr("refX", 15)
                            .attr("refY", -1.5)
                            .attr("markerWidth", 10)
                            .attr("markerHeight", 10)
                            .attr("orient", "auto")
                            .style("fill", "#424242")
                            .append("svg:path")
                            .attr("d", d3.svg.symbol().type("triangle")(10, 1))
                            .attr("d", "M0,-5L10,0L0,5");
                        var consequence = Math.round(currentRisk['riskScore']);
                        var likelihood = Math.round(currentRisk['likelihood']);
                        svg.append("line")
                            .attr("x1", function () {
                            return (consequence - 0.5) * gridSize;
                        })
                            .attr("y1", function () {
                            return (10 - likelihood - 0.5) * gridSize;
                        })
                            .attr("x2", function () {
                            return (predictedRisk['riskScore'] - 0.5) * gridSize;
                        })
                            .attr("y2", function () {
                            return (10 - predictedRisk['likelihood'] - 0.5) * gridSize;
                        })
                            .attr("marker-end", "url(#end)")
                            .attr("stroke-width", 0.5)
                            .attr("stroke", "#424242");
                        var legend = svg.selectAll(".legend")
                            .data([0].concat(colorScale.quantiles()), function (d) {
                            return d;
                        })
                            .enter().append("g")
                            .attr("class", "legend");
                        svg.append("text")
                            .attr("class", "mono")
                            .attr("x", 4.5 * gridSize)
                            .attr("y", 11 * gridSize)
                            .style("font-size", "14px")
                            .text("Risk score");
                    });
                    this.heatmapSpinner = 0;
                }
                ;
                closeModal() {
                    this.dialog.close();
                }
                ;
            };
            ActionWindow = __decorate([
                core_1.Component({
                    selector: 'modal-content',
                    templateUrl: './app/risk-graph/modals/action-modal/courses.action.modal.html',
                    directives: [ng2_nvd3_1.nvD3],
                    providers: [courses_service_1.ActionModalService, http_1.HTTP_PROVIDERS]
                }),
                __metadata("design:paramtypes", [angular2_modal_1.DialogRef,
                    courses_service_1.ActionModalService])
            ], ActionWindow);
            exports_1("ActionWindow", ActionWindow);
        }
    };
});
//# sourceMappingURL=courses.action.modal.js.map