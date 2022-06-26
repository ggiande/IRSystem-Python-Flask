#IRSystem
The Information Retrieval System implements the IRSystemABC class. This class will take the list of files, open them, process the words in the files, and build the IRSystem. The IRSystem inherits the _list_files:_ contains the list of files that the system is built upon and _list_words:_ the list of words inside the files. Each entry is of type Word. The IRSystem has the _build_system_ method, that fully processes the files for IRSystem. The _word_search_ method is a helper method for build_system that searches if a string is in other instances of Word. If so, it collects a list of instances of Word. The _query_search_ method, returns relevant docs associated with Word as a list of strings. The _word_frequency_ method returns the frequency of a word. If the word does not exist, then it returns a -1.


- [ ] Consider rewriting build system to match an inverted index
 

# Regex Explanation
```regexp
([A-z])\-([A-z])

Match the regex below and capture its match into backreference number 1 «([A-z])»
   Match a single character in the range between “A” and “z” «[A-z]»
Match the character “-” literally «\-»
Match the regex below and capture its match into backreference number 2 «([A-z])»
   Match a single character in the range between “A” and “z” «[A-z]»

\1 \2

Insert the text that was last matched by capturing group number 1 «\1»
Insert the character “ ” literally « »
Insert the text that was last matched by capturing group number 2 «\2»
```