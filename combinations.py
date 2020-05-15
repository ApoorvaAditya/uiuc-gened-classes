import csv

rows = []
combinations = []

instructions = '''Instructions:\nThis program will create combinations of two classes that don't have overlapping general education requirements from the file "courses.csv". Open the file in Excel, Google Docs or something similar and go over the courses and see which ones you want to study or not. Mark the ones you don't want to study with either "n" or "no" under the "Consider" (last) column and the ones you do want to study  with anything else other than blank and save it in the same folder as the this program. You can leave the ones you don't want to skip blank and enter "y" to "Consider blanks?" below. The program will skip all the courses with "no" and blanks if you didn't enter "y" for "Consider blanks?", and makes combinations of 2 for the rest of the courses. It will show you all the possible combinations and after that you can enter the course you want to study the most and it will give you the courses that don't overlap with the requirements of the course you entered. You can then look through those courses and find the combination that works for you the best.'''
print(instructions)

blanks = input('\nConsider blanks? (y/n)')

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