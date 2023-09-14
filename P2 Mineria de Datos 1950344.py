import pandas as pd

# Lee la base de datos descargada
archivo_csv = "JugadoresFIFA.csv"
df = pd.read_csv(archivo_csv)

# Elimina las columnas que no queremos
columnas_a_eliminar = ['potential','value_euro','wage_euro','international_reputation(1-5)','weak_foot(1-5)','skill_moves(1-5)','work_rate','body_type','release_clause_euro','club_rating','national_rating','national_team_position','national_jersey_number','crossing','heading_accuracy','balance','long_shots','aggression','interceptions','positioning','composure','marking','standing_tackle','sliding_tackle','GK_diving','GK_handling','GK_kicking','GK_positioning','GK_reflexes','tags','traits','LS','ST','RS','LW','LF','CF','RF','RW','LAM','CAM','RAM','LM','LCM','CM','RCM','RM','LWB','LDM','CDM','RDM','RWB','LB','LCB','CB','RCB','RB']
df = df.drop(columns=columnas_a_eliminar)

# Se guarda en un archivo nuevo
nuevo_archivo_csv = "JugadoresFIFA_Normalizado.csv"
df.to_csv(nuevo_archivo_csv, index=False)


