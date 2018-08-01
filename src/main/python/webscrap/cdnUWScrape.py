import re, requests, bs4, csv, datetime


def CAUW_PRSS_Scrape(numPages):
    # Canadian Underwiter Headlines
    # https://www.canadianunderwriter.ca/inspress/page/2/
    # https://www.canadianunderwriter.ca/inspress/

    # Preset BeautifulSoup tag selection criteria
    tagPick_HL = '.media-body .headline.media-heading' #Headline
    tagPick_SL = '.media-body .meta' #Subline (date and company)
    output = [] # Initialize List, to contain Tuples. Each Tuple representing
    # a (Headline, date, author).

    # Preset Regular Expressions to remove white space characters etc. (incl new lines)
    # and to break down sub-headline into Date and Author.
    regex_HL = re.compile(r'^[\s]+|[\s]+$') # identify all leading or ending white spaces
    regex_SL_date = re.compile(r'[A-Z]{1}[a-z]{2,8}[ ]{1}\d{1,2},[ ]\d{4}') # identify Month (1 upper case letter followed by 2-8
    # lower case letters), space, Day (1-2 digit number),
    # comma, space, and Year(4 digit number).
    regex_SL_enty = re.compile(r'( by ).+$') # identify ' by ' and any characters to the end

    # From Page 1 to the last page...
    for i in range(1,numPages+1):
        # Set URL, using the incrementing i as the page number
        url = 'https://www.canadianunderwriter.ca/inspress/page/'+str(i)+'/'
        mySoup = bs4.BeautifulSoup(requests.get(url).text, 'html.parser')
        # On page i, numHeadlines holds number of articles
        numHeadlines = len(mySoup.select(tagPick_HL))
        # Cross check that there's as many Sub-Headlines as Articles on the page.
        if numHeadlines==len(mySoup.select(tagPick_SL)):
            # If above checks ok, capture a (Headline, Date, Author) Tuple and append to output[] list.
            for j in range(numHeadlines): #j counts from first to last article on page i
                # Refer Preset Regular Expressions above
                output.append((regex_HL.sub('',mySoup.select(tagPick_HL)[j].getText()), #replace identified Regex w/ '' (nothing)
                               regex_SL_date.search(mySoup.select(tagPick_SL)[j].getText()).group(), #capture identified Regex
                               regex_SL_enty.search(mySoup.select(tagPick_SL)[j].getText()).group().strip() #same, plus trim
                               ))
        else: print('Error on page '+str(i))

    print('Canadian Underwriter Headlines Scrape Complete. CSV file writing in working path...')

    # The below converts our output[] list of Tuples to a comma-seperated-values (csv) file, ready for analysis in R (or Excel).
    # 'dump' represents a new file written (to be written) with the specified filename
    dump = open('cdnUWScrape.csv','w',newline='',encoding='utf-8') #hardcode encoding. was getting encoding error.
    #https://stackoverflow.com/questions/16346914/python-3-2-unicodeencodeerror-charmap-codec-cant-encode-character-u2013-i
    # Initialize a csv writing Python engine, so to speak
    csvWriter = csv.writer(dump,delimiter=',',lineterminator='\n')
    # writing engine to write one line for each element in output[]. In our case, it's one Tuple/record of Headline, Date, Author
    for i in range(len(output)):
        csvWriter.writerow(output[i])
        # close the csv file after writing is complete.
    dump.close()
    print('CSV file written.')

    #Check in Console
    for k in range(len(output)):
        print(str(output[k]))

if __name__ == '__main__':
    CAUW_PRSS_Scrape(5)