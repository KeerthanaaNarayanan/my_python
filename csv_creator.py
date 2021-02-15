from aptest_files.common import *
import csv
ids = []
automated = []
authors = []
titles = []
descriptions = []


def creators():
    test_keys = get_list(dict123)
    length = len(test_keys)
    for i in range(0, length):
        if i < 9:
            ids.append('TC00' + str(i + 1))
        if (i >= 9) and (i < 99):
            ids.append('TC0' + str(i + 1))
        if (i >= 99) and (i < 999):
            ids.append('TC' + str(i + 1))
        if (i >= 999) and (i < 9999):
            ids.append('TC' + str(i+1))
    for i in test_keys:
        automated.append('yes')
        authors.append('KNarayanan')
        titles.append(i)
        descp = ''
        for j in i:
            if j is '_':
                j = ' '
            descp = descp + str(j)
        descriptions.append(descp)


creators()


with open('aptest_file.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['ID', 'automated', 'author', 'title', 'description', 'procedure', 'initial_setup'])
    for tc_id, yes, author, title, description in zip(ids, automated, authors, titles, descriptions):
        writer.writerow([tc_id, yes, author, title, description, description, description])