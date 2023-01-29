# Find me in the Hearthstone Battlegrounds Leaderboards

A small project to finding you in the Hearthstone Battlegrounds leaderboards. The project is based on the new leaderboards of Hearthstone Battlegrounds that gives us all player playing Battlegrounds. But there are no way to find someone with a search bar, so I created a small program that gives your rank and the pages with your username and your rank.

![lb](https://user-images.githubusercontent.com/110813707/187700890-9426646c-3100-4c7f-86da-93ab8cb99827.png)

## How to use

Clone the project, install package write below and run the program. It will ask your four things : Name of the player, his rating, which season and which region. After that, the program will tell you your rank and on witch page you are

## Library to install

`pip install urllib3` 
`pip install requests`
`pip install bs4`

**Exemples**

![exemples](https://user-images.githubusercontent.com/110813707/187700724-1892d5a8-40ef-4676-9a8a-3be87a7a5195.png)

## Issues

* Sometime, the leaderboard will load only the top 200 of BG, so the number of pages will not be right and the program can't find player under top 200
* During the search, the page may not be completely loaded and therefore crash the program which will not be able to load the information correctly
* If you make a mistake on the username or the rating, the program will looping infinty so you can just close the window

---

## Disclaimer

* It is the [dichotomous algorithm](https://en.wikipedia.org/wiki/Dichotomic_search) searching the usersame (it is low iteration algorithm). But the leaderboard server is low so at every iteration, it takes some seconds to get the respond of the server, it is why it is slow
* I can't release a .exe because all antivirus will block the program
* I'm a beginner, so the code isn't perfect (and the english too)
