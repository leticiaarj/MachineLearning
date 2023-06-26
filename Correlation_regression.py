import numpy as np

corr = []

def Read():
    for i in range(2):
        m = input().split()
        a = []
        for j in range(2, len(m)):
            a.append(m[j])
        corr.append(a)
    return corr

if __name__ == "__main__":
    matrix = Read()
    correlacao = np.corrcoef(list(map(int, matrix[0])), list(map(int, matrix[1])))
    print("Correlacao: ", round(correlacao[0,1], 3))


