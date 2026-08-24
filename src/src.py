import pandas as pd
import numpy as np
from pulp import *

# --- 1. VERİ YÜKLEME ---
# Veri setiniz data/ klasörü altında kabul edilir
df_scenarios = pd.read_excel("data/411_scenarios_data.xlsx")

nurses = ["H" + str(i) for i in range(1, 30)]  # 29 Hemşire
days = ["G1", "G2", "G3", "G4", "G5", "G6", "G7"]
shifts = ["S", "A", "G"]  # Sabah, Akşam, Gece

# --- 2. MODEL VE KARAR DEĞİŞKENLERİ ---
prob = LpProblem("Robust_Nurse_Scheduling", LpMinimize)

# Karar Değişkeni: x[hemşire][gün][vardiya] -> 0 veya 1
x = LpVariable.dicts("assign", (nurses, days, shifts), 0, 1, LpBinary)

# --- 3. OPTİMİZASYON KISITLARI ---
# Her hemşire günde en fazla 1 vardiya
for n in nurses:
    for d in days:
        prob += lpSum([x[n][d][s] for s in shifts]) <= 1

# Robust Talep Kısıtı: En kötü senaryo talebini karşılama
worst_case_demand = df_scenarios.max(axis=1)
for d in days:
    for s in shifts:
        prob += lpSum([x[n][d][s] for n in nurses]) >= worst_case_demand[d][s]

# --- 4. MODELİN ÇALIŞTIRILMASI ---
prob.solve()
print("Çözüm Durumu:", LpStatus[prob.status])
