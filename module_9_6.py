def all_variants(text: str):
    count = 0
    repeats = len(text)
    slicer = 1
    while slicer <= len(text):
        yield text[count: count + slicer]
        count += 1
        if count == repeats:
            repeats -= 1
            count = 0
            slicer += 1


result = all_variants('123456')
for i in result:
    print(i)
