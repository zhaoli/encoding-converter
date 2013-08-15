import sys
import os
import chardet
import codecs

def encode_converter(file_name):
    """检测文件编码，如果是utf-8则通过，如果是其他编码转换成utf-8"""
    # 读取文件，是否可以只读前面100个字节？
    source_file = open(file_name, 'rb')
    print(file_name)
    content = source_file.read()
    source_file.close()
    # 检测编码
    result = chardet.detect(content)
    print(result['encoding'])
    # 根据编码读取文件，生成中间文件
    if result['encoding'] == 'utf-8':
        pass
    else:
        temp_content = content.decode(result['encoding'],'ignore')
        print(temp_content)
        dist_file = open(file_name, 'w', encoding='utf-8')
        dist_file.truncate()
        dist_file.write(temp_content) # 重新编码成utf-8，写入
        dist_file.close()

# 指定文件夹
path_name = input('请输入文件夹路径：\n')
if os.path.isdir(path_name): #判断目录是否存在
    os.chdir(path_name) #切换目录
    file_list = os.listdir(path_name)
    print(file_list)
else:
    print('目录不存在。')
    sys.exit()


# 指定文件类型：srt/ass/txt/html
file_type = input('请指定要转换的文件类型：srt、ass、txt、html或其他\n')
for files in file_list:
    if file_type in files:
        encode_converter(files)



