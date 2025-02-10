def lcs(X, Y):























































































































































































































































































































































































































































































































































































































































































    m = len(X)
    n = len(Y)
    L = [[None] * (n + 1) for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    index = L[m][n]
    lcs_str = [''] * (index + 1)
    lcs_str[index] = ''

    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_str[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(lcs_str)

def all_subsequences(s):
    subsequences = set()
    for i in range(1 << len(s)):
        subsequence = ''.join(s[j] for j in range(len(s)) if i & (1 << j))
        subsequences.add(subsequence)
    return subsequences

def common_subsequences(X, Y):
    subseq_X = all_subsequences(X)
    subseq_Y = all_subsequences(Y)
    return subseq_X.intersection(subseq_Y)

if __name__ == "__main__":
    X = "AGPTAB"
    Y = "GRRXAYB"
    
    lcs_result = lcs(X, Y)
    print("Longest Common Subsequence:", lcs_result)
    
    common_subseq = common_subsequences(X, Y)
    print("All Common Subsequences:")
    for subseq in sorted(common_subseq):
        print(subseq)
