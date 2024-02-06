fh = open('output.txt','w')
import random
length = 12
i = 1
char_set  = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*1234567890"
password = ""

while i <= length:
    password += random.choice(char_set)
    i += 1

fh.write(password + '\n')

fh.close