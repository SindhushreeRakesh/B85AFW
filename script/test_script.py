from generic.base_setup import Base_SetUp


class Test1(Base_SetUp):

    def test1(self):
        print("executing test")
        print(self.driver.title)