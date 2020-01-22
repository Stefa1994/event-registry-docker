import json
import os

from annotated_classes.Event import Event
from annotated_classes.Context import Context
from annotated_classes.Place import Place

def mapper_to_ld():
    # Data from input json file
    data_in = {}

    # Data resulting after parsing
    data_out = {}

    # Read and load in a local variable input json file content
    with open('./data.json') as f:
        data_in = json.load(f)

    # CONTEXT
    context = Context()

    # Bulding output json file
    data_out['@context'] = context.repr()

    # LIST OF EVENTS
    events_arr_in = data_in["events"]["results"]

    # Building output json file
    data_out['eventArray'] = []

    for event in events_arr_in:
        curr_event = Event(event)
        data_out['eventArray'].append(curr_event.repr())

    # Dump data_out dictionary in a JSON output file
    with open('data_mapped.json','w') as outfile:
        json.dump(data_out, outfile, indent=4)
        outfile.write("\n")
    
    print("[INFO] Mapping has been completed")

if __name__ == "__main__":
    print("---- Mapper to JSON-LD ---")
    print("[INFO] Fetch JSON file to be mapped in current directory...")

    mapper_to_ld()