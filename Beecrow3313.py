
counter = 0
while True:
    arr = set()
    word = input()
    if word == '*':
        break
    
    n = len(word)
    idx = 0
    while idx < n:
        new_word = f"{word[n-1]}{word[0:n-1]}"
        arr.add(new_word)
        word = new_word
        idx += 1

    arr = sorted(arr)
    counter += 1
    print(f"Caso {counter}: {arr[0]} {arr[n-1]}")
