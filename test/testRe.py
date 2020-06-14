#-*- coding = utf-8 -*-
#@Time : 6/13/20 9:54 PM
#@Author : Sean Zhang
#@File : testRe.py
#@Software : PyCharm

#Regular Expression : String Mode : Check whether the string is in the right format

import re 
# pat = re.compile("AA")
# m = pat.search("AACBAAAA") # Search only find the first
# print(m) # span=(0, 2), match='AA'>

# Without the mode
# m = re.search("asd", "Aasd") # (1,4)
# m = re.findall("asd", "asdAasd") # ['asd', 'asd']

print(re.findall("[A-Z]", "ASflsdkjZDdfK")) # A S Z D K

print(re.findall("[A-Z]+", "ASflsdkjZDdfK")) #AS ZD K when it finds that something not compatible, it stops

print(re.sub("a", "A", "adfasdfasdF")) #replace a with A

# Note: we can add a r in front of the string to avoid escape character












