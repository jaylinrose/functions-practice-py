# Hello Function

def hello():
    print("Hi there Mate!")

# Pack Function 

def pack(a, b, c):
    return[a, b, c]

# Eat Lunch Function

def eat_lunch(my_lst):
  if len(my_lst) == 0:
    print("Dang, boxed air again it is.")
  else:
    for i in range(len(my_lst)):
      if i == 0:
        print(f"First I eat {my_lst[0]}")
      else:
        print(f"Next I eat {my_lst[i]}")

hello()
print(pack("a","b","c"))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["lumpia"])
eat_lunch(["ramen","bao","lumpia","taco"])