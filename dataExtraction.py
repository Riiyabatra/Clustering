from xlrd import open_workbook
from nltk.corpus import stopwords
wb = open_workbook('Book1.xlsx')
abstract = []
filtered_abstract = []
for s in wb.sheets():
    for row in range(1, s.nrows):
        abstract.append((s.cell(row,0).value).split())
        #print(abstract)
print("####################################################################################################")
stop_words = set(stopwords.words('english'))
newStopWords = ['the','The','then','to','etc.','This','It', 'Our']
stopWordsList = stop_words.union(newStopWords)
#print(stopWordsList)

for l in abstract:
        for sublist in l:
                l=list(filter(lambda a: a not in stopWordsList, l))
        filtered_abstract.append(l)
        print('-------------------------------------------------')
        print(l)
#print(filtered_abstract)
