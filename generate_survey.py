from jinja2 import Template

# ====================== FULL 24 QUESTIONS WITH YOUR EXACT SCORING ======================
questions = [
    {
        "id": "consent",
        "type": "radio",
        "text": "1. Consent<br>I have read the information above about this research study. I understand that:<br>• My participation is voluntary and I may stop at any time.<br>• My responses are anonymous and will be kept confidential.<br>• The results will be used in a master’s thesis and may also be published or presented in academic settings.<br>• I am at least 18 years of age",
        "choices": [
            {"label": "I agree", "value": "agree"},
            {"label": "I do not agree to participate", "value": "disagree"}
        ],
        "required": True
    },
    {
        "id": "llm_understand",
        "type": "radio",
        "text": "2. Understanding of LLM<br>Do you understand that LLM refers to AI tools such as ChatGPT, DeepSeek, Claude and other similar programs?",
        "choices": [
            {"label": "Yes", "value": "1"},
            {"label": "No", "value": "0"}
        ]
    },
    {
        "id": "years_cs",
        "type": "radio",
        "text": "3. Years Studied Computer Science<br>How long have you studied computer science in a learning environment such as high school or college?",
        "choices": [
            {"label": "0–1 years", "value": "0.5"},
            {"label": "2–3 years", "value": "2.5"},
            {"label": "3–5 years", "value": "4"},
            {"label": "5+ years", "value": "5"}
        ]
    },
    {
        "id": "academic_level",
        "type": "radio",
        "text": "4. Academic Level<br>Are you an Undergraduate or Graduate of the Computer Science Department at Lewis University?",
        "choices": [
            {"label": "Undergraduate", "value": "0"},
            {"label": "Graduate", "value": "1"}
        ]
    },
    {
        "id": "disciplines",
        "type": "checkbox",
        "text": "5. Discipline Studied (Select all that apply)<br>What discipline of computer science have you studied formally or informally?",
        "choices": [
            {"label": "Cyber Security"},
            {"label": "Software Engineering"},
            {"label": "Data Analytics"},
            {"label": "AI or Machine Learning"},
            {"label": "Algorithms and Theory"},
            {"label": "Programming/Coding"},
            {"label": "Networking"},
            {"label": "IT"},
            {"label": "Computer Graphics"},
            {"label": "Video Games / Media Development"},
            {"label": "Other"}
        ]
    },
    {
        "id": "familiarity",
        "type": "radio",
        "text": "6. Familiarity with LLMs<br>How familiar are you with LLMs?",
        "choices": [
            {"label": "I do not know what it is", "value": "0"},
            {"label": "I have heard of it", "value": "1"},
            {"label": "I know a little about it", "value": "2"},
            {"label": "I know a lot about it", "value": "3"}
        ]
    },
    {
        "id": "availability",
        "type": "radio",
        "text": "7. Availability of LLMs When Starting<br>Were LLM tools available when you started studying computer science?",
        "choices": [
            {"label": "No AI tools were available when I started learning", "value": "0"},
            {"label": "Some AI tools were available when I started learning", "value": "1"},
            {"label": "AI tools were available when I started learning, but they were not prominent", "value": "2"},
            {"label": "AI tools were very available when I started learning", "value": "3"}
        ]
    },
    {
        "id": "personal_use",
        "type": "radio",
        "text": "8. Personal Use of LLMs (usage index)<br>Do you use LLMs personally (non-school related)?",
        "choices": [
            {"label": "I do not use it", "value": "0"},
            {"label": "I sometimes use it", "value": "1"},
            {"label": "I use it a lot", "value": "2"}
        ]
    },
    {
        "id": "school_use",
        "type": "radio",
        "text": "9. School Use of LLMs (usage index)<br>Do you use LLM tools to assist in school-related activities such as homework or studying?",
        "choices": [
            {"label": "Yes", "value": "1"},
            {"label": "No", "value": "0"}
        ]
    },
    {
        "id": "how_used_school",
        "type": "checkbox",
        "text": "10. How LLMs Are Used for School (Select all that apply)<br>How do you use LLM tools for school activities?",
        "choices": [
            {"label": "I need help studying"},
            {"label": "I need more explanation for course materials"},
            {"label": "I need help answering homework questions"},
            {"label": "I need help during online quizzes and tests"},
            {"label": "I need visual aids for course materials"}
        ]
    },
    {
        "id": "dependency",
        "type": "radio",
        "text": "11. Dependency on LLMs (dependency index)<br>How much do you depend on LLM tools in your computer science courses?",
        "choices": [
            {"label": "I do not depend on them", "value": "0"},
            {"label": "I depend on them a little", "value": "1"},
            {"label": "I depend on them a lot", "value": "2"}
        ]
    },
    {
        "id": "gen_ed_use",
        "type": "radio",
        "text": "12. Use in General Education<br>How have you used LLM tools for general education courses?",
        "choices": [
            {"label": "I do not use any tools to help me", "value": "0"},
            {"label": "I research fundamental concepts", "value": "1"},
            {"label": "I use it as a helpful tool", "value": "2"},
            {"label": "I rely on it", "value": "3"}
        ]
    },
    {
        "id": "helpfulness",
        "type": "radio",
        "text": "13. Helpfulness for Understanding (Learning Impact)<br>How helpful have LLM tools been in improving your understanding of computer science concepts?",
        "choices": [
            {"label": "Very unhelpful", "value": "0"},
            {"label": "Somewhat unhelpful", "value": "1"},
            {"label": "Neither helpful nor unhelpful", "value": "2"},
            {"label": "Somewhat helpful", "value": "3"},
            {"label": "Very helpful", "value": "4"}
        ]
    },
    {
        "id": "impact_problem_solving",
        "type": "radio",
        "text": "14. Impact on Problem Solving (Learning Impact)<br>How have LLM tools impacted your ability to problem solve?",
        "choices": [
            {"label": "It reduced my ability to problem solve", "value": "3"},
            {"label": "It has not helped me at all", "value": "2"},
            {"label": "It helps me a little", "value": "1"},
            {"label": "It helps me a lot", "value": "0"}
        ]
    },
    {
        "id": "impact_retention",
        "type": "radio",
        "text": "15. Impact on Retention (Learning Impact)<br>Have LLM tools impacted your ability to retain and remember computer science fundamentals?",
        "choices": [
            {"label": "I remember more without it", "value": "0"},
            {"label": "I remember the same amount with or without it", "value": "1"},
            {"label": "I remember a little less without it", "value": "2"},
            {"label": "I remember a lot less without it", "value": "3"}
        ]
    },
    {
        "id": "critical_thinking",
        "type": "radio",
        "text": "16. Critical Thinking (Learning Impact)<br>How have LLM tools affected your ability to think critically?",
        "choices": [
            {"label": "I can think critically better without it", "value": "0"},
            {"label": "I can think critically with or without it", "value": "1"},
            {"label": "I can think a little less critically with it", "value": "2"},
            {"label": "I can think a lot less critically with it", "value": "3"}
        ]
    },
    {
        "id": "partial_assignment",
        "type": "radio",
        "text": "17. Partial Assignment Use (Integrity Index)<br>Have you ever turned in an assignment that had partial answers or work from LLM tools?",
        "choices": [
            {"label": "No", "value": "0"},
            {"label": "Maybe", "value": "0.5"},
            {"label": "Yes", "value": "1"}
        ]
    },
    {
        "id": "partial_test",
        "type": "radio",
        "text": "18. Partial Test Use (Integrity Index)<br>Have you ever taken a quiz or test with partial answers from LLM tools?",
        "choices": [
            {"label": "No", "value": "0"},
            {"label": "Maybe", "value": "0.5"},
            {"label": "Yes", "value": "1"}
        ]
    },
    {
        "id": "full_assignment",
        "type": "radio",
        "text": "19. Full Assignment Use (Integrity Index)<br>Have you ever turned in an assignment fully generated by LLM tools?",
        "choices": [
            {"label": "No", "value": "0"},
            {"label": "Maybe", "value": "0.5"},
            {"label": "Yes", "value": "1"}
        ]
    },
    {
        "id": "full_test",
        "type": "radio",
        "text": "20. Full Test Use (Integrity Index)<br>Have you ever taken a quiz or test fully using LLM tools?",
        "choices": [
            {"label": "No", "value": "0"},
            {"label": "Maybe", "value": "0.5"},
            {"label": "Yes", "value": "1"}
        ]
    },
    {
        "id": "non_cs_writing",
        "type": "radio",
        "text": "21. LLM Use for Non-CS Writing (dependency index)<br>How often do you use LLM when writing for non-computer science courses?",
        "choices": [
            {"label": "Never", "value": "0"},
            {"label": "Almost never", "value": "1"},
            {"label": "Sometimes", "value": "2"},
            {"label": "Often", "value": "3"},
            {"label": "Almost Always", "value": "4"},
            {"label": "Always", "value": "5"}
        ]
    },
    {
        "id": "cs_writing",
        "type": "radio",
        "text": "22. LLM Use for CS Writing (dependency index & usage index)<br>How often do you use LLM tools when writing for computer science courses?",
        "choices": [
            {"label": "Never", "value": "0"},
            {"label": "Almost never", "value": "1"},
            {"label": "Sometimes", "value": "2"},
            {"label": "Often", "value": "3"},
            {"label": "Almost Always", "value": "4"},
            {"label": "Always", "value": "5"}
        ]
    },
    {
        "id": "programming",
        "type": "radio",
        "text": "23. LLM Use for Programming (dependency index)<br>Do you rely on LLM tools for programming?",
        "choices": [
            {"label": "I do not need LLM tools at all", "value": "0"},
            {"label": "LLM tools help me a little", "value": "1"},
            {"label": "I moderately rely on LLM tools", "value": "2"},
            {"label": "I heavily rely on LLM tools", "value": "3"}
        ]
    },
    {
        "id": "theory_questions",
        "type": "radio",
        "text": "24. LLM Use for Theory Questions (dependency index & usage index)<br>How often do you use LLM tools when answering theory questions in computer science courses?",
        "choices": [
            {"label": "Never", "value": "0"},
            {"label": "Almost never", "value": "1"},
            {"label": "Sometimes", "value": "2"},
            {"label": "Often", "value": "3"},
            {"label": "Almost Always", "value": "4"},
            {"label": "Always", "value": "5"}
        ]
    }
]

# ====================== HTML TEMPLATE WITH IMMEDIATE PERSONAL RESULTS ======================
template_str = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>LLM Learning Survey - Get Your AI Dependency Score</title>
    <style>
        body {font-family: Arial, sans-serif; max-width: 950px; margin: 40px auto; padding: 20px; line-height: 1.6;}
        h1, h2 {color: #0066cc;}
        fieldset {margin: 30px 0; padding: 20px; border: 1px solid #ddd; border-radius: 8px;}
        label {display: block; margin: 8px 0;}
        button {padding: 14px 32px; font-size: 18px; background: #0066cc; color: white; border: none; border-radius: 6px; cursor: pointer;}
        .result-box {background: #f0f8ff; padding: 25px; border: 3px solid #0066cc; border-radius: 10px; margin-top: 40px; display: none;}
        .score {font-size: 1.4em; font-weight: bold;}
    </style>
</head>
<body>
    <h1>LLM Impact on Computer Science Learning</h1>
    <p>View the full research results and case studies <a href="results.html" target="_blank">here</a>.</p>

    <form id="llm-survey">
        {% for q in questions %}
        <fieldset>
            <legend><strong>{{ loop.index }}. {{ q.text | safe }}</strong></legend>
            {% if q.type == 'radio' %}
                {% for c in q.choices %}
                <label><input type="radio" name="{{ q.id }}" value="{{ c.value }}" {% if q.required %}required{% endif %}> {{ c.label }}</label>
                {% endfor %}
            {% elif q.type == 'checkbox' %}
                {% for c in q.choices %}
                <label><input type="checkbox" name="{{ q.id }}[]" value="1"> {{ c.label }}</label>
                {% endfor %}
            {% endif %}
        </fieldset>
        {% endfor %}
        <button type="button" onclick="submitSurvey()">Submit & See My Personal AI Dependency Score</button>
    </form>

    <div id="personal-results" class="result-box">
        <h2>Your Personal AI Dependency Profile</h2>
        <p><strong>Dependency Index:</strong> <span id="dep-score" class="score"></span></p>
        <p><strong>Usage Index:</strong> <span id="usage-score" class="score"></span></p>
        <p><strong>Learning Impact Score:</strong> <span id="learn-score" class="score"></span></p>
        <p><strong>Integrity / Risk Level:</strong> <span id="risk-score" class="score"></span></p>
        <div id="interpretation" style="margin-top:20px; font-size:1.1em;"></div>
        <p style="margin-top:30px;"><a href="results.html" target="_blank">Compare your score with the full research findings</a></p>
    </div>

    <script>
        function calculateScores(formData) {
            let dep = 0, usage = 0, learn = 0, risk = 0;

            // === YOUR SCORING LOGIC (mapped from the values you provided) ===
            dep += parseFloat(formData.get("years_cs") || 0);
            dep += parseFloat(formData.get("dependency") || 0);
            dep += parseFloat(formData.get("non_cs_writing") || 0);
            dep += parseFloat(formData.get("cs_writing") || 0);
            dep += parseFloat(formData.get("programming") || 0);
            dep += parseFloat(formData.get("theory_questions") || 0);

            usage += parseFloat(formData.get("personal_use") || 0);
            usage += parseFloat(formData.get("school_use") || 0);
            usage += parseFloat(formData.get("cs_writing") || 0);
            usage += parseFloat(formData.get("theory_questions") || 0);

            learn += parseFloat(formData.get("helpfulness") || 0);
            learn += (4 - parseFloat(formData.get("impact_problem_solving") || 0));  // inverted
            learn += (3 - parseFloat(formData.get("impact_retention") || 0));       // inverted
            learn += (3 - parseFloat(formData.get("critical_thinking") || 0));      // inverted

            risk += parseFloat(formData.get("partial_assignment") || 0);
            risk += parseFloat(formData.get("partial_test") || 0);
            risk += parseFloat(formData.get("full_assignment") || 0);
            risk += parseFloat(formData.get("full_test") || 0);

            // Normalize or scale as needed for your research
            const max_dep = 20;   // adjust based on your case studies
            const interpretation = dep > 14 ? "High AI Dependency - Similar to heavy users in the case studies." :
                                  dep > 8  ? "Moderate AI Dependency" : "Low AI Dependency";

            return {
                dependency: dep.toFixed(1),
                usage: usage.toFixed(1),
                learning: learn.toFixed(1),
                risk: risk.toFixed(1),
                interpretation: interpretation
            };
        }

        function submitSurvey() {
            const form = document.getElementById('llm-survey');
            const formData = new FormData(form);
            const scores = calculateScores(formData);

            document.getElementById('dep-score').textContent = scores.dependency;
            document.getElementById('usage-score').textContent = scores.usage;
            document.getElementById('learn-score').textContent = scores.learning;
            document.getElementById('risk-score').textContent = scores.risk;
            document.getElementById('interpretation').innerHTML = `<strong>Interpretation:</strong> ${scores.interpretation}`;

            const resultBox = document.getElementById('personal-results');
            resultBox.style.display = 'block';
            resultBox.scrollIntoView({ behavior: "smooth" });
        }
    </script>
</body>
</html>
"""

# Generate the file
template = Template(template_str)
html_output = template.render(questions=questions)

with open("survey.html", "w", encoding="utf-8") as f:
    f.write(html_output)

print("✅ survey.html has been generated with all 24 questions!")
print("✅ Users can now take the survey and instantly see their personal AI Dependency score.")
print("\nNext: Create a simple index.html that links to survey.html and results.html")
