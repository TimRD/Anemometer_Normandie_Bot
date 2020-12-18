from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import xlrd

from xlwt import Workbook, Formula

def exo1():
    options = Options()
    options.headless = False
    # options.add_argument("--window-size=1920,1200")
    DRIVER_PATH = '/Users/timotheemarguier/Downloads/chromedriver'
    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

    path = r"fichier.xls"

    # On créer un "classeur"
    classeur = Workbook()
    # On ajoute une feuille au classeur
    feuille = classeur.add_sheet("OCB2")
    # Ecrire "1" dans la cellule à la ligne 0 et la colonne 0
    feuille.write(0, 0, "Numéro")
    feuille.write(0, 1, "Titre")


    x=0
    pages = [str(i) for i in range(1,5)] # range is exclusively, that's why we need to add 1 to the final number we want
    for page in pages:
      driver.get('http://books.toscrape.com/catalogue/page-' + page + '.html')
      offers = driver.find_elements_by_css_selector("li.col-xs-6.col-sm-4.col-md-3.col-lg-3")
      for offer in offers:
          x=x+1
          title = offer.find_element_by_css_selector("h3").text
          price = offer.find_element_by_css_selector("p.price_color").text
          print("Titre : ",title)
          print("Prix : ", price)
          print(page)
          print("x :",x)
          feuille.write(x, 0, x)
          feuille.write(x, 1, title)
    classeur.save(path)
    driver.quit()


def exo2():
    options = Options()
    options.headless = False
    # options.add_argument("--window-size=1920,1200")
    DRIVER_PATH = '/Users/timotheemarguier/Downloads/chromedriver'
    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

    path = r"fichier.xls"

    # On créer un "classeur"
    classeur = Workbook()
    # On ajoute une feuille au classeur
    feuille = classeur.add_sheet("OCB2")
    # Ecrire "1" dans la cellule à la ligne 0 et la colonne 0
    feuille.write(0, 0, "Numéro")
    feuille.write(0, 1, "Titre")


    x=0
    pages = [str(i) for i in range(1,5)] # range is exclusively, that's why we need to add 1 to the final number we want
    for page in pages:
      driver.get('http://books.toscrape.com/catalogue/page-' + page + '.html')
      offers = driver.find_elements_by_css_selector("li.col-xs-6.col-sm-4.col-md-3.col-lg-3")
      for offer in offers:
          x=x+1
          title = offer.find_element_by_css_selector("h3").text
          price = offer.find_element_by_css_selector("p.price_color").text
          print("Titre : ",title)
          print("Prix : ", price)
          print(page)
          print("x :",x)
          feuille.write(x, 0, x)
          feuille.write(x, 1, title)
    classeur.save(path)
    driver.quit()
#exo1()

exo2()


