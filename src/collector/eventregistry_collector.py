from eventregistry import *
import eventregistry as ER
import argparse
import json
import re

from .icollector import Collector

from pprint import pprint

class ERCollector(Collector):

    def __init__(self, access_token = None):
        self._access_token = access_token
        self._er = None

        super(Collector, self).__init__()

    def connect_to_service(self):
        """
        Establish connection with EventRegistry service
        """
        if self._access_token is not None:
            self._er = ER.EventRegistry(self._access_token)
        else:
            raise Exception("[ERROR] No access_token has been specified")

        return self._er

    def exec_query(self, filters = None):

        er = self.connect_to_service()
        # set query to get events
        q = QueryEvents(
            locationUri = er.getLocationUri(filters["location"]),
            dateStart = filters["startDate"],
            dateEnd = filters["endDate"],
            #conceptUri = er.getConceptUri("Obama")
        )
        # keep just the first 2000 results
        q.setRequestedResult(
            ER.RequestEventsInfo(
                count=50,
                sortBy = "eventDate",
                sortByAsc = False,
                returnInfo = ReturnInfo(locationInfo = LocationInfoFlags(
                    wikiUri = True,     # return wiki url og the place/country
                    countryDetails = True,  # return details about country
                    geoLocation = True  # return geographic coordinates of the place/country
            ))
        ))
        # exec query
        res = er.execQuery(q)

        # dump result on a JSON file
        with open('{}_{}_{}.json'.format(filters["location"], filters["startDate"], filters["endDate"]), 'w') as outfile:
            json.dump(res, outfile)

        # check if query returned at least one result
        if res["events"]["totalResults"] == 0:
            print("[INFO] Query has not returned results!")
            print("* Check filters specified, maybe there were no events in that location in that date")
            print("* Check the validity of dates interval: start date must be less recent than end date or they must be the same date")
            sys.exit()

        # TODO: remove the following code in this function after test activity
        #elem = res["events"]["results"][0]
        #del elem["concepts"]

        #with open('data_elem.json','w') as outfile:
        #    json.dump(elem, outfile)
