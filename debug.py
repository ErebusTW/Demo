#IDE單步調適按F5
def sum_even(n):
    result = 0
    for i in range(0, n, 2):
        #print(i)
        #assert(i % 2  == 0)
        result += i
    return result

n = sum_even(50)
print(n)