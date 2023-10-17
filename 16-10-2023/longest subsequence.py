def print_matrix(mat):
    for row in mat:
        print(row)
def LCS(s1, s2):
    row, col = len(s1)+1, len(s2)+1
    mat = [[None]*col for i in range(row)]
    for i in range(row):
        for j in range(col):
            if i==0 or j == 0:
                mat[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                mat[i][j] = mat[i-1][j-1] + 1
            else:
                mat[i][j] = max(mat[i-1][j], mat[i][j-1])
    res=""
    for i in range(row,1,-1):
        for j in range(col,1,-1):
            if i==row and j==col:
               res+=s1(i-1)
            elif mat[i-1]==mat[j-1]:
                res+=s1[i-j]
    print_matrix(mat)
    return mat[row-1][col-1],res
s1 = "AGTAB"
s2 = "GXTAYB"
answer = LCS(s1, s2)
print("My answer is: ",answer)