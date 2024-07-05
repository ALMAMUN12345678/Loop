#################################  Question-->1 ##################################
# def find_minimum():
#     num_1 = int(input("Any Number_1:"))
#     num_2 = int(input("Any Number_2:"))
#     num_3 = int(input("Any Number_3:"))
#     if num_1 > num_2 > num_3:
#         print("num_3 is Min")
#     elif num_3 > num_2 > num_1:
#         print("num_1 is Min")
#     elif num_3 > num_1 > num_2:
#         print("num_2 is Min")
#     else:
#         print("All Numbers are equal")
#
#
# find_minimum()

#################################  Question-->2 ##################################
# num = int(input("Enter a number:"))
# temp = num
# rev = 0
# while num > 0:
#     dig = num % 10  ### Reminder
#     rev = rev * 10 + dig
#     num = num // 10  ## Divisor
# if temp == rev:
#     print("The number is palindrome!")
# else:
#     print("Not a palindrome!")

# num = int(input("Enter a number:"))
# rev = 0
# while num > 0:
#     dig = num % 10  ### Reminder
#     rev = rev * 10 + dig
#     num = num // 10  ## Divisor
#     print(rev)

#################################  Question-->3 ##################################
# num_1 = int(input("Any Number-1: "))
# sum_divisible_by_4 = 0
#
# while num_1 > 0:
#     if num_1 % 4 == 0:
#         sum_divisible_by_4 += num_1
#         print("Sum of numbers divisible by 4:", sum_divisible_by_4)
#     num_1 -= 1
#
#
# def sum_divisible_by_4():
#     # Initialize sum
#     total_sum = 0
#
#     while True:
#         try:
#             # Ask user for input
#             num = int(input("Enter a number (enter 0 to stop): "))
#
#             # Check if the input is divisible by 4
#             if num % 4 == 0:
#                 # Add the number to the sum
#                 total_sum += num
#
#             # Check if the input is 0 to stop
#             if num == 0:
#                 break
#         except ValueError:
#             print("Please input a number not string---->")
#
#     return total_sum
#
# # Call the function and display the final sum
# final_sum = sum_divisible_by_4()
# print("The sum of numbers divisible by 4 is:", final_sum)

#################################  Question-->4 ##################################


# while True:
#     try:
#         num = int(input("Any Number: "))
#         sum = 0
#         temp = num
#         p = len(str(num))
#         while temp > 0:
#             dig = temp % 10
#             sum += dig ** p
#             temp //= 10
#         if num == sum:
#             print("Number is Armstrong")
#             break
#         else:
#             print("Number is not Armstrong")
#     except ValueError:
#         print("Please provide Number:::")

#################################  Question-->5 ##################################
# def Student_scholarship():
#     Branch_of_study = str(input("Please input the Branch:"))
#     Score = int(input("Please proved the score of the student:"))
#     Course_fee = int(input("Please input the course fee:"))
#     if Branch_of_study == "Arts" and Score >= 90:
#         Scholarship = Course_fee * 50 / 100
#         print(f"Total self.Scholarship will be: {Scholarship}")
#         final_fee = Course_fee - Scholarship
#         print(f"Final Fee is:{final_fee}")
#     elif Branch_of_study == "Arts" and Score % 2 == 0:
#         Scholarship = Course_fee * 5 / 100
#         print(f"Total self.Scholarship will be: {Scholarship}")
#         final_fee = Course_fee - Scholarship
#         print(f"Final Fee is:{final_fee}")
#     elif Branch_of_study == "Engineering" and Score >= 85:
#         Scholarship = Course_fee * 50 / 100
#         print(f"Total self.Scholarship will be: {Scholarship}")
#         final_fee = Course_fee - Scholarship
#         print(f"Final Fee is:{final_fee}")
#     elif Branch_of_study == "Engineering" and Score % 7 == 0:
#         Scholarship = Course_fee * 5 / 100
#         print(f"Total self.Scholarship Will be: {Scholarship}")
#         final_fee = Course_fee - Scholarship
#         print(f"Final Fee is:{final_fee}")
#     else:
#         print("I don't Know:::")
#
#
# Student_scholarship()
#
#
# #### I was use OOP#############
#
# class Admission:
#     def __init__(self, name_of_Student: str, Branch_of_Study: str, Score: int, Course_fee: int):
#         self.name_of_Student = name_of_Student
#         self.Branch_of_Study = Branch_of_Study
#         self.Score = Score
#         self.Course_fee = Course_fee
#         if (Branch_of_Study == "Engineering" or "Arts") and (Score >= 90):
#             self.Scholarship = self.Course_fee * 50 / 100
#             self.Final_Fee = self.Course_fee - self.Scholarship
#         elif (Branch_of_Study == "Engineering" or "Arts") and (Score % 2 == 0):
#             self.Scholarship = self.Course_fee * 5 / 100
#             self.Final_Fee = self.Course_fee - self.Scholarship
#         elif (Branch_of_Study == "Engineering" or "Arts") and (Score >= 85):
#             self.Scholarship = self.Course_fee * 50 / 100
#             self.Final_Fee = self.Course_fee - self.Scholarship
#         elif (Branch_of_Study == "Engineering" or "Arts") and (Score % 7 == 0):
#             self.Scholarship = self.Course_fee * 5 / 100
#             self.Final_Fee = self.Course_fee - self.Scholarship
#         else:
#             print("I Don't Know what can I do?::")
#
#     def scholarship(self):
#         return self.Scholarship
#
#     def get_final_fee(self):
#         return self.Final_Fee
#
#     def get_summary(self):
#         return f"Name:{self.name_of_Student}, Course Fee:{self.Course_fee},Branch of Student:{self.Branch_of_Study},Scholarship amount: {self.Scholarship},Total Expanse: {self.Final_Fee}"
#
#
# # student = Admission("Mamun","Arts",49,100000)
# # print(student.get_summary())
# person_list = []
# person_list.append(Admission("Mamun", "Arts", 94, 250205))
# person_list.append(Admission("Shahid", "Engineering", 85, 15795))
# person_list.append(Admission("Labib", "Engineering", 14, 265489))
# person_list.append(Admission("Shabat", "Engineering", 90, 23648))
# person_list.append(Admission("Lotion", "Arts", 49, 815068))
# person_list.append(Admission("Eamon", "Arts", 91, 175559))
# print(person_list)
#
# for person in person_list:
#     print(person.get_summary())


#################################  Question-->6 ##################################

# class MumbaiDubai:
#     def __init__(self,Number_of_Adult:int,Number_of_Children:int,Day_type:str):
#         self.Number_of_Adult = Number_of_Adult
#         self.Number_of_Children = Number_of_Children
#         self.Day_type = Day_type
#         if self.Day_type == "Regular":
#             self.Rate_per_Adult = 37550
#             self.Rate_per_Children = int(self.Rate_per_Adult)*0.34
#             self.total_cost = float((self.Number_of_Adult * self.Rate_per_Adult) + (self.Number_of_Children * self.Rate_per_Children))
#             self.Service_Charge = float(self.total_cost * 7/100)
#             self.final_cost = float(self.total_cost + self.Service_Charge)
#         elif self.Day_type == "Holiday":
#             self.Rate_per_Adult = 37550.0
#             self.Rate_per_Children = int(self.Rate_per_Adult) * 0.34
#             self.total_cost = float((self.Number_of_Adult * self.Rate_per_Adult) + (self.Number_of_Children * self.Rate_per_Children))
#             self.Service_Charge = float(self.total_cost * 7/100)
#             self.final_cost = float(self.total_cost + self.Service_Charge)
#             self.Holiday_Cost = float(self.final_cost * 10/100)
#     def group_expense(self):
#         return self.final_cost
#     def get_output(self):
#         return f"Number of Adults: {self.Number_of_Adult},Number of Children: {self.Number_of_Children}," \
#                f"Service Charge: {self.Service_Charge},Total Cost:{self.total_cost} ," \
#                f"Group of Expense: {self.final_cost if self.Day_type == 'Regular' else self.Holiday_Cost }," \
#                f"Day Type:{self.Day_type if self.Day_type=='Regular'else 'Holiday'}"

# Passenger = MumbaiDubai(10,15,"Holiday")
# print(Passenger.get_output())

# class Passengerlist(MumbaiDubai):
#     def __init__(self, Number_of_Adult: int, Number_of_Children: int, Day_type: str,Name:str, Age:str):
#         super().__init__(Number_of_Adult, Number_of_Children, Day_type)
#         self.Name = Name
#         self.Age = Age
#     def get_output(self):
#         return f"Name of Passenger:{self.Name}\nAge of Passenger: {self.Age}\n" \
#                f"Number of Adults: {self.Number_of_Adult}\nNumber of Children: {self.Number_of_Children}\n" \
#                f"Service Charge: {self.Service_Charge}\nTotal Cost: {self.total_cost}\n" \
#                f"Group of Expense: {self.final_cost if self.Day_type == 'Regular' else self.Holiday_Cost }\n" \
#                f"Day Type: {self.Day_type if self.Day_type=='Regular'else 'Holiday'}"

# def get_output(self):
#     return f"Name of Passenger:{self.Name},Age of Passenger: {self.Age}," \
#            f"Number of Adults: {self.Number_of_Adult},Number of Children: {self.Number_of_Children}," \
#            f"Service Charge: {self.Service_Charge},Total Cost: {self.total_cost}," \
#            f"Group of Expense: {self.final_cost if self.Day_type == 'Regular' else self.Holiday_Cost }," \
#            f"Day Type: {self.Day_type if self.Day_type=='Regular' else 'Holiday'}"

# Passenger_1 = Passengerlist(10,25,"Holiday","Mamun,Sabir,Tarek,Selim","25,10,18,15")
# print(Passenger_1.get_output())

#################################  Question-->7 ##################################

# def multiplication():
#     num = int(input("Would you Please Suggest me a Number: "))
#     if num % 3 == 0 and num % 5 != 0:
#         print("Zip")
#     elif num % 5 == 0 and num % 3 != 0:
#         print("Zap")
#     elif num % 3 == 0 and num % 5 == 0:
#         print("Zoom")
#     else:
#         print("Invalid")
#
# multiplication()

#################################  Question-->8 ##################################
# def Grade(Score):
#     if 80 <= Score <= 100:
#         print("Grade is - A")
#     elif 79 <= Score <= 79:
#         print("Grade is - B")
#     elif 65 <= Score <= 72:
#         print("Grade is - C")
#     elif 10 <= Score <= 64:
#         print("Grade is - D")
#     else:
#         print("Grade is - Z")
#
#
# Grade(85)

#################################  Question-->9 ##################################

# def find_product_number(num1,num2,num3):
#     if num1 != 7 and num2 != 7 and num3 != 7:
#         print("Product : ", num1 * num2 * num3)
#     elif num1 == 7 and num2 != 7 and num3 != 7:
#         print("Product :", num2 * num3)
#     elif num1 != 7 and num2 == 7 and num3 != 7:
#         print("Product :", num3)
#     elif num1 != 7 and num2 != 7 and num3 == 7:
#         print("Product :",-1)
#
# find_product_number(3,7,9)

# def find_product_number(num1, num2, num3):
#     if num1 != 7 and num2 != 7 and num3 != 7:
#         return num1 * num2 * num3
#     elif num1 == 7 and num2 != 7 and num3 != 7:
#         return num2 * num3
#     elif num1 != 7 and num2 == 7 and num3 != 7:
#         return num3
#     elif num1 != 7 and num2 != 7 and num3 == 7:
#         return -1
#
# x = find_product_number(87, 7, 9)
# print("Product: ", x)

#################################  Question-->10 ##################################
# def item_by():
#     Need_1 = 0
#     Need_2 = 0
#     Coin_1 = int(input("Available Rs. 1 coins: "))
#     Coin_2 = int(input("Available Rs. 5 notes: "))
#     Prize = int(input("Amount to be made: "))
#     if (Coin_1 * 1 + Coin_2 * 5) >= Prize:
#         Need_1 = Prize // 5
#         print("Rs. 5 notes needed: ", Need_1)
#         Need_2 = Prize % 5
#         print("Rs. 1 notes needed: ", Need_2)
#     elif (Coin_1 * 1 + Coin_2 * 5) < Prize:
#         print("You Haven't Enough Money of Shopping: -1 ")
#
# item_by()

#################################  Question-->11 ##################################
# List_1 = []
# List_2 = []
# for num in range(1888,2050,1):
#     if num == 0:
#         break
#     if num % 400 == 0 or (num % 4 == 0 and num % 100 != 0):
#         List_1.append(num)
#     else:
#         List_2.append(num)
#
# print("List of leap Year: ", List_1)
# print("List of is not leap Year: ", List_2)

# List_1 = []
# List_2 = []
# while True:
#     try:
#         num = int(input("Any Number without Zero: "))
#         if num < 2024:
#             break
#         if num % 4 == 0:
#             if num % 100 == 0:
#                 if num % 400 == 0:
#                     List_1.append(num)
#                 else:
#                     List_2.append(num)
#             else:
#                 List_1.append(num)
#         else:
#             List_2.append(num)
#     except ValueError:
#         print("Please Prove a Number Not String: ")
#
# print("Leap Year is: ", List_1)
# print("Leap Year is not: ", List_2)

# List_1 = []
# List_2 = []
# for num in range(1888,2050,1):
#     try:
#         if num % 4 == 0:
#             if num % 100 == 0:
#                 if num % 400 == 0:
#                     List_1.append(num)
#                 else:
#                     List_2.append(num)
#             else:
#                 List_1.append(num)
#         else:
#             List_2.append(num)
#     except ValueError:
#         print("Please Prove a Number Not String: ")
#
# print("Leap Year is: ", List_1)
# print("Leap Year is not: ", List_2)

#################################  Question-->12 ##################################
# import math
# gems_list = ["Emerald", "Ivory", "Jasper", "Ruby", "Garnet"]
# price_list = [1760, 2119, 1599, 3920, 3999]
# order_list = []
# order_prize = []
# price_final = []
# def prize_calculation():
#     while True:
#         step_1 = str(input("Please input from gem list: "))
#         if step_1 == "exit":
#             break
#         step_2 = int(input("How much require the gem each individual: "))
#         order_list.append(step_1)
#         order_prize.append(step_2)
#         if step_1 == gems_list[0]:
#             price_final.append(price_list[0] * step_2)
#         elif step_1 == gems_list[1]:
#             price_final.append(price_list[1] * step_2)
#         elif step_1 == gems_list[2]:
#             price_final.append(price_list[2] * step_2)
#         elif step_1 == gems_list[3]:
#             price_final.append(price_list[3] * step_2)
#         elif step_1 == gems_list[4]:
#             price_final.append(price_list[4] * step_2)
#         else:
#             price_final.append(-1)
#         # elif step_1 != gems_list[0] and step_1 != gems_list[1] and step_1 != gems_list[2] and step_1 != gems_list[3] and step_1 != gems_list[4]:
#         #     price_final.append(-1)
#     return f"Order of gem list is:{order_list}\n" \
#            f"Total piece list is:{order_prize}\n" \
#            f"Final Prize Will be: {price_final}\n" \
#            f"Sum of total will be: {sum(price_final)+1 if order_list == gems_list else -1}"
#
# print(prize_calculation())

#################################  Question-->13 ##################################
# num = int(input("Please Suggest a number"))
# for i in range(num):
#     a = i + 5
#     b = i + 2
#     c = i + 7
#     if a + b > c and a + c > b and b + c > a:
#         print(a,b,c)
#     else:
#         print("Not make triangle")

# def triangle(a,b,c):
#     if a + b > c and a + c > b and b + c > a:
#         return a, b, c
#     else:
#         print("These number does not make triangle: ")
#
# x = triangle(5,7,9)
# print("Triangle make : ", x)

###########################  Question-->14 ##################################
# def chinese_puzzle(heads, legs):
#     ns = "There is No solution"
#     for i in range(heads):
#         j = heads - i
#         if i * 2 + j * 4 == legs:
#             return f"Number of Chicken will be :{i}\n" \
#                    f"NUmber of Rabbit Will be : {j}"
#         # else:
#         #     i = i
#     return ns
#
# print(chinese_puzzle(3,12))


# def puzzle(heads, legs):
#     if (4 * heads - legs) % 2 == 0:
#         Chicken = (4 * heads - legs) // 2
#         Rabbit = heads - Chicken
#         return f"Number of Chicken will be : {Chicken}\n" \
#                f"Number of Rabbit Will be : {Rabbit}"
#     else:
#         return "There is No Solutions:>>>"
#
#
# print(puzzle(1,33))


# x = "500000"
# print(x[0:4:])
# y = f"Khan:{x}"
# print(y)
# z = str(55)
# k = int(len(z))
# sum = 0
# for i in range(k):
#     i = int(z[i])
#     sum = sum + i
# print(sum)

###########################  Question-->15 ##################################
def sum(num1, num2):
    List = []
    for i in range(num1,num2+1):
        global value
        digit1 = str(i)
        sum_1 = 0
        for j in range(len(digit1)):
            value = int(digit1[j])
            sum_1 = sum_1 + value
        if sum_1 % 3 == 0 and len(digit1) == 2 and value % 5 == 0:
            List.append(digit1)
    return List


print(sum(1,99))
print(max(sum(1,99)))

###########################  Question-->16 ##################################
# List = []
# def source_destination():
#     global v1
#     airlines = str(input("Please Suggest Airlines Name: "))
#     source = str(input("Please Suggest Source Name: "))
#     destination = str(input("Please Suggest Destination Name: "))
#     passenger = int(input("Please Suggest the Number of Passenger: "))
#     for i in range(passenger+1):
#         x = 100 + i
#         if airlines == "AI":
#             v1 = f'{airlines}:{source[0:3:]}:{destination[0:3:]}:{x}'
#         elif airlines == "BA":
#             v1 = f'{airlines}:{source[0:3:]}:{destination[0:3:]}:{x}'
#         List.append(v1)
#     return List
#
# total = source_destination()
# print(total[len(total)-5:len(total)])


# List = []
# def source_destination():
#     global v1
#     airlines = str(input("Please Suggest Airlines Name: "))
#     passenger = int(input("Please Suggest the Number of Passenger: "))
#     for i in range(passenger+1):
#         x = 100 + i
#         if airlines == "AI":
#             v1 = f'{airlines}:Ban:Lon:{x}'
#         elif airlines == "BA":
#             v1 = f'{airlines}:Aus:Fra:{x}'
#         List.append(v1)
#     return List
#
# total = source_destination()
# print(total[len(total)-5:len(total)])

########################### Question-->17 ##################################
def calculate_profit():
    num1 = int(input("Please Number of Passenger: "))
    num2 = int(input("Please Number of KM Travel :"))
    Prize_of_fuel_km_L = 70
    Per_KM_fuel_need = 0.01
    Price_Per_Ticket = 80
    cost = 80 * num1
    Total_Fuel_Cost = (0.01 * num2) * 70
    if Total_Fuel_Cost < cost:
        print("Profit")
    else:
        print(-1)
calculate_profit()

