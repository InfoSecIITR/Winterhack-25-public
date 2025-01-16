from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

# In-memory data
bugs = []
FLAG = os.environ.get("FLAG", "winterhack{DO_NOT_SUBMIT_THIS_FLAG}")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/report", methods=["GET", "POST"])
def report_bug():
    if request.method == "POST":
        title = request.form.get("title", "")
        description = request.form.get("description", "")
        if title and description:
            bugs.append({"title": title, "description": description, "comments": []})
            return redirect(url_for("view_bugs"))
        return "Invalid input!"
    return render_template("report.html")

@app.route("/bugs")
def view_bugs():
    return render_template("bugs.html", bugs=bugs)

@app.route("/bugs/<int:bug_id>", methods=["GET", "POST"])
def bug_details(bug_id):
    if bug_id >= len(bugs):
        return "Bug not found!", 404

    bug = bugs[bug_id]
    if request.method == "POST":
        comment = request.form.get("comment", "")
        if comment:
            bug["comments"].append(comment)
            return redirect(url_for("bug_details", bug_id=bug_id))
    return render_template("bug_details.html", bug=bug, bug_id=bug_id)

@app.route("/forbidden")
def forbidden():
    return "Forbidden access!", 403

@app.route("/flag")
def flag():
    return FLAG

# if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=5000)

