# for index in range(7):
#     print(index)

# fruit = ["Apple", "Banana", "Cherry", "Lychee"]
# for name in fruit:
#     print(name)

# adj = ["red", "Big", "tasty"]
# fruit = ["Green Apple", "Mango", "Guava", "Mango"]
# for x in adj:
#     for y in fruit:
#         print(x,y)

# fruit = ["Green Apple", "Mango", "Guava", "Lychee"]
# for x in fruit:
#     if x == "Mango":
#         break
#     print(x)

# fruit = ["Green Apple", "Mango", "Guava", "Lychee"]
# for x in fruit:
#     if x == "Guava":
#         continue
#     print(x)

# Name = ["a", "b", "c", "d", "e"]
# for x in Name:
#     if x == "d":
#         continue
#     print(x)

# Name = ["a", "b", "c", "d", "e"]
# for x in Name:
#     if x == "c":
#         break
#     print(x)

# for data in range(1):
#     print("*")

# for data in range (1,6):
#     print("*" * data)

# for data in range (5):
#     print("*" * (data+1))

# height = 5
# for row in range (1, height+1):
#     spaces = height-row
#     stars = 2*row-1
#     print(" "*spaces+"*"*stars)

# for r in range (3):
#     for c in range (3):
#         print(f"{r} {c}",end="  ")
# print()

# for row in range (1, 4):
#     print("#" *  (2*row))

for row in range (1,7):
    print("#" * (3*row))
    