class Student:
    name = None  # 姓名
    sex = None  # 性别
    country = None  # 国籍
    native_place = None  # 籍贯
    age = None  # 年龄



    name = "张三"
    def self01(self):
        print(f"测试self方法{self.name}")

myStu1 = Student();
myStu1.self01()