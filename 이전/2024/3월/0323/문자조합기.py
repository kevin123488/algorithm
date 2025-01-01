import random

language = ['a', 'b', 'c', 'd', 'e',
            'f', 'g', 'h', 'i', 'j', 
            'k', 'l', 'm', 'n', 'o', 
            'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 
            'z']

num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

random_idx = [0, 1]

word_list = ''

# how_long = int(input())
for i in range(3):
    take_list = random.choice(random_idx)
    if take_list == 0:
        word_list += random.choice(language)
    else:
        word_list += random.choice(num)


lotto = random.sample(range(1, 46), 6)

lotto.sort()
for i in lotto:
    print(i, end=' ')