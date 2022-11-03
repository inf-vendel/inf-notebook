import os
from markdown import markdown

basedir = os.path.abspath(os.path.dirname(__file__))
data = os.path.join(basedir, 'data/')

def get_items():
    # Return a sorted list of all .md files' names (without extension) as a list
    return sorted([i.replace(".md", "") for i in os.listdir(data) if ".md" in i], reverse=True)

def get_item(page):
    items = get_items()
    if page in [p.replace(".md", "") for p in items]:
        text = ""
        with open(os.path.join(data, f'{page}.md'), "r", encoding="utf-8") as file:
            text = file.read()
        html = markdown(text, extensions=['fenced_code', 'footnotes'])
        return html
    else:
        return f"Not found learning material with {page}."

def save_data(file):
    filename = file["title"] 
    if filename in  get_items():
        return {"type":"danger", "text":"Filename already taken."}
    with open(os.path.join(data + filename + ".md"), "x", encoding = 'utf-8') as f:
        f.write(file["input"])
    return {"type":"success", "text":"Saved successfully."}
