
#Print a row of c characters, and a being at the beggining and end
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
def main():
    ch = get_char()
    size = get_size()
    print_line("|", ch, size)
main()

