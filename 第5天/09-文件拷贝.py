# -*- coding:utf-8

source_file="/var/www/index.html"
#目标文件在当前目录下,文件名在原始文件名的前面加上copy-
dest_file="copy-"+source_file[source_file.rfind("/")+1:]
print("目标文件名字:%s"%dest_file)

#打开文件
source_f = open(source_file)
dest_f = open(dest_file,"w")

#读取原始文件
content = source_f.read()

#把读取的内容写到目标文件中
dest_f.write(content)

#关闭文件
source_f.close()
dest_f.close()
