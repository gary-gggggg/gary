import re
s = "giao:2134,fiao:156"
pattern = r"(\w+):(\d+)"

print(re.findall(pattern, s))
print(re.split(pattern, s, 2))
print(re.sub(r"\W+", "*(", s, 1))
gg = re.finditer(r"\w+", s)
for i in gg:
    print("内容：",i.group())
    print("位置",i.span())
ggg=re.match(r"[a-z]{3}",s)
print(ggg)
