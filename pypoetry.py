"""Just a convenient interface to manipulate poems."""

from typing import Iterator


__author__ = "Timéo Arnouts"
__version__ = 1.0


def structure(text: str) -> tuple[tuple[str]]:
    """Returns a tuple containing two tuples of strings: strophes and
    verses of given text.
    """
    verses = []
    strophes = []

    for strophe in text.split(Poem.strophe_separator):
        for verse in strophes:
            verses.append(verse)

        strophes.append(strophe)

    return (tuple(strophes),
            tuple(verses))


class Poem:
    """Encapsulate a poem."""

    strophe_separator = "\n"*2

    def __init__(self, content: str):
        self.content = content.strip().replace("\n\n", 
                                               Poem.strophe_separator)
        self.strophes, self.verses = structure(self.content)

        self.struct = [strophe.split("\n")
                           for strophe in self.strophes]

    def __getitem__(self, key) -> list[list[str]]:
        """Returns strophe of poem corresponding to given slice."""
        if isinstance(key, int):
            return self.struct[key]
        else:    
            return self.struct[key.start:key.stop:key.step]

    def __repr__(self) -> str:
        """Returns a representation of poem where verses except the
        first and the last are truncated."""
        fst_strophe, *_, lst_strophe = self.struct

        fst_verse, *_ = fst_strophe
        *_, lst_verse = lst_strophe 

        overview = f"{fst_verse} [...] {lst_verse}"

        return f"Poem('{overview}')" 

    def __iter__(self) -> Iterator[list[str]]:
        """Returns a generator containing list in which verses of each
        strophe are grouped.
        """
        return iter(self.struct)

    def __reversed__(self) -> list[list]:
        """Return a generator containing reversed strophes of poem
        containing verses themselves reversed.
        """
        return list(list(reversed(strophe))
                        for strophe in reversed(self.struct))

    @property
    def form(self) -> tuple[int]:
        """Returns an integer tuple containing number of verses per
        strophes.
        """
        return tuple(len(strophe.split("\n"))
                         for strophe in self.strophes)
