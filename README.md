Eksamensoppgave INS300 Data Science – Høsten 2018
================

### Oppgave utført av Khalid & Pär

Oppgave 1: Importering av data (5%)
-----------------------------------

Denne oppgaven innebærer å analysere og arbeide med et datasett. Du har to valgmuligheter:

**1) Du kan bruke datasettet som er vedlagt i filen «restaurant-and-market-health- inspections.csv»**

eller

**2) Du kan velge et datasett fra nettstedet www.kaggle.com . Hvis du velger et eget datasett, skal dette godkjennes av Siri (email <siri.fagernes@kristiania.no> ) før du går i gang med oppgaven.**

Including Code
--------------

You can include R code in the document as follows:

``` r
  dataset <- read.csv("csv/restaurant-and-market-health-inspections.csv")
```

Including ggplot2
-----------------

``` r
  library(ggplot2)
  ggplot(dataset, aes(score, facility_zip)) + geom_point()
```

![](README_files/figure-markdown_github/ggplot-1.png)
