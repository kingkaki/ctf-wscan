#encoding=utf8
import requests

def file_scan(dirs):
    with open("dict/sensitive_file.txt") as f:
        files = [file.rstrip() for file in f.readlines()]
    urls = (_dir+file for _dir in dirs for file in files)
    founded_files = []
    for url in urls :
        r = requests.head(url)
        if(r.status_code!=404):
            founded_files.append(url)
        print(url,r)
    return list(set(founded_files))


def main():
    #root_url = "http://118.190.152.202:8006/"
    dirs = ['http://118.190.152.202:8006/flag/',
            'http://118.190.152.202:8006/upload/',
            'http://118.190.152.202:8006/uploads/',
            'http://118.190.152.202:8006/download/',]
    file_scan(dirs)

if __name__ == '__main__':
    main()
