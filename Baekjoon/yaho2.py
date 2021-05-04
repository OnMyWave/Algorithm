#3

def say_cal0(obj):
    def say_cal1(*args,**kwargs):
        b= obj(*args,**kwargs)
        if kwargs :
            a=list(kwargs.values())
            return f"{b}\n{a[0]}!, Good Luck!!\n{args[0]}를 {args[1]}로 나누었을 때의 몫 연산\n{args[0]//args[1]}"
    return say_cal1

@say_cal0
def say_cal(a, b, name):
    print(f"{name}, good job!!")


# main code

print(say_cal(10, 3, name='Yuna'))

print('*' * 30, '\n')

print(say_cal(15, 2, name='Gildong'))
