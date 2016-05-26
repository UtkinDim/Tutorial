__author__ = 'Администратор'
three = 0b11
print (0b001)

def check_bit4(input):
    if input&0b100>0:
        return "on"
    else:
        return "off"

inp=0b1011

print (check_bit4(inp))
#Меняет 1 или 0 на противоположный в позиции, которую задает пользователь
def flip_bit(number,n):
    x=0b1<<int(n-1)
    result=number^x
    result=bin(result)
    print (bin(x))
    return result

print (flip_bit(7,2))