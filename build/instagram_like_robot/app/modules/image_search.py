import pyautogui as pg
import time
import cv2
from pyscreeze import ImageNotFoundException

class ImageLocator:
    def __init__(self, img_path, max_attempts=1, search_interval=1, confidence=0.9):
        self.img_path = img_path
        self.max_attempts = max_attempts
        self.search_interval = search_interval
        self.confidence = confidence
        self.attempts = 0

    def start_search(self):
        while True:
            try:
                # Captura a imagem a ser procurada
                template = cv2.imread(self.img_path)

                # Localiza a imagem na tela
                result = pg.locateAllOnScreen(template, confidence=self.confidence)

                # Se o elemento for encontrado
                position = next(result, None)  # Obtém o próximo resultado ou None se não houver mais
                if position:
                    # Obtém a posição do canto da imagem
                    corner_x = position[0]
                    corner_y = position[1]
                    
                    # Move o cursor para o canto da imagem
                    pg.moveTo(corner_x, corner_y, duration=1)
                    
                    # Clica no canto da imagem
                    pg.leftClick()
                    print("Elemento localizado!")
                    print(f"Posição: {position}")
                    break
            
            except ImageNotFoundException as e:
                # A imagem não foi encontrada
                print(f"Erro: {e}")
                print("Buscando..")

            # Após 'n' tentativas, o programa encerra    
            if self.attempts >= self.max_attempts:
                print(f"Elemento não encontrado após {self.max_attempts + 1} tentativas de busca!")
                break

            time.sleep(self.search_interval)
            self.attempts += 1