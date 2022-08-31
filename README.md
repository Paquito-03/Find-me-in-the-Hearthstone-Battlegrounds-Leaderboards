# Find me in the Hearthstone Battlegrounds Leaderboards

A small project to finding you in the Hearthstone Battlegrounds leaderboards. The project is based on the new leaderboards of Hearthstone Battlegrounds that gives us all player playing Battlegrounds. But there are no way to find someone with a search bar, so I created a small program that gives your rank and the pages with your username and your rank.

![lb](https://user-images.githubusercontent.com/110813707/187700890-9426646c-3100-4c7f-86da-93ab8cb99827.png)

## How to use

Download the last release, run it, it will ask you the username are you looking for (upper and lower case are important) then press enter. After put the rating of the player, press enter again and the program will research the player

**Exemples**

![exemples](https://user-images.githubusercontent.com/110813707/187700724-1892d5a8-40ef-4676-9a8a-3be87a7a5195.png)

---

## Library to install

`pip install urllib3` 
`pip install requests`
`pip install bs4`

## Disclaimer

* At this moment, it work only in Europe
* It is the [dichotomous algorithm](https://en.wikipedia.org/wiki/Dichotomic_search) searching the usersame (it is low iteration algorithm). But the leaderboard server is low so at every iteration, it takes some seconds to get the respond of the server, it is why it is slow
* If you make a mistake on the username or the rating, the program will looping infinty so you can just close the window
* I'm a beginner, so the code is'nt perfect (and the english too)
