# spotistash

![GitHub](https://img.shields.io/github/license/jibstack64/spotistash) 

*A script I cooked up that compiles all of your playlist's songs to a single playlist.*

![image](https://user-images.githubusercontent.com/107510599/221301053-2db1a718-d5af-4468-a3ba-27f2f327b7ef.png)

Simply change the `CLIENT_ID` and `CLIENT_SECRET` variables to the values corresponding with your Spotify bot client.

You can create a playlist based on **other people's** playlists by providing the link to their Spotify profile, like so: `python spotistash.py <url>`.

If you'd like, you may choose to increase `MAX`. The higher the `MAX`, the more playlists and songs the script will capture and add to the new playlist. However, it is very unlikely you have over 1000 playlists...

**You may randomly get a `Insufficient client scope` error. This is fault of Spotify's API and not the program.**

