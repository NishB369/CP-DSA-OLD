s1=input('Enter the first string: ')
s2=input('Enter the second string: ')

if len(s1)==len(s2):
    if set(s2) == set(s1):
        print(f'Yes, {s2} is anagram of {s1}')
    else:
        print(f'No, {s2} is not anagram of {s1}')
else:
    print(f'Yes, {s2} is not anagram of {s1}')