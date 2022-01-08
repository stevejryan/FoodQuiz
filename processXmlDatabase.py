import pandas as pd


df = pd.read_excel('FoodBibleDatabase.xlsx')
df.rename(columns={'Ingredient\nIncludes concepts':'ingredient'}, inplace=True)
listOfMyIngs = list(df.ingredient.unique())

listOfXmlNodes = []
with open('flavorBibleGraphTrimmed2.xml', 'r') as file:
  for line in file:
    if 'node id' in line:
      listOfXmlNodes.append(line.strip()[10:-4])


setOfNodes = set(listOfXmlNodes)
setOfNodes = {string.lower() for string in setOfNodes}
setOfNodes = {string.strip() for string in setOfNodes}
print(len(setOfNodes))

setOfMyIngs = set(listOfMyIngs)
setOfMyIngs = {string.lower() for string in setOfMyIngs}
setOfMyIngs = {string.strip() for string in setOfMyIngs}
print(len(setOfMyIngs))

breakpoint()