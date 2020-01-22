from arango import ArangoClient
from pprint import pprint
import json

from src.db_connector.iconnector import DBConnector  # db connector interface

class ArangoDBConnector(DBConnector):

    def __init__(self, host = 'localhost', port = '8529', protocol = 'http', user = 'root', password = ''):
        self._protocol = protocol
        self._host = host
        self._port = port
        self._user = user
        self._password = password

        super(DBConnector, self).__init__()

    def connect(self, db_name, collection_name):
        client = ArangoClient(
            protocol = self._protocol,
            host = self._host,
            port= self._port
            )
        sys_db = client.db('_system', username='root', password='')

        # create db if not exists
        if not sys_db.has_database(db_name):
            sys_db.create_database(db_name)

        # establish connection with db
        db = client.db(db_name, username=self._user, password=self._password)

        # create collection if not exists
        if not db.has_collection(collection_name):
            evnt_coll = db.create_collection(collection_name)

        return db

    def save_all(self, db):

        context = {}
        events = []
        coll = db.collection("events_coll")

        with open('./data_mapped.json') as f:
            data_in = json.load(f)
            context = data_in["@context"]
            events = data_in["eventArray"]

        for event in events:
            e = event
            e["@context"] = context
            e["_id"] = e.pop("identifier")
            e["_id"] = coll.name + "/" + str(e["_id"])

            # save event as a ArangoDB document
            if not db.has_document(e):
                db.insert_document('events_coll', e)