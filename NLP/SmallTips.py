# 是否为汉字
import re
nw = '在顺义附近住，来光华路参加工作上的活动碰到的。基础不好，对学习资料试听课有兴趣。周末休息有空。'
s =re.findall("[\u4e00-\u9fa5]+", nw)
print(s)
