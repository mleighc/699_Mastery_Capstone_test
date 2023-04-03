import os.path
import markdown


def openfile(filename):
    filepath = os.path.join("frontend/app/pages/", filename)
    with open(filepath, "r", encoding="utf-8") as input_file:
        text = input_file.read()

    html = markdown.markdown(text)
    data = {"text": html}
    return data


# source: https://levelup.gitconnected.com/building-a-website-starter-with-fastapi-92d077092864
