from zhiliao import *
print(GLOBAL_ZHILIAO)
hello()
p1 = Person()

from tools import *
#从包中导入*，没有任何作用，如果要生效的话就要在`___init__.py`定义`__all__=['function']`
