import pyautogui
import time
import pandas

pyautogui.PAUSE = 1

pyautogui.press("win")

pyautogui.write("chrome")

pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(5)

pyautogui.click(x=680, y=409)
pyautogui.write("email@gmail.com")


pyautogui.press("tab")
pyautogui.write("1234")

pyautogui.press("enter")
time.sleep(3)

tabel = pandas.read_csv("produtos.csv")
print(tabel)

for line in tabel.index:
    pyautogui.click(x=776, y=293)
    
    pyautogui.write(tabel.loc[line, "codigo"])
    pyautogui.press("tab")

    pyautogui.write(tabel.loc[line, "marca"])
    pyautogui.press("tab")

    pyautogui.write(tabel.loc[line, "tipo"])
    pyautogui.press("tab")

    pyautogui.write(str(tabel.loc[line, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabel.loc[line, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabel.loc[line, "custo"]))
    pyautogui.press("tab")
    obs = tabel.loc[line, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    
    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(5000)