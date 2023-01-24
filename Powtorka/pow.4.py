def znaki(string):
    S = {}
    for i in string:
        if i in S.keys():
            S[i] = S[i]+1
        else:
            S[i] = 1 #jezeli nie ma takiej pary to program dodaje nowa do slownika
    return S
W = (znaki("dsanjdhefwba p"))
for k in sorted(W.keys()):
    print(k, W[k])

