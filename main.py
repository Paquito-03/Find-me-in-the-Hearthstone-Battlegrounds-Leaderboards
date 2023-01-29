from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

playerToFind = input("What player do you search : ")
playerToFindRating = int(input("How many rating : "))
seasonReseach = int(input("What season are you looking for : "))
regionResearch = int(input("Which region are you looking for (US = 1, AP = 2, EU = 3) : "))

seasonReseach -= 1  # seasonId starting to 0, so season 9 have the 8 id

# replace number enter by user by the right word for the url
if regionResearch == 1:
    regionResearch = "US"
elif regionResearch == 2:
    regionResearch = "AP"
elif regionResearch == 3:
    regionResearch = "EU"

url = 'https://hearthstone.blizzard.com/fr-fr/api/community/leaderboardsData?region=' + str(regionResearch) + '&leaderboardId=battlegrounds&page=10&seasonId=' + str(seasonReseach)  # open a request for taking the max pages
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})  # to prove we are not a robot

webpage = urlopen(req).read()  # read the page
page_soup = soup(webpage, "html.parser")  # make it readable
textFind = str(page_soup)  # transform the page for use fonction like .find()
pageMaxFind = textFind.find("totalPages")  # find the position in the string (textFind)

x = 0  # for the while
maxPage = ""  # be sure it is empty
while textFind [pageMaxFind + 12 + int(
        x)] in "0123456789":  # loop for collect number of page : it is reading 12 letter after the position of totalPages in the request and loop when it is a figure. it avoid to make mistake for number because we don't known how many figure the number has
    maxPage = maxPage + textFind [pageMaxFind + 12 + int(x)]
    x = x + 1
maxPage = int(maxPage)  # convertion into a int
minPage = 1  # the first page
i = int((maxPage + minPage) / 2)  # for dichotomous algorithm
goAHead = True  # when he found page with the same rating, it search one + one, if he doesnt find the player, it goes into the 1 - 1

while True:  # it is horrible, i know
    url = 'https://hearthstone.blizzard.com/fr-fr/api/community/leaderboardsData?region=' + str(regionResearch) + '&leaderboardId=battlegrounds&page=' + str(
        i) + '&seasonId=' + str(seasonReseach)  # url with the page number of i
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    page_soup = soup(webpage, "html.parser")
    textFind = str(page_soup)
    pageRating = textFind.find("rating\":")  # to find the position of the  word rating

    x = 0
    iRating = ""
    while textFind [pageRating + 8 + int(x)] in "0123456789":  # same loop for MaxPage
        iRating = iRating + textFind [pageRating + 8 + int(x)]
        x = x + 1

    posPlayer = textFind.find(playerToFind)  # to find if the player is on this page

    if posPlayer != -1:  # if the player is find
        displayRank = ""  # same loop for MaxPage
        x = 0
        while textFind [posPlayer + len(playerToFind) + len(str(playerToFindRating)) + 21 + int(x)] in "0123456789":
            displayRank = displayRank + textFind [
                posPlayer + len(playerToFind) + len(str(playerToFindRating)) + 21 + int(x)]
            x = x + 1
        print("We find " + playerToFind + " at page " + str(
            i) + ", rank : " + displayRank)  # print the Name, page where is it and its rank
        break  # exit this loop
    else:  # if the player isn't find
        if playerToFindRating > int(iRating):  # if the player has more rating then the page
            maxPage = int(i)
            i = int((maxPage + minPage) / 2)
            goAHead = False  # change the direction if the player has the same rating as the page
        elif playerToFindRating < int(iRating):  # if the player has less rating then the page
            minPage = int(i)
            i = int((maxPage + minPage) / 2)
            goAHead = True  # change the direction if the player has the same rating as the page
        else:  # if the player has the same rating as the page. It is for when he found page with the same rating, it search one + one, if he doesnt find the player, it goes into the 1 - 1
            if goAHead:
                i = i + 1
            else:
                i = i - 1
        print("Searching page " + str(
            i) + " (best rating on this page : " + iRating + ")")  # for see what page he is looking for

# small condition to exit the program with only pressing enter
x = input("Hit Enter to Exit")
if not x:
    print("Exiting the Program.")
    exit()
