from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

class Test(unittest.TestCase):

    def url_prueba(self):
        link = self.driver.get("https://www.booking.com/index.html")
        return link
        
    #CONFIGURACION DE DRIVER
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_01_login(self):
        ##TEST PROBANDO HISTORIA N°1: Iniciar Sesion
        self.driver.get("https://account.booking.com/sign-in")
        self.connect = self.driver.find_element(By.NAME, 'username')
        self.connect.click()
        self.connect.send_keys("20211809@itla.edu.do")

        screenshot = r"C:\\Users\\usuario\\OneDrive - Instituto Tecnológico de Las Américas (ITLA)\\5to cuatrimestre\\Programación III\\tarea4\\Capturas"
        img = "historia_usuario1.png"
        together = screenshot + "/" + img
        self.driver.save_screenshot(together)

        self.send = self.driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/div[2]/div[1]/div/div/div/div/div/div/form/div[3]/button")
        self.send.submit()
        time.sleep(3)

        img2 = "historia_usuario1_2.png"
        together2 = screenshot + "/" + img2
        self.driver.save_screenshot(together2)

        self.password = self.driver.find_element(By.NAME, 'password')
        self.password.click()
        self.password.send_keys("Programacion3")

        img3 = "historia_usuario1_3.png"
        together3 = screenshot + "/" + img3
        self.driver.save_screenshot(together3)

        self.contra = self.driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/div[2]/div[1]/div/div/div/div/div/div/form/div[2]/button")
        self.contra.submit()

        img4 = "historia_usuario1_4.png"
        together4 = screenshot + "/" + img4
        self.driver.save_screenshot(together4)
        time.sleep(5)


    def test_02_lugar(self):
        self.url_prueba()
        self.test_01_login()
        #TEST PROBANDO HISTORIA N°2: Agregar Destino
        self.detele = self.driver.find_element(By.XPATH, "//*[@id='indexsearch']/div[2]/div/div/form/div[1]/div[1]/div/div/div[1]/div/div/div[3]/span")
        self.detele.click()

        screenshot = r"C:\\Users\\usuario\\OneDrive - Instituto Tecnológico de Las Américas (ITLA)\\5to cuatrimestre\\Programación III\\tarea4\\Capturas"
        img5 = "historia_usuario2.png"
        together5 = screenshot + "/" + img5
        self.driver.save_screenshot(together5)

        self.lugar = self.driver.find_element(By.NAME, 'ss')
        self.lugar.click()
        self.lugar.send_keys("Juan Dolio")
        time.sleep(2)

        img6 = "historia_usuario2_1.png"
        together6 = screenshot + "/" + img6
        self.driver.save_screenshot(together6)

        #TEST PROBANDO HISTORIA N°6: Funcion boton Buscar
        self.buscar = self.driver.find_element(By.XPATH, "//button[@class='fc63351294 a822bdf511 d4b6b7a9e7 cfb238afa1 c938084447 f4605622ad aa11d0d5cd' and @type='submit']")
        self.buscar.submit()
        time.sleep(3)
        

    def test_03_fecha(self):
        #TEST PROBANDO HISTORIA N°3: Seleccionar fechas
        self.test_02_lugar()
        visibilidad = WebDriverWait(self.driver, 15)
        visibilidad.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='calendar-searchboxdatepicker']/div/div[1]/div[1]/table/tbody/tr[4]/td[5]/span")))

        self.check_in = self.driver.find_element(By.XPATH, "//*[@id='calendar-searchboxdatepicker']/div/div[1]/div[1]/table/tbody/tr[4]/td[5]/span")
        self.check_in.click()

        screenshot = r"C:\\Users\\usuario\\OneDrive - Instituto Tecnológico de Las Américas (ITLA)\\5to cuatrimestre\\Programación III\\tarea4\\Capturas"
        img7 = "historia_usuario3.png"
        together7 = screenshot + "/" + img7
        self.driver.save_screenshot(together7)

        self.b_co = self.driver.find_element(By.XPATH, "//*[@id='left_col_wrapper']/div[1]/div/form/div/div[3]/div[4]/button").click()
        self.check_out = self.driver.find_element(By.XPATH,"//*[@id='calendar-searchboxdatepicker']/div/div[1]/div[1]/table/tbody/tr[5]/td[1]/span")
        self.check_out.click()

        img8 = "historia_usuario3_1.png"
        together8 = screenshot + "/" + img8
        self.driver.save_screenshot(together8)
        time.sleep(2)
   

    def test_04_personas(self):
        #TEST PROBANDO HISTORIA N°4: Agregar personas
        self.test_03_fecha()
        self.addperson = self.driver.find_element(By.XPATH, "//*[@id='left_col_wrapper']/div[1]/div/form/div/div[4]/div/button").click()
        self.addadult = self.driver.find_element(By.XPATH, "//*[@id='left_col_wrapper']/div[1]/div/form/div/div[4]/div/div/div/div/div[1]/div[2]/button[2]").click()
        
        screenshot = r"C:\\Users\\usuario\\OneDrive - Instituto Tecnológico de Las Américas (ITLA)\\5to cuatrimestre\\Programación III\\tarea4\\Capturas"
        img9 = "historia_usuario4.png"
        together9 = screenshot + "/" + img9
        self.driver.save_screenshot(together9)
        time.sleep(3)

    def test_05_habitacion(self):
        #TEST PROBANDO HISTORIA N°5: Agregar habitacion
        self.test_04_personas()
        self.addrooms = self.driver.find_element(By.XPATH, "//*[@id='left_col_wrapper']/div[1]/div/form/div/div[4]/div/div/div/div/div[3]/div[2]/button[2]")
        self.addrooms.click()
        
        screenshot = r"C:\\Users\\usuario\\OneDrive - Instituto Tecnológico de Las Américas (ITLA)\\5to cuatrimestre\\Programación III\\tarea4\\Capturas"
        img10 = "historia_usuario5.png"
        together10 = screenshot + "/" + img10
        self.driver.save_screenshot(together10)
        time.sleep(5)
    
    def test_06_filtro(self):
        #TEST PROBANDO HISTORIA N°7: Probando Filtro
        self.test_05_habitacion()
        self.filtro = self.driver.find_element(By.ID, ':Ra7ksq:').click()
        screenshot = r"C:\\Users\\usuario\\OneDrive - Instituto Tecnológico de Las Américas (ITLA)\\5to cuatrimestre\\Programación III\\tarea4\\Capturas"
        img11 = "historia_usuario6.png"
        together11 = screenshot + "/" + img11
        self.driver.save_screenshot(together11)
        time.sleep(5)

    #PARA CERRAR EL DRIVER
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()