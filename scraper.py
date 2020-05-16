import csv, time
from selenium.webdriver import Opera
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup, SoupStrainer

def removeSpaces(text):
    s = ""
    for ch in text:
        if ch != " " and ch != "\n":
            s += ch
    return s

def moreThanOne(geneds):
    count = 0
    for elem in geneds:
        if elem != '':
            count += 1
    return count > 1

def getGPA(row):
    total = int(row['A+']) + int(row['A']) + int(row['A-']) + int(row['B+']) + int(row['B']) + int(row['B-']) + int(row['C+']) + int(row['C']) + int(row['C-']) + int(row['D+']) + int(row['D']) + int(row['D-']) + int(row['F']) + int(row['W'])
    gpa = int(row['A+']) * 4 + int(row['A']) * 4 + int(row['A-']) * 3.7 + int(row['B+']) * 3.3 + int(row['B']) * 3.0 + int(row['B-']) * 2.7 + int(row['C+']) * 2.3 + int(row['C']) * 2.0 + int(row['C-']) * 1.7 + int(row['D+']) * 1.3 + int(row['D']) * 1 + int(row['D-']) * 0.7
    return gpa / total


classes = []
runMain = True

baseLink = "https://courses.illinois.edu/schedule/2020/fall/"
mainlinks = ["https://courses.illinois.edu/gened/2020/fall/HUM", "https://courses.illinois.edu/gened/2020/fall/SBS", "https://courses.illinois.edu/gened/2020/fall/CS", "https://courses.illinois.edu/gened/2020/fall/ACP"]
gpaLink = "http://waf.cs.illinois.edu/discovery/grade_disparity_between_sections_at_uiuc/"

if runMain:
    with Opera() as browser:
        with open('coursestemp.csv', 'w') as csvFile:
            fieldnames = ['Course', 'Title', 'Description', 'Credits', 'ACP', 'CS', 'HUM', 'NAT', 'QR', 'SBS']
            writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
            writer.writeheader()
            for mainLink in mainlinks:
                browser.get(mainLink)
                page = browser.page_source
                soup = BeautifulSoup(page, features="html.parser")
                i = 0
                table = soup.findAll('table')[0].tbody.findAll('tr')
                for row in table:
                    allCells = row.findAll('td')
                    courseAvailable = len(allCells[1].contents) == 5
                    if courseAvailable:
                        acp = allCells[3].text
                        cs = allCells[4].text
                        hum = allCells[5].text
                        nat = allCells[6].text
                        qr = allCells[7].text
                        sbs = allCells[8].text
                        if moreThanOne([acp, cs, hum, nat, qr, sbs]):
                            courseTag = allCells[0].contents[1]
                            courseName = removeSpaces(courseTag.text)
                            browser.get(baseLink + courseTag['href'].replace("/schedule/terms/", ''))
                            courseSoup = BeautifulSoup(browser.page_source, features="html.parser")
                            allParas = courseSoup.findAll('p')
                            courseCredits = allParas[3].text[8]
                            flag = True
                            for c in classes:
                                if courseName != c['Course']:
                                    flag = False
                                    break
                            if flag:
                                writer.writerow({'Course': courseName, 'Title': allCells[2].contents[0], 'Description': allParas[4].text, 'Credits': courseCredits, 'ACP': acp, 'CS': cs, 'HUM': hum, 'NAT': nat, 'QR': qr, 'SBS': sbs})

courses = {}
counts = {}
bestInstructors = {}
bestInstructorsGPA = {}
with open('uiuc-gpa-dataset.csv', 'r') as gpaFile:
    reader = csv.DictReader(gpaFile)
    i = 0
    for row in reader:
        rowGPA = getGPA(row)
        course = row['Subject'] + row['Number']
        if course in courses:
            courses[course] += rowGPA
            counts[course] += 1
            if course in bestInstructorsGPA:
                if bestInstructorsGPA[course] < rowGPA:
                    bestInstructors[course] = row['Primary Instructor']
                    bestInstructorsGPA[course] = rowGPA
        else:
            courses[course] = rowGPA
            counts[course] = 1
            bestInstructors[course] = row['Primary Instructor']
            bestInstructorsGPA[course] = rowGPA
    for course in courses:
        courses[course] /= counts[course]

with open('coursestemp.csv', 'r') as f1:
    reader = csv.DictReader(f1)
    fieldnames = ['Course', 'Title', 'Description', 'Credits', 'ACP', 'CS', 'HUM', 'NAT', 'QR', 'SBS', 'Average GPA', 'Best Instructor', 'Best Instructor GPA']
    with open('courses.csv', 'w') as f2:
        writer = csv.DictWriter(f2, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            if row['Course'] in courses:
                row['Average GPA'] = courses[row['Course']]
                row['Best Instructor'] = bestInstructors[row['Course']]
                row['Best Instructor GPA'] = bestInstructorsGPA[row['Course']]
            else:
                row['Average GPA'] = ''
                row['Best Instructor'] = ''
                row['Best Instructor GPA'] = ''
            writer.writerow(row)