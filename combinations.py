import csv

rows = []
combinations = []

instructions = '''Instructions:\nThis program will create combinations of two classes that don't have overlapping general education requirements from the file "courses.csv". Open the file in Excel, Google Docs or something similar and go over the courses and see which ones you want to study or not. Mark the ones you don't want to study with either "n" or "no" under the "Consider" (last) column and the ones you do want to study with "y" or "yes" and save it in the same folder as this program. You can set whether the blanks under the "Consider" column are considered as "yes" or "no" below. The program will skip all the courses with "no" and also blanks if you enter "n" for "Consider blanks as yes or no?", and makes combinations of 2 for the rest of the courses. If you enter "y" for "Restrict humanity and social science courses?", the program will consider the presence of humanity and social science requirements in both courses as overlap and will not make their combinations. You can use this to reduce the number of combinations. The program will show you all the possible combinations and after that, you can enter the course you want to study the most and it will give you the courses that don't overlap with the requirements of the course you entered. You can then look through those courses and find the combination that works for you the best.'''
print(instructions)

blanks = input('\nConsider blanks as "yes" or "no": (y for "yes"/n for "no")')
restrict = input('\nRestrict humanity and social science courses? (y/n)')

with open('courses.csv', 'r') as csvFile:
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
    hasAcp = row['ACP'] != ''
    for otherRow in rows:
        if otherRow != row and cs != '' and otherRow['CS'] != cs:
            otherHasHum = otherRow['HUM'] != ''
            otherHasSbs = otherRow['SBS'] != ''
            otherHasAcp = otherRow['ACP'] != ''
            if restrict.lower() == 'y':
                if (hasHum and not otherHasHum) or (hasSbs and not otherHasSbs) or (hasAcp and not otherHasAcp):
                    if [otherRow, row] not in combinations :
                        combinations.append([row, otherRow])
            else :
                if (hasHum and not otherHasHum) or (hasSbs and not otherHasSbs) or (hasHum and otherHasHum) or (hasSbs and otherHasSbs) or(hasAcp and not otherHasAcp):
                    if [otherRow, row] not in combinations :
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
    a = input('\nGet combinations for other courses? (y/n)')