

import math

def projectCost(yarnCost,skeins):
    projectCost = yarnCost * skeins
    return projectCost

def skeins(patternYardage,yarnYardage):
    skeins = patternYardage % yarnYardage
    return skeins


print('\n\t\t-----------------------')
print('\t\tProject Cost Calculator')
print('\t\t-----------------------')
print('\n')

patternInfo = str(input('What is the name of the pattern that you picked out?  '))
patternYarn = str(input('What is the yarn weight that the pattern calls for?  '))
patternYardage = int(input('How many yards does the pattern call for?  '))

yarn_que = (input('     Are you ready to enter yarn? (y/n) '))
print('\n')

while (yarn_que == "y"):
    yarnName = (input('What is the name of the yarn? '))
    yarnWeight = str(input('What is the weight of the yarn?  '))
    yarnYardage = int(input('How many yards are in a skein? '))
    yarnCost = float(input('What is the cost of the yarn per skein?  $ '))
    yarnDouble = (input('Is the yarn being held double? (y/n) '))
    if (yarnDouble == "y"):
        patternYardage = patternYardage * 2
        skeins = int(patternYardage) / int(yarnYardage)
        projectCost = int(yarnCost) * skeins 
        print ('\n You will need' , round(skeins,2), 'skeins of your' , yarnWeight, yarnName , 'yarn, and it will cost: ', "${:,.2f}".format(projectCost))
        addYarn = (input('\nIs there another yarn you would like to compare? (y/n) '))
    else:
        skeins = int(patternYardage) / int(yarnYardage)
        projectCost = int(yarnCost) * skeins
        print ('\n You will need' , round(skeins,2), 'skeins of your' , yarnWeight, yarnName , 'yarn, and it will cost: ',"${:,.2f}".format(projectCost))
        addYarn = (input('\nIs there another yarn you would like to compare? (y/n) '))
        print('\n')
    if (addYarn == "n"):
        print ('\nGreat! Happy knitting your', str(patternInfo),'! ')
        break
else:
    print ( 'Please pick out a yarn and try again!' )
    



