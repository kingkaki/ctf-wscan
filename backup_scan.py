#encoding=utf8
import os
import requests

def backup_scan(files):
    _files = [os.path.splitext(file)[0] for file in files] #获取不带后缀的文件名
    bfiles = files + _files
    
    with open("dict/backup_suffix.txt","r") as f:
        suffixs = [suffix.rstrip() for suffix in f.readlines()]
    back_files = (file+suffix for file in bfiles for suffix in suffixs)
    founded_bakcups = []
    for back_file in back_files:
        r = requests.head(back_file)
        if r.status_code != 404:
            founded_bakcups.append(back_file)
        print(r,back_file)
    return list(set(founded_bakcups))



def main():
    files = [
        'http://118.190.152.202:8006/download/index.txt',
        'http://118.190.152.202:8006/download/admin.php',
        'http://118.190.152.202:8006/download/admin.txt',
        'http://118.190.152.202:8006/download/flag.txt',
        ]
    backup_scan(files)

if __name__ == '__main__':
    main()
