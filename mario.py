def main():
    brick =  int(input("enter no. of bricks you want: "))

    row = int(input("enter no. of rows you want: "))

    square = int(input("enter no. of columns you want: "))

    rectangle = int(input("enter the width of rectangle: "))

    l = int(input("enter the length of rectangle: "))
    
    print_column(brick)

    print_row(row)

    print_square(square)

    print_rectangle(rectangle, l)
    

def print_rectangle(width, length):
    for rectangle in range(width):
        print("!" * length)
    
def print_row(length):

    print("@"*length)


def print_column(height):
    
    for brick in range(height):
        print("#")


def print_square(size):
    for square in range(size):
        print("?" * size)



main()