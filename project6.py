# Basic Math Quiz Game
def basic_quiz():
    print("""
Question 1: What is 150% of 100?

A) 150

B) 50

C) 100

D) 200


Question 2: What is 8 divided by 2?

A) 4

B) 16

C) 6

D) 10


Question 3: What is the next number in the sequence: 2, 4, 6, 8, ...?

A) 9

B) 10

C) 12

D) 11

Question 4: If you have 5 apples and you eat 2, how many are left?

A) 3

B) 7

C) 5

D) 2

Question 5: What is the sum of 20 and 15?

A) 35

B) 30

C) 25

D) 40


Question 6: Which number is smaller, 0 or -1?

A) 0

B) -1

C) Both are equal

D) Cannot be determined


Question 7: What is 10 times 10?

A) 100

B) 1000

C) 10

D) 20


Question 8: If a dozen eggs cost ₹240, what is the cost of one egg?

A) ₹20

B) ₹40

C) ₹30

D) ₹60


Question 9: What is the square root of 81?

A) 7

B) 9

C) 8

D) 10


Question 10: How many sides does a hexagon have?

A) 5

B) 6

C) 7

D) 8


Question 11: What is 7 subtracted from 100?

A) 93

B) 107

C) 97

D) 103


Question 12: If you divide 50 by half and add 20, what do you get?

A) 120

B) 100

C) 45

D) 70


Question 13: What is the product of 12 and 12?

A) 144

B) 124

C) 134

D) 154


Question 14: Which number is an odd number?

A) 22

B) 18

C) 15

D) 30


Question 15: What is 45 minutes as a fraction of an hour?

A) 1/2

B) 1/4

C) 3/4

D) 2/3


Question 16: What is the value of 2 to the power of 5?

A) 10

B) 32

C) 25

D) 16


Question 17: What is the result of 19 minus 9?

A) 10

B) 8

C) 11

D) 9


Question 18: How many zeros are in the number one thousand?

A) 2

B) 3

C) 4

D) 1


Question 19: What is the average of 10, 20, and 30?

A) 20

B) 25

C) 15

D) 30


Question 20: If a rectangle's length is twice its width, and the perimeter is 60 cm, what is the width?

A) 15 cm

B) 20 cm

C) 10 cm

D) 25 cm


Question 21: What is 1000 multiplied by 0?

A) 1000

B) 0

C) 1

D) 10
""")
    answer = ['A','A','B','A','A','B','A','A','B','B','A','A','A','C','C','B','A','B','A','C','B']

    i = 0
    point =0
    while i<21:
        ans = input("Enter the option A,B,C,D",)
        if answer[i]== ans:
            point+=1
        i+=1
    return point

print("--------->Welcome to Math Quiz Game<------------")
highest_score = 0
top_scorer = ''
user = input("Enter Your name: ")
result = basic_quiz()
if result>highest_score:
    print("******>>>>>Highest Score!!!!<<<<<<********")
    print(result)
    top_scorer = user

else:
    print("Your Score: ",result)

