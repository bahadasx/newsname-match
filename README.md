NewsName-Match
==============

![Newspaper Image](https://commons.wikimedia.org/wiki/File%3AThe_San_Francisco_Call_newspaper_front_page%2C_thursday%2C_feb_8_1906%2C_featuring_Thomas_B._Bishop_closer_crop.png)

A tool for finding variations of person names in OCR'ed news articles

About
-----

This project is part of the District Data Research Labs on Entity Resolution

Data
----

This dataset contains OCR text extracted from the front page of newspapers in 1961.  It has been gathered from http://chroniclingamerica.loc.gov

Goal
----

The problem with these newspaper text files is that a person can be mentioned in a variety of ways in an article other than by using their full name.

The goal of this project is first, to create a method to identify all variations of a person's name that can be used and to create a map of those variations that can be used to perform further analytics such as how frequently a person's name appears per article/newspaper.

The goal of this project is the create a method of identifying mentions of a person's name, regardless of how they are mentioned.  This can then be used to perform further analytics such as how frequently a person's name appears per article/newspaper.

Approach
--------

The approach to solving this problem involves the use of a couple different libraries.  First, NLTK is used to tokenize sentences in each file and separate them into parts of speech.  Below is a diagram of the NLTK approach:

![NLTK Approach](/docs/ie-architecture.png)

By identifying all the person mentions in the files, you can then compare that to a canonical list of persons you are interested in(in this case it is presidential candidates from the 1916 election) to create a map.  For instance, Woodrow Wilson could be mapped to a number of variants used to describe him:

```
"Woodrow Wilson" -> ["President Wilson","W. Wilson", "Woodrow"]
```
