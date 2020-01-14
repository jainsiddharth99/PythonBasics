word = "bottles"
for beer_num in range(99,0,-1):
    print(beer_num, word, "of beer on the wall.")
    print(beer_num, word, "of beer.")
    print("take one down")
    print("pass it around")
    if beer_num == 1:
        print("no more bootles of beer on the wall")
    else:
        new_num = beer_num - 1
        if new_num == 1:
            word= "bottle"
        print(new_num, word, "of beers on the wall.")
    print()