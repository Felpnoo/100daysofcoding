import sys

CAPITAL = ".....O"  # Ponto 6: indica que a próxima letra é MAIÚSCULA
NUMBER = ".O.OOO"  # Pontos 3, 4, 5, 6: indica que os próximos caracteres são NÚMEROS
SPACE = "......"  # Nenhum ponto: espaço em branco

# Alfabeto em Braille (letras minúsculas)
ALPHABET_TO_BRAILLE = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.",
    "p": "OOO.O.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO",
    " ": "......",
}

# Números (1 a 9, e 0) mapeados para as letras correspondentes ('a' até 'j')
DIGIT_TO_LETTER = {
    "1": "a",
    "2": "b",
    "3": "c",
    "4": "d",
    "5": "e",
    "6": "f",
    "7": "g",
    "8": "h",
    "9": "i",
    "0": "j",
}

BRAILLE_TO_ALPHABET = {v: k for k, v in ALPHABET_TO_BRAILLE.items()}
LETTER_TO_DIGIT = {v: k for k, v in DIGIT_TO_LETTER.items()}


def isBraille(texto):
    return len(texto) > 0 and len(texto) % 6 == 0 and set(texto).issubset({".", "O"})


def tradutor_en_to_br(texto):
    traduzido = ""
    modoNum = False
    for i in texto:
        if i.isdigit():
            if not modoNum:
                modoNum = True
                traduzido += NUMBER
                traduzido += ALPHABET_TO_BRAILLE[DIGIT_TO_LETTER[i]]
            else:
                traduzido += ALPHABET_TO_BRAILLE[DIGIT_TO_LETTER[i]]

        elif i == " ":
            modoNum = False
            traduzido += SPACE

        elif i.isupper():
            traduzido += CAPITAL
            traduzido += ALPHABET_TO_BRAILLE[i.lower()]
        else:
            traduzido += ALPHABET_TO_BRAILLE[i]
    return traduzido


def tradutor_br_to_en(texto):
    modoNum = False
    proxUp = False
    traduzido = ""

    for i in range(0, len(texto), 6):
        cell = texto[i : i + 6]

        if cell == NUMBER:
            modoNum = True
        elif cell == CAPITAL:
            proxUp = True
        elif cell == SPACE:
            modoNum = False
            proxUp = False
            traduzido += " "
        elif modoNum:
            traduzido += LETTER_TO_DIGIT[BRAILLE_TO_ALPHABET[cell]]
        elif proxUp:
            proxUp = False
            traduzido += BRAILLE_TO_ALPHABET[cell].upper()
        else:
            traduzido += BRAILLE_TO_ALPHABET[cell]
    return traduzido


if __name__ == "__main__":
    texto = " ".join(sys.argv[1:])

    if isBraille(texto):
        print(tradutor_br_to_en(texto))
    else:
        print(tradutor_en_to_br(texto))
