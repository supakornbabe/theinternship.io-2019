# Hangman
## Credit
CSV to JSON : http://www.convertcsv.com/csv-to-json.htm
## Usage
> cd hangman

> python hangman.py

## How to add new category

You need to have category in json file with this template below.

```json
{
    "WORDLIST": [{
        "TITLE": "Word to play",
        "HINT1": "Hint 1",
        "HINT2": "Hint 2"
    }, 
    ...
    ],
    "HINT": "any hint to say with $HINT1 and $HINT2"
}
```