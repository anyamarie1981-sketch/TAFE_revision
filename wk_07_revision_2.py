file = open("wk_7_test_file.txt", "r")
print(f'File contents: {file.read()}')
file.close()
print('file = open("wk_7_test_file.txt", "r")')
print("print(f'File contents: {file.read()}')")
print('file.close()')

print('------------------------------')

file = open("wk_7_test_file.txt", "r")
for line in file:
    print(line.strip())




