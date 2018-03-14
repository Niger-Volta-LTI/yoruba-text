from bs4 import BeautifulSoup
import requests
import time
import os

bib_books = dict()
bib_books['GEN'] = 50  # GEN.1.BMY --> GEN.50.BMY
bib_books['EXO'] = 40  # EXO.1.BMY --> GEN.40.BMY
bib_books['LEV'] = 27
bib_books['NUM'] = 36
bib_books['DEU'] = 34
bib_books['JOS'] = 24
bib_books['JDG'] = 21
bib_books['RUT'] = 4
bib_books['1SA'] = 31
bib_books['2SA'] = 24
bib_books['1KI'] = 22
bib_books['2KI'] = 25
bib_books['1CH'] = 29
bib_books['2CH'] = 36
bib_books['EZR'] = 10
bib_books['NEH'] = 13
bib_books['EST'] = 10
bib_books['JOB'] = 42
bib_books['PSA'] = 150
bib_books['PRO'] = 31
bib_books['ECC'] = 12
bib_books['SNG'] = 8
bib_books['ISA'] = 66
bib_books['JER'] = 52
bib_books['LAM'] = 5
bib_books['EZK'] = 48
bib_books['DAN'] = 12
bib_books['HOS'] = 14
bib_books['JOL'] = 3
bib_books['AMO'] = 9
bib_books['OBA'] = 1
bib_books['JON'] = 4
bib_books['MIC'] = 7
bib_books['NAM'] = 3
bib_books['HAB'] = 3
bib_books['ZEP'] = 3
bib_books['HAG'] = 2
bib_books['ZEC'] = 14
bib_books['MAL'] = 4
bib_books['MAT'] = 28
bib_books['MRK'] = 16
bib_books['LUK'] = 24
bib_books['JHN'] = 21
bib_books['ACT'] = 28
bib_books['ROM'] = 16
bib_books['1CO'] = 16
bib_books['2CO'] = 13
bib_books['GAL'] = 6
bib_books['EPH'] = 6
bib_books['PHP'] = 4
bib_books['COL'] = 4
bib_books['1TH'] = 5
bib_books['2TH'] = 3
bib_books['1TI'] = 6
bib_books['2TI'] = 4
bib_books['TIT'] = 3
bib_books['PHM'] = 1
bib_books['HEB'] = 13
bib_books['JAS'] = 5
bib_books['1PE'] = 5
bib_books['2PE'] = 3
bib_books['1JN'] = 5
bib_books['2JN'] = 1
bib_books['3JN'] = 1
bib_books['JUD'] = 1
bib_books['REV'] = 22

prefix = "https://www.bible.com/bible/911/"

def bible_strings():
    for book in bib_books:
        # print(book, bib_books[book])
        for chapter in range(1, bib_books[book]+1):
            url_string = prefix + book + "." + str(chapter) + ".BMY"
            # print(url_string)
            yield url_string

def scrape_chapter(url):

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    text = ""
    # Take out the <div> of name and get its value
    heading = soup.find_all('span', attrs={'class': 'heading'})
    # grab chapter heading
    try:
        text += heading[0].contents[0] + "."  # do we need headings, should these go to their own file?
    except IndexError:
        # print("IndexError @  " + url)
        text = ""

    for verse in soup.find_all('span', attrs={'class': 'content'}):
        utt = verse.contents[0]
        if len(utt) > 0:
            text += utt + " "  # iohavoc -- get rid of this

    return text


for url_string in bible_strings():
    with open("chapters/bibeli_ede_yoruba_" + os.path.basename(url_string) + ".txt", 'w', encoding='utf-8') as f:
        print("Scraping: " + url_string)
        blurb = scrape_chapter(url=url_string)
        f.write(blurb)
        #time.sleep(5.5)

# url_string = "https://www.bible.com/bible/911/2PE.1.BMY"
# print(scrape_chapter(url=url_string))