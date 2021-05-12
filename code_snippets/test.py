from datetime import datetime

product = {}

class InventoryControl:
    def __init__(self):
        self.time = datetime.now()
        self.product =

    class ProductReceiving:
        def __init__(self):
            self.time = datetime.now()
            self.product = input("어떤 상품을 입고하시겠습니까?")
            self.quantity = int(input("입고하고자 하는 수량이 총 몇 개입니까"))
            if self.product in product :
                product[self.product]+=self.quantity
            else:
                product[self.product]=self.quantity
            print(f"{self.product} 상품에 {self.quantity}만큼 입고했습니다.")

    class ProductShipping:
        def __init__(self):
            self.product = input("어떤 상품을 출고하시겠습니까")
            self.quantity = int(input("출고하고자 하는 수량이 총 몇 개입니까"))
            if self.product in product :
                if product[self.product] < self.quantity:
                    print("출고하고자 하는 상품의 수량이 부족합니다.")
                else :
                    product[self.product] -= self.quantity
                    print(f"{self.product} 상품에 {self.quantity}만큼 출고했습니다.")
            else:
                print("해당하는 상품 항목이 존재하지 않습니다.")

    class ProductOrder:
        def __init__(self):
            self.time = datetime.now()
            self.



    class StockStatus:


if __name__ == '__main__':
    print("*"*10+"재고 관리 프로그램입니다."+"*"*10+"Made by 2019170812이종근")
    print("재고 관리 프로그램의 사용 목적을 입력해주세요")
    select1=input("1:상품 입고\n2:상품 출고\n3:상품 주문\n4:상품 현황 조회\n다른 키:재고 관리 프로그램 종료")
    if select1 == 1:
        select2 = int(input("1:신제품 입고\n2:고객 반품"))
        person =
    elif select1 == 2:



