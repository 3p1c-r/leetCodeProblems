def countSegments(s: str) -> int:
        list1 = s.split()
        return len(list1)

print(countSegments(s="Hello, my name is John."))
