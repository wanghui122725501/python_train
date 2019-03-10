# 单例模式&异常处理
[toc]
## 单例模式
- 某个类或者模型在程序运行期间最多只能有一个对象被创建
- 我们可以判断，如果这个类没有创建过对象，那么就创建一个对象保存在某个地方
- 如果以后要再一次创建对象，会去判断，如果之前创建了一个对象，那么就不在创建，而是直接把之前那个对象返回

## 异常
确保程序的正常处理
```
try：
	#正常的代码逻辑
except 异常名字：
    #执行异常代码
else:
    #try中没有异常的代码
finally:
    #不管有没有异常，都会执行
```
**抛出异常&自定义异常**
- 抛出异常&自定义异常
```
class ArgumentError(Exception):
	def __init__(self,*args,**kwargs):
		tmp_args = args + (u'参数错误',)
		super(ArgumentError,self).__init__(*tmp_args,**kwargs)
		# print("参数错误")

def greet(name,age):
	if not isinstance(name,str):
		raise ArgumentError('name must be string type')
	if not isinstance(age,int):
		raise ArgumentError('age must be int type')
	print('my name is %s my age is %d'%(name,age))


try:
	greet(123,34)
except Exception as err:
	print(err.args)

```

- 常见的异常

```
1. AttributeError
2. ImportError
3. IndexError
4. KeyError
5. NameError
6. NotImplementError
7. StopIteration
8. IndentationError
9. TabError
10. TypeError
11. UnicodeEncodeError
12. UnicodeDecodeError
13. ValueError
14. ZeroDevisionError
15. IOError
16. FileNotFoundError
```
## 模块和包
出现的意义就是为了规范项目，使得项目清晰易懂，管理方便
```
import module_func
from package_or_module_func import *
from my_app import my_app as mp
```

