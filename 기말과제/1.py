while True:
    print("놀이공원 매표소 매출 프로그램")
    print("1. 평일")
    print("2. 주말, 공휴일")
    print("0. 운영 종료")
    
    choice = int(input("원하는 메뉴를 선택하세요: "))
    
    if choice == 1:
        print("평일 가격 설정")
        child_price = int(input("아동 가격을 입력하세요: "))
        youth_price = int(input("청소년 가격을 입력하세요: "))
        adult_price = int(input("성인 가격을 입력하세요: "))
        
    elif choice == 2:
        print("주말, 공휴일 가격 설정")
        child_price = int(input("아동 가격을 입력하세요: "))
        youth_price = int(input("청소년 가격을 입력하세요: "))
        adult_price = int(input("성인 가격을 입력하세요: "))
        
    elif choice == 0:
        print("운영을 종료합니다.")
        break
        
    else:
        print("잘못된 입력입니다. 다시 선택해주세요.")
        continue
    
    total_amount = 0
    
    while True:
        print("\n인원수를 입력하세요 (0 입력 시 종료): ")
        child_count = int(input("아동 수: "))
        youth_count = int(input("청소년 수: "))
        adult_count = int(input("성인 수: "))
        
        if child_count == 0 and youth_count == 0 and adult_count == 0:
            print("운영을 종료합니다.")
            break
        
        amount = child_count * child_price + youth_count * youth_price + adult_count * adult_price
        total_amount += amount
        
        print(f"\n가격: {amount}원")
        print(f"누적 매출: {total_amount}원")
    
    print("===================================")
