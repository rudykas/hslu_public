def string_reverse(a):
    b = ''
    for i in range(len(a)-1, 0, -1):
        b += a[i]
    print(b)

string_reverse('test12345')

print('1234567abcde'[6::-2])