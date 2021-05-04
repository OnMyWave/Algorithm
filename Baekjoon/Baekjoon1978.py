product = {}
o_product = {}


class Customer:
    print("주문자 정보 입력")

    def __init__(self):
        self.name = input("이름을 입력:: ")
        self.pn = input("전화번호 입력:: ('-' 포함)")
        self.ad = input("주소 입력::")

    def cus_inf(self):
        print("가입 하신 회원정보는 이름:%s, 전화번호:%s, 주소:%s 입니다." % (self.name, self.pn, self.ad))


class Inbound_s():
    print("새상품 입고하기")

    def __init__(self):
        self.n_prod = input("어떤 상품을 입고 하시겠습니까? ::")
        self.quan = int(input("몇개를 입고 하시겠습니까? ::"))
        if self.n_prod in product:
            product[self.n_prod] += self.quan
        else:
            product[self.n_prod] = self.quan
        print("입고처리 완료")

    def return_(self):
        print("반품하기")
        self.return_pn = input("반품할 품목을 입력하세요 ::")
        self.return_quan = int(input("몇개를 반품 하시겠습니까? ::"))
        product["계란"] += self.return_quan


class Order():
    print("주문하기")

    def __init__(self):
        self.prod_n = input("구매하실 상품을 입력 ::")
        self.prod_q = int(input("구매하실 상품의 개수를 입력::"))
        self.prod_c = int(input("상품의 개당 가격을 입력::"))
        self.date = input("오늘의 날짜를 입력하세요:: (Ex: 2020년 5월 10일)")
        self.total = self.total = self.prod_q * self.prod_c

        if self.prod_n in o_product:
            o_product[self.prod_n] += self.prod_q
        else:
            o_product[self.prod_n] = self.prod_q

    def order__(self):
        print("주문가능여부")
        if o_product[self.prod_n] < product[self.prod_n]:
            print("주문 가능")
        else:
            print("주문 불가")

    def check_olist(self):
        print("주문 명세서")
        print(
            " 주문 하신 상품: %s \n 주문한 상품의 개수: %d개 \n 주문한 상품의 개당 가격: %d원 \n 총금액: %d원 \n 주문한 날짜: %s \n 주문자: %s \n 전화번호: %s \n 주소: %s \n" % (
            self.prod_n, self.prod_q, self.prod_c, self.total, self.date, Person.name, Person.pn, Person.ad))


class Storage:
    print("현황 재고")

    def __init__(self):
        self.s_product = product.keys()
        self.s_quantity = product.values()

    def check_stor(self):
        print("현황재고는 :", product.items())

    def check_pro(self):
        print("품목의 종류는", self.s_product)


class Outbound_s:
    print("출고하기")

    def __init__(self):
        self.out_product = input("출고할 품목을 입력하세요 ::")
        self.out_quan = int(input("몇개를 출고 하시겠습니까? ::"))

    def company_out(self):
        print("업체반품 출고")
        product[self.out_product] -= self.out_quan
        print("출고후, 남은 품목 =", product.items())

    def cus_out(self):
        print("고객 출고")
        product["계란"] -= self.out_quan
        print("출고후, 남은 품목 =", product.items())


Person = Customer()
Person_inbound = Inbound_s()
Person_order = Order()
Person_order.order__()
Person_order.check_olist()

# select=1
# while select_number != 5:
# select = input("숫자를 입력해주세요 :: (1=주문하기, 2=현황보기, 3=입고하기, 4=출고하기, 5=종료")
# if select == 3:
# Person_

