#!/usr/bin/python2.7

import os, sys, re
import fileinput

def list_files(directory):
    """
List html files in 'directory'.
"""
    result = []
    for dirpath, dirnames, filenames in os.walk(directory):
        print("Scanning {0}".format(dirpath))
        for filename in filenames:
            if filename.lower().endswith('.html'):
                path = os.path.join(dirpath, filename)
                try:
                        result.append(path)
                except:
                    print("Error loading {0}".format(path))
    return result

def replace_avi_for_flv_in_files(files):
    """
Looks inside each file and replaces strings according to the dict
"""
    for eachfile in files:
        print("replacing avi for flv in "+eachfile);
	bytes = open(eachfile,"r+")
	print "filename ", bytes.name
	for line in open(eachfile):
		line = replacements(d,line)
		bytes.write(line)
	bytes.close()
	
def replacements(adict, astring):
	pat = '|'.join(re.escape(s) for s in adict)
	there = re.compile(pat)
	def onerepl(mo): return adict[mo.group()]
	return there.sub(onerepl, astring)
	
if __name__ == '__main__':
    directory = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else '.')
    d = {'avi':'flv','IMG':'EMBED'}
print("Changing avi text to flv in files in {0}".format(directory))
replace_avi_for_flv_in_files(list_files(directory))