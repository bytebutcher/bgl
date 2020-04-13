#!/usr/bin/python3
import os
import sys
import argparse
from pathlib import Path
import json

app_name = "bgl"
app_version = "1.0"
app_description = "Manage global bash environment variables"
app_config_path = os.path.join(str(Path.home()), "." + app_name)
app_config_file = os.path.join(app_config_path, "data.json")

class Bgl(object):

    def __init__(self, data_file):
        self._data_file = data_file
        self._data = self.__load()

    def export(self, key_value):
        string_sep_pos = key_value.find("=")
        if (string_sep_pos <= 0):
            raise Exception("Parsing '{}' failed! Invalid format!".format(key_value)) 
        key, value = key_value.split("=")
        self._data[key] = value
        self.__save()

    def unset(self, key):
        item = self._data.pop(key, None)
        self.__save()
        return item

    def exports(self):
        return self._data.items()

    def __save(self):
        try:
            config_path = os.path.dirname(self._data_file)
            if not os.path.exists(config_path):
                os.mkdir(config_path)
            with open(self._data_file, "w") as f:
                json.dump(self._data, f)
        except Exception as e:
            print(e)
            raise Exception("ERROR: Failed writing config!")

    def __load(self):
        if os.path.isfile(self._data_file):
            try:
                with open(self._data_file, "r") as f:
                    return json.loads(f.read())
            except Exception as e:
                raise Exception("ERROR: Failed loading config!")
        else:
            return {}


parser = argparse.ArgumentParser(description=app_description)
parser.add_argument("--export", dest="export", metavar="NAME=VALUE",
	help="Exports a name and value.") 
parser.add_argument("--unset", dest="unset", metavar="NAME",
	help="Unsets a previously added name.") 
parser.add_argument("--exports", dest="exports", action='store_true', 
	help="Lists exported names and values.") 

arguments = parser.parse_args()

bgl = Bgl(app_config_file)
try:
    if arguments.export:
        bgl.export(arguments.export)
    elif arguments.unset:
        bgl.unset(arguments.unset)
    elif arguments.exports:
        for key, value in bgl.exports():
            print("{}={}".format(key, value))
    else:
        parser.print_help()
        sys.exit(1)
except Exception as e:
    print("bgl: {}".format(e))
    sys.exit(1)
