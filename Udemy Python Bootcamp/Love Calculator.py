print("Welcome to The Love Calculator!!! Find out how compatible you are with your partner!!!!")
yourName = input("Please enter YOUR name: ").upper()
partnerName = input("Please enter YOUR PARTNERS name: ").upper()

T = yourName.count("T") + partnerName.count("T")
R = yourName.count("R") + partnerName.count("R")
U = yourName.count("U") + partnerName.count("U")
E = yourName.count("E") + partnerName.count("E")

L = yourName.count("L") + partnerName.count("L")
O = yourName.count("O") + partnerName.count("O")
V = yourName.count("V") + partnerName.count("V")
E = yourName.count("E") + partnerName.count("E")

trueScore = T+R+U+E
loveScore = L+O+V+E

total = int(str(trueScore) + str(loveScore))

if 10 > total < 85:
    print(f"Your score is {total}, you go together like Coke and Mentos!!")
elif 40 <= total <= 70:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is: {total}")
