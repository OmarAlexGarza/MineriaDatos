import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

df = pd.read_csv('JugadoresFIFAv2.csv')

modelo = ols('remate ~ penales', data=df).fit()

anova_table = sm.stats.anova_lm(modelo, typ=2)

print("Tabla de ANOVA:")
print(anova_table)