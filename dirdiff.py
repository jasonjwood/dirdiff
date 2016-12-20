import sys
import os
from os.path import join, getsize


def main(rootA, rootB):
    contents_a = {}
    contents_b = {}

    list_files_in_tree(rootA, contents_a)
    print "Got files A loaded"
    list_files_in_tree(rootB, contents_b)
    print "Got files B loaded"
    find_diffs(contents_a, contents_b, rootA, rootB, False)
    find_diffs(contents_b, contents_a, rootB, rootA, True)


def find_diffs(reference, copy, ref_label, copy_label, skip_size):
    print "\n\n\n"
    print "Checking diffs: ref=" + ref_label + "        copy="+copy_label
    for ref_key in reference:
        if copy.get(ref_key, None) is None:
            print "Only this exists: " + ref_key
        elif not skip_size and copy[ref_key] != reference[ref_key]:
            print "Different sizes: " + ref_key


def list_files_in_tree(root_folder, contents_list):
    for root, dirs, files in os.walk(root_folder):
        for name in dirs:
            path = (join(root, name))
            path = path[len(root_folder):]
            contents_list["FOLDER  " + path] = "DIR"
        for name in files:
            path = (join(root, name))
            try:
                size = os.path.getsize(path)
            except:
                size = -1
            path = path[len(root_folder):]
            contents_list["FILE    " + path] = size


#main("C:\\Users\\jwood\\Documents\\dirdiff\\test1", "C:\\Users\\jwood\\Documents\\dirdiff\\test2")

main(sys.argv[1], sys.argv[2])
