def code():
    buchstaben = {'a': {0: 0.06, 1: 0.18}, 'b': {0: 0.18, 1: 0.06, 2: 0.06, 3: 0.06},
                  'c': {0: 0.18, 1: 0.06, 2: 0.18, 3: 0.06},
                  'd': {0: 0.18, 1: 0.06, 2: 0.06}, 'e': {0: 0.06}, 'f': {0: 0.06, 1: 0.06, 2: 0.18, 3: 0.06},
                  'g': {0: 0.18, 1: 0.18, 2: 0.06}, 'h': {0: 0.06, 1: 0.06, 2: 0.06, 3: 0.06},
                  'i': {0: 0.06, 1: 0.06}, 'j': {0: 0.06, 1: 0.18, 2: 0.18, 3: 0.18},
                  'k': {0: 0.18, 1: 0.06, 2: 0.18}, 'l': {0: 0.06, 1: 0.18, 2: 0.06, 3: 0.06},
                  'm': {0: 0.18, 1: 0.18}, 'n': {0: 0.18, 1: 0.06},
                  'o': {0: 0.18, 1: 0.18, 3: 0.18}, 'p': {0: 0.06, 1: 0.18, 2: 0.18, 3: 0.06},
                  'q': {0: 0.18, 1: 0.18, 2: 0.06, 3: 0.18},
                  'r': {0: 0.06, 1: 0.18, 2: 0.06}, 's': {0: 0.06, 1: 0.06, 2: 0.06}, 't': {0: 0.18},
                  'u': {0: 0.06, 1: 0.06, 2: 0.18},
                  'v': {0: 0.06, 1: 0.06, 2: 0.06, 3: 0.18}, 'w': {0: 0.06, 1: 0.18, 2: 0.18},
                  'x': {0: 0.18, 1: 0.06, 2: 0.06, 3: 0.18},
                  'y': {0: 0.18, 1: 0.06, 2: 0.18, 3: 0.18}, 'z': {0: 0.18, 1: 0.18, 2: 0.06, 3: 0.06},
                  'ä': {0: 0.06, 1: 0.18, 2: 0.06, 3: 0.18}, 'ö': {0: 0.18, 1: 0.18, 2: 0.18, 3: 0.35},
                  'ü': {0: 0.06, 1: 0.06, 2: 0.18, 3: 0.18},
                  'A': {0: 0.06, 1: 0.18}, 'B': {0: 0.18, 1: 0.06, 2: 0.06, 3: 0.06},
                  'C': {0: 0.18, 1: 0.06, 2: 0.18, 3: 0.06},
                  'D': {0: 0.18, 1: 0.06, 2: 0.06}, 'E': {0: 0.06}, 'F': {0: 0.06, 1: 0.06, 2: 0.18, 3: 0.06},
                  'G': {0: 0.18, 1: 0.18, 2: 0.06},
                  'H': {0: 0.06, 1: 0.06, 2: 0.06, 3: 0.06}, 'I': {0: 0.06, 1: 0.06},
                  'J': {0: 0.06, 1: 0.18, 2: 0.18, 3: 0.18},
                  'K': {0: 0.18, 1: 0.06, 2: 0.18}, 'L': {0: 0.06, 1: 0.18, 2: 0.06, 3: 0.06},
                  'M': {0: 0.18, 1: 0.18}, 'N': {0: 0.18, 1: 0.06},
                  'O': {0: 0.18, 1: 0.18, 3: 0.18}, 'P': {0: 0.06, 1: 0.18, 2: 0.18, 3: 0.06},
                  'Q': {0: 0.18, 1: 0.18, 2: 0.06, 3: 0.18},
                  'R': {0: 0.06, 1: 0.18, 2: 0.06}, 'S': {0: 0.06, 1: 0.06, 2: 0.06}, 'T': {0: 0.18},
                  'U': {0: 0.06, 1: 0.06, 2: 0.18},
                  'V': {0: 0.06, 1: 0.06, 2: 0.06, 3: 0.18}, 'W': {0: 0.06, 1: 0.18, 2: 0.18},
                  'X': {0: 0.18, 1: 0.06, 2: 0.06, 3: 0.18},
                  'Y': {0: 0.18, 1: 0.06, 2: 0.18, 3: 0.18}, 'Z': {0: 0.18, 1: 0.18, 2: 0.06, 3: 0.06},
                  'Ä': {0: 0.06, 1: 0.18, 2: 0.06, 3: 0.18}, 'Ö': {0: 0.18, 1: 0.18, 2: 0.18, 3: 0.35},
                  'Ü': {0: 0.06, 1: 0.06, 2: 0.18, 3: 0.18},
                  '1': {0: 0.06, 1: 0.18, 2: 0.18, 3: 0.18, 4: 0.18},
                  '2': {0: 0.06, 1: 0.06, 2: 0.18, 3: 0.18, 4: 0.18},
                  '3': {0: 0.06, 1: 0.06, 2: 0.06, 3: 0.18, 4: 0.18},
                  '4': {0: 0.06, 1: 0.06, 2: 0.06, 3: 0.06, 4: 0.18},
                  '5': {0: 0.06, 1: 0.06, 2: 0.06, 3: 0.06, 4: 0.06},
                  '6': {0: 0.18, 1: 0.06, 2: 0.06, 3: 0.06, 4: 0.06},
                  '7': {0: 0.18, 1: 0.18, 2: 0.06, 3: 0.06, 4: 0.06},
                  '8': {0: 0.18, 1: 0.18, 2: 0.18, 3: 0.06, 4: 0.06},
                  '9': {0: 0.18, 1: 0.18, 2: 0.18, 3: 0.18, 4: 0.06},
                  '0': {0: 0.18, 1: 0.18, 2: 0.18, 3: 0.18, 4: 0.18},
                  '.': {0: 0.06, 1: 0.18, 2: 0.06, 3: 0.18, 4: 0.06, 5: 0.18},
                  ',': {0: 0.18, 1: 0.18, 2: 0.06, 3: 0.06, 4: 0.18, 5: 0.18},
                  ':': {0: 0.18, 1: 0.18, 2: 0.18, 3: 0.06, 4: 0.06, 5: 0.06},
                  '-': {0: 0.18, 1: 0.06, 2: 0.06, 3: 0.06, 4: 0.06, 5: 0.18},
                  'ß': {0: 0.06, 1: 0.06, 2: 0.06, 3: 0.18, 4: 0.18, 5: 0.06, 6: 0.06},
                  '?': {0: 0.06, 1: 0.06, 2: 0.18, 3: 0.18, 4: 0.06, 5: 0.06},
                  ';': {0: 0.18, 1: 0.06, 2: 0.18, 3: 0.06, 4: 0.18, 5: 0.06},
                  '_': {0: 0.06, 1: 0.06, 2: 0.18, 3: 0.18, 4: 0.06, 5: 0.18},
                  '(': {0: 0.18, 1: 0.06, 2: 0.18, 3: 0.18, 4: 0.06},
                  ')': {0: 0.18, 1: 0.06, 2: 0.18, 3: 0.18, 4: 0.06, 5: 0.18},
                  "'": {0: 0.06, 1: 0.18, 2: 0.18, 3: 0.18, 4: 0.18, 5: 0.06},
                  '=': {0: 0.18, 1: 0.06, 2: 0.06, 3: 0.06, 4: 0.18},
                  '+': {0: 0.06, 1: 0.18, 2: 0.06, 3: 0.18, 4: 0.06},
                  '/': {0: 0.18, 1: 0.06, 2: 0.06, 3: 0.18, 4: 0.06},
                  '@': {0: 0.06, 1: 0.18, 2: 0.18, 3: 0.06, 4: 0.18, 5: 0.06}}
    return buchstaben

def test():
    buchstaben = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z', 'Ä', 'Ö', 'Ü', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                  'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ä', 'ö', 'ü', '1', '2',
                  '3', '4', '5', '6', '7', '8', '9', '0', ':', '-', 'ß', '?', '.', ',', ';', '_', '(', ')', "'", '=',
                  '+', '/', '@']
    return buchstaben