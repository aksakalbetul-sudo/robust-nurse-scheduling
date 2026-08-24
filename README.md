# robust-nurse-scheduling
Robust Integer Programming model for nurse scheduling and workload optimization under 411 demand scenarios
# Hospital Nurse Scheduling & Workload Optimization 🏥

This project presents a **Robust Integer Programming (RIP)** model designed to solve the Nurse Scheduling Problem (NSP) under high demand uncertainty. Developed as part of the Advanced Mathematical Programming graduate course at Istanbul University-Cerrahpaşa.

## 📌 Project Overview
* **Problem Type:** NP-Hard Combinatorial Optimization
* **Context:** A large hospital in Belgium with 29 nurses over a 7-day planning horizon.
* **Key Challenge:** High fluctuation and unpredictability in patient care demand.
* **Methodology:** Robust Integer Programming considering **411 distinct demand scenarios** to ensure operational resilience in worst-case conditions.

---

## 🛠️ Mathematical Model & Constraints
The optimization framework balances workload distribution while strictly adhering to legal, ergonomic, and operational constraints:

* **Shift Structure:** Morning (S), Evening (A), Night (G), Off (-).
* **Single Shift Limit:** Maximum 1 shift per nurse per day.
* **Rest Constraints:** Mandatory minimum 12-hour rest (e.g., no Morning shift after a Night shift).
* **Workload Limits:** Maximum 5 working days per week per nurse.
* **Robust Demand Coverage:** Staffing levels guaranteed to meet worst-case demand thresholds across 411 scenarios.

---

## 💻 Tech Stack & Architecture
* **Language:** Python 3.x
* **Optimization Framework:** PuLP / Gurobi
* **Data Handling:** Pandas, NumPy
* **Input Data:** `411_scenarios_data.xlsx`

---

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/robust-nurse-scheduling.git](https://github.com/YOUR_USERNAME/robust-nurse-scheduling.git)
   cd robust-nurse-scheduling
