import random
counter = 10
truns = 0
print(f"{'~' * 8} Guss Number Game {'~' * 8}")
actual_number = random.randint(0, 50)
while counter != 0:
    num = int(input("\nEnter any Number: "))
    if counter == 1 and num != actual_number:
          print("you Fail to guss number!")
    elif num == actual_number:
          print(f"Congratulate! You guss the right number in {truns} turns.")
          break
    elif num > actual_number:
          print("Your guss is wrong! Guss some lower number")
    else:
          print("Your guss is wrong! Guss some Higher number")
    counter -= 1
    truns += 1
    print(f"{counter} truns remaining ")