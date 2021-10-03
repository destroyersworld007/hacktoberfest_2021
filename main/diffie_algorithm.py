from random import randint

if __name__ == '__main__':
    #  prime number
    P_Num = 23
    G = 9

    print('Prime number :%d' % (P_Num))
    print('Primitive Root :%d' % (G))

    # private key a
    pubA = 4
    print('The Private Key of A :%d' % (pubA))

    x = int(pow(G, pubA, P_Num))

    # private key b
    pubB = 3
    print('The Private Key of B :%d' % (pubB))

    y = int(pow(G, pubB, P_Num))

    # Secret key A
    keyA = int(pow(y, pubA, P_Num))

    # Secret key B
    keyB = int(pow(x, pubB, P_Num))

    print('Secret key for A: %d' % (keyA))
    print('Secret Key for B: %d' % (keyB))