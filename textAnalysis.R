rm(list = ls())
require(tm)
require("wordcloud")
require("ggplot2")
require("dplyr")
require("xtable")
require("syuzhet")
require(readr)

setwd("Vox Scrape")

wordCorpus = VCorpus(DirSource("Stromberg"))
wordCorpus = wordCorpus %>% tm_map(removePunctuation) %>% 
                            tm_map(content_transformer(tolower)) %>%
                            tm_map(removeWords, stopwords("english")) %>%
                            tm_map(stripWhitespace)
dtm = DocumentTermMatrix(wordCorpus)
dtm<-as.matrix(dtm)
v <- sort(colSums(dtm),decreasing=TRUE)

head(v,14)
words <- names(v)

d <- data.frame(word=words, freq=v)
pal <- brewer.pal(9,"YlGnBu")
pal <- pal[-(1:4)]
set.seed(52)

png("WordCloud.png", width=12,height=8, units='in', res=300)
wordcloud(d$word,d$freq,scale=c(5,0.3), max.words=100, random.order=FALSE, 
          rot.per=0.1, use.r.layout=FALSE, colors=pal)
dev.off()

