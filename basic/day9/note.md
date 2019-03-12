# 补充知识
[toc]
## 列表生成式
- 复杂方式：
```
values = []
for i in range(1,100):
    values.append(i)
```
- 列表生成式
```
values = [i for i in range(1,102) if i % 2 == 0]
```
