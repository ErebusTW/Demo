def sum_even(n):
    result = 0
    for i in range(0, n, 2):
        # print(i)
        # assert(i % 2  ==1)
        result += i
    return result


# import datetime
# print("當前時間是", datetime.datetime.now())

# from datetime import *
# print("當前時間是", datetime.now())

# from datetime import datetime
# print("當前時間是", datetime.now())

# 當主程序運行時命名空間是__main__,當模塊運行時命名是模塊級運行空間module_demo
print(f"當前片段代碼運行所在的命名空間{__name__}")

if __name__ == "__main__":
    n = sum_even(50)
    print("sum_even函數測試調適結果", n)
    