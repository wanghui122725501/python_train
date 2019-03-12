#import b
import sys
#执行b中的代码
#将b这个模块添加到sys.modules这个字典中【sys.modules的作用就是来判断某个模块是否导入当前文件中】
print(sys.modules)
is_in_modules = 'b' in sys.modules
print(is_in_modules) 

#在当前文件中，创建一个变量叫做b来指向b这个模块
from b import my_add

'''
1. 执行b中的代码
2. 将b这个模块添加到sys.modules这个字典中
3. 创建一个变量叫做my_add来指向b这个模块的my_add函数
'''