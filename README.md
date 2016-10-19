# Vox-Scrape
# Synopsis

This project contains a short python script ("scrapeArticles.py") that is set up to scrape the text of a Vox.com journalist
and save the output in text files.  There is also an R Script ("textAnalysis.r") that takes the articles and produces a wordcloud
and histogram of most commonly used words in the articles.

# How to use

To run the python script, you need to supply two arguments.  The first is the name of the Vox.com journalist whose articles
you intend to scrape (As it appears in the URL for their archive on Vox).  The second is a folder in which to store the articles.  For example, the script was run on Joseph Stromberg
by entering the command python scrapeArticles.py Joseph-Stromberg Stromberg.  Once the python script is run, you can run the R script to produce the charts.

# Motivation

I am relatively new to both Python and R, and trying to learn more of each.  I am friends with the example journalist and thought it might be fun
to analyze his work.

