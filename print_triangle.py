def print_line(a, b, c):
    print(a, str(b) * (c - 2), a, sep = "")
 
#------------------------------------------------------------------------
 
#Prompts the user for an integer between 3 and 8.
#Error check the input to ensure it is valid.
 
def get_size():
    num = int(input("Enter a number between 4 and 20:"))
    while (num < 4) or (num > 20):
        num = int(input("Invalid entry - Try again:"))
    return num
 
#------------------------------------------------------------------------
 
def get_char():
    single_char = input("Enter a character:")
    while len(single_char) != 1:
        single_char = input("Invalid - Try again:")
    return single_char
#------------------------------------------------------------------------
 
def print_triangle():
    size = get_size()
    char = get_char()
    for i in range(1,size - 2):
        print_line(char, " ", i)
    print_line(char, char, size)
 #-----------------------------------------------------------------------
def main():
    print_triangle()


main()
