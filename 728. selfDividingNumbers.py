def selfDividingNumbers(left: int, right: int) -> list[int]:
        selfDividingNumbersList = []
        counter = 0
        for i in range(left, right + 1):
            x = list(map(int, str(i)))
            counter = 0
            if "0" in str(i): continue
            for j in x:
                if i % j == 0: counter += 1
            if counter == len(x): selfDividingNumbersList.append(i)
        return selfDividingNumbersList

print(selfDividingNumbers(left=47,right=85))
