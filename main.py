from characters import *

with open("./txt/romeo-and-juliet_TXT_FolgerShakespeare.txt", "r") as file_in, open("output.txt", "w") as file_out:
    line = file_in.readline()
    capture = False
    meta_over = False
    current_character = character_default

    while line:
        if not line.strip():
            capture = False
            current_character = character_default
        if line.strip() == "THE PROLOGUE":
            meta_over = True

        if not meta_over:
            pass
        elif capture:
            file_out.write(current_character.hiss(line))
        elif any(character := [name for name in character_names if line[:len(name)].lower() == name.lower()]):
            character = character[0]
            if character in character_formatting.keys():
                current_character = character_formatting[character]
            capture = True
            dialog = line.split("  ")
            if len(dialog) == 2:
                dialog[1] = current_character.hiss(dialog[1])
            file_out.write("  ".join(dialog))
        else:
            file_out.write(line)

        line = file_in.readline()
