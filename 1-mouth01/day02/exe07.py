"""斤和两的问题，1斤为16两，做转换器
"""
liang=int(input("请输入几两："))
zhengjin=liang//16
yujin=liang%16
print(str(liang)+"两等于"+str(zhengjin)+"斤"+str(yujin)+"两")