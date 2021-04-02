
import textwrap as tw
from typing import Generator, Optional


def structure(text: str) -> tuple[list]:
    verses = []
    strophes = []

    for strophe in text.split("\n\n"):
        for verse in strophes:
            verses.append(verse)

        strophes.append(strophe)

    return verses, strophes


class Poem:

    def __init__(self, content: str):
        self.verses, self.strophes = structure(content.strip())

        self.struct = tuple(strophe.split("\n")
                                for strophe in self.strophes)

    def __getitem__(self, key) -> Optional[list]:
        return self.struct[key.start:key.stop:key.step]

    def __repr__(self) -> str:
        fst_strophe, *_, lst_strophe = self.struct
        
        fst_verse, *_ = fst_strophe
        *_, lst_verse = lst_strophe 

        overview = f"{fst_verse} [...] {lst_verse}"

        return f"Poem('{overview}')" 

    def __iter__(self) -> Generator:
        return iter(self.struct)

    def __reversed__(self) -> Optional[list[list]]:
        return list(list(reversed(strophe))
                        for strophe in reversed(self.struct))

    @property
    def form(self) -> tuple[int]:
        return tuple(len(strophe.split("\n"))
                         for strophe in self.strophes)


poem = """
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

poem = Poem(poem)

print(poem.form)
print(poem[1:3])

for strophe in poem:
    for verse in strophe:
        print(verse)

print(reversed(poem))

print(poem)