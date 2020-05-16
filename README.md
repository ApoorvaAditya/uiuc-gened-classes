# Gened Classes Dataset and Combinations
I would recommend you go through at least the [About][8] subtopics below but if you just want the dataset and the program, head to [Usage][7].
## Usage
1. Download the repo by clicking the green "Clone or download" button and click download as ZIP.
2. Extract the files.
2. Open "courses.csv" in Excel, Google Docs or something similar.
3. To help in readability, expand the size of the title and description column and enable wrap text on the columns (In Excel, right-click on the column, click on Format Cells, go to Alignment and enable Wrap text. If the row height is wrong, click on Format in the Home tab on the ribbon and click AutoFit Row Height).
4. Go over the courses (about 135 much better than 300 on course explorer) and see which ones you want to study or not. Mark the ones you don't want to study with either "n" or "no" under the "Consider" (last) column and the ones you do want to study with "y" or "yes" and save it in the same folder as this program. You can set blanks in the "Consider" column to be considered as yes or no in the program.
5. Run combinations.exe. The program will skip all the courses with "no" and blanks if you enter "n" for "Consider blanks as yes or no?", and makes combinations of 2 for the rest of the courses.
6. It will show you all the possible combinations and after that, you can enter the course you want to study the most and it will give you the courses that don't overlap with the requirements of the course you entered. You can then look through those courses and find the combination that works for you the best.
7. If you want to reduce the number of combinations, enter "y" on "Restrict humanities and social science?"
### Making Combinations
The program makes the combinations of 2 courses in which the general requirements do not overlap. Here are the specific rules:
* Cannot take a course that satisfies Humanities and Social Science at the same time. This condition is already satisfied by the dataset which doesn't contain such courses. 
* Consider same type of Cultural Studies requirement (i.e. US Minority, Western/Comparative Culture etc.) as overlap but not the presence of Cultural Studies as overlap. So for example, if one course and US and other WCC, it will not be an overlap but if one course is US and other is also US, then it is an overlap.

If "Restrict humanities and social science?" is enabled (i.e you enter "y"):
* Consider any type of other requirements as overlap. So for example, if one course has Social and Behavioural Science requirement of whichever type and the other course also has Social and Behavioural Science requirement, then it will be an overlap.

I added this because I thought that the best way to choose the gened class would be if there were no overlaps on the requirements between the 2 courses and your time is maximised since you're not wasting it on repeating a requirement but that isn't the case when you need atleast 2 courses to fully complete the humanities and social science requirements of 6 credit hours. You can use this option to reduce the number of combinations if you want but it really was just a mistake I left in.

## About
### Dataset
This repo contains the dataset scraped from the [UIUC course explorer][1]. It contains the general education courses for fall 2020, their name, description, credit hours, general education requirements, average GPA of fall 2019, the instructor with the highest GPA (denoted by best here, indicative of the best in terms of the GPA) of fall 2019, and the average GPA of the class of the same instructor. The last three columns of data have been extracted from [this dataset][2] provided [here][3]. The main objective is to combine the data from courses and GPA datasets for freshmen to help them decide on their general requirements courses and maximise their time and credits and help them find what they really want to learn. Instead of going through hundreds of courses and clicking on each of them to find out what the course is about and its description, this dataset brings it all to one place. The average GPA is included for those who are not interested in what they study but how easy it is to get good grades. The best instructor is included to let the students which instructor to look for in the course for the best understanding, assuming of course that GPA is indicative of a better teacher. If someone has a better heuristic to judge this, feel free to make a pull request. There were duplicates in the original dataset of that was actually scraped where the course name (e.g. AAS100) were different but the course title (e.g. Intro to Asian American Studies) was the same. Not really sure why they are there because most of these duplicates don't have descriptions but it might be that they are a part of the same courses or something like that. Since they don't have descriptions, I removed the duplicates and the edited file is "courses with atleast 2 gened reqs - no duplicates.csv" and "courses.csv" is just a copy of the same.  The dataset "courses with atleast 2 gened reqs - duplicates.csv" is the original one and contains duplicates. If you want to use that, rename it to "courses.csv" and it should work with the combinations program.
### Notes
* I skipped going through the Natural Science, Advanced Composition and Quantitative Reasoning requirements since most engineering and science majors will complete them through the 4 years in their major's curriculum. If you want to expand the dataset to include these, change and use scraping.py to extract those. 
* The GPA calculation isn't completely accurate as it only includes the fall 2019 GPA and a better calculation and idea of best instructor can be found [here][6]. The current implementation gives an approximate idea of how "easy" the course is so I think it works but if you want more accurate readings, it would be a good idea to either scrape the above link or calculate it yourself using [this dataset][2].
### Combinations
The second part of this small project is combinations.exe, which goes through the dataset and makes combinations of 2 courses whose general requirements do not overlap with each other. This includes the cultural studies restriction that students have to take one course that is designated as Western/Comparative Culture(s), one that is designated as Non-Western Culture(s), and one that is designated as U.S. Minority Culture, so only same cultural study course type is considered an overlap but not so with the rest of the general requirements where any type is considered an overlap. This also includes the restriction that courses that simultaneously satisfy the humanities and social science general requirements are not allowed to be taken as general education classes but this is satisfied by the dataset itself which doesn't contain such courses since none were present on the sites that were scraped. This makes combinations of 2 classes because most engineering majors have 2 gened classes in fall (assuming that you have credit for RHET 105 and therefore can skip it in fall, which you can find out [here][5].)
## Technical Stuff
### Scraping
scraping.py scrapes (ofc) the general requirements courses of fall 2020 from the [UIUC course explorer][1]. If you want to scrape the course explorer yourself, feel free to use my code or change it to your requirements. Note that I used selenium instead of requests as the course explorer generates the page of each course through Javascript and isn't loaded when requests gets the webpage while selenium waits for the whole page to load. 
To run scraper.py, you need to install the requirements present in the requirements.txt through pip using:
```pip install -r requirements.txt ``` and the opera driver for selenium [here][4] under the Browsers section. Opera because that's my current browser but feel free to download another. The only piece of code to change should be line 35 of scraper.py where the driver is launched.
### Combinations
The program runs a quite brute force method to get the combinations and for a dataset of this size, computation time is pretty small so it's not really necessary to optimize it. 

Sorry for the bad code, this was just a personal tool that I decided to share and I have other projects to work on so I'll be leaving this as it is.

[1]: https://courses.illinois.edu/gened/DEFAULT/DEFAULT
[2]: https://raw.githubusercontent.com/wadefagen/datasets/master/gpa/uiuc-gpa-dataset.csv
[3]: https://github.com/wadefagen/datasets/tree/master/gpa
[4]: https://www.selenium.dev/downloads/
[5]: https://citl.illinois.edu/citl-101/measurement-evaluation/placement-proficiency/proficiency-testing/subjects-with-proficiency-exams/rhetoric-proficiency
[6]: http://waf.cs.illinois.edu/discovery/grade_disparity_between_sections_at_uiuc/
[7]: https://github.com/ApoorvaAditya/uiuc-gened-classes#usage
[8]: https://github.com/ApoorvaAditya/uiuc-gened-classes#about
