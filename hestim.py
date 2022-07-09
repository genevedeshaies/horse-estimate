#imports si nécessaires
#constantes s'il y a lieu


# def getData():
#     """Collecter les données"""
#     return None

# def convert(height: float, unit: str) -> float:
#     """Convertir les données"""
#     return None
def heightRange(smallFactor, tallFactor, height):
    """Calculer la taille possible pour un cheval"""
    smallHorse = int(((100*height)/smallFactor))
    tallHorse = int(((100*height)/tallFactor))
    return (smallHorse, tallHorse)

def estimate(height, age):
    """Estimer la taille mature"""
    
    if 0 <= age < 7:
        prediction = heightRange(60, 50, height)
    elif 7 <= age <= 12:
        prediction = heightRange(75, 65, height)
    elif 12 < age <= 18:
        prediction = heightRange(90, 75, height)
    elif 18 < age <= 24:
        prediction = heightRange(90, 85, height)
    elif 24 < age <= 36:
        prediction = heightRange(95, 90, height)
    elif 36 < age <= 60:
        prediction = heightRange(100, 97, height)
    elif age >= 60 :
        prediction = height

    return prediction


#Rouler le programme
def main():
    height = float(input("How tall is your horse in inches? "))
    age = float(input("How old is your horse in months? "))
    return estimate(height, age)

if __name__ == "__main__":
    raise SystemExit(main())