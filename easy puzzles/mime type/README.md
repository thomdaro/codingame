# Information for "MIME Type"

### Rules and Implementation

This one is fairly simple. We're given a series of file extensions and their associated MIME types, then a series of filenames. The filenames have extensions on them which may or may not have associated types. For every file that has an extension with a known type, we print the type. For every unknown extension, we simply print `UNKNOWN`.

A typical round of input looks like this:

* __Line 1__: a number `N`, which is the number of elements in the association table.
* __Line 2__: a number `Q`, which is the number of files to be processed.
* __Next N Lines__: an extension and the corresponding MIME type, separated by a space.
* __Next Q Lines__: the filenames to be analyzed.

Python makes this fairly simple, as we can use a dictionary to associate extensions and MIME types. `lower()` is used to mitigate case comparison issues. Filenames may have multiple dots to trick us into associating the wrong extension, so we can use `rfind` to search backwards though the string and get all characters after the last dot. From here, it's a simple matter of checking if the given extension is in the association table.

### Orginal Codingame Problem

https://www.codingame.com/ide/puzzle/mime-type
