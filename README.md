# Dictionary-App-with-PyDictionary-tkinter
This is a simple dictionary Application using pyDictionary and tkinter. for Learning perpose. and below information I implement in this application

## What is pyDictionary ##

PyDictionary is a Dictionary Module for Python 2/3 to get meanings, translations, synonyms and Antonyms of words. It uses WordNet for
getting meanings, Google for translations, and thesaurus.com for getting synonyms and antonyms.

This module uses Python Requests, BeautifulSoup4 and goslate as

### dependencies ###

### Installation ###

Installation is very simple through pip (** or easy_install **)

**For pip**

```
pip install PyDictionary
```
### Usage ###

PyDictionary can be utilised in 2 ways, either by creating a dictionary instance which can take words as arguments or by creating a
dictionary instance with a fixed amount of words.

For example,

 ```python
 from PyDictionary import PyDictionary

dictionary=PyDictionary()
```

This is will create a local instance of the PyDictionary class and now it can be used to get meanings, translations etc.

``` python
print (dictionary.meaning("indentation"))
```

This will return a dictionary containing the meanings of the word. For

example the above code will return:

```
{'Noun': ['a concave cut into a surface or edge (as in a coastline', 'the

 formation of small pits in a surface as a consequence of corrosion', 'th

e space left between the margin and the start of an indented line', 'the

act of cutting into an edge with toothlike notches or angular incisions']

}
```
