import pyautogui
script = "- Avant de partir sale espion, fais-moi l’amour ! - Non je ne crois pas non… - Pourquoi ? - Pas envie…"
for x in script.split():
    pyautogui.write(x, interval=0.25)
    pyautogui.press("enter")
