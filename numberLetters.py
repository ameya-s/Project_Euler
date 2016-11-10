#! python
import sys
print(sys.version)
import math
import time
'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
'''
startTime = time.time()
letterings = {'1' : 'one','2':'two','3':'three','4':'four','5':'five', '6':'six', '7':'seven', '8':'eight','9':'nine','10':'ten','11':'eleven','12':'twelve','13':'thirteen','14':'fourteen','15':'fifteen','16':'sixteen','17':'seventeen','18':'eighteen','19':'nineteen','20':'twenty','30':'thirty','40':'forty','50':'fifty','60':'sixty','70':'seventy','80':'eighty','90':'ninety'}

number_string = ""
for x in range(1, 1001):
    x_str = str(x)
    len_x = len(x_str)

    if len_x == 1:
        number_string = number_string + letterings[x_str]
    elif len_x == 2:
        if x_str in letterings:
            number_string = number_string + letterings[x_str]
        else:
            x_10 = str(int(x/10) * 10)
            x_1 = str(x % 10)
            number_string = number_string + letterings[x_10] + letterings[x_1]
    elif len_x == 3:
        #x=342
        x_100 = str(int(x/100))
        x_10 = str(int(x % 100))
        if x % 100 == 0:
            x_100 = str(int(x/100))
            number_string = number_string + letterings[x_100] + "hundred"
        else:
            if x_10 in letterings:
                number_string = number_string + letterings[x_100] + "hundredand" + letterings[x_10]
            else:
                x_10 = str((x % 100)-((x%100)%10))
                x_1 = str((x % 100) % 10)
                number_string = number_string + letterings[x_100] + "hundredand" + letterings[x_10] + letterings[x_1]
    elif len_x == 4:
        number_string = number_string + 'onethousand'

print(len(number_string))
print("Time Required for execution : " + str(time.time()-startTime))
