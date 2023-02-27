# open and read xlsx file with openpyxl module
def main():
    sqlFile = open('202201.sql', 'r')
    newSqlFile = open("out.sql", "wt")
    for line in sqlFile:
        splitline = line.split()

        # Add the all without the last part corresponding to the values part
        aux = splitline.pop()
        for word in splitline:
            newSqlFile.write(word)
            newSqlFile.write(' ')
        #Add the values part with the new values
        newLine = ""
        values = aux.split(',')
        auxItem = ''
        for i in range(values.__len__()):
            if i == 2:
                auxItem = values[i].split('-')[0].replace('\'', '')
                newLine += '\'' + values[i].replace('-', '').replace('\'', '') + '\','
            elif i == 3:
                newLine += 'default,'
            elif i == 7:
                newLine += f'TIMESTAMPDIFF(YEAR, {values[i]}, \'{auxItem}-01-01\'),'
            elif i == values.__len__() - 1:
                newLine += values[i]
            else:
                newLine += values[i] + ','
        newLine += '\n'
        # print(newLine)
        newSqlFile.write(newLine)

    sqlFile.close()
    newSqlFile.close()








if __name__ == '__main__':
    main()