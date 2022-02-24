""" Number Guessing Game
-------------------------------------------------------------------------
"""
import random

attempts_list = []

# Hiển thị số điểm tốt nhất của người chơi
def show_score():
    if len(attempts_list) <= 0:
        print("Chưa có ai tham gia! Hãy là người đầu tiên!")
    else:
        print("Thành tích tốt nhất là {} lần thử".format(min(attempts_list)))

# Chương trình chính của trò chơi
def start_game():
    print("Chào mừng bạn đến với trò chơi đoán số!")
    player_name = input("Bạn tên là gì? ")
    show_score()
    wanna_play = input("Bạn có muốn tham gia không, {}? (C/K) ".format(player_name))
    random_number = int(random.randint(1, 10))
    attempts = 0
    while wanna_play.lower() == "c":
        try:
            pick_number =  int(input(("Hãy chọn một số trong khoảng từ 1 đến 10: ")))
            if (pick_number < 1) or (pick_number > 10):
                raise ValueError
            if pick_number == random_number:
                attempts += 1
                attempts_list.append(attempts)
                print("Thật tuyệt vời! Bạn đã đoán chính xác!")
                play_again = input("Bạn có muốn chơi tiếp không, {}? (C/K) ".format(player_name))
                if play_again == "c":
                    random_number = int(random.randint(1, 10))
                    attempts = 0
                    show_score()
                    wanna_play = play_again
                else:
                    print("Tiếc quá! Hãy quay lại khi có thời gian nhé!")
                    break
            elif pick_number > random_number:
                print("Số bạn đoán lớn hơn số được lựa chọn!")
                attempts += 1
            else:
                print("Số bạn đoán nhỏ hơn số được lựa chọn!")
                attempts += 1
        except ValueError:
            print("Dữ liệu bạn nhập vào không hợp lệ")
            print("Hãy nhập vào một số trong khoảng từ 1 đến 10")
    else:
    	print("Tiếc quá! Hãy quay lại khi có thời gian nhé!")

if __name__ == "__main__":
    start_game()
