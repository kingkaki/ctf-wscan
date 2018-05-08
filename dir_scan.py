#encoding=utf8
import requests


def dir_scan(url):
    with open("dict\sensitive_dir.txt", "r") as f:
        dirs = f.readlines()
    dirs = [url+_dir.rstrip() for _dir in dirs]
    for _dir in dirs:
        r = requests.head(_dir)
        print(_dir, r)

def main():
    url = "http://118.190.152.202:8006/"
    dir_scan(url)

if __name__ == '__main__':
    main()

