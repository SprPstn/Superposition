#!/usr/bin/env python
# -*- coding: utf-8 -*-


import basc_py4chan


b = basc_py4chan.Board('biz')
thread = b.get_thread(3561745)

print(thread)

for file in thread.files():
    print(file)

# In a while...
print("I fetched", thread.update(), "new replies.")