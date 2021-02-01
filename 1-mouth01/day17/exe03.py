def verify_permissions(func):
    def giao(*args,**kwargs):
        print("验证权限")
        res=func(*args,**kwargs)
        return res
    return giao
@verify_permissions
def insert():
    print("插入")
    return True

@verify_permissions
def delete():
    print("删除")
    return False


print(insert(4563))
print(delete(156,456))


