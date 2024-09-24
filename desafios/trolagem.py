import pyautogui as py
import random
import time

time.sleep(5)

mensagens = ["Postgres", "FastApi", "sql", "Api",
             "Python", "JavaScript", "Nuxt.js",
             "React.js", "Next.js", "Vue.js",
             "Vscode", "git", "GitHub", "GitLab",
             "Docker", "Docker Composer", "Linux",
             "Windowns"]

for i in range(50):
    msg = random.choice(mensagens)
    py.write(msg)
    py.press("enter")