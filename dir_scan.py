#encoding=utf8
import requests


def dir_scan(url):
    with open("dict\sensitive_dir.txt", "r") as f:
        dirs = f.readlines()
    dirs = [url+_dir.rstrip() for _dir in dirs]
    founded_dirs = []  #存储状态码非404的dir
    for _dir in dirs:
        r = requests.head(_dir)
        if(r.status_code!=404):
            founded_dirs.append(_dir)
        print(_dir, r)
    return list(set(founded_dirs))

def main():
    url = "http://118.190.152.202:8006/"
    dir_scan(url)

if __name__ == '__main__':
    main()

