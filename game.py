import time

time.sleep(2)
room = 'Main Hall'
cash = 0
game_running = True
name=input("Enter your name: ")
time.sleep(1)
print(f"Welcome {name} to the game! Your goal is to escape the room by unlocking the Out Door. You can earn cash by solving puzzles in the Chamber. Good luck!")
while game_running:
    if room == 'Main Hall':
        time.sleep(1)
        print("You find yourself in a strange place. To your left, a giant Out Door with two coin slots. To your right, a large, cavernous room")
        print("")
        time.sleep(1)
        print("If you want to try to unlock the Out Door, enter '1'. To enter the chamber, enter '2'")
        print('')
        answer = input("1-2:  ")

        if answer == '1':
            room = 'Out Door'
        elif answer == '2':
            room = 'Chamber'
        else:
            time.sleep(1)
            print("Invalid input. Please enter '1' or '2'.")
            continue

    if room == 'Out Door':
        time.sleep(2)
        print("You approach the giant Out Door. It has two cash slots. You need to insert 5 cash to unlock it.")
        print('')
        time.sleep(1)
        print(f"You currently have {cash} cash.")

        if cash >= 5:
            time.sleep(1)
            print("You insert 5 cash into the slots. The Out Door unlocks and you step out of the Out Door into the sunlight. Congratulations, you've escaped!")
            game_running = False
        else:
            print("You don't have enough cash to unlock the Out Door. You need 5 cash.")
            room = 'Main Hall'

    elif room == 'Chamber':
        time.sleep(1)
        print("You enter the large, cavernous room and look around. there, to your left, you see a GK Question on the wall. To your right, you see a Jumbled word on the wall.")
        print('')
        time.sleep(1)
        print("for the GK question, enter '1'. For the Jumbled word, enter '2'. to go back to the Main Hall room, enter '3'. But you also see a small chest in the middle of the room. You can open it to see if there is any cash inside. To open the chest, enter '4'.")
        print('')
        answer = input("1-4:  ")
        
        if answer == '1':
            room = 'GK Question'
        elif answer == '2':
            room = 'jumbled words'
        elif answer == '3':
            room = 'Main Hall'
        elif answer == '4':
            time.sleep(1)   
            print("You open the chest and find 3 cash inside!")
            cash += 3
            print(f"You now have {cash} cash.")
        else:
            print("Invalid input. Please enter '1', '2', '3', or '4'.")
            continue
    if room == 'GK Question':
        time.sleep(1)
        print("You approach the general knowledge question. It reads: 'How many provinces are there in Nepal?'")
        print('')
        answer = input("Your answer: ")

        if answer == '7':
            print("Correct! You have solved the question and earned 1 coin.")
            cash += 1
            print(f"You now have {cash} cash.")
            room = 'Chamber'
        else:
            print("Incorrect. The correct answer was 7. You return to the chamber.")
            room = 'Chamber'
    elif room == 'jumbled words':
        time.sleep(1)
        print("You approach the Jumbled word. It reads: 'Unscramble the letters: 'O C I N '. What is the word?'")
        print('')
        answer = input("Your answer: ")

        if answer.lower() == 'coin':
            print("Correct! You have solved the Jumbled word and earned 1 coin.")
            cash += 1
            print(f"You now have {cash} cash.")
            room = 'Chamber'
        else:
            print("Incorrect. The correct answer was 'coin'. You return to the chamber.")
            room = 'Chamber'  
    elif room == 'Main Hall':
        time.sleep(1)
        print("You are back in the Main Hall room. To your left, a giant Out Door with two coin slots. To your right, a large, cavernous room")
        print("If you want to try to unlock the Out Door, enter '1'. To enter the chamber, enter '2'")
        print('')   
        answer = input("1-2:  ")

        if answer == '1':
            room = 'Out Door'
        elif answer == '2':
            room = 'Chamber'
        else:
            print("Invalid input. Please enter '1' or '2'.")
            continue          
        
        

            
    