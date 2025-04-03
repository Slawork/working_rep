a = [10, 14, 100, 5, 0]
b = [-15, -20, 11, 16, -16]

def decor (func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        return [int(item) for item in result]
    return wrapper


@decor
def numbers(lst: list):
    ans = []

    for i in range(len(lst)-1):
        if lst[i] < lst[i+1]:
            ans.append(f'-{abs(lst[i-1] - lst[i])}')
        else:
            ans.append(f'+{abs(lst[i -1] - lst[i])}')
    ans.append(f"+{abs(lst[-2] - lst[-1])}" if lst[-1] > lst[-2] else f"-{abs(lst[-2] - lst[-1])}")

    return ans
print(numbers(a))
print(numbers(b))

