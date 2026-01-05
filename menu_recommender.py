import random
import os

MENU_FILE = "menus.txt"


def load_menus():
    # 메뉴 파일이 없으면 기본 파일 생성
    if not os.path.exists(MENU_FILE):
        with open(MENU_FILE, "w", encoding="utf-8") as f:
            f.write("김치볶음밥\n제육덮밥\n비빔밥\n라면\n")
    
    with open(MENU_FILE, "r", encoding="utf-8") as f:
        menus = [line.strip() for line in f if line.strip()]
    return menus


def save_menu(new_menu):
    with open(MENU_FILE, "a", encoding="utf-8") as f:
        f.write(new_menu + "\n")


def recommend_menu():
    menus = load_menus()
    if not menus:
        print("메뉴가 없습니다.")
        return

    choice = random.choice(menus)
    print(f"\n오늘의 메뉴 추천: {choice}")


def main():
    while True:
        menus = load_menus()
        recommend_menu()

        retry = input("재시도? (ㅇㅇ / ㄴㄴ): ").strip()

        if retry == "ㅇㅇ":
            continue

        elif retry == "ㄴㄴ":
            add_menu = input("메뉴 추가? (ㅇㅇ / ㄴㄴ): ").strip()

            if add_menu == "ㄴㄴ":
                print("프로그램을 종료합니다.")
                break

            elif add_menu == "ㅇㅇ":
                new_menu = input("추가할 메뉴를 입력하세요: ").strip()

                if new_menu in menus:
                    print("이미 있는 메뉴.")
                else:
                    save_menu(new_menu)
                    print(f"'{new_menu}' 메뉴가 추가되었습니다.")

            else:
                print("잘못된 입력입니다.")

        else:
            print("잘못된 입력입니다.")


if __name__ == "__main__":
    main()
