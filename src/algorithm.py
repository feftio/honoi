A = [3, 2, 1]
B = []
C = []

def move(n, source, target, auxiliary):
    if n > 0:
        move(n - 1, source, auxiliary, target)
        target.append(source.pop())
        print(A, B, C, '##############', sep='\n')
        move(n - 1, auxiliary, target, source)

#               A       C        B
def move1(n, source, target, auxiliary):
  if n > 0:

    #1 
    target.append(source.pop())
    print(A, B, C, '##############', sep='\n')

    #2
    auxiliary.append(source.pop())
    print(A, B, C, '##############', sep='\n')
    
    auxiliary.append(target.pop())
    print(A, B, C, '##############', sep='\n')

    #3
    target.append(source.pop())
    print(A, B, C, '##############', sep='\n')

    #3-1
    source.append(auxiliary.pop())
    print(A, B, C, '##############', sep='\n')

    #2-1
    target.append(source.pop())
    print(A, B, C, '##############', sep='\n')

move1(3, A, C, B)