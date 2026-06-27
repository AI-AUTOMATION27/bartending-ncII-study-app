# NC II Bar Operations Quiz

A Python Flask multiple-choice reviewer website for NC II Bar Operations, Wine Service, Champagne Service, and Sensory Evaluation topics.

## What Is Inside

- `app.py` - the Python Flask application
- `templates/index.html` - the quiz webpage template
- `static/styles.css` - the design and mobile layout
- `requirements.txt` - Python packages needed by Render
- `render.yaml` - optional Render deploy settings

## Run Locally

Install the dependencies:

```bash
pip install -r requirements.txt
```

Start the website:

```bash
python app.py
```

Open this in your browser:

```text
http://localhost:10000
```

## How To Use

1. Choose an answer for each question.
2. Use the section buttons to jump between topics.
3. Click **Submit Answers** to see the score.
4. Review the highlighted correct and wrong answers.
5. Click **Reset** to answer again.

## Deploy To Render

Use **Web Service** on Render.

Settings:

- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`

## Notes

This quiz does not need a database or login.
