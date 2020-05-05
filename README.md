# The Racial Backlash of Pandemics
### Yunkai Tang and Joyce Guo
---------------------------------------
## Introduction
As two people of asian descent experiencing the global covid-19 pandemic in New York City, we felt we were constantly hearing stories from our fellow asian classmates about hate-based incidents--the derorgatory message left on a Columbia whiteboard, an angry side-comment of a passerby telling us to "go back", the suddenly cleared hole in subway space from neighbors scared to touch you. We wanted a way to document these stories and more importantly we wanted a way to measure this very real racial backlash that seems to follow not only this pandemic, but a history of epidemics and diseases. In a time when we are being told to rely on data, we wanted to use that data to give these stories another dimensions, to illustrate just how concrete and palpable the increase in racial tension is. 
## Data
For our data, we wanted to analyze a social-media platform in order to gauge sentiment towards Asians, however most social media platforms we considered (facebook, twitter, instagram) both did not allow unrestricted access to their data and did not fully anonymize their users. As such we drew inspiration from past work like Vice's  [article](https://www.vice.com/en_us/article/d3nbzy/we-analyzed-more-than-1-million-comments-on-4chan-hate-speech-there-has-spiked-by-40-since-2015), and focused our analysis on data from the image-board site 4chan, which allowed for anonymous users and unrestricted access to their data. 4chan also conveniently has an archive site, 4plebs, which archives posts from the /pol board (which stands for politically incorrect and which all our analysis is done off of).

For data prior to 2019, we used this [data] (https://archive.org/details/4plebs-org-data-dump-2020-01) from archive.org
For data after January 4, 2020, we created a web crawler also located in this repo under 4chan_crawler.py because unfortunately there had been no data dump yet of data post Jan 2020.

## Analysis
For the analysis of the data, we once again took inspiration from the Vice 2019 article and decided to gauge racial-tension through frequency of hate-terms which were classified as "Asian" hate-terms.
For this dictionary, we used [HateBase](https://hatebase.org/), which provides a free api and access to different classification of hate-terms. We decided to use this dictionary because it is widely used in academia and media, however a huge drawback of this approach is that alot of the terms seemed either outdated, recycled into a different meaning, or the database itself was missing obvious racial epiteths that are in circulation today. But we used this database without editing it or adding to it in order to remove our own personal biases from this part of the analysis as much as possible. 

We chose to do text analysis and ran a script which would go through the data, and count the number of posts in a given day contained "Asian" hate terms, to see how many times such terms were used on /pol and to see if there were any correlations with the pandemic timing. We then did the same analysis, but with a dictionary of "African" targeted hate-terms (as defined by Hatebase).

## Summary of results
The Asian-directed hate-term analysis yielded the following graph: 
(please note that the break in data from 2020-01-04 to 2020-04-24 are because that is where the archive data ends and when our webcrawler started) ![image](https://github.com/jguo13/ITFinalProject/blob/master/Asian-hateterm-frequency.png)

Im the months leading up to the epidemic, the amount of posts containing hate-terms directed at Asians hovered around 50 posts/day. For the week of March 24 to April 2, the number of posts increased to around the 300-200 range, an increase of around 500%.

When we ran the same analysis for African targeted hate-terms in 2014 (when the ebola epidemic was at its worst), we found a very similar trend. Our analysis yielded the following graph: ![image](https://github.com/jguo13/ITFinalProject/blob/master/African-hateterm-frequency.png)

As can be seen, there is a similar spike in hate-based terms from around 100 in August of 2014 to spiking into well-over 300 posts a day containing hate-based terms derogatory towards Africans after the same time we saw the first case of ebola in NYC. 

## Future work
In order to strengthen our analysis, we would like to finely and manually comb through the posts that our programs classified as "containing hate-speech" to see if there is any additional data to be gleaned from these posts, as well as to rule out any confounding event besides the pandemic that could be causing the increase in hate-speech.
