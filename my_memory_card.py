from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QButtonGroup, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QGroupBox
from random import randint, shuffle
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
question_list = []
question_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский'))
question_list.append(Question("Сколько лет ёжику", "36", "25", "40", "54"))
question_list.append(Question("Какая фамилия у Путина", "Путин", "Брежнев", "Ельцин", "Горабачёв"))
app = QApplication([])
main_win = QWidget()
main_win.resize(400, 400)
main_win.setWindowTitle("Memory Card")

lb_Question = QLabel("Какой национальности не существует?")
button = QPushButton("Ответить")
RadioGroupBox = QGroupBox("Варианты ответов")
btn_answer1 = QRadioButton("Энцы")
btn_answer2 = QRadioButton("Смурфы")
btn_answer3 = QRadioButton("Чулымцы")
btn_answer4 = QRadioButton("Алеуты")

RadioGroup = QButtonGroup()
RadioGroup.addButton(btn_answer1)
RadioGroup.addButton(btn_answer2)
RadioGroup.addButton(btn_answer3)
RadioGroup.addButton(btn_answer4)

layoutH1 = QHBoxLayout()
layoutV2 = QVBoxLayout()
layoutV3 = QVBoxLayout()
# layoutH1.addWidget(question, alignment = Qt.AlignCenter)
layoutV2.addWidget(btn_answer1)
layoutV2.addWidget(btn_answer2)
layoutV3.addWidget(btn_answer3)
layoutV3.addWidget(btn_answer4)
layoutH1.addLayout(layoutV2)
layoutH1.addLayout(layoutV3)
# layout_main = QVBoxLayout()
# layout_main.addLayout(layoutH1)
# layout_main.addLayout(layoutV2)
# layout_main.addLayout(layoutV3)
RadioGroupBox.setLayout(layoutH1)
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel("прав ты или нет")
lb_Correct = QLabel("ответ будет тут!")
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()
layout_line3.addStretch(1)
layout_line3.addWidget(button, stretch=2)
layout_line3.addStretch(1)
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
main_win.setLayout(layout_card)


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText('Следующий вопрос')
 
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    button.setText('Ответить')
    RadioGroup.setExclusive(False) 
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    RadioGroup.setExclusive(True) 
 
answers = [btn_answer1, btn_answer2, btn_answer3, btn_answer4]
 
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer) 
    show_question() 
 
def show_correct(res):
    lb_Result.setText(res)
    show_result()
 
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
def next_question():
    # main_win.cur_question = main_win.cur_question + 1
    cur_question = randint(0 , len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)
    question_list.remove(q)
    if len(question_list) <= 0:
        print("Поздравляем!Вы ответили на все вопросы.")
        button.setText(" ")
def click_OK():
    if button.text() == "Ответить":
        check_answer()
    else:
        next_question()
# main_win.cur_question = -1
button.clicked.connect(click_OK)
next_question()
main_win.show()
app.exec_()