import pandas as pd

input_path = 'JugadoresFIFAv2.csv'

df = pd.read_csv(input_path)

edadprom = df['edad'].mean()
conteopierna = df['piernahabil'].value_counts()
piernacomun = df['piernahabil'].mode()[0]
mincalif = int(df['calificacion'].min())
maxcalif = int(df['calificacion'].max())
sumpeso = df['peso'].sum()
varianzaremate= df['remate'].var()
desviacionpasecorto = df['pasecorto'].std()
asimetriapenales = df['penales'].skew()
kurtosisdribles = df['dribles'].kurtosis()

print('Edad promedio jugadores: ', edadprom)
print('Conteo de pierna habil:', conteopierna)
print('Pierna Habil Comun: ', piernacomun)
print('Calificacion minima: ', mincalif)
print('Calificacion maxima: ', maxcalif)
print('Sumatoria de pesos de jugadores en kg: ', sumpeso)
print('Varianza de remates: ', varianzaremate)
print('Desviacion estandar de pase corto: ', desviacionpasecorto)
print('Asimetria de penales: ', asimetriapenales)
print('Kurtosis de dribles: ', kurtosisdribles)
