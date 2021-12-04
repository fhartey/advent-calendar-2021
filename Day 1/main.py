print("hello world")
filename = "./input.txt"

with open(filename) as f:
  numbers = [int(i) for i in f]

print(numbers[0])

print(len(numbers))
#for x in numbers:


#for x in numbers:
   # print(x.numerator)
   #counter = counter + 1
  # print(counter)
IncreasedVal = 0
for counter,item in enumerate(numbers):
    #print(item)
    if counter == 1999:
        break
    if item < numbers[counter + 1]:
        print(True)
        print(item)
        print(numbers[counter + 1])

        IncreasedVal = IncreasedVal + 1
    else:
        print(False)
        print(item)
        print(numbers[counter + 1])

# answer
print(IncreasedVal)