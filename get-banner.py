import os
import random as rand

try:
    import pexpect as pp
except ModuleNotFoundError:
    os.system('pip install pexpect')
    import pexpect as pp

try:
    pp.spawn('figlet testing')
except pp.exceptions.ExceptionPexpect:
    os.system('pkg install figlet')
    try:
        pp.spawn('figlet testing')
    except pp.exceptions.ExceptionPexpect:
        exit()
try:
    pp.spawn('toilet testing')
except pp.exceptions.ExceptionPexpect:
    os.system('pkg install toilet')
    try:
        pp.spawn('toilet testing')
    except pp.exceptions.ExceptionPexpect:
        exit()

FpD = ''
FpPtf = '0'
TpPtf = '0'
os.system('clear')
os.system(rand.choice(('toilet -F ' + rand.choice(('gay ', 'metal ')
                                                  ) + 'Easy Banner', 'figlet Easy Banner')))
input('Приветствую! Я помогу создать тебе хороший банер! Нажми Enter...')

while 1:
    txt = input("Введите любой текст ('-skip' - пропуск): ")
    if txt != "" and txt != " ":
        break
    elif txt == '-skip':
        txt = ''

while 1:
    os.system("clear")
    use = input("""t - toilet
f - figlet
Выберите утилиту: """)
    use = use.lower()

    if use == "t" or use == "1":
        use = "toilet "
        break
    elif use == "f" or use == "2":
        use = "figlet "
        break

while 1:
    mores = input("""
2 - Посмотреть справку по """ + use.replace(' ', '') +
                  """
1 - С доп. опциями
0 - без доп. опций
""")
    if mores == "0" or mores == "00":
        os.system('clear')
        try:
            print('Команда:' + use + txt)
            os.system(use + txt)
            exit()
        except Exception as e:
            print(e)
            break
    elif mores == "1" or mores == "01":
        break
    elif mores == "2" or mores == "01":
        try:
            pp.spawn('man')
        except pp.exceptions.ExceptionPexpect:
            os.system('pkg install man')
        os.system('man ' + use.replace(' ', ''))


def FpPm(use, FpC, FpW, FpK, FpD, FpF, FpP):
    f = open(FpP, 'r')
    print('Команда: ' + use + FpC + FpW + FpK + FpD + FpF + '-p < ' + FpP)
    for line in f:
        line = line.replace('(', '[').replace(')', ']')
        # ^ чтобы не возникло ошибки:
        # syntax error near unexpected token `(' | `)'
        try:
            os.system(use + FpC + FpW + FpK + FpD + FpF + line)
        except Exception as e:
            print(str(e))
    f.close()


def TpPm(use, Tprm, TpW, TpD, Tpf, TpF, TpP):
    f = open(TpP, 'r')
    print('Команда: ' + use + Tprm + TpW + TpD + Tpf + TpF + '-p < ' + TpP)
    for line in f:
        line = line.replace('(', '[').replace(')', ']')
        # ^ чтобы не возникло ошибки:
        # syntax error near unexpected token `(' | `)'
        try:
            os.system(use + Tprm + TpW + TpD + Tpf + TpF + line)
        except Exception as e:
            print(str(e))
    f.close()


if use == "figlet ":
    FpC = input(
        "c - По центру. l - По левому краю. r - по правому краю. x - стандартный.")
    FpC = FpC.lower()
    if FpC == "c" or FpC == "center":
        FpC = "-c "
    elif FpC == "l" or FpC == "left":
        FpC = "-l "
    elif FpC == "r" or FpC == "right":
        FpC = "-r "
    elif FpC == "x" or FpC == "default":
        FpC = "-x "
    else:
        FpC = ""
        print('Пропуск.')

    FpW = input(
        "Указывать ли ширину? (Enter для пропуска или введите цифру). t - растянуть на весь терминал: ")
    FpW = FpW.lower()
    if FpW == "" or FpW == " ":
        FpW = ""
        print("Пропуск.")
    elif FpW == 't' or FpW == 'terminal':
        FpW = '-t '
    else:
        try:
            int(FpW)
            FpW = "-w " + FpW + " "
        except ValueError:
            FpW = "-w 80 "
    FpK = input("Ставить пробелы между символами? (y/n) ")
    FpK = FpK.lower()
    if FpK == "y" or FpK == "yes":
        FpK = "-k "
    else:
        FpK = ''
        print('Пропуск.')
    FpP = input(
        "Считать ли текст с файла? (Enter пропустить или введите имя файла): ")
    if FpP == "" or FpP == " ":
        FpP = ""
        print("Пропуск.")
    else:
        try:
            f = open(FpP, 'r')
            ftxt = f.read()
            f.close()
            FpPtf = '1'
        except Exception as e:
            print(str(e))
            FpPtf = '0'
            print("Пропуск.")
    while 1:
        FpF = input(
            "Выберите шрифт (? - узнать, какие есть шрифты), d - чтобы выбрать папку со шрифтами: ")
        FpF = FpF.lower()
        if FpF == "?":
            print("Все шрифты Figlet находятся здесь\ncd $HOME/../usr/share/figlet\nФайлы .flf или .tlf, вводите только название")
        elif FpF == 'd' or FpF == 'dir':
            FpD = input('Введите имя папки: ')
            if FpD != '' and FpD != ' ':
                FpD = '-d ' + FpD
            else:
                FpD = ''
        elif FpF == '' or FpF == ' ':
            print("Пропуск.")
            break
        else:
            print("Выбран шрифт " + FpF)
            FpF = '-f ' + FpF + ' '
            break
    if FpPtf == '1':
        FpPm(use, FpC, FpW, FpK, FpD, FpF, FpP)
    else:
        try:
            print('Команда: ' + use + FpC + FpW + FpK + FpD + FpF + txt)
            os.system(use + FpC + FpW + FpK + FpD + FpF + txt)
        except Exception as e:
            print(str(e))


elif use == 'toilet ':

    TpP = input(
        "Считать ли текст с файла? (Enter пропустить или введите имя файла): ")
    if TpP == "" or TpP == " ":
        TpP = ""
        print("Пропуск.")
    else:
        try:
            f = open(TpP, 'r')
            ftxt = f.read()
            f.close()
            TpPtf = '1'
        except Exception as e:
            print(str(e))
            TpPtf = '0'
            print("Пропуск.")

    Tprm = input(
        "режим рендеринга (s - по умолчанию, S - принудительное сжатие, k - кернинг, W - полная ширина, o - перекрытие): ")
    if Tprm == 'S' or Tprm.lower() == 'force smushing' or Tprm == '2':
        Tprm = '-S '
    elif Tprm == 'W' or Tprm.lower() == 'full width' or Tprm == '4':
        Tprm = '-W'
    else:
        Tprm = Tprm.lower()
        if Tprm == 's' or Tprm == 'default' or Tprm == '1':
            Tprm = '-s '
        elif Tprm == 'k' or Tprm == 'kerning' or Tprm == '3':
            Tprm = '-k '
        elif Tprm == 'o' or Tprm == 'overlap' or Tprm == '5':
            Tprm = '-o '
        else:
            print('Пропуск.')
            Tprm = ''

    TpW = input(
        "Указывать ли ширину? (Enter для пропуска или введите цифру...) t - растянуть на весь терминал: ")
    TpW = TpW.lower()
    if TpW == "" or TpW == " ":
        TpW = ""
        print("Пропуск.")
    elif TpW == 't' or TpW == 'terminal':
        TpW = '-t '
    else:
        try:
            int(TpW)
            TpW = "-w " + TpW + " "
        except ValueError:
            TpW = "-w 80 "

    TpD = input('Папка со шрифтами: ')
    if TpD == '' or TpD == ' ':
        print('Пропуск.')
    else:
        TpD = '-d ' + TpD
    Tpf = input('Введите название шрифта (? - узнать, какие есть шрифты): ')
    if Tpf == "?":
        print("Все шрифты Toilet находятся здесь\ncd $HOME/../usr/share/figlet\nФайлы .flf или .tlf, вводите только название")
    else:
        if Tpf != '' and Tpf != ' ':
            print("Выбран шрифт " + Tpf)
            Tpf = '-f ' + Tpf + ' '
        else:
            Tpf = ''
            print('Пропуск.')

    TpF = input('Введите фильтр (1/m - Металический. 2/g - радужный): ')
    TpF = TpF.lower()

    if TpF == '1' or TpF == 'm' or TpF == 'metal':
        TpF = '-F metal '

    elif TpF == '2' or TpF == 'g' or TpF == 'gay':
        TpF = '-F gay '
    TpE = input('Экспортировать в формат (html/irc): ')
    TpE = TpE.lower()
    if TpE == 'html' or TpE == '1':
        TpE = '-E html '
    elif TpE == 'irc' or TpE == '2':
        TpE == '-E irc '

    if TpPtf == '1':
        FpPm(use, Tprm, TpW, TpD, Tpf, TpF, TpP)
    else:
        try:
            print('Команда: ' + use + Tprm + TpW + TpD + Tpf + TpF + txt)
            os.system(use + Tprm + TpW + TpD + Tpf + TpF + txt)
        except Exception as e:
            print(str(e))

#Автор: NIKDISSV
