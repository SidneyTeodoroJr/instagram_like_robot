import time
import pyautogui as pg
import webbrowser as web
from pynput import keyboard
import tkinter as tk
from tkinter import messagebox

from modules.image_search import ImageLocator

running = True  # Variável que controla a execução do script

def main_bot():
    def on_press(key):
        global running
        if key == keyboard.Key.esc:
            print("Tecla ESC pressionada!")
            print("Bot interrompido.")
            running = False
            return False  # Retorna False para parar de ouvir eventos de teclado

    def bot_run():
        root = tk.Tk()
        root.withdraw()  # Oculta a janela principal

        messagebox.showinfo("Aviso", "Para interromper a automação, aperte 'ESC' no teclado.")

        url = "https://www.instagram.com/"
        web.open(url)

        pg.sleep(10)
        home_position = pg.locateCenterOnScreen("app\img\seta.png", confidence=0.7)
        if home_position:
            pg.moveTo(home_position, duration=1)
            pg.click()
        pg.sleep(1.5)
        pg.hotkey("f11")

        def bot_click_like():
            imagens = ["app\img\msg_alerta1.png", "app\img\msg_alerta2.png", "app\img\like_1.png", "app\img\like_2.png"]

            time.sleep(0.5)
            for img_path in imagens:
                if img_path == "app\img\notificacao_1.png":
                    continue

                if img_path == "app\img\notificacao_2.png":
                    continue

                if img_path == "app\img\like_red_1.png":
                    continue

                if img_path == "app\img\like_red_2.png":
                    continue

                # Se a imagem não deve ser evitada, prossiga com a busca
                locator = ImageLocator(img_path)
                locator.start_search()

                time.sleep(0.5)

        def like_loop():
            while running:  # Loop continua enquanto a variável global 'running' for True
                pg.sleep(0.5)
                pg.scroll(-500)
                bot_click_like()
                time.sleep(0.5)

        like_loop()

    # Inicia o listener de teclado para capturar a tecla 'esc'
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    bot_run()

    pg.hotkey("f11")
    messagebox.showinfo("Aviso", "Automação do Instagram, encerrada!")

main_bot()