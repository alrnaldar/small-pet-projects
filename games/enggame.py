import random

   
with open('wordlist.10000.txt', 'r') as file:
    words = file.readlines()
    words = [s.strip("\n") for s in words]
    
    def random_word():
        for i in range(10):
            word = random.choice(words)
            print(word)
random_word()