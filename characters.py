import re


def ignore_bracketed(string_in):
    return f"(?!\[[^[]*){string_in}(?![^[]*\])"

class Character:
    def __init__(self, prefix, fill, suffix):
        self.prefix = prefix
        self.suffix = suffix
        self.fill = fill

    def sanitize(self, string_in):
        return re.sub(
            ignore_bracketed("(?<=[A-Za-z])([A-Z]+)"),
            lambda t: t.group(0).lower(),
            string_in
        )

    def add_prefix(self, string_in):
        string_out = re.sub(
            ignore_bracketed("[A-Z](?![^{]*})"),
            self.prefix.upper(),
            string_in
        )
        string_out = re.sub(
            ignore_bracketed("((?<=^)|(?<=\W))[a-z]"),
            self.prefix.lower(),
            string_out
        )
        return string_out

    def add_suffix(self, string_in):
        return re.sub(
            ignore_bracketed(f"(?<=[a-z{self.prefix.upper()}])([a-z]+)"),
            lambda t: self.suffix.lower() * len(t.group(0)),
            string_in
        )

    def add_fill(self, string_in):
        return re.sub(
            ignore_bracketed(f"(?<={self.prefix.upper()}|{self.prefix.lower()}){self.suffix * 2}(?![^{{]*}})"),
            f"{self.fill}{self.suffix}".lower(),
            string_in
        )

    def hiss(self, string_in):
        string_out = self.sanitize(string_in)
        string_out = self.add_prefix(string_out)
        string_out = self.add_suffix(string_out)
        string_out = self.add_fill(string_out)

        return string_out

character_names = [
    "ROMEO",
    "MONTAGUE",
    "LADY MONTAGUE",
    "MERCUTIO",
    "BENVOLIO",
    "BALTHASAR",
    "ABRAM",
    "JULIET",
    "CAPULET",
    "LADY CAPULET",
    "NURSE",
    "PETER",
    "TYBALT",
    "SAMPSON",
    "GREGORY",
    "PETRUCHIO",
    "Capulet's Cousin",
    "FIRST SERVINGMAN",
    "SECOND SERVINGMAN",
    "THIRD SERVINGMAN",
    "ESCALUS",
    "PARIS",
    "Paris' Page",
    "FRIAR LAWRENCE",
    "FRIAR JOHN",
    "APOTHECARY",
    "CITIZENS",
    "FIRST MUSICIAN",
    "SECOND MUSICIAN",
    "THIRD MUSICIAN",
    "FIRST WATCH",
    "SECOND WATCH",
    "THIRD WATCH",
    "CHORUS",
    "Attendants",
    "Maskers",
    "Torchbearers",
    "a Boy with a drum",
    "Gentlemen",
    "Gentlewomen",
    "PAGE",
    "SERVINGMAN",
    "FIRST SERVINGMAN",
    "SECOND SERVINGMAN",
    "PRINCE"
]

character_montague = Character("T", "z", "s")
character_capulet = Character("T", "s", "z")
character_default = Character("H", "i", "s")

character_formatting = {
    "ROMEO": character_montague,
    "MONTAGUE": character_montague,
    "LADY MONTAGUE": character_montague,
    "MERCUTIO": character_montague,
    "BENVOLIO": character_montague,
    "BALTHASAR": character_montague,
    "ABRAM": character_montague,
    "JULIET": character_capulet,
    "CAPULET": character_capulet,
    "LADY CAPULET": character_capulet,
    "NURSE": character_capulet,
    "PETER": character_capulet,
    "TYBALT": character_capulet,
    "SAMPSON": character_capulet,
    "GREGORY": character_capulet,
}