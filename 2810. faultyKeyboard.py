def finalString(s: str) -> str:
        list1 = []
        for i in s:
            if i == "i": list1.reverse()
            else: list1.append(i)
        return "".join(list1)

print(finalString(s="string"))
