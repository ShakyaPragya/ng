def replace(string):
    return string.replace('A', '@').replace('a', '@').replace('s', '$').replace('S', '$')
string = replace(input('enter a sting:'))
print("Modified string : ",string)