text = 'New text added'
testFile = open('C:\Movies\ExFile.txt', 'w')
testFile.write(text)
testFile.close()
appendFile = open('C:\Movies\ExFile.txt', 'a')
appendFile.write('\n')
appendFile.write('Appended text!')
appendFile.close()
readme = open('C:\Movies\ExFile.txt', 'r').read()
print(readme)


