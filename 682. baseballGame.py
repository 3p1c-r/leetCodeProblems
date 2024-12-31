Given a list of operations for the points for a baseball game, log all the points and return the sum of the points.

def calPoints(operations: list[str]) -> int:
        points = []
        for i in operations:
            if i.lstrip("-").isdigit() == True:
                points.append(int(i))
            elif i == "C": 
                points.pop()
            elif i == "D":
                points.append(points[-1]*2)
            elif i == "+":
                points.append(points[-1] + points[-2])
        print(sum(points))
        return(sum(points))
