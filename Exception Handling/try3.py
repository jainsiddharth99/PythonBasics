try:
    with open('myfile.txt')as fh:
        file_data=fh.read()
    print(file_data)
except FileNotFoundError:
    print('the data file is missing')
except PermissionError:
    print('this is not allowed')