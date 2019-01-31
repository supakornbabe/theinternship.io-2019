# Hangman
## Credit
CSV to JSON : http://www.convertcsv.com/csv-to-json.htm
## How To Play
> python hangman.py

## How to add new category

You need to have category in json file with this template below.

```json
{
    "WORDLIST": [{
        "TITLE": "Kasetsart University",
        "HINT1": "Thailand",
        "HINT2": "Bangkok"
    }, 
    ...
    ],
    "HINT": "any hint to say with $HINT1 and $HINT2"
}
```