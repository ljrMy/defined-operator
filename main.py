from typing import*
from typing import Any, Callable
class Operator:
    """
    创建一个二元运算符（实际上就是进行类的比较运算）
    下面是例子：
    >>> add=Operator(lambda a,b:a+b)
    >>> 1<add>2
    3
    >>> cmp=Operator(lambda a,b:(a>b)-(a<b))
    >>> 2<cmp>5
    -1
    """
    def __init__(self,func:Callable[[Any,Any],Any]):
        self.func=func
        self.__value=Any
    def __gt__(self,other:Any):
        if self.__value==Any:
            self.__value=other
            return self
        else:
            result=self.func(self.__value,other)
            self.__value=Any
            return result

add=Operator(lambda a,b:a+b)
cmp=Operator(lambda a,b:(a>b)-(a<b))
avg=Operator(lambda a,b:(a+b)/2)
def gcd_(a:int,b:int)->int:
    if a%b==0:
        return b
    else:
        return gcd_(b,a%b)
gcd=Operator(gcd_)

print(
    1 <add> 2 , # 相加
    2 <cmp> 3 , # 比较，和C++20中的飞船运算符（三路运算符）差不多
    1 <cmp> 1 ,
    5 <cmp> 4 ,
    13 <avg> 17 , #求平均数
    14 <gcd> 36 , #最大公因数
    sep="\n"
)
