from flask import Flask, render_template, request, redirect, url_for
from database import get_tasks, add_task, show_task

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        tasks = get_tasks()
        return render_template("index.html", tasks=tasks)

    else:
        title = request.form["title"]
        content = request.form["content"]
        due_date = request.form["due_date"]
        status = request.form["status"]
        add_task(title, content, due_date, status)
        return redirect(url_for("index"))


@app.route("/show/<int:id>")
def show(id):
    task = show_task(id)
    return render_template("show.html", task=task)



if __name__ == "__main__":
    app.run(port=8000, debug=True)
