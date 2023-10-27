import alfheim

print("==================================================================")
print("=====================  Ragnarok Origin v0.1 ======================")
print("==================================================================")

while True:
    print("Menu: ")
    print("  0. Exit")
    print("  1. Alfhelm")
    print("  2. Demon Treasure")

    input_number = int(input("Enter Number: "))

    if input_number == 0:
        break
    elif input_number == 1:
        alfheim.start()
