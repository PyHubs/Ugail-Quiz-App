from prompt_toolkit.shortcuts import message_dialog #<= prompt_toolkit is great!
from prompt_toolkit.shortcuts import radiolist_dialog
from prompt_toolkit.styles import Style

red = Style.from_dict({
  'dialog':             'bg:#ff0000',
  'dialog frame.label': 'bg:#000000 #ff0000',
  'dialog.body':        'bg:#000000 #ff0000',
  'dialog shadow':      'bg:#ff0000',
})

green = Style.from_dict({
  'dialog':             'bg:#1da865',
  'dialog frame.label': 'bg:#000000 #1da865',
  'dialog.body':        'bg:#000000 #1da865',
  'dialog shadow':      'bg:#1da865',
  'button': 'bg:#1da865 #000000'
})

blue = Style.from_dict({
  'dialog':             'bg:#8babcc',
  'dialog frame.label': 'bg:#000000 #8babcc',
  'dialog.body':        'bg:#000000 #8babcc',
  'dialog shadow':      'bg:#8babcc',
  'button': 'bg:#8babcc #000000'
})

# Variabls
CORRECT = 0
WRONG = 0

# Dialogs
def msg(title, text): return message_dialog(title=title, text=text, style=blue).run()
def alert(title, text): return message_dialog(title=title, text=text, style=red).run()
  
def ask(title, text, values):
  return radiolist_dialog(title=title, text=text, values=values, style=green).run()

# Start
msg(
  title='Izkaans Python Quiz',
  text='Welcome to my basic Python Quiz! Click OK to continue. Better to use natively using powershell than replit.',
)

# Question 1
q1 = ask(
    title="hello world",
    text="Whats the correct method to say hello world?",
    values=[
        ("wrong", "write('Hello world')"),
        ("correct", "print('Hello world')"),
        ("wrong", "echo('Hello world')"),
        ("wrong", "writeln('Hello world')")
    ])

# Check if question 1 is correct or wrong
if q1 == "wrong":
  WRONG += 1
  alert(f"Correct: {CORRECT} Wrong: {WRONG}", "The answer is print('Hello world')")
else:
  CORRECT += 1
  msg(f"Correct: {CORRECT} Wrong: {WRONG}", "The answer is print('Hello world')")

# Question 2
q2 = ask(
  title='whats your account password?',
  text='How do we ask the user for their password?',
  values = [
    ("correct", "input('Enter your password> ')"),
    ("wrong", "ask('Enter your password> ')"),
    ("wrong", "prompt('Enter your password> ')"),
    ("wrong", "readline('Enter your password> ')"),
  ]
)

# Check if question 2 is correct or wrong
if q2 == "wrong":
  WRONG += 1
  alert(f"Correct: {CORRECT} Wrong: {WRONG}", "The answer is input('Hello world')")
else:
  CORRECT += 1
  msg(f"Correct: {CORRECT} Wrong: {WRONG}", "The answer is input('Hello world')")

# Question 3
q3 = ask(
  title="Make a variable store the version_info",
  text=("How do we make a variable called version_info contain a float?"),
  values = [
    ('correct', 'version_info = 1.0'),
    ('wrong', 'float version_info = 1.0'),
    ('wrong', 'var float version_info = 1.0'),
    ('wrong', 'var:float version_info = 1.0'),
  ]
)

# Check q3
if q3 == "wrong":
  WRONG += 1
  alert(f"Correct: {CORRECT} Wrong: {WRONG}", "The answer is version_info = 1.0")
else:
  CORRECT += 1
  msg(f"Correct: {CORRECT} Wrong: {WRONG}", "The answer is version_info = 1.0")

# Question 4
q4 = ask(
  title="Make a function in python",
  text=("How do we make a function that says Hello $name"),
  values = [
    ('wrong', 'function Say(name):\n    print(f"Hello {name}")'),
    ('correct', 'def Say(name):\n    print(f"Hello {name}")'),
    ('wrong', 'fn Say(name):\n    print(f"Hello {name}")'),
    ('wrong', 'function Say(name):\n     print(f"Hello {name}")'),
  ]
)

if q4 == "wrong":
  WRONG += 1
  alert(f'Correct: {CORRECT} Wrong: {WRONG}', 'The answer is def Say(name):\n    print(f"Hello {name}")')
else:
  msg(f"Correct: {CORRECT} Wrong: {WRONG}", "The answer is def say(name):\n print(f'Hello {name}')")

# Question 5
q5 = ask(
  title="Make an if statement",
  text=("How do we check if you are stupid"),
  values = [
    ('correct', 'if stupid == True: print("ur stupid")'),
    ('correct', 'if (stupid == True): print("ur stupid")'),
    ('dont', 'while stupid == True: print("ur stupid") break'),
  ]
)

if q5 == "correct":
  msg(f"Correct: {CORRECT} Wrong: {WRONG}", "The answer is def say(name):\n print(f'Hello {name}')")

# Question 6
q6 = ask(
  title="Execute function if its only a module",
  text=("Execute function if its only a module"),
  values = [
    ('wrong', 'if __module__ == False: main()'),
    ('correct', 'if __main__ == "__name__": main()'),
    ('wrong', 'if __executable__ == True: main()'),
  ]
)

if q6 == "wrong":
  WRONG += 1
  alert(f'Correct: {CORRECT} Wrong: {WRONG}', 'The answer is if __main__ == "__name__": main()')
else:
  msg(f"Correct: {CORRECT} Wrong: {WRONG}", "The answer is if __main__ == '__name__': main()")

# Question 7
q7 = ask(
  title="What is the worst GUI framework for python",
  text=("What is the worst GUI framework for python"),
  values = [
    ('correct', 'tkinter'),
    ('wrong', 'kivy'),
    ('wrong', 'pyqt'),
  ]
)

if q7 == "wrong":
  WRONG += 1
  alert(f'Correct: {CORRECT} Wrong: {WRONG}', 'The answer is tkinter')
else:
  msg(f"Correct: {CORRECT} Wrong: {WRONG}", "The answer is tkinter")

# Question 8
q8 = ask(
  title="How make tkinter window",
  text=("How make tkinter window"),
  values = [
    ('wrong', 'App()'),
    ('wrong', 'tk()'),
    ('wrong', 'Win()'),
    ('correct', 'Tk()'),
  ]
)

if q8 == "wrong":
  WRONG += 1
  alert(f'Correct: {CORRECT} Wrong: {WRONG}', 'The answer is Tk()')
else:
  msg(f"Correct: {CORRECT} Wrong: {WRONG}", "The answer is Tk()")

# Question 9
q9 = ask(
  title="What button will look better",
  text=("What button will look better"),
  values = [
    ('correct', 'tk.Button(root, text="Click me :)", command=download_virus)'),
    ('wrong', 'ttk.Button(root, text="Click me :)", command=download_virus)'),
  ]
)

if q9 == "wrong":
  WRONG += 1
  alert(f'Correct: {CORRECT} Wrong: {WRONG}', 'The answer is ttk.Button(root, text="Click me :)", command=download_virus) because ttk looks more native')
else:
  msg(f"Correct: {CORRECT} Wrong: {WRONG}", 'The answer is ttk.Button(root, text="Click me :)", command=download_virus) because ttk looks more native')

# Question 10
q10 = ask(
  title="Exit tkinter window",
  text=("What code* will exit a tkinter window"),
  values = [
    ('correct', 'root.quit()'),
    ('correct', 'root.destroy()'),
    ('wrong', 'root.leave()'),
  ]
)

if q10 == "wrong":
  WRONG += 1
  alert(f'Correct: {CORRECT} Wrong: {WRONG}', 'The answer is root.quit()')
else:
  msg(f"Correct: {CORRECT} Wrong: {WRONG}", 'The answer is root.quit()')

msg("Final scores", f"Correct: {CORRECT} Wrong: {WRONG}")