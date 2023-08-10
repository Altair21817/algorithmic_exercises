"""
У умного телевизора есть игра: можно сколько угодно раз выбрать две
произвольные буквы латинского алфавита и заменить в строке все вхождения
первой буквы на вторую, а второй — на первую.

Необходимо определить возможно ли получить из строки s1 строку s2.
Для каждой пары слов нужно вывести "YES", если из s1 можно получить s2
и "NO" в противном случае.

В первой строке задано число t (1 ≤ t ≤ 100) — количество пар строк.
В следующих 2t строках вводятся t пар слов равной длины, разделенных переводом
строки и состоящих из строчных латинских букв — s1 и s2 соответственно.

Например, при выборе букв "a" и "b" строка "abc" превратится в "bac",
а при выборе "a" и "x" - в строку "xbc".
"""

"""Примеры с ответами для тестов со всеми условиями."""
INPUT_1: list[int, str] = [  # 2
    4,
    'abcd',   # YES
    'pqrs',
    'abc',    # YES
    'zyc',
    'sssss',  # YES
    'ppppp',
    'xx',     # NO
    'ab']

INPUT: list[int, str] = INPUT_1


def main():
    from collections import Counter

    t: int = INPUT[0]
    for i in range(t):
        s1: str = INPUT[1+i*2]
        s2: str = INPUT[2+i*2]
        if len(s1) != len(s2):
            print('NO')
            break
        count_s1_chars: Counter = Counter(s1)
        count_s2_chars: Counter = Counter(s2)
        if sorted(count_s1_chars.values()) != sorted(count_s2_chars.values()):
            print('NO')
        else:
            flag: bool = 'YES'
            common_keys: set[str] = (
                set(count_s1_chars.keys()) & set(count_s2_chars.keys()))
            for key in common_keys:
                if count_s1_chars[key] != count_s2_chars[key]:
                    flag: bool = 'NO'
                    break
            print(flag)


if __name__ == '__main__':
    main()
