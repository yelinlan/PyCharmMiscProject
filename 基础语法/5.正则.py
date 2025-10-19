# 测试正则
import re

pattern = r"\w+"
mails = "S007-S009-S006-S005"

# 匹配邮箱地址
print(re.match(pattern, mails))

# 查找所有匹配的邮箱地址
all_emails = re.findall(pattern, mails)
print(all_emails)

# search 第一个
print(re.search(pattern, mails))

# 替换
print(re.sub(pattern, "XXX", mails))

# split
print(re.split("-", mails))

# 非贪婪匹配 最小满足串
print(re.match(r"\w+?", mails))
