cp1 = float(input('Digite a nota do primeiro checkpoint:'))
cp2 = float(input('Digite a nota do segundo checkpoint:'))
cp3 = float(input ('Digite a nota do ultimo checkpoint:'))
sprint1 = float(input('Digite a nota do primeiro sprint:'))
sprint2 = float(input('Digite a nota do segundo sprint:'))
gs = float(input('Digite a nota do global solution:'))

cps = [cp1, cp2, cp3]

def verification_checkpoint():
    if cp1 <= cp2 and cp1 <= cp3:
        cps.remove(cp1)
    elif cp2 <= cp1 and cp2 <= cp3:
        cps.remove(cp2)
    else:
        cps.remove(cp3)

def function_average():
    average = ((cps[0] + cps[1] + sprint1 + sprint2) / 4 )
    averagefinal = average * 0.4 + gs * 0.6
    print(average)
    print(averagefinal)

verification_checkpoint()
function_average()
