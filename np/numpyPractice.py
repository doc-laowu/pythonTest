import numpy as np

scoretype = np.dtype({
    'names': ['name', 'chinese', 'english', 'math'],
    'formats': ['S32', 'i', 'i', 'i']})

peoples = np.array(
        [
            ("zhangfei", 66, 65, 30),
            ("guanyu", 95, 85, 98),
            ("zhaoyun", 93, 92, 96),
            ("huangzhong", 90, 88, 77),
            ("dianwei", 80, 90, 90)
        ], dtype=scoretype)

# print(peoples)


print("chinese", np.nanmean(peoples[:]["chinese"]))
print("chinese", np.amin(peoples[:]["chinese"]))
print("chinese", np.amax(peoples[:]["chinese"]))
print("chinese", np.var(peoples[:]["chinese"]))
print("chinese", np.std(peoples[:]["chinese"]))

print(peoples[:]['chinese', 'english', 'math'])
# print(np.sum(peoples[:][1:3], axis=1))