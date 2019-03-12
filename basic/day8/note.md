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
- 模块
```
import module_func
from package_or_module_func import *
from my_app import my_app as mp
```
- 包
要有`__init__.py`文件
`__all__`变量:控制包中的模块的访问性质

- import xxx 和 from xxx import xxx原理
```
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
```
### 循环引用
两个py文件相互通过`from`导入，就有可能会导致循环导入（出现导入失败的问题），
解决办法就是将互相导入的部分抽离到第三个单独的py文件中。这样就能有效避免循环引用
```

## __name__
如果一个python文件或模块是被导入运行的，那么就不是作为朱运行文件来运行的
如果这个python文件是被导入的，那么这个文件的`__name__`也就是他的`包的名字.模块名称`
如果`from xxx import xxx`所在的`__name__`就是`main模块`
如果在`__init__.py`中，那么这个文件的`__name__`也就是他的`包的名字`

## pip
使用方法：
```
E:>pip --help

Usage:
  pip <command> [options]

Commands:
  install                     Install packages.
  download                    Download packages.
  uninstall                   Uninstall packages.
  freeze                      Output installed packages in requirements format.
  list                        List installed packages.
  show                        Show information about installed packages.
  check                       Verify installed packages have compatible dependencies.
  config                      Manage local and global configuration.
  search                      Search PyPI for packages.
  wheel                       Build wheels from your requirements.
  hash                        Compute hashes of package archives.
  completion                  A helper command used for command completion.
  help                        Show help for commands.
```