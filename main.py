constant = 0.002898
loop = 0

choice = input("What are you trying to find? Lambda-max(LM) or T(T)? ")
if choice == "LM":
  T_input = float(input("Please insert the value of T: "))
  LM_ans = constant/T_input
  print("The value of Lambda-max is", LM_ans)
elif choice == "T":
  LM_input = float(input("Please insert the value of Lambda-max: "))
  T_ans = constant/LM_input
  print("The value of T is", T_ans)
else:
  print("Invalid input.")