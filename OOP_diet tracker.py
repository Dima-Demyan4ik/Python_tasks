class Diet:
    def __init__(self, breakfast_calories, lunch_calories,dinner_calories, exercise, basic_metabolic_rate):
        self.breakfast_calories=breakfast_calories
        self.lunch_calories=lunch_calories
        self.dinner_calories=dinner_calories
        self.exercise=exercise
        self.basic_metabolic_rate=basic_metabolic_rate

    def calorie_deficit(self):
        deficit = self.basic_metabolic_rate + self.exercise - (self.breakfast_calories + self.lunch_calories + self.dinner_calories)
        return deficit

breakfast_calories=int(input("How many calories did you have for breakfast?"))
lunch_calories=int(input("How many calories did you have for lunch?"))
dinner_calories=int(input("How many calories did you have for dinner?"))
exercise=int(input("How many calories did you burn exercising?"))
basic_metabolic_rate=int(input("What is your mbr?"))

fitness=Diet(breakfast_calories,lunch_calories, dinner_calories,exercise,basic_metabolic_rate)
weekly_deficit=7 * fitness.calorie_deficit()

if weekly_deficit > 0:
    print(f"You will lose {round(weekly_deficit/3600,2)} lbs per week")
elif weekly_deficit == 0:
    print(f"your weight will stay the same")
else:
    print(f"You will gain{round(-1 * weekly_deficit/3600,2)} lbs per week")
