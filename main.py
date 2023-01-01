import requests
from datetime import datetime
from sheets import ReadWrite
from passcode import ai_api_id, ai_app_key

# <----OPENAI---->
ai_end_point = "https://trackapi.nutritionix.com/v2/natural/exercise"

sheet_row = {}
sheet_list = []
GENDER = 'male'
WEIGHT_KG = 63
HEIGHT_CM = 180
AGE = 22

# <----API HEADERS---->
ai_header = {
    "x-app-id": ai_api_id,
    "x-app-key": ai_app_key,
}

exercise_input = input("Tell me about your exercise: ")

# <----PARAMS---->
ai_parameters = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}
# <----API REQUEST---->
exercise_response = requests.post(ai_end_point, json=ai_parameters, headers=ai_header)
result = exercise_response.json()
print(result, end="\n\n")

# <----DATE AND TIME FOR GOOGLE SHEETS---->
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_row = [
        today_date,
        now_time,
        exercise["name"].title(),
        str(exercise["duration_min"]),
        str(exercise["nf_calories"]),
    ]
    sheet_list.append(sheet_row)
print(sheet_list)

# <----INSTANCE OF ReadWrite OBJECT---->
g_sheet_editor = ReadWrite()
g_sheet_editor.write(sheet_list)
