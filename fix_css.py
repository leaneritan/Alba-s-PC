import re

with open('/app/index.html', 'r') as f:
    content = f.read()

# Define the entire CSS block we want for quiz-strip and quiz-toggle
css_replacement = '''    .quiz-strip { height: 220px; background: var(--teal-quiz); padding: 0 48px; display: flex; align-items: center; gap: 24px; border-top: 1px solid rgba(0, 0, 0, 0.05); position: relative; }
    .quiz-intro { display: flex; align-items: center; gap: 12px; min-width: 180px; }
    .quiz-icon { color: var(--primary); font-size: 1.8rem; }
    .quiz-labels h4 { font-weight: 800; color: var(--primary); }
    .quiz-labels span { font-size: 0.7rem; opacity: 0.6; }
    .quiz-body { flex: 1; display: flex; flex-direction: column; justify-content: center; overflow: hidden; position: relative; height: 100%; }
    .quiz-question { font-weight: 700; margin-bottom: 12px; font-size: 1.1rem; }
    .quiz-options { display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 8px; }
    .quiz-opt {
        background: var(--white);
        border: 1px solid #ddd;
        padding: 10px 24px;
        border-radius: 100px;
        font-weight: 700;
        font-size: 0.9rem;
        transition: all 0.2s;
        cursor: pointer;
    }
    .quiz-opt:hover { border-color: var(--secondary); }

    .quiz-strip.collapsed {
        height: 60px;
        cursor: pointer;
    }
    .quiz-strip.collapsed .quiz-body,
    .quiz-strip.collapsed .skip-link,
    .quiz-strip.collapsed .quiz-feedback {
        display: none;
    }
    .quiz-toggle {
        position: absolute;
        top: 15px;
        right: 48px;
        width: 30px;
        height: 30px;
        background: white;
        border: 1px solid var(--primary);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        z-index: 10;
        color: var(--primary);
    }
    .quiz-feedback { margin-left: 16px; font-weight: 800; font-size: 1.2rem; min-width: 150px; }'''

# Match from .quiz-strip to .quiz-feedback
pattern = re.compile(r'\.quiz-strip\s*\{.*?\.quiz-feedback\s*\{.*?\}(?=\s*\n\s*\.skip-link)', re.DOTALL)
new_content = pattern.sub(css_replacement, content)

with open('/app/index.html', 'w') as f:
    f.write(new_content)
