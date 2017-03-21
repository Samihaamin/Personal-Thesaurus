# Personal-Thesaurus
A program to create personal dictionary &amp; thesaurus, allowing transitive properties of synonyms.

Feed in data file in the following format (lines can be in any order):
```
addWord:word1:definition1
lookupWord:word1
addSynonym:cold:chilly
addSynonym:chilly:freezing
lookupSynonyms:cold
```

Terminal command to run the program with the text-file as input:
```
python dict.py data.txt
```
