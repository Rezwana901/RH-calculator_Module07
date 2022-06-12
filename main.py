print("Rezwana Sultana \n")

'''You are making a Relative Humidity Calculator! You will make modules and functions for each part of this Program.

Q: Make a Program named “YourName’s Weather Forecast”. It will show the user a welcome message. Then asks the User’s name. Then Addressing his name, your
program will ask the user about the region you stay in. Then it will ask for the temperature in degrees Celsius, and Dew Point in degrees Celsius. Make the
program such, so that the user can compare the Relative Humidity in as many regions as he/she wants. It will show the user, which region has the highest 
and the lowest Relative Humidity of all inputs. It also should show the sequence from low humidity to high humidity. If the user does not want to compare, 
he/she can calculate RH for only one region. You can also make the program more user friendly, by taking input from any unit (Celsius or Fahrenheit).'''

#Relative Humidity Calculator
print("Rezwana's Weather Forecast\n Welcome to Rezwana's Weather Forecast")
user = input("Enter your name please: ")
location = input(user + ", please enter the region where you stay in: ")
n = int(input("Please enter the total number of regions:"))

def region(n):
    list1 = []

    for i in range(n):
        i = str(input("Enter the region name {}: ".format(i+1)))
        list1.append(i)
    return list1
reg_name = region(n)
print("\nThe list of all regions: ", reg_name)

def temperature(n):
    list2 = []

    for j in range(n):
        j = float(input("Enter the temperature(oC) {}: ".format(j+1)))
        list2.append(j)
    return list2
T = temperature(n)
print("\nThe list of all temperatures(oC): ", T)

def dewpoint(n):
    list3 = []

    for k in range(n):
        k = float(input("Enter the dewpoint temperature(oC) {}: ".format(k+1)))
        list3.append(k)
    return list3
Dp = dewpoint(n)
print("\nThe list of dewpoint temperatures(oC): ", Dp)

import math
RH = []
for l in range(n):
    hum = 100 * (math.exp((17.625 * Dp[l]) / (243.04 + Dp[l])) / math.exp((17.625 * T[l]) / (243.04 + T[l])))
    RH.append(hum)

print("\nThe list of relative humidity(%): ", RH)

for m in range(n):
    if RH[m] == max(RH):
        print("\nThe region with the highest relative humidity is: ", reg_name[m])
    if RH[m] == min(RH):
        print("\nThe region with the lowest relative humidity is: ", reg_name[m])

RH.sort()
print("\nThe sequence from low humidity to high humidity(%):", RH)
