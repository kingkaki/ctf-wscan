#encoding=utf8
import requests
import file_scan
import dir_scan
import backup_scan
import codeleak_scan

url = "http://118.190.152.202:8001"
url += '/'
dir_list = [url]

print('************************dir scanning********************************')
t = dir_scan.dir_scan(url)
dir_list += t

# print(dir_list)
# exit()
print('************************file scanning********************************')
files = file_scan.file_scan(dir_list)

# print(files)
print('************************backup file scanning**************************')
backups = backup_scan.backup_scan(files)

print('************************source code leak scanning**********************')
leakdir = codeleak_scan.codeleak_scan(dir_list)

print('***********************results********************************')
print(files)
print(backups)
print(leakdir)
