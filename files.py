# Program 1
name = input("Enter your name:")
FILENAME = "name.txt"
# open output file for writing (this creates a new file if it doesn't exist)
out_file = open(FILENAME, 'w')
print(name, file=out_file)
out_file.close()

# Program 2
SHOWFILE = "name.txt"
show_file = open(FILENAME, 'r')
for line in show_file:
    print(f"Your name is {line}")
show_file.close()

# Program 3
NEWFILE = "numbers.txt"
in_file = open(NEWFILE, 'r')
total_sum = 0
for line in range(0, 2):
    number = in_file.readline()
    total_sum += int(number)
print(total_sum)
in_file.close()

# Program 4
new_file = open("numbers.txt", 'r')
total_sum = 0
for i in new_file:
    number = int(i)
    total_sum += number
print(total_sum)
new_file.close()
