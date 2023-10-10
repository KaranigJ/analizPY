import customtkinter
import Data

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("1560x1080")
app.title("CustomTkinter simple_example.py")

textsBlood = ["СОЭ", "Эретроциты", "Гемоглобин", "Гематокрит", "MCV", "MCH", "MCHC", "RDW", "Тромбоциты", "MPV",
              "PCT", "PDW", "WBC", "Моноциты", "Эозинофилы", "Базофилы", "Лимфоциты", "Нейтрофилы"]
textsHim = ["Креатинин", "Мочевина", "Общий белок", "Щелочная фосфатаза", "СБР", "Гомоцистеин", "Антистрептолизин-О"]
textsPiss = ["ОПМ", "pH мочи", "Белокэпителий", "Глюкоза", "билирубин", "эр-ты, гем-ин и миогем-ин",
             "эпителий", "слизь", "Цилиндры ", "нитриты, грибы и бактерии", "лейкоциты", "КРИСТАЛЫ",
             "Прочие компоненты"]

blood = []
him = []
piss = []
resoults = {}


tabview_1 = customtkinter.CTkTabview(master=app)
tabview_1.pack(pady=0, padx=0)
tabview_1.add("Анализы")
tabview_1.add("Результат")
tab_1 = tabview_1.tab("Анализы")
tab_2 = tabview_1.tab("Результат")


bloodFrame = customtkinter.CTkFrame(master=tab_1)
bloodName = customtkinter.CTkLabel(master=bloodFrame, text='Клинический анализ крови', font=("arial", 18))

himFrame = customtkinter.CTkFrame(master=tab_1)
himName = customtkinter.CTkLabel(master=himFrame, text='Биохимический анализ крови', font=("arial", 18))

pissFrame = customtkinter.CTkFrame(master=tab_1)
pissName = customtkinter.CTkLabel(master=pissFrame, text='Анализ мочи', font=("arial", 18))

bloodFrame.grid(row=0, column=0, padx=50, pady=0, sticky="nsew")
bloodName.grid(row=0, column=0, padx=50, pady=0)

himFrame.grid(row=0, column=1, padx=50, pady=0, sticky="nsew")
himName.grid(row=0, column=4, padx=50, pady=0)

pissFrame.grid(row=0, column=2, padx=50, pady=0, sticky="nsew")
pissName.grid(row=0, column=6, padx=50, pady=0)

for i in range(0, len(textsBlood)):
    label = customtkinter.CTkLabel(master=bloodFrame, text=textsBlood[i])
    label.grid(row=i+1, column=0, padx=5, pady=10)
    entery = customtkinter.CTkEntry(master=bloodFrame, placeholder_text='рузультат')
    entery.grid(row=i+1, column=1, padx=0, pady=10)
    blood.append([label, entery])

for i in range(0, len(textsHim)):
    label = customtkinter.CTkLabel(master=himFrame, text=textsHim[i])
    label.grid(row=i+1, column=4, padx=5, pady=10)
    entery = customtkinter.CTkEntry(master=himFrame, placeholder_text='рузультат')
    entery.grid(row=i+1, column=5, padx=0, pady=10)
    him.append([label, entery])

for i in range(0, len(textsPiss)):
    label = customtkinter.CTkLabel(master=pissFrame, text=textsPiss[i])
    label.grid(row=i+1, column=6, padx=5, pady=10)
    entery = customtkinter.CTkEntry(master=pissFrame, placeholder_text='рузультат')
    entery.grid(row=i+1, column=7, padx=0, pady=10)
    piss.append([label, entery])


def button_event():
    write(blood)
    write(him)
    write(piss)

    print(resoults)


def write(mass):
    for j in range(0, len(mass)):
        value = mass[j][1].get()
        name = mass[j][0].cget('text')
        if len(value) == 0:
            value = '0'
        r = {name: int(value)}
        resoults.update(r)


button = customtkinter.CTkButton(master=tab_1, text="Отправить", command=button_event)
button.grid(row=19, column=1, pady=10, padx=10)


#-----------------------------------------------------------------------------------------------------------------------

for i in range(0, len(Data.inc)):
    button = customtkinter.CTkButton(master=tab_2, text=Data.inc[i][0])
    button.grid(row=i, column=1, pady=10, padx=10)






app.mainloop()