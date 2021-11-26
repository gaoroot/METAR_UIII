import json
import requests
import URL

url = requests.get(URL.UIII)
text = url.text
data = json.loads(text)


# print(data['name'])
# print(data['metar'])


def MetarUIIIName():
    print(data['name'])


def MetarUIIIMetar():
    l = data['metar']

    # print(type(l))
    l2 = (l.split(" ", 11)[5])
    temperature = (l2.split("/", 1)[0])
    dew_point = (l2.split("/", 1)[1])
    # print("Температура", "=", temperature)
    # print("Точка росы", "=", dew_point)

    for letter in temperature[0]:
        if letter == "M":
            temperature = temperature.replace(letter, "-")
            print("Температура", "=", temperature, "℃")
        else:
            print("Температура", "=", temperature, "℃")

    for letter in dew_point[0]:
        if letter == "M":
            dew_point = dew_point.replace(letter, "-")
            # for letter in dew_point[1]:
            #     if letter == "0":
            #         dew_point = dew_point.replace(letter, "")
            print("Точка росы", "=", dew_point, "℃")
        else:
            print("Точка росы", "=", dew_point, "℃")


# def MetarQNH():
#     q = data['metar']
#     q2 = (q.split(" ", 11)[6])
#     # print("Давление", "=", q2)
#     for letter in q2[0]:
#         if letter == "Q":
#             qnh = q2.replace(letter, "")
#             # print("Давление", "=", qnh)
#             mmrt = (float(qnh) / float(1.333))
#             print("Давление", "=", "%.2f" % mmrt)

def MetarUIIIQFE():
    qfe = data['metar']
    qfe2 = (qfe.split(" ", 11)[10])
    pressure_mmrt = (qfe2.split("/", 1)[0])
    for letter in pressure_mmrt:
        if letter == 'Q':
            pressure_mmrt = pressure_mmrt.replace(letter, " ")
    print("Давление", "=", pressure_mmrt, "мм рт.ст.")

    # for letter in pressure_mmrt[0]:
    #     if letter == "QFE":
    #         pressure_mmrt = pressure_mmrt.replace(letter, "")
    #         print("Температура", "=", pressure_mmrt, "℃")
    #     else:
    #         print("Температура", "=", pressure_mmrt, "℃")

    # print(pressure_mmrt)


MetarUIIIName()
MetarUIIIMetar()
MetarUIIIQFE()
