# Scrapping Data from MyAnimeList

## Overview
This project aims to scrape data from MyAnimeList, collecting a vast amount of information from over 19,000 entries, including details such as titles, rankings, URLs, cover images, the number of episodes, and scores. The scraped data is then transformed into a structured JSON format for easy integration and consumption by other applications.

The data retrieval is achieved by making HTTP requests to the MyAnimeList API URLs, as the website sources its data from these APIs. You can identify the API URLs by using browser developer tools.

This project leverages Scrapy, a powerful web scraping framework, to automate the data collection process, ensuring efficiency and accuracy in the extraction of MyAnimeList data.

## Features
- Successfully scraped more than 19,000 entries from MyAnimeList.
- Gathered information, including titles, rankings, URLs, cover images, episode counts, and scores.
- Transformed the scraped data into a structured JSON format for easy integration with other applications.
- Utilized Scrapy to automate the data collection process, ensuring efficiency and accuracy.

## Data Sample
```bash
{"id": 2578, "rank": "5107", "title": "TaoTao Ehonkan Sekai Doubutsu Banashi", "url": "https://myanimelist.net/anime/2578/TaoTao_Ehonkan_Sekai_Doubutsu_Banashi", "image": "https://cdn.myanimelist.net/images/anime/9/3365.jpg", "listStatus": null, "mediaType": "TV", "numEpisodes": 52, "score": "6.77", "numListUsers": 1236, "status": 2},
{"id": 1208, "rank": "5108", "title": "Tatsu no Ko Tarou", "url": "https://myanimelist.net/anime/1208/Tatsu_no_Ko_Tarou", "image": "https://cdn.myanimelist.net/images/anime/1874/112893.jpg", "listStatus": null, "mediaType": "Movie", "numEpisodes": 1, "score": "6.77", "numListUsers": 4068, "status": 2},
{"id": 54275, "rank": "5109", "title": "Temple", "url": "https://myanimelist.net/anime/54275/Temple", "image": "https://cdn.myanimelist.net/images/anime/1879/136896.jpg", "listStatus": null, "mediaType": "TV", "numEpisodes": 12, "score": "6.77", "numListUsers": 64949, "status": 2},
{"id": 10351, "rank": "5110", "title": "Tenchi Muyou! Ryououki 2nd Season Picture Drama", "url": "https://myanimelist.net/anime/10351/Tenchi_Muyou_Ryououki_2nd_Season_Picture_Drama", "image": "https://cdn.myanimelist.net/images/anime/9/28449.jpg", "listStatus": null, "mediaType": "Special", "numEpisodes": 1, "score": "6.77", "numListUsers": 6019, "status": 2},
{"id": 12727, "rank": "5111", "title": "Thermae Romae Specials", "url": "https://myanimelist.net/anime/12727/Thermae_Romae_Specials", "image": "https://cdn.myanimelist.net/images/anime/2/35741.jpg", "listStatus": null, "mediaType": "Special", "numEpisodes": 2, "score": "6.77", "numListUsers": 4055, "status": 2},
{"id": 2715, "rank": "5112", "title": "Totsuzen! Neko no Kuni Banipal Witt", "url": "https://myanimelist.net/anime/2715/Totsuzen_Neko_no_Kuni_Banipal_Witt", "image": "https://cdn.myanimelist.net/images/anime/6/58211.jpg", "listStatus": null, "mediaType": "Movie", "numEpisodes": 1, "score": "6.77", "numListUsers": 2869, "status": 2},
{"id": 48952, "rank": "5113", "title": "Twisted-Wonderland 1-shuunen Kinen PV", "url": "https://myanimelist.net/anime/48952/Twisted-Wonderland_1-shuunen_Kinen_PV", "image": "https://cdn.myanimelist.net/images/anime/1477/115439.jpg", "listStatus": null, "mediaType": "ONA", "numEpisodes": 1, "score": "6.77", "numListUsers": 1353, "status": 2},
{"id": 1925, "rank": "5114", "title": "Urusei Yatsura Movie 6: Itsudatte My Darling", "url": "https://myanimelist.net/anime/1925/Urusei_Yatsura_Movie_6__Itsudatte_My_Darling", "image": "https://cdn.myanimelist.net/images/anime/5/88665.jpg", "listStatus": null, "mediaType": "Movie", "numEpisodes": 1, "score": "6.77", "numListUsers": 8143, "status": 2},


