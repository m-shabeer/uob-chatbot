from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# --- Home page ---
@app.get("/")
def home():
    return render_template("index.html")


# --- Chat API ---
@app.post("/api/chat")
def chat():
    data = request.get_json(silent=True) or {}
    q = str(data.get("question", "")).strip()
    t = q.lower()

    def ans(text: str):
        return jsonify({"answer": text})

    if not q:
        return ans("Please type a question.")

    # ADHD / Focus / Executive function
    if any(k in t for k in ["adhd", "focus", "distract", "attention", "procrast", "executive"]):
        return ans(
            "ADHD / focus help (Canvas):\n"
            "1) Use 10–15 minute study blocks + short breaks.\n"
            "2) Keep one Canvas tab open to reduce distraction.\n"
            "3) Write one next action: Modules → Week X → resource.\n"
            "4) Use Canvas To-Do / Calendar to track deadlines.\n"
            "If you tell me your task (reading / submitting / quiz), I’ll give step-by-step."
        )

    # Autism / Overwhelm / Need predictability
    if any(k in t for k in ["autism", "overwhelm", "routine", "change", "uncertain", "shutdown", "meltdown"]):
        return ans(
            "Autism / feeling overwhelmed:\n"
            "1) Start in Modules and follow the weekly order (predictable path).\n"
            "2) Break tasks into 3 steps max at a time.\n"
            "3) Open items in a new tab so you don’t lose your place.\n"
            "If the module layout is unclear, ask the module team for a weekly summary."
        )

    # Dyslexia / Reading difficulty
    if any(k in t for k in ["dyslexia", "reading", "hard to read", "long text", "spelling", "visual stress"]):
        return ans(
            "Dyslexia / reading support:\n"
            "1) Use browser zoom (Ctrl + +) and increase text size.\n"
            "2) Read headings first, then small chunks.\n"
            "3) Use text-to-speech / ‘listen’ tools if available.\n"
            "4) Ask for accessible formats (HTML / tagged PDF / audio) if needed."
        )

    # Dyspraxia / Motor / Organisation
    if any(k in t for k in ["dyspraxia", "motor", "coordination", "organisation", "organization", "planning"]):
        return ans(
            "Dyspraxia / organisation support:\n"
            "1) Use Canvas Calendar/To-Do to track what’s due.\n"
            "2) Keep one folder per module/week for downloads.\n"
            "3) Use a submission checklist (file name, format, upload, confirm).\n"
            "If uploading is difficult, tell me your device/browser and what step fails."
        )

    # Anxiety / Stress
    if any(k in t for k in ["anxiety", "panic", "stress", "worried", "overthinking"]):
        return ans(
            "Anxiety / stress support:\n"
            "1) Do one small step first (open module → find task → note due date).\n"
            "2) Use a timer and short breaks.\n"
            "3) If assessments are affected, contact your module team early.\n"
            "If you need wellbeing support, use University support services."
        )

    # Sensory overload / Busy interface
    if any(k in t for k in ["sensory", "overstim", "overload", "too much", "busy", "noise"]):
        return ans(
            "Sensory overload / busy interface:\n"
            "1) Focus on Modules (reduces jumping around pages).\n"
            "2) Close side panels and keep one tab open.\n"
            "3) Use reader mode where possible.\n"
            "Tell me which page feels overwhelming and I’ll suggest a simpler path."
        )

    # Captions / transcripts / video accessibility
    if any(k in t for k in ["caption", "captions", "subtitle", "subtitles", "transcript", "video"]):
        return ans(
            "Captions & transcripts:\n"
            "1) Check the video player for CC/captions.\n"
            "2) Look for a transcript link near the video.\n"
            "3) If missing, ask the module team to provide captions/transcripts."
        )

    # Screen reader / keyboard / contrast
    if any(k in t for k in ["screen reader", "keyboard", "tab", "accessibility", "contrast", "aria"]):
        return ans(
            "Keyboard / screen-reader tips:\n"
            "1) Tab / Shift+Tab to move, Enter to activate.\n"
            "2) Increase text size/contrast in your browser settings.\n"
            "3) If PDFs/images aren’t accessible, report it to the module team."
        )

    # Quizzes / extra time / adjustments
    if any(k in t for k in ["quiz", "test", "exam", "extra time", "extended time", "time limit", "adjustment", "accommodation"]):
        return ans(
            "Quiz/exam adjustments:\n"
            "1) Adjustments are usually arranged via Disability Service.\n"
            "2) Once approved, module staff can apply quiz settings in Canvas.\n"
            "3) If urgent, email your module leader for short-term support."
        )

    # Deadlines / extensions / mitigation
    if any(k in t for k in ["deadline", "late", "extension", "mitigation", "missed"]):
        return ans(
            "Deadlines & extensions:\n"
            "1) Check the due date in Canvas (Assignments/To-Do/Calendar).\n"
            "2) Request an extension from your module team as early as possible.\n"
            "3) If difficulties are ongoing, discuss support/adjustments with University services."
        )

    # Navigation / can't find assignment/content
    if any(k in t for k in ["can't find", "cannot find", "where", "lost", "confusing", "modules", "assignment", "submission"]):
        return ans(
            "Finding things in Canvas:\n"
            "1) Go to Modules → choose the correct week/unit.\n"
            "2) Use Ctrl+F to search the page.\n"
            "3) Check Assignments for submission links.\n"
            "Tell me what you’re looking for (lecture / quiz / assignment) and I’ll guide you."
        )

    # Contact support (UoB routing)
    if any(k in t for k in ["contact", "support", "disability", "bradford", "uob", "help", "it services", "it service"]):
        return ans(
            "University of Bradford support routes:\n"
            "• Disability Service: reasonable adjustments and study support.\n"
            "• IT Services: Canvas login/access technical issues.\n"
            "• Module team: content layout, captions, assessment arrangements.\n"
            "If you say whether it’s (A) adjustment, (B) technical, or (C) module content, I’ll direct you."
        )

    # Default fallback
    return ans(
        "I’m a prototype Canvas accessibility chatbot for the University of Bradford.\n"
        "Ask about: ADHD/focus, autism/overwhelm, dyslexia/reading, dyspraxia/organisation, "
        "captions/transcripts, keyboard/screen reader, quizzes/extra time, deadlines/extensions, or support contacts."
    )


# --- Run (Render-friendly) ---
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
