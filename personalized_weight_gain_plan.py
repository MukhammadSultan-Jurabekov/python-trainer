def calculate_bmi(weight, height):
    # Calculate BMI = weight(kg) / height(m)^2
    return weight / (height / 100) ** 2

def is_underweight(bmi):
    return bmi < 18.5

def meal_plan():
    return [
        {
            "Meal": "Breakfast",
            "Description": "Whole-grain toast with nut butter and a banana. Smoothie with whole milk, protein powder, spinach, and frozen berries."
        },
        {
            "Meal": "Mid-Morning Snack",
            "Description": "Greek yogurt with honey and a handful of nuts."
        },
        {
            "Meal": "Lunch",
            "Description": "Turkey and cheese sandwich on whole-grain bread with avocado slices. Side of sweet potato fries."
        },
        {
            "Meal": "Afternoon Snack",
            "Description": "Granola bar or homemade trail mix with dried fruits and nuts."
        },
        {
            "Meal": "Dinner",
            "Description": "Grilled salmon with quinoa, steamed broccoli, and a mixed greens salad topped with olive oil."
        },
        {
            "Meal": "Evening Snack",
            "Description": "Small bowl of cottage cheese with pineapple chunks or a glass of milk."
        }
    ]

def exercise_plan():
    return [
        {
            "Exercise": "Strength Training",
            "Description": "Include exercises like weight lifting, squats, lunges, and push-ups to build muscle mass. Train 3-4 times per week."
        },
        {
            "Exercise": "Cardio",
            "Description": "Light cardio like walking or cycling to stimulate appetite. Do not overdo it, as too much cardio can burn excessive calories."
        }
    ]

def weight_gain_tips():
    return [
        "Eat more frequently: 5-6 smaller meals during the day.",
        "Choose nutrient-dense foods like avocados, nuts, seeds, whole grains, and full-fat dairy.",
        "Add extra calories to meals by incorporating cheese, nut butter, dry or liquid milk.",
        "Incorporate smoothies and shakes made with high-calorie ingredients.",
        "Avoid drinking beverages before or during meals if they make you feel full.",
        "Strength training exercises will help build muscle mass, contributing to healthy weight gain."
    ]

def recommend_strength_training(age):
    if age < 20:
        return {
            "Focus": "Functional Training",
            "Exercises": [
                "Squats", 
                "Lunges", 
                "Push", 
                "Pull", 
                "Compound Exercises", 
                "Plyometric Exercises", 
                "Unilateral Exercises"
            ],
            "Workout Week": [
                "1x 30-min upper-body functional training",
                "1x 30-min lower-body functional training",
                "1x 30-min core functional training"
            ]
        }
    elif 20 <= age < 35:
        return {
            "Focus": "Hypertrophy and Power Training",
            "Exercises": [
                "Hypertrophy Training (3-4 sets of 10-12 reps)",
                "Power Training (2-4 reps)"
            ],
            "Workout Week": [
                "2x 60-min hypertrophy sessions (non-consecutive days)",
                "2x 30-45 min power sessions (non-consecutive days)"
            ]
        }
    elif 35 <= age < 50:
        return {
            "Focus": "Heavy Lifting and Power Training",
            "Exercises": [
                "Heavy Lifting (3-5 sets of 6-8 reps)",
                "Power Training"
            ],
            "Workout Week": [
                "Up to 4x 45-60 min weightlifting/power sessions"
            ]
        }
    elif 50 <= age < 60:
        return {
            "Focus": "Heavy Lifting and Mobility",
            "Exercises": [
                "Heavy Lifting (gradual phasing)",
                "Mobility Work (2x 20-minute sessions)",
                "Optional HIIT (1x 15-min session)"
            ],
            "Workout Week": [
                "1x 45-60 min lower-body weightlifting (and mobility)",
                "1x 45-60 min upper-body weightlifting (and mobility)",
                "1x 45-60 min full-body weightlifting (and mobility)"
            ]
        }
    else:
        return {
            "Focus": "Hypertrophy and Power Training",
            "Exercises": [
                "Hypertrophy Training (3 sets of 10-12 reps)",
                "Power Training"
            ],
            "Workout Week": [
                "3-4x hypertrophy/power sessions, up to 30 mins each"
            ]
        }

def personalized_plan(name, age, weight, height):
    bmi = calculate_bmi(weight, height)
    
    print(f"\nHello {name}, here is your personalized weight gain and strength training plan:")
    
    if is_underweight(bmi):
        print(f"Your BMI is {bmi:.2f}, which is considered underweight.")
    else:
        print(f"Your BMI is {bmi:.2f}.")
    
    print("\n**Nutritional Tips**")
    for tip in weight_gain_tips():
        print(f"- {tip}")
    
    print("\n**Meal Plan**")
    for meal in meal_plan():
        print(f"{meal['Meal']}: {meal['Description']}")
    
    print("\n**Exercise Plan**")
    for exercise in exercise_plan():
        print(f"{exercise['Exercise']}: {exercise['Description']}")
    
    print("\n**Strength Training Recommendations Based on Age**")
    strength_training_plan = recommend_strength_training(age)
    print(f"Focus: {strength_training_plan['Focus']}")
    print("Recommended Exercises:")
    for exercise in strength_training_plan["Exercises"]:
        print(f" - {exercise}")
    print("\nExample Workout Week:")
    for workout in strength_training_plan["Workout Week"]:
        print(f" - {workout}")

    print("\nIt's always a good idea to consult with your healthcare provider or a dietitian to ensure that this plan is right for you.")

def main():
    # Get user inputs
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in centimeters: "))

    # Generate personalized plan
    personalized_plan(name, age, weight, height)

if __name__ == "__main__":
    main()
