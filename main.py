from PIL import Image
import os
import numpy as np

rand = np.random

path = os.getcwd()

background_list = os.listdir(f'{path}\\Layers\\Background')
char_list = os.listdir(f'{path}\\Layers\\Char')
body_list = os.listdir(f'{path}\\Layers\\Body')
head_list = os.listdir(f'{path}\\Layers\\Head')
eye_list = os.listdir(f'{path}\\Layers\\Eye')

img_num = input("How much images you want to Generate? ")

if img_num.isdigit():
    for i in range(int(img_num)):
        background_roll = rand.randint(0, 6) # Change the second number with the number of assets you have of each layer
        char_roll = rand.randint(0, 5)
        body_roll = rand.randint(0, 2)
        head_roll = rand.randint(0, 3)
        eye_roll = rand.randint(0, 4)

        name = f'{background_roll}{char_roll}{body_roll}{head_roll}{eye_roll}'

        background = Image.open(f'Layers/Background\\{background_list[background_roll]}')
        char = Image.open(f'Layers/Char\\{char_list[char_roll]}')
        body = Image.open(f'Layers/Body\\{body_list[body_roll]}')
        head = Image.open(f'Layers/Head\\{head_list[head_roll]}')
        eye = Image.open(f'Layers/Eye\\{eye_list[eye_roll]}')

        background.paste(char, (0, 0), mask=char)
        background.paste(body, (0, 0), mask=body)
        background.paste(head, (0, 0), mask=head)
        background.paste(eye, (0, 0), mask=eye)

        background.save(f'GeneratedImages\\{name}.PNG', 'PNG')
        print(name)

else:
    print('Insert only numbers!')