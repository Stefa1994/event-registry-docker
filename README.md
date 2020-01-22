# EventRegistry collector (README out of date, updating in progress)
Collector written in Python to get events from EventRegistry, querying its API. Queries results are mapped basing on a custom JSON schema for EW-Shopp project.
These two phases are implemented seperately in two different scripts. A centralized script determines the entry point for your command-line.
Events defined after mapping phase are saved in a ArangoDB database. This define the third phase of the whole pipeline.

## Executing the collector
The entry point is given by the script `entry_point.py` which is in the root directory. To see which options can be specified you shall just type `py entry_point.py -h` or `python entry_point.py -h`, according to the shell used.

### Mode
Since the whole pipeline is diveded into two steps (download and mapping), parameter `MODE` is used to specify if you are interested only in events retrieval or only in events mapping into custom schema or both.

#### Download phase: Retrieve events from EventRegistry
This is the first phase of the complete pipeline. To run this phase, `MODE` parameter must be set on `d` (only download) or `dm` (download and mapping). Then, you have to specify a valid EventRegistry API key.
Optionally, you can specify filters on location and event date. After querying EventRegistry, the results will be dumped in a JSON file.
If you are in `dm` mode, mapping phase will be automatically execute.

#### Mapping phase
This is the second phase of the complete pipeline. To run this phase, `MODE` paramter must be set on `m` (only mapping, it require a source JSON file to be mapped) or `dm`. This phase requires that the JSON source file is located in root directory. 
Mapping phase produces another JSON file, based on custom schema for EW-Shopp project.

#### Saving phase
This third phase does not depend on the execution mode set. This phase take the JSON file produced in second phase e save each event in a document in provided ArangoDB collection.



