cat=input('''Please enter your category as per following code:
General -> GEN
Sch. Cst. -> SC
Sch. Tr. -> ST
Enter: ''')

age=int(input('Please enter your age: '))

exp=int(input('PLease enter your number of work experience years in numbers: '))

if age>=18:
    if cat=='GEN':
        if exp>=3:
            print('Eligible')
        else:
            print('Not Eligible')

    elif cat=='SC':
        if exp>=2:
            print('Eligible')
        else:
            print('Not Eligible')

    elif cat=='ST':
        if exp>=1:
            print('Eligible')
        else:
            print('Not Eligible')

    else:
        print('Wrong Category Input, please re-eter')

else:
    print('Not Eligible')
