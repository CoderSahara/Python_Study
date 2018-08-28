# -*- coding: utf-8

# 写一个工具方法, 判断字符串是否为null. 当字符串为None 为 null, 还有"" 还为null, 还有 '    ' 也为Null
def isnull(str):
    if not str:
        return True
    elif str.strip() == '':
        return True
    else:
        return False

def test1():
    print("-----module 1 中的test1")


if __name__ == '__main__':  # 由python解释器主动执行该模块代码为了测试
    # 这行代码虽然是测试代码. 但是只要模块被导入, 就会自动执行
    print(isnull('q'))