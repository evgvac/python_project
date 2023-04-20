import collections
import difflib

l1 = open("/home/evgvac/Git/test-1.txt", "r") .strip().splitlines()
l2 = open("/home/evgvac/Git/test-2.txt", "r") .strip().splitlines()

#if collections.Counter(l1) == collections.Counter(l2): 
#    print ("The lists l1 and l2 are the same") 
#else: 
#    print ("The lists l1 and l2 are not the same") 
#    if collections.Counter(l1) == collections.Counter(l3): 
#        print ("The lists l1 and l3 are the same") 
#    else: 
#        print ("The lists l1 and l3 are not the same")

for line in difflib.unified_diff(l1, l2, fromfile='file1', tofile='file2', lineterm=''):
    print (line)