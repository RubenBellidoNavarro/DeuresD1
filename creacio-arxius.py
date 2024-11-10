for i in range(11):
    filename = f'exercici{i:03}.py'
    with open(filename, 'w') as file:
        file.write(f'#Arxiu {filename}') 
