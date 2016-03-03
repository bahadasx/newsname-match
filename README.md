NewsName-Match
==============

A tool for finding variations of names in news OCR'ed news articles

About
-----

This project is part of the District Data Research Labs on Entity Resolution

Data
----

This dataset contains OCR text extracted from the front page of newspapers in 1961.  It has been gathered from http://chroniclingamerica.loc.gov

Goal
----

The problem with these news article files is that there is no way to identify variations of particular names.  In this case, primary candidates from the 1916 election are being used.

The goal of this project is to provide a method in which to identify the occurrence of these candidates within a particular newspaper from a particular date, as well as how frequently these names appear.

Approach
--------

The first approach to solving this problem is to find variations of the defined candidate names within the text files and map them to the canonical name.  By performing this task, this map can be used to identify the frequency in which these variations appear in each newspaper.  This is performed by using the NLTK library which tokenizes sentences and separates them into parts of speech.  For example:

![alt tag](https://raw.githubusercontent.com/bahadasx/newsname-match/docs/ie-architecture.png)

```
Woodrow Wilson
```
