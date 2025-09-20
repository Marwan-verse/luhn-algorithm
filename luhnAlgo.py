import random
#importing a "random" module to get random numbers i.e getting the numbers for the card

# Prompt user for a single digit
while True: # Loop until valid input is received
    user_digit = input("Enter a single digit (0-9) for the card number (for example 4 is for visa and 5 is for mastercard): ")
    #negitive numbers are counted as more then one digit
    #same with decimals
    if user_digit.isdigit() and len(user_digit) == 1: # Check if input is a single digit
        cardNum = [int(user_digit)] #adding the user input to a list if valid
        break
    else: #break if a number is not between 0-9 or if the input is more than one digit
        print("Invalid input. Please enter exactly one digit (0-9).")
#ints set to 0 to avoid errors
sum = 0
val_number = 0
#loop to get random numbers to fill the card number 
for x in range(1,15):  
    # 14 digits total , why since first digit is user input depending on the card type and last is the validation number
    cardNum.append(random.randint(0,9))#random number between 0-9
print(cardNum) #printing the card number to check if everything is working

for z in range(2 ,15):#starting from index 2 since index 0 is user input and index 1 is not doubled
    if z % 2 == 0:#checking if the index is even , since we only need every other number starting from index 2 to be doubled
        cardNum[z]= cardNum[z]*2 #number at that index is doubled
print(cardNum) #checking if the numbers are doubled correctly

for nums in cardNum: #loop to checking if any number is greater than 9
    if nums > 9: #check if number is greater than 9
        nums = nums - 9 #subtracting 9 from the number because adding the digits the 2 digits together is the same as subtracting 9
                        #for example 18 -> 1 + 8 = 9 -> 18 - 9 = 9
                        #for example 14 -> 1 + 4 = 5 -> 14 - 9 = 5
                        #for example 12 -> 1 + 2 = 3 -> 12 - 9 = 3
                        #for example 10 -> 1 + 0 = 1 -> 10 - 9 = 1
                        #for example 9 -> 9 (no change needed)
        cardNum[cardNum.index(nums + 9)] = nums #replacing the number in the list with the new value after subtracting 9

for nums in range(1,15): #loop to add all the numbers together , starting from index 1 since index 0 is user input
    sum = sum + cardNum[nums] #total

print(sum) #printing the total to check if everything is working correctly

val_number = (10 - (sum % 10)) % 10 #calculating the validation number
#the extra % 10 at the end is to handle the case where sum % 10

print(val_number)#printing the validation number to check if everything is working correctly

cardNum.append(val_number) #adding the validation number to the end of the card number list to make the total length 16 digits

print(cardNum) #final card number with validation number at the end and the user input at the start
#example output [4, 7, 8, 2, 4, 7, 3, 2, 3, 5, 2, 8, 5, 8, 5]
#with a card number of 4264 4808 5678 5510