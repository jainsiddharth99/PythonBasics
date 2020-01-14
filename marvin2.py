paranoid_android="marvin, the paranoid android"
letters=list(paranoid_android)
for eachword in letters[:6]:
    print('\t',eachword)
for eachword in letters[::-1]:
    print('\t'*2,eachword)
for eachword in letters[-7:]:
    print('\t'*3,eachword)
for eachword in letters[12:24]:
    print('\t'*4,eachword)
