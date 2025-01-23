import rich as r
from datetime import *
def info(text, loglvl):
 nowtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
 r.print(f'{nowtime}: [bold green][{loglvl}] info: {text}')
def warn(text, loglvl):
 nowtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
 r.print(f'{nowtime}: [bold yellow][{loglvl}] warning: {text}')
def error(text, loglvl):
 nowtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
 r.print(f'{nowtime}: [bold red][{loglvl}] error: {text}')

def encode(text, vocabulary):
    mapping = {char: str(i + 1) for i, char in enumerate(vocabulary)}
    encoded = '|'.join(mapping[char] for char in text if char in mapping)
    return encoded

def decode(encoded, vocabulary):
    inverse_mapping = {str(i + 1): char for i, char in enumerate(vocabulary)}
    numbers = encoded.split('|')
    decoded = ''.join(inverse_mapping[num] for num in numbers if num in inverse_mapping)
    return decoded

class Char:
 vocabulary = "qwertyuiopasdfghjklzxcvbnm .,?(:)!/\@йцукенгшщзхфывапролджэячсмитьбюЙЦУКЕНГШЩЗХФЫВАПРОЛДЖЭЯЧСМИТЬБЮQWERTYUIOPASDFGHJKLZXCVBNM|1234567890"
