'''
Created on 2020年5月31日

@author: julia
'''
import requests
r = requests.get("https://www.baidu.com/",verify = False)
print(r.text)
