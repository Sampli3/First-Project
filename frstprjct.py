#В этой программе пользователь сможет подсчитать сколько ему предстоит заплатить за коммунальные услуги.
#Поздороваемся с пользователем и узнаем стоимость постоянных платежей, которые он должен совершать.
import math
print('Добрый день, эта программа поможет рассчитать стоимость',
      'ваших коммунальных услуг.')
name = input('Как я могу к вам обращаться?')
const_price = float(input('Напишите, пожалуйста, стоимость ежемесячных сборов на капитальный ремонт и содержание дома. '
                          'Эти услуги являются постояннымии и их стоимость одинакова каждый месяц.'))
#Введем переменные, которые будут ссылаться на стоимость единиц потребляемых пользоветелем ресурсов.
price_kw = 2.68
price_cm = 32.8
#Узнаем сколько человек проживает в помещении, чтобы рассчитать индивидуальне траты.
people = int(input('Сколько человек проживает в помещении?'))
#Посчитаем траты на воду.
shower = float(input('Сколько, примерно, каждый человек тратит времени(в минутах) на пребывание в душе?'))
shower_cm = shower*0.012                            #Сколько тратит 1 человек воды в кубических метрах за прием душа.
shower_monthtime = people*shower_cm*30*price_cm     #Траты воды на душ за месяц для всех жильцов.
#Посчитаем траты на остальную воду в сильно усредненном значении.
another_waterfor1 = 5*0.012*4*30                    #Остальная вода помимо душа на человека в кубических метрах(месяц).
another_waterforall = people*another_waterfor1      #Остальная вода за месяц для всех жильцов в кубометрах.
all_water = shower_monthtime+another_waterforall    #Общие траты за воду в месяц.
#Электричество в усреднемнном значении на бытовые приборы.
computer = float(input('Сколько часов в день вы пользуетесь компьютером? Если его нет - поставьте значение 0.'))
computer_price = 220*0.001*computer*30*price_kw
fridge = 1*30*price_kw
electric_range = 1.5*2*2*15*price_kw
kettle = 2100*0.001*0.3*30*price_kw
tv_hour = int(input('Сколько времени в сутки у вас работает телевизор(укажите примерное значение в часах)?'))
tv = 50*0.001*tv_hour*30
#Электричество на освещение.
lamp = int(input('Сколько лампочек у вас в доме?'))
lamp_w = float(input('Какой мощности(усредненное значение) эти лампочки?(укажите в в/ч)'))
lamp_hour = lamp*lamp_w*0.001                       #Потребление одной лампочкой электроэнергии в Кв/ч.
lamp_all = lamp_hour*6*30*price_kw                  #Стоимость электроэнергии на все освещение за месяц.
#Общие траты за электричество.
electric_all = fridge+electric_range+kettle+lamp_all+tv+computer_price
#Посчитаем общие траты за все коммунальные услиги.
all = electric_all+all_water+const_price
print('Уважаемый', name, ',', 'примерная стоимость ваших коммунальных услуг за месяц составит:', '{:.2f}'.format(all), 'рублей.')
