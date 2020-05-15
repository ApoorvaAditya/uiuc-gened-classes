import csv

rows = []
combinations = []

blanks = input('Consider blanks? (y/n)')

with open('classes.csv', 'r') as csvFile:
    reader = csv.DictReader(csvFile)
    for row in reader:
        if row['Consider'].lower() == 'no' or row['Consider'].lower() == 'n':
            continue
        if row['Consider'] == '' and blanks.lower() != 'y':
            continue
        rows.append(row)

for row in rows:
    cs = row['CS']
    hasHum = row['HUM'] != ''
    hasSbs = row['SBS'] != ''
    for otherRow in rows:
        if otherRow != row and cs != '' and otherRow['CS'] != cs:
            otherHasHum = otherRow['HUM'] != ''
            otherHasSbs = otherRow['SBS'] != ''
            if (hasHum and not otherHasHum) or (hasSbs and not otherHasSbs):
                if [otherRow, row] not in combinations:
                    combinations.append([row, otherRow])

for i, e  in enumerate(combinations):
    first = e[0]
    second = e[1]
    print(str(i + 1) + ".", first['Course'], ":", first['Title'])
    print(str(i + 1) + ".", second['Course'], ":", second['Title'])
    print()

a = 'y'
while a.lower() == 'y':
    course = input("Get combinations for course (e.g. AAS100): ")
    flag = True
    index = 1
    for i in combinations:
        if i[0]['Course'] == course:
            print(str(index) + ". ", i[1]['Course'], ":", i[1]['Title'])
            flag = False
            index += 1
        elif i[1]['Course'] == course:
            print(str(index) + ". ", i[0]['Course'], ":", i[0]['Title'])
            flag = False
            index += 1
    if flag:
        print('No combinations')
    a = input('\nGet other combinations? (y/n)')