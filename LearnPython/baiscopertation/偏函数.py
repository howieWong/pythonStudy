print(int("11100111",base=2))
import functools

intfrombin = functools.partial(int,base=2)
print(intfrombin("101010101"))