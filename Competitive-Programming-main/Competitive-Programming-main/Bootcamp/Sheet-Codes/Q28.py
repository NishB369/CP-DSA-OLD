pass_type=int(input('''
Please enter your pass type: 
from:-
1. One time Journey
2. Monthly Pass\n'''))

block=int(input('''
Please enter your block: 
from:-
1. Sleeper
2. 3rd AC
3. 2th AC
4. 1st AC\n'''))

if pass_type==1:
    if block==1:
        print('Fair: 50')
    elif block==2:
        print('Fair: 100')
    elif block==3:
        print('Fair: 150')
    elif block==4:
        print('Fair: 200')
    else:
        print('Wrong Block Number input, Please re-enter from 1 to 4')

elif pass_type==2:
    if block==1:
        print('Fair: 500')
    elif block==2:
        print('Fair: 1000')
    elif block==3:
        print('Fair: 1500')
    elif block==4:
        print('Fair: 2000')
    else:
        print('Wrong Block Number input, Please re-enter from 1 to 4')

else:
    print('Wrong Pass Type input, Please re-enter from 1 to 2')
