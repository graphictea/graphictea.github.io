#!/usr/bin/python
from markdown import markdown
from bs4 import BeautifulSoup
import os, shutil


class Template:
    def __init__(self):
        self.header = None
        self.footer = None

#global variables I am so sorry
template = Template()

def delete(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')


def breadcrumbs(tree):
    header = "<header>\n    <ol>\n"

    backlink = "../"
    depth = len(tree) - 1

    for title in tree[:-1]:
        header += f"       <li><a href=\"{ depth * backlink }\">{title}</a></li>\n"
        depth -= 1

    header += f"       <li>{tree[-1]}</li>\n"
    header += "    </ol>\n</header>"
    return header


def transform(infile, outfile, tree):
    global template

    with open(infile, 'r') as file:
        content = file.read()
        html = markdown(content, extensions=['attr_list'])

    header = template.header.replace("{{ breadcrumbs }}", breadcrumbs(tree))
    footer = template.footer.replace("{{ breadcrumbs }}", breadcrumbs(tree))
    html = header + html + footer

    with open(outfile, "w") as out:
        out.write(html)



def build(folder, outfolder, tree = []):
    # traverse root directory, and list directories as dirs and files as files
    for dirpath, subdirs, files in os.walk(folder):
        indirectory = os.path.join(dirpath)
        outdirectory = indirectory.replace(folder, outfolder)

        if not os.path.exists(outdirectory):
            os.makedirs(outdirectory) 

        titlepage = os.path.join(indirectory, "index.md")
        if not os.path.exists(titlepage):
            print(f"Missing {titlepage}, ending...")
            return

        with open(titlepage, 'r') as file:
            soup = BeautifulSoup(markdown(file.read()), "html.parser")
            title = soup.find('h1').get_text().lower()
            tree.append(title)

        for x in files:
            if x.endswith(".md"):
                infile = os.path.join(indirectory, x)
                outfile = os.path.join(outdirectory, x.replace(".md", ".html"))

                print(f"{infile} ---> {outfile}")
                transform(infile, outfile, tree)

        for subdir in subdirs:
            build(os.path.join(folder, subdir), os.path.join(outfolder, subdir), tree)
        
        tree.pop()
        break
    


def loadtemplate(source):
    global template

    with open(os.path.join(source, 'header.html'), 'r') as file:
        header = file.read()

    with open(os.path.join(source, 'footer.html'), 'r') as file:
        footer = file.read()

    template.header = header
    template.footer = footer


if os.path.exists("./docs"):
    #delete previous build
    delete("./docs")
else:
    #create new build dir
    os.mkdir("./docs")

#init global template vars
loadtemplate("./template")

build("./md", "./docs")



