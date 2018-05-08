#encoding=utf8
import requests
import file_scan, dir_scan, backup_scan

url = "http://118.190.152.202:8001"
url += '/'
dir_list = [url]

print('********dir scanning****************')
t = dir_scan.dir_scan(url)
dir_list += t

# print(dir_list)
# exit()
print('********file scanning****************')
files = file_scan.file_scan(dir_list)

# print(files)
print('********backup file scanning****************')
backups = backup_scan.backup_scan(files)

print('********results****************')
print(files)
print(backups)
