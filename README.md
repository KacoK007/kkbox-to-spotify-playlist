# kkbox to Spotify Playlist convertor
__Author: Kaco__
## Description
It scrape playlist from KKBOX, a music streaming platform, and put the songs into a new Spotify playlist.
It is written in python using the BeautifulSoup library, Spotipy library and Spotify API.

## How to use
1. install required library
    1. install BeautifulSoup library
       ```
       pip install BeautifulSoup4
       ```
    2. install Spotipy
       ```
       pip install spotipy
       ```
2. Set up your account in Spotify Developer Dashboard
   refer to [Getting started with Web API](https://developer.spotify.com/documentation/web-api/tutorials/getting-started/)

3. Put your own token and secret into the code

## Diffcult facing
    Spotify search sometimes gives wrong result, I believe it is a problem about the keyword search in spotify search api.
