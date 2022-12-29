import requests
import json

def pathwalk(path='.', result=[]):
    dirlist = os.listdir(path=path)
 
    for item in dirlist:
        child = os.path.join(path, item)
        if os.path.isfile(child):
            result.append(child)
            # print(child)
        else:
            pathwalk(child, result)
def generate(files=[], outputpath='./readme.md'):
    info = {}
    for file in files:
        if 'readme.' in str(file):
            continue
        with open(file, 'r', encoding='utf8') as f:
            temp = getdescription(f.readlines())
            temp = temp[15:]
            info[str(file)] = temp
            f.close()
    # print(len(info), info)
    info = {k:v for k,v in info.items() if v!='' and 'readme.' not in str(k)}
    print(len(info), info)
 
    # 生成Markdown文件
    with open(outputpath, 'a', encoding='utf8') as f:
        # f.write('标题部分\n---')
        for key, value in info.items():
            temp = " - [{}]({})\n\n".format(value, key)
            f.write(temp)
        f.close()
    print('文件已生成！')
