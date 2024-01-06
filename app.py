import os
import random

logo = '''
    __         ______     ______   ______   ______     ______     ______    
   /\ \       /\  ___\   /\__  _\ /\__  _\ /\  ___\   /\  == \   /\  ___\   
   \ \ \____  \ \  __\   \/_/\ \/ \/_/\ \/ \ \  __\   \ \  __<   \ \___  \  
    \ \_____\  \ \_____\    \ \_\    \ \_\  \ \_____\  \ \_\ \_\  \/\_____\ 
     \/_____/   \/_____/     \/_/     \/_/   \/_____/   \/_/ /_/   \/_____/ 
                                                                            
'''

with open("russian_words.txt", "r") as txt_file:
    words = txt_file.read().split()

answer = random.choice(words)
counter = 0
history = []


def mask(word: str) -> str:
    word_mask = ""

    local_a = answer

    if word == answer:
        return word

    for i in range(5):
        if word[i] == answer[i]:
            word_mask += answer[i]
        elif word[i] in local_a:
            word_mask += "#"
        else:
            word_mask += "0"
        local_a = local_a.replace(word[i], "", 1)

    return word_mask

# UI
print(logo)
while True:
    inpw = input().lower()
    if len(inpw) == 5:
        os.system('cls' if os.name == 'nt' else 'clear')
        history.append(f"{inpw} - {mask(inpw)}")
        print(logo)
        print("-------------")
        for entry in history:
            print(entry)
        print("-------------")
    else:
        print("Введите слово из 5 букв.")
        continue
    
    counter += 1

    if inpw == answer:
        print("Это правильное слово!")
        break
    if counter >= 6:
        print(f"У вас закончились попытки. Загаданное слово: {answer}")
        break
