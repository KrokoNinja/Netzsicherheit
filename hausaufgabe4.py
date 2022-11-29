n = 3
MOD = 2**n


def KSA(key):
    key_length = len(key)
    # create the array "S"
    S = list(range(MOD))  # [0,1,2, ... , 255]
    j = 0
    for i in range(MOD):
        j = (j + S[i] + key[i % key_length]) % MOD
        S[i], S[j] = S[j], S[i]  # swap values
    return S


def PRGA(S):
    result = []
    i = 0
    j = 0
    while len(result) < 20:
        i = (i + 1) % MOD
        j = (j + S[i]) % MOD

        S[i], S[j] = S[j], S[i]  # swap values
        K = S[(S[i] + S[j]) % MOD]
        result.append(K)
    return result

def get_keystream(key):
    S = KSA(key)
    return PRGA(S)

#Aufgabe 1
KL = [24, 128, 83, 11, 204, 69, 41, 239]
KY = [110, 123, 217, 243, 255, 115, 253, 149]

# print(get_keystream(KL)[7])
# print(get_keystream(KY)[7])
# print(get_keystream(KL)[16])
# print(get_keystream(KY)[16])

#Aufgabe 2

possible_iv_zo = [
    # ([3,7,1],5),
    # ([5,4,0],3),
    # ([5,7,1],3),
    # ([3,7,5],7),
    # ([6,6,4],5)
    #([3,7,7],7)
    ]



possible_keys = []


for i in range(8):
    for j in range(8):
        possible_keys.append([i, j])

for i in possible_keys:
    for j in possible_iv_zo:
        if get_keystream(j[0] + i)[0] == j[1]:
            print("Key: " + str(i) + " IV: " + str(j[0]) + " z0: " + str(j[1]))
print("fertig")