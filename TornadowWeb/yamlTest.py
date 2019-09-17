


import os
import yaml
# 获取当前脚本所在文件夹路径
root = os.path.split(os.path.realpath(__file__))[0]

print("dir: " + root)

# 获取yaml文件路径
yamlPath = os.path.join(root, "config.yaml")

print(yamlPath)

# open方法打开直接读出来
f = open(yamlPath, 'r', encoding='utf-8')
cfg = f.read()
f.close()
print(type(cfg))  # 读出来是字符串
print(cfg)

d = yaml.load(cfg)  # 用load方法转字典
print(d)
print(type(d))

print(d['USER']['NAME'])