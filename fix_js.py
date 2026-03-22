with open('/app/index.html', 'r') as f:
    content = f.read()

bad_js = '''            else if (state.view === 'slide') startLearning();
            const quizSaved = localStorage.getItem("alba-quiz-collapsed");
            if (quizSaved !== null) {
                state.quizCollapsed = quizSaved === "true";
            }

            const quizStrip = document.getElementById("quiz-strip");
            const quizIcon = document.getElementById("quiz-toggle-icon");
            if (state.quizCollapsed) {
                quizStrip.classList.add("collapsed");
                if (quizIcon) quizIcon.innerText = "expand_less";
            } else {
                quizStrip.classList.remove("collapsed");
                if (quizIcon) quizIcon.innerText = "expand_more";
            }

            else if (state.view === 'final-quiz') startFinalQuiz();'''

good_js = '''            const quizSaved = localStorage.getItem("alba-quiz-collapsed");
            if (quizSaved !== null) {
                state.quizCollapsed = quizSaved === "true";
            }

            const quizStrip = document.getElementById("quiz-strip");
            const quizIcon = document.getElementById("quiz-toggle-icon");
            if (state.quizCollapsed) {
                quizStrip.classList.add("collapsed");
                if (quizIcon) quizIcon.innerText = "expand_less";
            } else {
                quizStrip.classList.remove("collapsed");
                if (quizIcon) quizIcon.innerText = "expand_more";
            }

            if (state.view === 'dashboard') showDashboard();
            else if (state.view === 'slide') startLearning();
            else if (state.view === 'final-quiz') startFinalQuiz();'''

content = content.replace(bad_js, good_js)

with open('/app/index.html', 'w') as f:
    f.write(content)
