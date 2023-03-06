# open and read xlsx file with openpyxl module
def main():
    sqlFile = open('input/2022-1S.sql', 'r')
    newSqlFile = open("out.sql", "wt")
    for line in sqlFile:
        splitline = line.split("VALUES")
        values = splitline[1].split(",")

        #Add the values part with the new values
        newLine = splitline[0] + "VALUES"
        print(values)
        for i in range(values.__len__()):

            if i == 1:
                if values[i] == "'T'":
                    newLine += "\'TI\',"
                if values[i] == "'C'":
                    newLine += "\'CC\',"
                if values[i] == "'E'":
                    newLine += "\'CE\',"
                if values[i] == "'P'":
                    newLine += "\'PS\',"
                # else:
                #     newLine += values[i] + ','

            else:
                newLine += values[i] + ','
        newLine = newLine[:-1]


        # print(newLine)
        newSqlFile.write(newLine)

    sqlFile.close()
    newSqlFile.close()








if __name__ == '__main__':
    main()