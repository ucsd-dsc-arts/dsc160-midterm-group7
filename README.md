# Project Title

DSC160 Data Science and the Arts - Midterm Project Repository - Spring 2020

Project Team Members: 
- Kevin Elkin, kelkin@ucsd.edu
- Liam McCarthy, lamccart@ucsd.edu
- Umang Saraf, usaraf@ucsd.edu
- Charul Sharma, c4sharma@ucsd.edu
- Karan Sunil, ksunil@ucsd.edu

## Abstract

(10 points) 

For the project proposal, please write a short abstact addressing the questions below. You should replace the entire contents of this section with one to two paragraphs addressing the following:

In America, looking at the Billboard Hot 100 at any given time will reveal an overwhelming majority of  artists that are from America (or at least from the Western hemisphere). However, with the increased ease of information flow across continents, America has been exposed to and finally embraced Eastern cultures of music. From labels like 88Rising creating a label based solely around artists with Asian cultural influences, to the phenomenons of K-Pop and J-Pop, the songs getting millions of plays are no longer solely from Western artists. In our project, we are going to study the differences and similarities between the music of popular Eastern and Western artists, specifically in the genre of hip hop/rap. The data set we are going to analyze will be audio scraped and sampled from YouTube and contain modern-day artists from both the East and the West. Our data will be in the form of mp3 files similar to the ones analyzed in Exercise 2 using Librosa. 

The research question we will be attempting to answer is, just how different or similar are the eastern and western cultures of music? Are certain artists we view as completely different (i.e. K-Pop, hip hop, and Atlanta rap) somewhat sonically similar or are the Western influences more closely related to each other than to Eastern influences? Our hypothesis is that the modern day evolution of these cultures of music has led to distinct similarities in certain features while other features remain wildly diverse between eastern and western artists.

We will be using the mel frequency cepstral coefficients (MFCCs) as features to train our model, allowing us to describe the overall shape of a spectral envelope. Additionally, we will look to do EDA to further explore potential differences and similarities between the music types we have selected; this will allow for further feature creation and model performance. 

We will likely use a variety of analytical techniques to build our model including creating a training, testing, and validation dataset to accurately create a model that is suitable to use on unseen data. In addition to this we will likely use a variety of different models to test on such as SVM, Neural Networks (MLPClassifier, Keras Sequential classifier), Random Forest, Logistic Regression, etc. We will assess our model based on accuracy, and a Confusion Matrix. 

Our results will consist of models that will be used to predict that type of song. The performance of the model will be depicted through numbers, different graphs and charts and other visualization that best explains our findings. We would then study which features were more or less useful in differentiation of eastern and western music, using that information to find what similarities and differences the two styles have.

We will be using coarse and audio features for our project. We will obtain our coarse features from the spotify API. We will consider the following features - accousticness, dancability, duration (ms), energy, instrumentalness, key, liveness, loudness, mode, speechiness, tempo, time signature, valence. This would allow us to get an overview of the entire song and allows us to compare songs across the classes. Using 30 second previews of songs that we got from the Spotify API we will calculate the MFCC’s, chroma frequencies and spectoral centroid. This will gave us an understanding of the sound, feel and style of the song.


As the world’s rate of information exchange increased dramatically and we edge closer and closer to a global culture, it is interesting to study just how close we have already become. “East” and “west” are the primary binary used in describing global culture, and as these separations dissolve, humanity takes a leap towards unity. Music is often a defining trait of a culture, and its exchange is a defining characteristic of two cultures coming closer together. 

## Data

Our dataset was collected using the Spotify API. The data set was generated based on two different Genres, Chinese Hip Hop artists and Bay Area Hip Hop artists. Artists from Bay Area included Young A.Z., Jon Nash, Big Cholo etc. and artists from China included Straight Fire Gang, 謝帝, Lil Ghost小鬼, Machi DIDI etc. We were able to extract 86 artists that represented Bay area Hip hop and 110 artists that represented Chinese Hip hop.

We collected the top songs for each of the artists based on spotify's algorithm for top songs. The songs in our dataset were created between 1999-2020 but a majority of the songs were created in the past 3 years. Over 60% of all the songs in our dataset were created after 2016 
  <img src="results/year_dist.png"/>

The songs in our dataset were created by either hip hop artists from China or Bay Area, California.  We created two different datasets, one was in native form and the other was in .mp3 format. Spotify had a feature which enabled us to query the features of each song which was saved in [Spotify_data](https://github.com/ucsd-dsc-arts/dsc160-midterm-group7/blob/master/data/Spotify_data.csv). In addition to this, we also downloaded the preview URL of each of these songs. The file containing all the downloaded songs was too big in size for github so instead we added songs from 2 different artists in the test-music-data directory for testing purposes. 


## Code

(20 points)

This section will link to the various code for your project (stored within this repository). Your code should be executable on datahub, should we choose to replicate your result. This includes code for: 

### Data acquisition/scraping
[ELT](https://github.com/ucsd-dsc-arts/dsc160-midterm-group7/blob/master/code/ELT.py)- `Conatains library code for the data extraction process`

[Data-extraction](https://github.com/ucsd-dsc-arts/dsc160-midterm-group7/blob/master/code/Data-extraction.ipynb)- `Conatins code to extarct artists, tracks, audio features and dowload songs of each artist.`

To collect the data for the Bay area hip hop artists and Chinese Hip hop artists we made use of the spotipy library, a lightweight python API for Spotify. The spotipy library contained a search features that allowed us to query from their  database based on Genre, location and type. Once we created a list of artists we were using for our analysis, we queried the Top 10 tracks for each of these artists using Spotipy's top_tracks_artists function. Each track accompanied some meta data such as data released, duration etc., a preview URL 30 seconds long and URI which was a unique indicator for the track. The preview URL of each of these tracks was downloaded and saved to a directory based on genre (bay area hip hop or chinese hip hop) and artist name. The URI was then used to extract features for each track. The spotipy library contained a function that returned broad features of each song such as speechiness, danceability, energy, acousticness and 13 other features. All these features and some other meta data extracted from each track were saved in a dataframe with the artist's name, song URI and type of artist. 

### cleaning

### analysis

### generating results. 

Link each of your notebooks or .py files within this section, and provide a brief explanation of what the code does. Reading this section we should have a sense of how to run your code.

## Results

(30 points) 

This section will contain links to documentation of your results. This can include figures, sound files, videos, bitmaps, as appropriate to your domain of analysis. Each result should include a brief textual description, and all should be listed below: 

- image files (`.jpg`, `.png` or whatever else is appropriate)
- audio files (`.wav`, `.mp3`)
- written text as `.pdf`

 <img src="results/speechiness_density.png"/>
 
[Goon.mp4 - Bay Area High Variation 95th Percentile](Song_Variation_MFCC/Goon.mp4)

[In My Hood.mp4 - Bay Area Median Variation 50th Percentile](Song_Variation_MFCC/In_My_Hood.mp4)

[I'm a Gunner.mp4 - Bay Area Low Variation 5th Percentile](Song_Variation_MFCC/I'm_a_Gunner.mp4)

[隻手遮天.mp4 - China High Variation 95th Percentile](Song_Variation_MFCC/隻手遮天.mp4)

[Know My Style (feat. 艾福傑尼 & 黃旭) - Gizzle Remix.mp4 - China Median Variation 50th Percentile](Song_Variation_MFCC/Know_My_Style_Gizzle_Remix.mp4)

[Life Is Beautiful.mp4 - China Low Variation 5th Percentile](Song_Variation_MFCC/Life_Is_Beautiful.mp4)

## Discussion

(30 points, three to five paragraphs)

The first paragraph should be a short summary describing your results.

The subsequent paragraphs could address questions including:
- Why is this culturally relevant?
- How does your computational approach differ from the traditional art historical, musicological, manuel/subjective approach to analyzing your cultural subject? 
- How do you think the original artists/musicians would respond to this type of analysis? Would it change/inform their practice in some way?
- How do your results relate to broader social, cultural, economic political, etc., issues? 
- In what future directions could you expand this work?

## Team Roles

Provide an account of individual members and their efforts/contributions to the specific tasks you accomplished.

- Umang Saraf

I had the task of setting up the Spotify API to work with python and to create the dataset. I wrote the scrpits to extract all artists representing the 2 different Genres in study, get the songs for each artis and then download the preview of the song and extract audio features for each of the song.

- Kevin Elkin
- Liam McCarthy

- Charul Sharma
- Karan Sunil


## Technical Notes and Dependencies

Any implementation details or notes we need to repeat your work. 
- Additional libraries you are using for this project
  - Spotipy
  - urllib
  - pandas  

- Does this code require other pip packages, software, etc?

To run the code you need to obatin a credentials to use the spotify API from their developers website.

- Does this code need to run on some other (non-datahub) platform? (CoLab, etc.)

## Reference

References to any papers, techniques, repositories you used:
- Papers
- Repositories
  - https://github.com/plamere/spotipy
  
- Blog posts
  - https://medium.com/@maxtingle/getting-started-with-spotifys-api-spotipy-197c3dc6353b
  
  
