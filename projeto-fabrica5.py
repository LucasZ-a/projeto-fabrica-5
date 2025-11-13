popA = 80.000
popB = 200.000
taxaA = 3
taxaB = 1.5
anos = 0
while True:
    popA = popA + (popA*(taxaA/100))
    popB = popB + (popB*(taxaB/100))
    anos +=1
    if popA >= popB:
        break
    print(anos)