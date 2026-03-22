with open('/app/index.html', 'r') as f:
    content = f.read()

old_line = '<div class="quiz-strip" id="quiz-strip">'
new_line = '''            <div class="quiz-strip" id="quiz-strip" onclick="if(this.classList.contains('collapsed')) toggleQuiz()">
                <button class="quiz-toggle" onclick="event.stopPropagation(); toggleQuiz()">
                    <span class="material-symbols-outlined" id="quiz-toggle-icon">expand_more</span>
                </button>'''

content = content.replace(old_line, new_line)

with open('/app/index.html', 'w') as f:
    f.write(content)
