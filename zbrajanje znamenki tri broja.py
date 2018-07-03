a = int(input('PLease enter a 3 digit number'))


def add (a):
    zbroj=0
    if a < 100:
        print('Invalid input')
    elif a > 999:
        print('Invalid input')
    else:
        while a:
            zbroj += a % 10
            a  //= 10
        print(zbroj)

add(a)