import sys
digit_string = sys.argv[1]
summ=0
for str_dig in digit_string:
    summ+=int(str_dig)
    
print(summ)