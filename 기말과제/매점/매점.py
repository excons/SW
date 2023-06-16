def read_inventory():
    inventory = {}
    with open('D:/SW/실습/기말과제/매점/inventory.txt', 'r',encoding='utf-8') as file:
        for line in file:
            item, price = line.strip().split(',')
            inventory[item] = int(price)
    return inventory

def write_sales(sales_data):
    with open('D:/SW/실습/기말과제/매점/sales.txt', 'a', encoding='utf-8') as file:
        file.write(','.join(str(data) for data in sales_data) + '\n')

def calculate_total_sales(sales):
    total_sales = 0
    for sale in sales:
        total_sales += int(sale[3])
    return total_sales

def read_sales():
    sales = []
    with open('D:/SW/실습/기말과제/매점/sales.txt', 'r',encoding='utf-8') as file:
        for line in file:
            sales.append(line.strip().split(','))
    return sales

def add_sale(inventory):
    date = input("날짜를 입력하세요 (YYYY-MM-DD): ")
    item = input("판매한 상품을 입력하세요: ")
    if item not in inventory:
        print("상품이 재고에 없습니다.")
        return
    quantity = input("상품의 개수를 입력하세요: ")
    if not quantity.isdigit():
        print("올바른 개수를 입력해주세요.")
        return
    amount = inventory[item] * int(quantity)
    sales_data = [date, item, quantity, amount]
    write_sales(sales_data)
    print("매출이 추가되었습니다.")

def view_sales():
    sales = read_sales()
    if not sales:
        print("매출이 없습니다.")
    else:
        sorted_sales = sorted(sales, key=lambda x: x[0])  # 날짜를 기준으로 정렬
        print("날짜\t\t상품\t\t개수\t\t매출 금액")
        for sale in sorted_sales:
            print(f"{sale[0]}\t{sale[1]}\t\t{sale[2]}\t\t{sale[3]}")

# 메뉴 출력
def print_menu():
    print("\n===== 매점 매출 관리 프로그램 =====")
    print("1. 매출 추가")
    print("2. 매출 조회")
    print("3. 종료")
    print("============================")

# 프로그램 실행
inventory = read_inventory()
while True:
    print_menu()
    choice = input("원하는 작업을 선택하세요: ")
    if choice == '1':
        add_sale(inventory)
    elif choice == '2':
        view_sales()
    elif choice == '3':
        break
    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")

total_sales = calculate_total_sales(read_sales())
print(f"총 매출: {total_sales}")