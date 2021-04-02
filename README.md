
# PyPoetry

**PyPoetry** is a simple tool with a convenient interface for manipulating **poems**.

### Requirements
- [**Python 3.9**](https://www.python.org/downloads/)

## Examples

```py
from pprint import PrettyPrinter

from pypoetry import Poem


text = """
Mignonne, allons voir si la rose
Qui ce matin avoit desclose
Sa robe de pourpre au Soleil,
A point perdu ceste vesprée
Les plis de sa robe pourprée,
Et son teint au vostre pareil.

Las ! voyez comme en peu d'espace,
Mignonne, elle a dessus la place
Las ! las ses beautez laissé cheoir !
Ô vrayment marastre Nature,
Puis qu'une telle fleur ne dure
Que du matin jusques au soir !

Donc, si vous me croyez, mignonne,
Tandis que vostre âge fleuronne
En sa plus verte nouveauté,
Cueillez, cueillez vostre jeunesse :
Comme à ceste fleur la vieillesse
Fera ternir vostre beauté.
"""

printer = PrettyPrinter()
poem = Poem(text)
```

### Get the form of a poem

```py
print(poem.form)
```
**Output:**
```py
(6, 6, 6)  # Three strophes of six verses.
```

### Iterate on the strophes and verses of a poem

```py
for strophe in poem:
    for verse in strophe:
        printer.pprint(verse)
    print()  # Print a blank line.
```
**Output:**
```py
'Mignonne, allons voir si la rose'
'Qui ce matin avoit desclose'
'Sa robe de pourpre au Soleil,'
'A point perdu ceste vesprée'
'Les plis de sa robe pourprée,'
'Et son teint au vostre pareil.'

"Las ! voyez comme en peu d'espace,"
'Mignonne, elle a dessus la place'
'Las ! las ses beautez laissé cheoir !'
'Ô vrayment marastre Nature,'
"Puis qu'une telle fleur ne dure"
'Que du matin jusques au soir !'

'Donc, si vous me croyez, mignonne,'
'Tandis que vostre âge fleuronne'
'En sa plus verte nouveauté,'
'Cueillez, cueillez vostre jeunesse :'
'Comme à ceste fleur la vieillesse'
'Fera ternir vostre beauté.'

```

### Get the reverse poem

```py
printer.pprint(reversed(poem))
```
**Output:**
```py
[['Fera ternir vostre beauté.',
  'Comme à ceste fleur la vieillesse',
  'Cueillez, cueillez vostre jeunesse :',
  'En sa plus verte nouveauté,',
  'Tandis que vostre âge fleuronne',
  'Donc, si vous me croyez, mignonne,'],
 ['Que du matin jusques au soir !',
  "Puis qu'une telle fleur ne dure",
  'Ô vrayment marastre Nature,',
  'Las ! las ses beautez laissé cheoir !',
  'Mignonne, elle a dessus la place',
  "Las ! voyez comme en peu d'espace,"],
 ['Et son teint au vostre pareil.',
  'Les plis de sa robe pourprée,',
  'A point perdu ceste vesprée',
  'Sa robe de pourpre au Soleil,',
  'Qui ce matin avoit desclose',
  'Mignonne, allons voir si la rose']]
```

### Get a specific strophe

#### Get the last strophe

```py
printer.pprint(poem[-1])
```
**Output:**
```py
['Donc, si vous me croyez, mignonne,',
 'Tandis que vostre âge fleuronne',
 'En sa plus verte nouveauté,',
 'Cueillez, cueillez vostre jeunesse :',
 'Comme à ceste fleur la vieillesse',
 'Fera ternir vostre beauté.']
```

#### Get one strophe out of two
```py
printer.pprint(poem[::2])
```
**Output:**
```py
[['Mignonne, allons voir si la rose',
  'Qui ce matin avoit desclose',
  'Sa robe de pourpre au Soleil,',
  'A point perdu ceste vesprée',
  'Les plis de sa robe pourprée,',
  'Et son teint au vostre pareil.'],
 ['Donc, si vous me croyez, mignonne,',
  'Tandis que vostre âge fleuronne',
  'En sa plus verte nouveauté,',
  'Cueillez, cueillez vostre jeunesse :',
  'Comme à ceste fleur la vieillesse',
  'Fera ternir vostre beauté.']]
```

### Get a specific verse

#### Get the second verse of the last strophe

```py
printer.pprint(poem[-1][1])
```
**Output:**
```py
'Tandis que vostre âge fleuronne'
```
