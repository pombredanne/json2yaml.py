#!/usr/bin/python

import json
import sys
from collections import OrderedDict

def json2yaml(fname):
    if fname.endswith('.json'):
        fname = fname.replace('.json', '')
    infile = open(fname + '.json')
    outfile = open(fname + '.yml', 'w')
    data = json.load(infile, object_pairs_hook=OrderedDict)

    def dump(data, indent=""):
        yml = ""
        for key in data:
            if isinstance(data[key], OrderedDict):
                yml += "\n%s%s:" % (indent, key)
                yml += dump(data[key], indent + "    ")
            else:
                val = data[key]
                if key == "_comment":
                    key = "#"
                if val is None:
                    val = "null"
                elif isinstance(val, bool):
                    val = "true" if val else "false"
                elif isinstance(val, basestring) and " " in val and key != "#":
                    val = '"%s"' % val
                yml += "\n%s%s: %s" % (indent, key, val)
        return yml
    outfile.write(dump(data))

if __name__ == "__main__":
    for fname in sys.argv[1:]:
        json2yaml(fname)
