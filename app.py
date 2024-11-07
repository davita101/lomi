import pyautogui as pa
import pyperclip
import keyboard
import time


from wines import *
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def first_step(product_id): # პროდუქტის ძიება
    # საიტის შეასვლელი
    def click_8000_web():
        x = 3152
        y = 221
        pa.moveTo(3152,221)
    # click_8000_web() 

 
    # პროდუქტის ძიება
    def search_product(product_id):
        x, y = 3323, 182

        pa.moveTo(x,y)
        pa.click()

        # დაკლიკდა სერჩზე
        pa.typewrite(product_id)
        pa.keyDown("enter")


    search_product(product_id)
    # ---------------------------------------------

    # ---------------------------------------------
# first_step(product_id)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# screen 

# აუცლიებლად უნდა იყოს ქართულზე გადართული ენა და 100% უნდა იდგდეს

# KEYBOARDS
def paste_using_keyboard():
   keyboard.press_and_release('ctrl+v')
def select_all_using_keyboard():
   keyboard.press_and_release('ctrl+a')
def enter_using_keyboard():
   keyboard.press_and_release('enter')
def arrow_down_using_keyboard():
   keyboard.press_and_release('down')

# კოდი დაწერილი არის 
# 1920 * 2 ღერძ ეკრანზე და 1080 y ღერძ ეკრანზე  
# ამიტომ ჩვენი კოდით ჯერ ერთ  ეკრანზე ჩამოვიყვანთ ეკრანს მერე ვამუშავებთ
program_screen_x , program_screen_y = 0 ,0


# 
def second_step(text_1, text_2 ,text_3): # ზოგადის შევსება
    def handle_general():
        name_x , name_y = 2538  - program_screen_x, 519 - program_screen_y

        pa.moveTo(name_x, name_y)
        pa.click()

        pyperclip.copy(text_3)
        select_all_using_keyboard()
        paste_using_keyboard()


    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # ვერ ვავსებთ კატეგორეიებს
# -----------------------------------------------
    def picture_search ():
        

        x , y = 2501  - program_screen_x, 718 - program_screen_y
        pa.moveTo(2700,0)

        pa.scroll(-500)
        pa.click()


        pyperclip.copy(text_3)

        pa.moveTo(x,y)
        pa.scroll(-500)
        time.sleep(.5)

        pa.click()
        
        time.sleep(.3)
        paste_using_keyboard()

        pyperclip.copy(text_1)
        # SEARCH -----
        pa.scroll(-3000)
        pa.scroll(-3000)

        
        pa.click()
        pyperclip.copy(text_2)
        paste_using_keyboard()

        pa.scroll(10000)
        new_x , new_y = 2417 - program_screen_x, 365 - program_screen_y
        pa.moveTo(new_x, new_y)
        pa.click()


    handle_general()
    picture_search()
    pyperclip.copy(text_1)

# -----------------------------------------------
def third_step(): # მიწოდების შევსება
    x, y = 2487  - program_screen_x ,521
    pa.moveTo(x,y)
    pa.click()
    select_all_using_keyboard()
    pa.typewrite("1.50")

    new_x, new_y = 2775  - program_screen_x , 367 - program_screen_y
    pa.moveTo(new_x , new_y)
    pa.click()
# -----------------------------------------------
def forth_step(): # meta 
    
    meta_x, meta_y = 2519  - program_screen_x , 620 - program_screen_y
    pa.moveTo(meta_x , meta_y)
    pa.click()
    paste_using_keyboard()

    meta_y+=50
    pa.moveTo(meta_x , meta_y)
    pa.click()
    paste_using_keyboard()

    meta_y+=90
    pa.moveTo(meta_x , meta_y)
    pa.click()
    paste_using_keyboard()
   
def eng_forth_step(text_1): # meta eng
    start_x, start_y = 2769  - program_screen_x, 365 - program_screen_y

    pa.moveTo(start_x , start_y)
    pa.click()

    seo_x , seo_y = 2593  - program_screen_x , 523 - program_screen_y
    time.sleep(.5)

    pa.moveTo()

    pa.moveTo(seo_x , seo_y)
    pa.click()

    select_all_using_keyboard()
    paste_using_keyboard()


    pyperclip.copy(text_1)

    url_x , url_y = 2466  - program_screen_x, 545 - program_screen_y
    pa.moveTo(url_x , url_y)
    pa.click()

    pyperclip.copy(text_1)
    
    x, y = 2763  - program_screen_x,359 - program_screen_y
    pa.moveTo(x, y)
    pa.click()

    meta_x , meta_y = 2521  - program_screen_x, 650 - program_screen_y
    pa.moveTo(meta_x , meta_y)
    pa.click()
    paste_using_keyboard()

    meta_y+=50
    pa.moveTo(meta_x, meta_y )
    pa.click()
    paste_using_keyboard()

    meta_y+=90
    pa.moveTo(meta_x  , meta_y )
    pa.click()
    paste_using_keyboard()

def categories(icon,alc,color,tech,orgn,plc,reg,yr):

    def icons():
        arr = ["ქვევრი", "კასრი", "ბიო"]
        if icon in arr:
            x_1 = 2661 - program_screen_x
            y_1 =  367 - program_screen_y

            pa.moveTo(x_1 , y_1)
            pa.click()

            x, y = 2469  - program_screen_x, 649 - program_screen_y
            pa.moveTo(x, y)
            pa.click()
            time.sleep(.5)
            pyperclip.copy(icon)
            time.sleep(.5)
            paste_using_keyboard()
            enter_using_keyboard()

    def volume():
        x_1  , x_2  , x_3  = 2661  - program_screen_x ,  2513  - program_screen_x ,  2520  - program_screen_x
        y_1 ,  y_2 , y_3 = 367 - program_screen_y, 713 - program_screen_y, 483  - program_screen_y

        pa.moveTo(x_1 , y_1)
        pa.click()

        pa.moveTo(x_2 , y_2)
        pa.click()

        time.sleep(.5)
        pa.moveTo(x_3 , y_3)
        pa.click()

    def alcohol():
        x_1 , y_1  = 2500  - program_screen_x,804 - program_screen_y
        pa.moveTo( x_1 , y_1)
        pa.click()
        time.sleep(.5)

        x_2 , y_2 = 2535  - program_screen_x, 764 - program_screen_y
        pa.moveTo(x_2 , y_2)
        pa.typewrite(alc)
        time.sleep(.5)
        pa.click()

    def wine_color(): 
        arr_color_2_to_down = ["ქარვისფერი","ჩალისფერი"]
        arr_color_1_to_down = ["ლალისფერი"]
        x , y = 2479  - program_screen_x, 880 - program_screen_y
        pa.moveTo(x, y)
#           თუ ერაში არის რომელიმე
        pa.click()
        pyperclip.copy(color)
        paste_using_keyboard()
        time.sleep(.5)

        if color in arr_color_2_to_down:
            for i in range(2):
                arrow_down_using_keyboard()
        elif color in arr_color_1_to_down:
            arrow_down_using_keyboard()
        
        enter_using_keyboard()
        pa.scroll(-300)
        pa.click()

    def technology():
        pa.click()

        pyperclip.copy(tech)
        paste_using_keyboard()
        time.sleep(.5)
        enter_using_keyboard()

        pa.scroll(-100)

    def origin():
        pa.click()

        pyperclip.copy(orgn)
        paste_using_keyboard()
        time.sleep(.5)
        enter_using_keyboard()

        pa.scroll(-200)

    def place():
        if plc != "":
            pa.click()

            pyperclip.copy(plc)
            paste_using_keyboard()
            time.sleep(.5)
            enter_using_keyboard()

            pa.scroll(-90)
        else:
            pa.scroll(-90)
            
    def region():
        pa.click()

        pyperclip.copy(reg)
        paste_using_keyboard()
        time.sleep(.5)
        enter_using_keyboard()

        pa.scroll(-90)

    def year():
        pa.click()

        pyperclip.copy(yr)
        paste_using_keyboard()
        time.sleep(.5)
        enter_using_keyboard()
    
    icons()
    volume()
    alcohol()
    wine_color()
    technology()
    origin()
    place()
    region()
    year()

#  👉👉👉!ACTIONS👈👈👈

def first_action(i):
    name_alt =bro()[i]["ღვინო •"]
    name = input("Enter wine name: .")
    search = bro()[i]["search"]

    icons = bro()[i]["ტექნოლოგია"]
    tech = bro()[i]["ტექნოლოგია"]
    year = input("შეიყვანე წელი: .")
    alcohol = str(bro()[i]["ალკოჰოლი %"])
    color = bro()[i]["ფერი"]
    place = bro()[i]["ადგილი"]
    origin = bro()[i]["ჯიში"]
    region = bro()[i]["რეგიონი"]
    if tech == "კასრი":
        tech = "კლასიკური/მუხის კასრი"
    if icons == "კასრი":
        icons = "მუხის კასრი"
    second_step(name_alt,search, name) # ზოგადი
    third_step() # მიწოდების ტიპი
    forth_step() # meta
    categories(icons, alcohol, color, tech, origin , place, region, year) # მახასიათებლები
    
    pa.scroll(1000)
    pa.moveTo(2319 - program_screen_x , 360 - program_screen_y)
    pa.click()
    if  bro()[i]["გაუფილტრავია?"] == "კი":
        print("-------------------------")
        print("გაუპილტრავია ღვინოო!!!")
        print("-------------------------")


def second_action(i):
    name_alt = bro()[i]["Eng"]
    name = input("Enter wine name: .")

    search = bro()[i]["search"]

    second_step(name_alt,search, name) # ზოგადი
    
    eng_forth_step(name_alt) # ენ

    pa.scroll(9000)
    
    
    pa.moveTo(2319 - program_screen_x , 360 - program_screen_y)
    pa.click()


def position(): 
    while True:
        x,y = pa.position()
        print(x,y)
# position()
print(bro()[9]["კოდი"])
first_action(9)
# second_action(9)
