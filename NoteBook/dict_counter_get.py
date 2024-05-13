def isUnique(input: str) -> str:
    hMap = {}

    for letter in input:
        hMap[letter] = hMap.get(letter, 0) + 1

    return hMap
