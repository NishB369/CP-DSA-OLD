def decimal_to_binary(decimal):
    if decimal==0:
        return '0'
    
    binary = ''
    while decimal > 0:
        remainder=decimal % 2
        binary=str(remainder)+binary
        decimal//=2

    return binary

decimal_num=int(input("Enter a decimal number: "))

binary_num=decimal_to_binary(decimal_num)

print("Binary representation:", binary_num)
