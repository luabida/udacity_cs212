"""
Here are some sandbox functions to understand
built-in method str.translate() and str.maketrans()
"""

s = 'abcdeABCDEfghiFGHI-abcdeABCDEfghiFGHI-abcdeABCDEfghiFGHI'
# Translations:
abc_xyz = str.maketrans('abc', 'xyz')
abCDe_11111 = str.maketrans('abCDe', '11111')
ab_none = str.maketrans({'a': None, 'b': None})
half_empty = str.maketrans('abcdeABCDE', '          ')

B = 'B'
mess = 'MESS'
messy = str.maketrans({'a': '300000000000', 'b': 'OMG', 'c': 'THIS', 'd': 'IS', 'A': 'SUCH', B: 'A', 'C': mess})

only_A = str.maketrans('abcdeBCDE', 'AAAAAAAAA', 'fghiFGHI')

import string
letters = string.ascii_letters
almost_empty = str.maketrans('-', ' ', letters)

print(abc_xyz)
print(s.translate(abc_xyz))
print(s.translate(abCDe_11111))
print(s.translate(ab_none))
print(s.translate(half_empty))
print(s.translate(messy))
print(s.translate(only_A))
print(s.translate(almost_empty), f'<- {len(s.translate(almost_empty))} spaces :)')
print('_______')


"""
Here goes a kinda creepy and cool cryptography swapping the letters in alphabet
"""
lowercases = string.ascii_lowercase
print(f'{lowercases} <<swapping half of the letters>> {lowercases[13:] + lowercases[:13]}')
crypto = str.maketrans(lowercases, lowercases[13:] + lowercases[:13])

s = 'hello out there'
encrypted_s = s.translate(crypto)
print(encrypted_s, '<- Unreadable')

decrypted_s = encrypted_s.translate(crypto)
print(decrypted_s, '<- Decrypted using the same crypto')
