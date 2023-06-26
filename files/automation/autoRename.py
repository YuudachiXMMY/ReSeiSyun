import os

# 图片存放的路径
path = r'W:/renpy/projects/ReSeiSyun/files/2022.03.23/lihui'

print(os.listdir(path))
for file in os.listdir(path):
    if file =='output':
        continue
    print(file)
    os.rename(os.path.join(path,file), os.path.join(path+"/output/",file[0:2]+" "+file[2:]))
