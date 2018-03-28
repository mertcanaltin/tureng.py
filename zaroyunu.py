

import random
import time

"""
    2 adet zar atılsın ve her iki zarın değeri de 6 olduğunda program dursun.
    İki zar da 6 gelene kadar kaç kez zar atıldığını bildiren programı yazınız.
"""

i = 1
while True:
    zar1 = random.randint(1, 6)
    zar2 = random.randint(1, 6)

    if zar1 == 6 and zar2 == 6:
        print("Deneme {}:\t({},{}) *** """.format(i, zar1, zar2))
        time.sleep(2)
        break

    print("Deneme {}:\t({},{}) """.format(i, zar1, zar2))
    i += 1
    time.sleep(0.5)

print("\n {}. denemede başarılı olduk  (6,6) oleeeyy".format(i))


