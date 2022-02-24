""" ROCK PAPER SCISSORS
--------------------------------------------------------------------------
"""
import random

def random_choice():
    list_choice = ['rock', 'paper', 'scissors']
    choice = random.choice(list_choice)
    return choice

print("Chào mừng đến với trò chơi kéo búa bao!")
wanna_play = input("Bạn có muốn chơi không? (C/K) ")
while wanna_play.lower() == "c":
    computer_choice = random_choice()
    player_choice = input("Mời nhập vào lựa chọn của bạn: ")
    try:
        if player_choice.lower() in ["rock", "paper", "scissors"]:
            print("Bạn đã chọn {}".format(player_choice.lower()))
            if computer_choice == "rock":
                print("Máy tính đã chọn rock")
                if player_choice == "rock":
                    print("Kết quả hòa!")
                elif player_choice == "paper":
                    print("Tuyệt vời! Bạn đã thắng!")
                else:
                    print("Tiếc quá! Thua mất rồi!")
            elif computer_choice == "paper":
                print("Máy tính đã chọn paper")
                if player_choice == "rock":
                    print("Tiếc quá! Thua mất rồi!")
                elif player_choice == "paper":
                    print("Kết quả hòa!")
                else:
                    print("Tuyệt quá! Bạn đã thắng!")
            else:
                print("Máy tính đã chọn scissors")
                if player_choice == "rock":
                    print("Tuyệt quá! Bạn đã thắng!")
                elif player_choice == "paper":
                    print("Tiếc quá! Thua mất rồi!")
                else:
                    print("Kết quả hòa!")
            play_again = input("Bạn có muốn chơi lại không? (C/K) ")
            if play_again.lower() == "c":
                wanna_play = play_again
            else:
                print("Tạm biệt! Hẹn gặp lại nhé!")
                break
        raise ValueError
    except ValueError:
    	print("Xin hãy chọn rock, paper hoặc scissors")






