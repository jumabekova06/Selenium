from selenium  import webdriver
import time 

Path='полный путь до драйвера /FirstProject/driver/chromedriver'#правильно укажите свой путь до браузера

driver=webdriver.Chrome(executable_path=Path)#инициализация chrome

driver.get('https://www.instagram.com/')# открывает инстаграмм
driver.maximize_window()#делает окно браузера на весь экран
time.sleep(2)# для того чтобы страница полностью загрузилась
username=driver.find_element_by_name("username")#находит элемент по атрибуту : name
username.send_keys('username') #вставить свой логин
password=driver.find_element_by_name('password')
password.send_keys('password')# вставить свой пароль 
time.sleep(4)

button=driver.find_element_by_xpath('//button[@type="submit"]')
button.click() #нажимет на найденный элемент
time.sleep(5)
moment=driver.find_element_by_class_name('sqdOP.yWX7d.y3zKF')
moment.click()
time.sleep(4)
dontnow=driver.find_element_by_class_name("aOOlW.HoLwm")
dontnow.click()
time.sleep(2)
driver.close()#всего лишь закрывает текушее окно.

# driver.quit() она закрывает хром полностью