countris = {
    'Thailand' : {'sea' : True,
                  'shengen' : False,
                  'average_temp' : 10,
                  'currency_rate' : 1.8,
                  'price_day_in_USD': 25,
                  'currency': 'BAT'},
    'Hungary' : {'sea' : False,
                  'shengen' : True,
                  'average_temp' : 10,
                  'currency_rate' : 0.8,
                  'price_day_in_USD': 70,
                  'currency': 'XE'},
    'Germany': {'sea': True,
                  'shengen': True,
                  'average_temp': 18,
                  'currency_rate': 8.1,
                  'price_day_in_USD': 40,
                  'currency': 'EURO'},
    'Ukraine': {'sea' : False,
                 'shengen': False,
                 'average_temp': 13,
                 'currency_rate': 2,
                 'price_day_in_USD': 70,
                 'currency': 'UAH'},

}
#
# shengen_country = set()
# sea_country = set()

money_amount = 2000
amount_country = set()
for country, properties in countris.items():
    limit_money = 30 * properties['price_day_in_USD']
    if (properties['average_temp'] >= 15 & properties['sea'] == True) or \
            (properties['shengen'] == True & money_amount > limit_money):
        amount_country.add(country)

print(amount_country)




# money_amount = 2000
# for country, country_money, in countris.items():
#         limit_money = 30 * country_money['price_day_in_USD']
#         print('Для перебування в країні: ', country, ' Потрібно:  ', limit_money)



# for country_name, properties in countris.items():
#     if properties['shengen']:
#         shengen_country.add(country_name)
#     if properties['sea']:
#         sea_country.add(country_name)
#
#
# print('Країна з морем: ', sea_country, 'та шенгеном: ', shengen_country)
# print('Країна з морем та шенгеном: ', shengen_country & sea_country)
#

# money_amount = 10000
# for country in countris.values():
#     currency_amount = money_amount / country['currency_rate']
#     print('В вас буде %.2f грошей в місцевій валюті: ' % currency_amount)

#sea_shengen_countries = sea_country & shengen_country
#
# for country_name in sea_shengen_countries:
#     for country in countris.keys():
#         if country == country_name:
#             print(country)
#             break



