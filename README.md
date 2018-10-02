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

Oppgave 2: Dataforståelse (10%)
-------------------------------

**1) Hva slags datasett er dette? Forklar hva slags objekter det er snakk om, og hva slags attributter (egenskaper) de har, samt eventuelle relasjoner.**

**2) Hva slags datatyper fins i datasettet? Gi konkrete eksempler og begrunn svaret ditt.**

Oppgave 3: Nytteverdi (15%)\*\*
-------------------------------

**1) Hva kan du bruke datasettet til? Vis 3 forskjellige anvendelser, eller eksempler på verdi du kan få ut av datasettet.**

**2) Er datasettet klart til å analyseres som det er, eller må noe bearbeides før bruk? Begrunn svaret ditt.**

Oppgave 4: Analyse og modellering (40%)
---------------------------------------

**1) Hvilke metoder vil du bruke for å analysere dataene, gitt minst en av anvendelsene du har nevnt over? Her bør du tenke over ting som modeller (f.eks. innen maskinlæring), statistiske metoder, visualiseringer og tilsvarende. Begrunn metodene du har valgt.**

**2) Gjennomfør analysene som nevnt over.**

Oppgave 5: Resultat og evaluering (30%)
---------------------------------------

**1) Hva fikk du ut av dataene? Her skal du vise konkrete tall, figurer, visualiseringer og liknende.**

**2) Gjennomfør en kritisk refleksjon over resultatet og innsikten du har kommet frem til. Gjør bruk av pensumlitteraturen og andre relevante kilder for å begrunne din argumentasjon.**
