from flask import Flask
import utlils

app = Flask(__name__)

candidates = utlils.load_candidates()

@app.route("/")
def page_index():

    str_candidates = '<pre>'
    for candidate in candidates.values():
        str_candidates += f"{candidate['name']} \n" \
                          f"{candidate['position']} \n" \
                          f"{candidate['skills']} \n\n"
    str_candidates += '</pre>'
    return str_candidates


@app.route("/candidates/<int:id>")
def profile(id):
    candidate = candidates[id]

    str_candidates = f"<img src={candidate['picture']}></img> <br><br>{candidate['name']} <br><br>{candidate['position']} <br><br>{candidate['skills']} <br><br>"

    return str_candidates

@app.route("/skills/<skill>")
def skills(skill):
    str_candidates = '<pre>'

    for candidate in candidates.values():
        candidate_skills = candidate['skills'].split(', ')
        candidate_skills = [x.lower() for x in candidate_skills]

        if skill in candidate_skills:
            str_candidates += f"{candidate['name']} \n" \
                          f"{candidate['position']} \n" \
                          f"{candidate['skills']} \n\n"
    str_candidates += '</pre>'

    return str_candidates

app.run(debug=True)

