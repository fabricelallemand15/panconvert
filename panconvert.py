import sys, io

# Récupération du nom du ficher MarkDown
# dans la commande console 'python panconvert.py fichier.md'

file_name = sys.argv[1]

# Ouverture et lecture du fichier
file = io.open(file_name,mode='r', encoding='utf8')
content = file.readlines()


def code_to_highlighter():
    for i in range(len(content)):
        if content[k] == '~~~~{.python}':
            content[k] = '<pre class="brush: python">'
        if content[k] == '~~~~':
            content[k] = '</pre>'
