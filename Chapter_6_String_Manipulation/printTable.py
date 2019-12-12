tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    colWidths = [0] * len(tableData)
    for i in range(len(tableData)):
        for j in range(len(tableData[i])):
            if len(tableData[i][j]) > colWidths[i]:
                colWidths[i] = len(tableData[i][j])
    
    maxLength = int(0)
    for i in range(len(colWidths)):
        if colWidths[i] > maxLength:
            maxLength = colWidths[i]
    
    output = ""

    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            output += tableData[j][i].rjust(maxLength)
        output += "\n"
    
    print(output)

printTable(tableData)