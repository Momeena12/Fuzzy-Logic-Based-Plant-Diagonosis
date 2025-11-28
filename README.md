# Fuzzy Logic--Based Leaf Disease Diagnosis System

<img width="1508" height="944" alt="Screenshot 2025-11-28 at 12 24 05 PM" src="https://github.com/user-attachments/assets/d91e0964-40a5-44e6-93e9-0f81248687ca" />


A fuzzy-logic--based expert system designed to diagnose common plant
leaf diseases using visible symptoms such as color deviation, spotting,
powdery growth, and water-soaked lesions.\
This system uses fuzzy inference to handle uncertainty in symptoms and
provides an intelligent, user-friendly diagnosis.

## 📌 Project Overview

Manually identifying leaf diseases is difficult because many
symptoms---yellowing, spots, discoloration---look similar.\
Fuzzy logic is ideal for this problem because it works with linguistic
terms (e.g., mild, moderate, severe) instead of requiring precise
numeric values.

This system: - Takes user-entered leaf symptoms\
- Uses fuzzy membership functions to interpret them\
- Applies a rule base derived from a credible plant pathology textbook\
- Produces the most likely disease using fuzzy inference

## 📚 Credible Source

All disease rules are built using:

Agrios, G. N. (2005). *Plant Pathology* (5th ed.). Academic Press.

## 🌿 Supported Leaf Diseases

  Disease               Type        Key Symptoms
  --------------------- ----------- ---------------------------------
  Leaf Spot             Fungal      Brown spots with yellow halos
  Powdery Mildew        Fungal      White powder-like growth
  Rust                  Fungal      Orange/brown pustules
  Bacterial Blight      Bacterial   Water-soaked lesions, wilting
  Mosaic Virus          Viral       Light/dark mosaic leaf patterns
  Nutrient Deficiency   Abiotic     Uniform yellowing, no spots

## 🔢 Linguistic Variables

### Input Variables

-   Leaf Color Deviation (Normal, Yellowing, Mosaic Pattern)
-   Spots Severity (None, Mild, Severe)
-   Powder Presence (None, Medium, High)
-   Wet Lesions Severity (None, Medium, High)

### Output Variable

<img width="1510" height="945" alt="Screenshot 2025-11-28 at 12 19 52 PM" src="https://github.com/user-attachments/assets/c2c8a85b-49b7-4bd0-ae79-6ce5ae576dc7" />

-   Most Likely Disease

## 📈 Membership Function Ranges

### Leaf Color (0--100)

-   Normal: 0--40
-   Yellowing: 20--70
-   Mosaic Pattern: 60--100

### Spots Severity (0--100)

-   None: 0--30
-   Mild: 20--60
-   Severe: 50--100

### Powder Presence (0--100)

-   None: 0--35
-   Medium: 25--70
-   High: 60--100

### Wet Lesions (0--100)

-   None: 0--30
-   Medium: 20--60
-   High: 50--100

### Output Disease Peaks

-   Leaf Spot: Peak 15\
-   Powdery Mildew: Peak 35\
-   Rust: Peak 55\
-   Bacterial Blight: Peak 72.5\
-   Mosaic Virus: Peak 87.5\
-   Nutrient Deficiency: Peak 95

## 🧠 Fuzzy Rule Base

Rules derived from Agrios (2005), e.g.: - IF Yellowing AND No Spots →
Nutrient Deficiency\
- IF Powder = High → Powdery Mildew\
- IF Spots = Severe → Rust\
- IF Wet Lesions = High → Bacterial Blight\
- IF Mosaic Pattern → Mosaic Virus\
- IF Yellowing + Mild Spots → Leaf Spot

## 🧮 Example Diagnosis

Input: - Leaf Color = 95\
- Spots = 35\
- Powder = 0\
- Wet Lesions = 0

Output: - Predicted Disease: **Mosaic Virus** - Crisp Value: **87.5** -
Confidence: **0.96**

## 🛠 Implementation (SciPy-Fuzzy)

Tools used: - numpy\
- scikit-fuzzy\
- scipy

Pipeline: 1. Define universe of discourse\
2. Membership functions\
3. Rule base\
4. Fuzzy inference\
5. Defuzzification

## 📖 References

Agrios, G. N. (2005). *Plant Pathology* (5th ed.). Academic Press.
