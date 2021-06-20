
def fizbuzz(end, fizz, buzz):
    for i in range(1, end + 1):
        if i % fizz == 0:
            if i % buzz == 0:
                print('FizzBuzz')
            else:
                print('Fizz')
        elif i % buzz == 0:
            print('Buzz')
        else:
            print(i)
    return 0

boolean = True
if __name__ == '__main__':
    while boolean:
        try:
            x = int(input('FizzBuzz from 1 to ? :'))
            y = int(input('Int for Fizz? :'))
            z = int(input('Int for Buzz? :'))
            boolean = False
        except:
           print("Not an integer")

    fizbuzz(x, y, z)