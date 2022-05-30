from flask import Flask, render_template, request
from persons import persons

print(persons)

app = Flask(__name__)

PAGE_LENGTH = 12

def toPaginatedList(list):
    return [list[i:i+PAGE_LENGTH] for i in range(0, len(list), PAGE_LENGTH)] 


@app.route("/")
def index():
    page = request.args.get('page', 1, type=int)
    list = toPaginatedList(persons)

    if page < 1:
        page = 1
    if page > len(list):
        page = len(list)

    return render_template('index.html', persons={
        "list": list[page - 1],
        "pages": len(list),
        "page": page
    })

if __name__ == '__main__':
    app.run()