#encoding=utf8
import requests

root_url = "http://118.190.152.202:8006/"
with open("dict\sensitive_dir.txt","r") as f:
    dirs = f.readlines()

dirs = [_dir.rstrip() for _dir in dirs]

for _dir in dirs :
    url = root_url+_dir
    r = requests.head(url)
    print(url,r)

