import tkinter as tk
from tkinter import ttk
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# ================== FUZZY VARIABLES ==================
leaf_color = ctrl.Antecedent(np.arange(0, 101, 1), 'leaf_color')
spots = ctrl.Antecedent(np.arange(0, 101, 1), 'spots')
powder = ctrl.Antecedent(np.arange(0, 101, 1), 'powder')
wet = ctrl.Antecedent(np.arange(0, 101, 1), 'wet')

diagnosis = ctrl.Consequent(np.arange(0, 101, 1), 'diagnosis')

# ================== MEMBERSHIP FUNCTIONS ==================
leaf_color['normal'] = fuzz.trimf(leaf_color.universe, [0, 0, 40])
leaf_color['yellowing'] = fuzz.trimf(leaf_color.universe, [20, 45, 70])
leaf_color['mosaic_pattern'] = fuzz.trimf(leaf_color.universe, [60, 80, 100])

spots['none'] = fuzz.trimf(spots.universe, [0, 0, 30])
spots['mild'] = fuzz.trimf(spots.universe, [20, 40, 60])
spots['severe'] = fuzz.trimf(spots.universe, [50, 100, 100])

powder['none'] = fuzz.trimf(powder.universe, [0, 0, 35])
powder['medium'] = fuzz.trimf(powder.universe, [25, 47.5, 70])
powder['high'] = fuzz.trimf(powder.universe, [60, 100, 100])

wet['none'] = fuzz.trimf(wet.universe, [0, 0, 30])
wet['medium'] = fuzz.trimf(wet.universe, [20, 40, 60])
wet['high'] = fuzz.trimf(wet.universe, [50, 100, 100])

diagnosis['Leaf_Spot'] = fuzz.trimf(diagnosis.universe, [0, 15, 30])
diagnosis['Powdery_Mildew'] = fuzz.trimf(diagnosis.universe, [20, 35, 50])
diagnosis['Rust'] = fuzz.trimf(diagnosis.universe, [40, 55, 70])
diagnosis['Bacterial_Blight'] = fuzz.trimf(diagnosis.universe, [60, 72.5, 85])
diagnosis['Mosaic_Virus'] = fuzz.trimf(diagnosis.universe, [75, 87.5, 100])
diagnosis['Nutrient_Deficiency'] = fuzz.trimf(diagnosis.universe, [90, 95, 100])

# ================== RULE BASE (ALL 25 RULES) ==================
rule1  = ctrl.Rule(leaf_color['yellowing'] & spots['mild']   & powder['none']   & wet['none'],   diagnosis['Leaf_Spot'])
rule2  = ctrl.Rule(leaf_color['yellowing'] & spots['severe'] & powder['none']   & wet['none'],   diagnosis['Leaf_Spot'])
rule3  = ctrl.Rule(leaf_color['yellowing'] & spots['mild']   & powder['none']   & wet['medium'], diagnosis['Leaf_Spot'])
rule4  = ctrl.Rule(leaf_color['yellowing'] & spots['severe'] & powder['none']   & wet['medium'], diagnosis['Leaf_Spot'])

rule5  = ctrl.Rule(leaf_color['normal']    & spots['none']   & powder['medium'] & wet['none'],   diagnosis['Powdery_Mildew'])
rule6  = ctrl.Rule(leaf_color['normal']    & spots['mild']   & powder['medium'] & wet['none'],   diagnosis['Powdery_Mildew'])
rule7  = ctrl.Rule(leaf_color['yellowing'] & spots['none']   & powder['high']   & wet['none'],   diagnosis['Powdery_Mildew'])
rule8  = ctrl.Rule(leaf_color['normal']    & spots['none']   & powder['high']   & wet['none'],   diagnosis['Powdery_Mildew'])

rule9  = ctrl.Rule(leaf_color['yellowing'] & spots['severe'] & powder['none']   & wet['none'],   diagnosis['Rust'])
rule10 = ctrl.Rule(leaf_color['normal']    & spots['severe'] & powder['none']   & wet['none'],   diagnosis['Rust'])

rule11 = ctrl.Rule(leaf_color['yellowing'] & spots['mild']   & powder['none']   & wet['high'],   diagnosis['Bacterial_Blight'])
rule12 = ctrl.Rule(leaf_color['yellowing'] & spots['severe'] & powder['none']   & wet['high'],   diagnosis['Bacterial_Blight'])
rule13 = ctrl.Rule(leaf_color['normal']    & spots['mild']   & powder['none']   & wet['high'],   diagnosis['Bacterial_Blight'])

rule14 = ctrl.Rule(leaf_color['mosaic_pattern'] & spots['none'] & powder['none'] & wet['none'], diagnosis['Mosaic_Virus'])
rule15 = ctrl.Rule(leaf_color['mosaic_pattern'] & spots['mild'] & powder['none'] & wet['none'], diagnosis['Mosaic_Virus'])
rule16 = ctrl.Rule(leaf_color['mosaic_pattern'] & spots['none'] & powder['medium'] & wet['none'], diagnosis['Mosaic_Virus'])

rule17 = ctrl.Rule(leaf_color['yellowing'] & spots['none'] & powder['none'] & wet['none'], diagnosis['Nutrient_Deficiency'])
rule18 = ctrl.Rule(leaf_color['yellowing'] & spots['none'] & powder['none'] & wet['medium'], diagnosis['Nutrient_Deficiency'])
rule19 = ctrl.Rule(leaf_color['yellowing'] & spots['mild'] & powder['none'] & wet['none'], diagnosis['Nutrient_Deficiency'])
rule20 = ctrl.Rule(leaf_color['normal'] & spots['none'] & powder['none'] & wet['none'], diagnosis['Nutrient_Deficiency'])
rule21 = ctrl.Rule(leaf_color['normal'] & spots['mild'] & powder['none'] & wet['none'], diagnosis['Nutrient_Deficiency'])

rule22 = ctrl.Rule(leaf_color['normal'] & spots['none'] & powder['medium'] & wet['medium'], diagnosis['Powdery_Mildew'])
rule23 = ctrl.Rule(leaf_color['yellowing'] & spots['mild'] & powder['medium'] & wet['none'], diagnosis['Leaf_Spot'])
rule24 = ctrl.Rule(leaf_color['yellowing'] & spots['severe'] & powder['medium'] & wet['none'], diagnosis['Leaf_Spot'])
rule25 = ctrl.Rule(leaf_color['normal'] & spots['severe'] & powder['medium'] & wet['none'], diagnosis['Rust'])

rules = [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10,
         rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18,
         rule19, rule20, rule21, rule22, rule23, rule24, rule25]

system = ctrl.ControlSystem(rules)
sim = ctrl.ControlSystemSimulation(system)

diseases = ['Leaf_Spot','Powdery_Mildew','Rust','Bacterial_Blight','Mosaic_Virus','Nutrient_Deficiency']

# ================== DIAGNOSE FUNCTION ==================
def diagnose():
    global sim

    # ✅ Handle "all sliders zero" case
    if leaf_slider.get() == 0 and spots_slider.get() == 0 and powder_slider.get() == 0 and wet_slider.get() == 0:
        result_label.config(text="⚠️ No disease detected")
        for bar in progress_bars:
            bar['value'] = 0
        for i, d in enumerate(diseases):
            labels[i].config(text=f"{d}: 0.00")
        return

    sim.reset()
    sim.input['leaf_color'] = leaf_slider.get()
    sim.input['spots'] = spots_slider.get()
    sim.input['powder'] = powder_slider.get()
    sim.input['wet'] = wet_slider.get()

    try:
        sim.compute()
        crisp_output = sim.output['diagnosis']
    except:
        result_label.config(text="⚠️ No rule matched. Adjust sliders.")
        return

    degrees = {}
    for d in diseases:
        mf = diagnosis[d].mf
        deg = fuzz.interp_membership(diagnosis.universe, mf, crisp_output)
        degrees[d] = float(deg)

    best_disease = max(degrees, key=degrees.get)
    result_label.config(text=f"✅ Predicted Disease: {best_disease}")

    for i, d in enumerate(diseases):
        progress_bars[i]['value'] = degrees[d] * 100
        labels[i].config(text=f"{d}: {degrees[d]:.2f}")

# ================== GUI DESIGN ==================
root = tk.Tk()
root.title("Plant Leaf Disease Diagnosis")
root.geometry("700x600")
root.config(bg="#E8F6F3")

heading = tk.Label(root, text="🌿 Plant Leaf Disease Diagnosis 🌿",
                   font=("Arial", 18, "bold"), bg="#2ECC71", fg="white", pady=10)
heading.pack(fill="x", pady=10)

input_frame = tk.Frame(root, bg="#E8F6F3")
input_frame.pack(pady=10)

leaf_slider = tk.Scale(input_frame, from_=0, to=100, orient='horizontal',
                       label='Leaf Color', troughcolor="#82E0AA", length=500)
leaf_slider.pack(pady=5)

spots_slider = tk.Scale(input_frame, from_=0, to=100, orient='horizontal',
                        label='Spots Severity', troughcolor="#F1948A", length=500)
spots_slider.pack(pady=5)

powder_slider = tk.Scale(input_frame, from_=0, to=100, orient='horizontal',
                         label='Powder Presence', troughcolor="#AED6F1", length=500)
powder_slider.pack(pady=5)

wet_slider = tk.Scale(input_frame, from_=0, to=100, orient='horizontal',
                      label='Wet Lesions', troughcolor="#D2B4DE", length=500)
wet_slider.pack(pady=5)

tk.Button(root, text="🔍 Diagnose Disease", command=diagnose,
          bg="#27AE60", fg="black", font=("Arial", 13, "bold"),
          padx=20, pady=6).pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 15, "bold"),
                        bg="#E8F6F3", fg="#C0392B")
result_label.pack(pady=10)

result_frame = tk.Frame(root, bg="#E8F6F3")
result_frame.pack(pady=10)

progress_bars = []
labels = []
colors = ["#58D68D", "#5DADE2", "#F5B041", "#EC7063", "#AF7AC5", "#F7DC6F"]

for i, d in enumerate(diseases):
    lbl = tk.Label(result_frame, text=f"{d}: 0.00",
                   bg="#E8F6F3", font=("Arial", 11, "bold"))
    lbl.grid(row=i, column=0, pady=4, sticky="w")

    style = ttk.Style()
    style.configure(f"color{i}.Horizontal.TProgressbar", background=colors[i])

    bar = ttk.Progressbar(result_frame, length=350, maximum=100,
                          style=f"color{i}.Horizontal.TProgressbar")
    bar.grid(row=i, column=1, padx=8, pady=4)

    labels.append(lbl)
    progress_bars.append(bar)

root.mainloop()