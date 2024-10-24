l=eval(input('Enter a list enclosed within [] and values separated by ",": '))
s=input('Enter the string to find in list: ')
if s in l:
    print(f'Yes, string {s} is in list {l}')
else:
    print(f'No, string {s} not in list {l}')