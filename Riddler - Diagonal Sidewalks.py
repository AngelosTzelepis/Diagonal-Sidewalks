from math import sqrt
file = open('Riddler - Diagonal Sidewalks.txt', 'w')
file.write('X,Y,Shorter\n')

for x in range(-200,201):
    for y in range(-200,201):
        if x==0 and y==0:
            a="CITY HALL"
        else:
            if (abs(x)+abs(y)) > max(abs(x),abs(y))*sqrt(2):
                a="D"
            else:
                a="H"
            file.write(str(x)+','+str(y)+','+a+'\n')


file.close