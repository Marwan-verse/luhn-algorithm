import random

cardNum = [4]
sum = 0
val_number = 0

for x in range(1,15):
    cardNum.append(random.randint(0,9))
print(cardNum)

for z in range(2 ,15):
    if z % 2 == 0:
        cardNum[z]= cardNum[z]*2
print(cardNum)

for nums in cardNum:
    if nums > 9:
        nums = nums - 9
        cardNum[cardNum.index(nums + 9)] = nums

for nums in range(1,15):
    sum = sum + cardNum[nums]

print(sum)

val_number = (10 - (sum % 10)) % 10

print(val_number)

cardNum.append(val_number)

print(cardNum)