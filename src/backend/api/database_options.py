import os
import pymongo as pm


_author_ = 'Owen Sims (sims.owen@gmail.com)'


"""
A set of functions used to infer information about the mission from the mission
network data, supplied by Risk Aware.
"""


class GetMongo:
    """
    Get data from a mongo collection.
    """
    def __init__(self, mongo_db):
        """
        Initiate the data to be passed on to functions within the class.
        """
        self.mongo_db = mongo_db

    def get_collection(self, mongo_collection):
        client = pm.MongoClient(host=os.environ.get('DB_HOSTNAME'), port=int(os.environ.get('DB_PORT')))
        db_collection = client[self.mongo_db][mongo_collection]
        mongo_data = list(db_collection.find())
        return mongo_data


class DropMongo:
    def __init__(self, mongo_db):
        """
        Initiate the data to be passed on to functions within the class.
        """
        self.mongo_db = mongo_db

    def drop_collection(self, mongo_collection):
        """
        Drop the Mongo collection.
        """
        client = pm.MongoClient(host = os.environ.get('DB_HOSTNAME'), port = int(os.environ.get('DB_PORT')))
        db_collection = client[self.mongo_db][mongo_collection]
        db_collection.drop()

    def drop_database(self):
        """
        Drop the entire Mongo database.
        """
        client = pm.MongoClient(host = os.environ.get('DB_HOSTNAME'), port = int(os.environ.get('DB_PORT')))
        client.drop_database(self.mongo_db)


class InsertMongo:
    def __init__(self, request_data, mongo_db, mongo_collection):
        """
        Post data to Mongo collection
        """
        client = pm.MongoClient(host=os.environ.get('DB_HOSTNAME'), port=int(os.environ.get('DB_PORT')))
        db_collection = client[mongo_db][mongo_collection]
        for data in request_data:
            db_collection.insert_one(data)


class GetActionDetails:
    def __init__(self, mongo_db, mongo_collection, asset_id):
        """
        Initiate by getting all actions for the given `asset_id`
        """
        client = pm.MongoClient(host = os.environ.get('DB_HOSTNAME'), port = int(os.environ.get('DB_PORT')))
        db_collection = client[mongo_db][mongo_collection]
        self.asset_actions = list(db_collection.find( { 'networkNodes' : asset_id } ))

    def get_highest_priority_action(self):
        """
        Retrieve the Object ID of the action relating to the `asset_id` with the highest `priorityScore`
        """
        if len(self.asset_actions) > 0:
            highest_score = 0
            for action in self.asset_actions:
                if action['priorityScore'] > highest_score:
                    highest_score = action['priorityScore']
                    highest_action_id = str(action['_id'])
        else:
            highest_action_id = "5937d310931e4a0696262103"

        return highest_action_id
