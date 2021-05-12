#1
class Car_Accident:
    number=0
    def __init__(self,type,name1,name2,location):
        self.type = type
        self.name1 = name1
        self.name2 = name2
        self.location = location
        Car_Accident.number += 1

    def accident_reception(self,date):
        Year = date[0:4]
        if self.type=="pileup":
            insurance = 100000
        elif self.type =="collision":
            insurance = 200000
        elif self.type =="other type":
            insurance = 50000

        return f"사건번호: no{Car_Accident.number}, 사건연도: {Year}, 사건장소: {self.location}, 보험비: {insurance}"

if __name__ == '__main__':
    local = ['강북', '성북', '송파', '종로']  # 사건장소 리스트

    accident_type = ['pileup', 'collision', 'other type']  # 사건타입 리스트

    accid01 = Car_Accident('pileup', '김고려', '박자연', '강북')

    print(accid01.accident_reception('2020-06-01'))  # 사건연도, 월, 일 입력, 형태는 반드시 예시처럼 입력할 것

    accid02 = Car_Accident('collision', '이산공', '최정시', '종로')

    print(accid02.accident_reception('2020-06-02'))

    accid03 = Car_Accident('other type', '김정보', '이공학', '영등포')

    print(accid03.accident_reception('2019-06-02'))
'''
사건번호: no1, 사건연도: 2020, 사건장소: 강북, 보험비: 100000
사건번호: no2, 사건연도: 2020, 사건장소: 종로, 보험비: 200000
사건번호: no3, 사건연도: 2019, 사건장소: 기타 지역, 보험비: 50000
'''
#2
class Item:
    def __init__(self,price,quantity,code):
        self.price= price
        self.quantity = quantity
        self.code =code

class seller:
    def __init__(self,name,number,grade,score):
        self.name= name
        self.number= number
        self.grade= grade
        self.score =score

class customer:
    def __init__(self,name,address,info,point):
        self.name=name
        self.address =address
        self.info = info
        self.point = point
    def grade(self):
        if

class Buy:

class Revenue:

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








