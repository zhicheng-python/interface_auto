#encoding:utf-8
#author:wangzhicheng
#time:2019/12/2 17:09
#file:obj_practice.py


class TestObj:
    pass

test_obj=TestObj()
#实例对象属性：
setattr(test_obj,"name","zhicheng")

setattr(TestObj(),"name1","zhicheng00")

#类属性：
setattr(TestObj,"name2","zhicheng11")

if __name__ == '__main__':
    print(test_obj.name)

    print(TestObj.name2)



    print(dir(TestObj))
    print(dir(TestObj()))

