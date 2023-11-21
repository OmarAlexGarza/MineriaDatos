import pandas as pd

def procesar_csv(input_path, output_path, columnas_a_eliminar, nuevos_nombres):
    # Cargar el archivo CSV en un DataFrame
    df = pd.read_csv(input_path)

    # Eliminar las columnas especificadas
    df = df.drop(columnas_a_eliminar, axis=1)

    # Cambiar los nombres de las columnas
    if nuevos_nombres is not None:
        df.columns = nuevos_nombres

    # Guardar el DataFrame resultante en un nuevo archivo CSV
    df.to_csv(output_path, index=False)

# Ejemplo de uso
input_path = 'JugadoresFIFA.csv'
output_path = 'JugadoresFIFAv2.csv'
columnas_a_eliminar = ['positions','value_euro', 'wage_euro','international_reputation(1-5)','weak_foot(1-5)','skill_moves(1-5)','work_rate','body_type','release_clause_euro','club_rating','national_rating','national_team_position','national_jersey_number','crossing','heading_accuracy','balance','long_shots','aggression','interceptions','positioning','composure','marking','standing_tackle','sliding_tackle','GK_diving','GK_handling','GK_kicking','GK_positioning','GK_reflexes','tags','traits','LS','ST','RS','LW','LF','CF','RF','RW','LAM','CAM','RAM','LM','LCM','CM','RCM','RM','LWB','LDM','CDM','RDM','RWB','LB','LCB','CB','RCB','RB']
nuevos_nombres = ['id','nombre','nombrecompleto','fechadenacimiento','edad','altura','peso','nacionalidad','calificacion','potencial','piernahabil','equipo','posicion','numero','antiguedad','terminacioncontrato','seleccionnacional','remate','pasecorto','volea','dribles','curvas','tirolibre','paselargo','controlbalon','aceleracion','velocidad','agilidad','reaccion','potencia','salto','resistencia','fuerza','vision','penales']

procesar_csv(input_path, output_path, columnas_a_eliminar, nuevos_nombres)
