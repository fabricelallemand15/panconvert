import sys, io, os


def code_to_highlighter():

    """ Fonction permettant d'utiliser Syntax Highlighter
    plutôt que la coloration par défaut de Pandoc
    dans le fichier html"""

    new_content = content[:]
    for i in range(len(content)):
        print(content[i])
        input()
        if content[i] == '~~~~{.python}':
            new_content[i] = '<pre class="brush: python">'
            print(content[i])
            input()
        if content[i] == '~~~~':
            new_content[i] = '</pre>'
    return new_content


def make_md_for_html():
    for_html_file = io.open('md_for_html.md',mode='w', encoding='utf8')
    for k in range(len(content)):
        if content[k]=='~~~~{.python}\n':
            for_html_file.write('<pre class="brush: python">\n')
        elif content[k]=='~~~~\n':
            for_html_file.write('</pre>\n')
        else:
            for_html_file.write(content[k])
    for_html_file.close()


if __name__ == '__main__':

    # Récupération du nom du ficher MarkDown
    # dans la commande console 'python panconvert.py fichier.md'
    file_name = sys.argv[1]

    # Ouverture et lecture du fichier
    file = io.open(file_name, mode='r', encoding='utf8')
    content = file.readlines()
    file.close()

    # Création du fichier modifié pour l'export en html
    make_md_for_html()

    # Création du fichier html
    print("appel à Pandoc ...")
    os.system('C:/Users/Fabrice/AppData/Local/Pandoc/pandoc.exe --template=modele.html -o '+file_name+'.html'+' md_for_html.md')
    input()

    # Destruction du fichier modifié
    print("nettoyage ...")
    os.remove('md_for_html.md')