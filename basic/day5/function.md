# 函数
[toc]
## 简介
减少重复代码，调用即可
## 函数的定义和调用
```
# 定义函数
def function_name(args,**kwargs):
	codes
# 调用函数
function_name(xxx,xxx1)
```
## 函数的参数
- 传递参数：
	- 形式参数： 定义的时候传递的参数
	- 实际参数： 调用的时候传递的参数
	- 位置参数： 严格按照定义函数的时候指定的参数位置去传递的参数
	- 关键字参数： 调用函数的时候对传入的参数带上定义函数的参数的变量形式去处理
	- 缺省的位置参数`（*args）`：
	- 缺省的关键字参数`(**kwargs)`：
	- `*args,**kwargs`
	- 默认参数： 默认参数只能在上述的其他参数的后面
