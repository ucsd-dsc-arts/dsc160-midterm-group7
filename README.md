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

We will be using the mel frequency cepstral coefficients (MFCCs) as features to train our model,, allowing us to describe the overall shape of a spectral envelope. Additionally, we will look to do EDA to further explore potential differences and similarities between the music types we have selected; this will allow for further feature creation and model performance. 

We will likely use a variety of analytical techniques to build our model including creating a training, testing, and validation dataset to accurately create a model that is suitable to use on unseen data. In addition to this we will likely use a variety of different models to test on such as SVM, Neural Networks (MLPClassifier), Random Forest, Logistic Regression, Gradient Boost Classifier, etc. We will assess our model based on F1 Score, Precision, Recall, Accuracy, and a Confusion Matrix. 

Our results will consist of models that will be used to predict that type of song. The performance of the model will be depicted through numbers, different graphs and charts and other visualization that best explains our findings. We would then study which features were more or less useful in differentiation of eastern and western music, using that information to find what similarities and differences the two styles have.

We will mainly be using techniques used in this class like MFCC’s for our project. We will be working on a problem similar to that in exercise 2, and expand the same by also using techniques like zero crossing rate, energy and autocorrelation. Further, we will be looking into more metrics like F1 Score, Precision, Recall, Accuracy, and a Confusion Matrix which was not covered in the class. We will also be working with different classification models.

As the world’s rate of information exchange increased dramatically and we edge closer and closer to a global culture, it is interesting to study just how close we have already become. “East” and “west” are the primary binary used in describing global culture, and as these separations dissolve, humanity takes a leap towards unity. Music is often a defining trait of a culture, and its exchange is a defining characteristic of two cultures coming closer together. 

## Data

(10 points) 

This section will describe your data and its origins. Each item should contain a name of the data source, a link to the source, and any necessary background information such as:
- What is your cultural data source? 
- When was it made? 
- Who created the works? 
- Is it digital native, or is it some kind of scan, recording, photo, etc., of an analog form? 

## Code

(20 points)

This section will link to the various code for your project (stored within this repository). Your code should be executable on datahub, should we choose to replicate your result. This includes code for: 

- data acquisition/scraping
- cleaning
- analysis
- generating results. 

Link each of your notebooks or .py files within this section, and provide a brief explanation of what the code does. Reading this section we should have a sense of how to run your code.

## Results

(30 points) 

This section will contain links to documentation of your results. This can include figures, sound files, videos, bitmaps, as appropriate to your domain of analysis. Each result should include a brief textual description, and all should be listed below: 

- image files (`.jpg`, `.png` or whatever else is appropriate)
- audio files (`.wav`, `.mp3`)
- written text as `.pdf`

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

## Technical Notes and Dependencies

Any implementation details or notes we need to repeat your work. 
- Additional libraries you are using for this project
- Does this code require other pip packages, software, etc?
- Does this code need to run on some other (non-datahub) platform? (CoLab, etc.)

## Reference

References to any papers, techniques, repositories you used:
- Papers
- Repositories
- Blog posts
