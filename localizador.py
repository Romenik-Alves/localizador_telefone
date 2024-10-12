import phonenumbers
from phonenumbers import geocoder, carrier
from geopy.geocoders import Nominatim
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

print('')
print('                              Digite o número do telefone:')
print('                              ############################')
print('                              #    Expemplo: +14167718021 ')
print('                              ############################')
print('')

Number= str(input("Digite o número de celular:"))

ch_number = phonenumbers.parse(Number, "CH")
print('')
print('Local:',geocoder.description_for_number(ch_number, "en"))
print('')
from phonenumbers import carrier
service_number = phonenumbers.parse(Number,"Ca")
print('Operadora:', carrier.name_for_number(service_number,"en"))