import Parent

#子类继承父类  分开写会报错
class Child(Parent): # 定义子类
    def __init__(self):
        print ("调用子类构造方法")

    def childMethod(self):
        print ('调用子类方法')

c = Child()          # 实例化子类
c.childMethod()      # 调用子类的方法
c.parentMethod()     # 调用父类方法
c.setAttr(200)       # 再次调用父类的方法 - 设置属性值
c.getAttr()          # 再次调用父类的方法 - 获取属性值