import os
from types import SimpleNamespace

from flask import Flask, render_template, request


app = Flask(__name__)


QUIZ = [
    {
        "section": "Part I - Bar Operations & Safety",
        "questions": [
            {
                "question": "What should you do if a grounded electrical equipment develops a grounding issue during operation?",
                "options": {
                    "A": "Continue using it carefully",
                    "B": "Unplug the grounded equipment to avoid accidents",
                    "C": "Pour water on the equipment",
                    "D": "Ignore the issue",
                },
                "answer": "B",
            },
            {
                "question": "When should the bar be cleaned?",
                "options": {
                    "A": "Before opening only",
                    "B": "After closing only",
                    "C": "During, before, and after operation",
                    "D": "Once a week",
                },
                "answer": "C",
            },
            {
                "question": "What should you do if cleaning equipment malfunctions during cleaning operations?",
                "options": {
                    "A": "Continue using it",
                    "B": "Store it immediately",
                    "C": "Shut down the equipment and repair or replace it",
                    "D": "Ignore the malfunction",
                },
                "answer": "C",
            },
            {
                "question": "What safety measure should be observed when cleaning tiled areas?",
                "options": {
                    "A": "Wear sunglasses",
                    "B": "Place a warning sign in the cleaning area",
                    "C": "Turn off all lights",
                    "D": "Close the establishment",
                },
                "answer": "B",
            },
            {
                "question": "A customer accidentally slips on a wet floor while cleaning is being conducted. What should you do first?",
                "options": {
                    "A": "Continue cleaning",
                    "B": "Ask another guest to help",
                    "C": "Apologize, check the guest's condition, assist, and provide first aid if needed",
                    "D": "Leave the customer alone",
                },
                "answer": "C",
            },
            {
                "question": "How should a clean bar area look after following enterprise cleaning procedures?",
                "options": {
                    "A": "Decorated only",
                    "B": "Dry only",
                    "C": "Clear and sanitized",
                    "D": "Empty",
                },
                "answer": "C",
            },
        ],
    },
    {
        "section": "Part II - Bar Knowledge",
        "questions": [
            {
                "question": "What are the three basic parts of the bar?",
                "options": {
                    "A": "Front Bar, Side Bar, Service Bar",
                    "B": "Front Bar, Under Bar, Back Bar",
                    "C": "Service Bar, Cocktail Bar, Lounge Bar",
                    "D": "Counter Bar, Ice Bar, Wine Bar",
                },
                "answer": "B",
            },
            {
                "question": "How would you differentiate a tumbler from a footed glass?",
                "options": {
                    "A": "Tumblers are made of plastic",
                    "B": "Footed glasses are always larger",
                    "C": "Tumblers have no stem, while footed glasses sit directly on a foot or base",
                    "D": "There is no difference",
                },
                "answer": "C",
            },
            {
                "question": "How many milliliters are in one ounce?",
                "options": {
                    "A": "15 ml",
                    "B": "20 ml",
                    "C": "25 ml",
                    "D": "30 ml",
                },
                "answer": "D",
            },
            {
                "question": "How would you differentiate a brandy from a Cognac?",
                "options": {
                    "A": "Cognac is not a brandy",
                    "B": "Brandy is a type of beer",
                    "C": "Cognac is a specific type of brandy produced under stricter standards",
                    "D": "They are exactly the same",
                },
                "answer": "C",
            },
        ],
    },
    {
        "section": "Part III - Cocktail Preparation",
        "questions": [
            {
                "question": "What is the correct procedure when using the stir method for cocktails?",
                "options": {
                    "A": "Shake vigorously",
                    "B": "Blend all ingredients",
                    "C": "Chill the glass with ice and stir the drink before serving in the proper glass",
                    "D": "Add soda first",
                },
                "answer": "C",
            },
            {
                "question": "How do you make a basic syrup?",
                "options": {
                    "A": "1 cup sugar and 2 cups water",
                    "B": "1 cup sugar and 1 cup hot water",
                    "C": "2 cups sugar and 1 cup water",
                    "D": "Sugar only",
                },
                "answer": "B",
            },
            {
                "question": "How would you make a Rainbow Cocktail?",
                "options": {
                    "A": "Mix all ingredients together",
                    "B": "Shake vigorously",
                    "C": "Layer ingredients from heavy to light liquors",
                    "D": "Stir continuously",
                },
                "answer": "C",
            },
        ],
    },
    {
        "section": "Part IV - Wine Knowledge",
        "questions": [
            {
                "question": "What is the proper storage position for wine bottles?",
                "options": {
                    "A": "Upright at all times",
                    "B": "Horizontal only",
                    "C": "45-degree slanted position with the cork moist",
                    "D": "Upside down",
                },
                "answer": "C",
            },
            {
                "question": "Which wine is commonly recommended for health benefits due to its antioxidants?",
                "options": {
                    "A": "White Wine",
                    "B": "Rose Wine",
                    "C": "Sparkling Wine",
                    "D": "Red Wine",
                },
                "answer": "D",
            },
            {
                "question": "What is the correct order when serving multiple types of wines?",
                "options": {
                    "A": "Sweet to dry",
                    "B": "Red to white",
                    "C": "Dry to sweet, young to old, light-bodied to full-bodied, white to red",
                    "D": "Expensive to inexpensive",
                },
                "answer": "C",
            },
            {
                "question": "What is the highest classification among French wines according to your reviewer?",
                "options": {
                    "A": "Merlot",
                    "B": "Cabernet Sauvignon",
                    "C": "Chardonnay",
                    "D": "Pinot Noir",
                },
                "answer": "C",
            },
        ],
    },
    {
        "section": "Part V - Wine Service",
        "questions": [
            {
                "question": "What is the proper method of decanting wine?",
                "options": {
                    "A": "Shake the bottle before serving",
                    "B": "Transfer the wine slowly to a decanter while observing for sediment",
                    "C": "Stir the wine continuously",
                    "D": "Pour directly into glasses",
                },
                "answer": "B",
            },
            {
                "question": "What should be done when presenting a decanted wine to guests?",
                "options": {
                    "A": "Serve immediately without explanation",
                    "B": "Leave the bottle in storage",
                    "C": "Present the decanted wine in front of the guest table and explain the procedure",
                    "D": "Ask guests to pour their own wine",
                },
                "answer": "C",
            },
            {
                "question": "If the cork breaks and falls into the bottle, what should you do?",
                "options": {
                    "A": "Serve the wine immediately",
                    "B": "Throw away the bottle",
                    "C": "Decant and strain the wine",
                    "D": "Shake the bottle",
                },
                "answer": "C",
            },
            {
                "question": "What should you do if the cork becomes disintegrated during opening?",
                "options": {
                    "A": "Ignore it",
                    "B": "Serve the wine anyway",
                    "C": "Report the wine as a spoiled item",
                    "D": "Add ice",
                },
                "answer": "C",
            },
            {
                "question": "If the guest says the wine is faulty, what should you do?",
                "options": {
                    "A": "Argue with the guest",
                    "B": "Replace the wine and allow the guest to evaluate the replacement",
                    "C": "Charge the guest again",
                    "D": "Ignore the complaint",
                },
                "answer": "B",
            },
            {
                "question": "What are the proper steps in handling a wine complaint?",
                "options": {
                    "A": "Ignore, argue, and leave",
                    "B": "Hear, empathize, apologize, respond, and take immediate action",
                    "C": "Call security immediately",
                    "D": "Offer another drink without listening",
                },
                "answer": "B",
            },
        ],
    },
    {
        "section": "Part VI - Champagne & Sparkling Wine Service",
        "questions": [
            {
                "question": "What is the proper procedure when opening and pouring Champagne or other sparkling wines?",
                "options": {
                    "A": "Point the bottle toward guests",
                    "B": "Shake the bottle before opening",
                    "C": "Cover the mouth with a clean napkin and point it away from guests while opening",
                    "D": "Open it as quickly as possible",
                },
                "answer": "C",
            },
        ],
    },
    {
        "section": "Part VII - Sensory Evaluation",
        "questions": [
            {
                "question": "What are the steps in conducting a sensory evaluation of wine?",
                "options": {
                    "A": "Pour, drink, finish",
                    "B": "Smell, sip, swallow",
                    "C": "See, swirl, sniff, sip, savor",
                    "D": "Taste only",
                },
                "answer": "C",
            },
        ],
    },
]


def numbered_questions():
    questions = []
    number = 1
    for group in QUIZ:
        for item in group["questions"]:
            questions.append({**item, "number": number, "section": group["section"]})
            number += 1
    return questions


def template_sections():
    return [
        SimpleNamespace(
            section=group["section"],
            questions=[SimpleNamespace(**question) for question in group["questions"]],
        )
        for group in QUIZ
    ]


@app.route("/", methods=["GET", "POST"])
def index():
    questions = numbered_questions()
    submitted = request.method == "POST"
    selected_answers = {}
    score = 0

    if submitted:
        for question in questions:
            selected = request.form.get(f"q{question['number']}", "")
            selected_answers[question["number"]] = selected
            if selected == question["answer"]:
                score += 1

    return render_template(
        "index.html",
        quiz=template_sections(),
        questions=questions,
        selected_answers=selected_answers,
        submitted=submitted,
        score=score,
        total=len(questions),
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
