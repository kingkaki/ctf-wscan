#encoding=utf8
import requests

def codeleak_scan(root_dirs):
    with open("dict\codeleak_dir.txt","r") as f:
        codeleak_dirs = [codeleak_dir.rstrip() for codeleak_dir in f.readlines()]
    codeleak_dirs = [root_dir+codeleak_dir for root_dir in root_dirs for codeleak_dir in codeleak_dirs]
    founded_dirs = []
    for url in codeleak_dirs:
        r = requests.head(url)
        if r.status_code != 404:
            founded_dirs.append(url)
            print(r, url)
        else:
            print(r, url, end="\r")
    return founded_dirs


def main():
    dirs = ['http://118.190.152.202:8001/']
    codeleak_scan(dirs)

if __name__ == '__main__':
    main()
