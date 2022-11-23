import re

characters = [
    "ROMEO",
    "MONTAGUE",
    "LADY MONTAGUE",
    "BENVOLIO",
    "ABRAM",
    "BALTHASAR",
    "JULIET",
    "CAPULET",
    "LADY CAPULET",
    "NURSE",
    "TYBALT",
    "PETRUCHIO",
    "Capulet's Cousin",
    "SAMPSON",
    "GREGORY",
    "PETER",
    "FIRST SERVINGMAN",
    "SECOND SERVINGMAN",
    "THIRD SERVINGMAN",
    "ESCALUS",
    "PARIS",
    "MERCUTIO",
    "Paris' Page",
    "FRIAR LAWRENCE",
    "FRIAR JOHN",
    "APOTHECARY",
    "Three or four Citizens",
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

def ignore_bracketed(string_in):
    return f"(?!\[[^[]*){string_in}(?![^[]*\])"

def hiss(string_in):
    string_out = re.sub(
        ignore_bracketed("(?<=[A-Za-z])([A-Z]+)"),
        lambda t: t.group(0).lower(),
        string_in
    )
    string_out = re.sub(
        ignore_bracketed("[A-Z](?![^{]*})"),
        "H",
        string_out
    )
    string_out = re.sub(
        ignore_bracketed("((?<=^)|(?<=\W))[a-z]"),
        "h",
        string_out
    )
    string_out = re.sub(
        ignore_bracketed("(?<=[a-zH])([a-z]+)"),
        lambda t: "s" * len(t.group(0)),
        string_out
    )
    string_out = re.sub(
        ignore_bracketed("(?<=H|h)ss(?![^{]*})"),
        "is",
        string_out
    )

    return string_out


with open("./txt/romeo-and-juliet_TXT_FolgerShakespeare.txt", "r") as file_in, open("output.txt", "w") as file_out:
    line = file_in.readline()
    capture = False
    meta_over = False

    while line:
        if not line.strip():
            capture = False
        if line.strip() == "THE PROLOGUE":
            meta_over = True

        if not meta_over:
            pass
        elif capture:
            file_out.write(hiss(line))
        elif any([line[:len(name)].lower() == name.lower() for name in characters]):
            capture = True
            dialog = line.split("  ")
            if len(dialog) == 2:
                dialog[1] = hiss(dialog[1])
            file_out.write("  ".join(dialog))
        else:
            file_out.write(line)

        line = file_in.readline()
