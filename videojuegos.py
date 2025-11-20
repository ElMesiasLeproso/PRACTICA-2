import pandas as pd
import numpy as np






sales_data= {
    "gameID":["g1","g2","g3","g4","g5", "g6"],
    "title":["Game A","Game B","Game C","Game D","Game E", "Game F"],
    "genre":["Action","Adventure","Action","RPG","Strategy", "RPG"],
    "publicher":["Pub1","Pub2","Pub1","Pub3","Pub4", "Pub3"],
    "unids_sold_millons":[2.5,3.0,1.5,4.0,2.0, 3.5],
}
sales_df= pd.DataFrame(sales_data)


#fuente 2 reseñas de criticos (externo)
reviews_data={
    "gameID":["g1","g2","g3","g4","g5", "g7"], #nota: g6 falta y g7 sobra
    "critic_score":[85,90,78,88,92, 80], #puntuacion de 0 a 100
    "user_score":[90,85,70,91, np.nan,75], #Alguien olvido puntuar al juego 5
}
reviews_df=pd.DataFrame(reviews_data)

print("---Datos de ventas---")
print(sales_df)
print("---Datos de reseñas---")
print(reviews_df)

#limpieza de datos y prepracion
#desciicon : rellenaremos el user_score que falta con el primerido

mean_user_score= reviews_df["user_score"].mean() # promedio de calificaciones de usuarios
reviews_df["user_score"] = reviews_df["user_score"].fillna(mean_user_score)

print(f"\n--- Reseñas (limpias, nan, rellenado con {mean_user_score})---")
print(reviews_df)

#fusuion de tablas  (merge)
#fusionar tabla de ventas con reseñas, game id como llave
#INNER JOIN. nos quedamos con los juegos que existen en ambas tablas
#g6 va a desaparecer, g7 tambien va a desaárecer
df = pd.merge(sales_df, reviews_df, on="gameID", how="inner")

print("\n--- Datos fusionados (ventas + reseñas) ---" )
print (df)

#crear nuevas   columnas que nos den mas informacion
#columna estimacion de ingresos(asumiendo que valen $50 cada uno)

df["estimated_revenue_millions"] = (df["unids_sold_millons"] * 50)/1000
 #millones de dolares

#columna brecha que hay entre resñeas de criticos y usuarios
df["score_gap"] = abs(df["critic_score"] - df["user_score"])

#columna estandar puntuacion de criticos convertida a escala de 0 a 10
df["critic_score_10"]=df ["critic_score"]/10

print("\n--- tabla transformada (con nuevas columnas) ---")
print(df)
