import pandas as pd
import random
import numpy as np

rows = []

shots = ["Cover Drive","Straight Drive","Cut Shot","Pull Shot","Flick","Defensive"]

for i in range(5000):

    ball_speed = random.randint(110,150)

    pace_spin = random.choice(["Pace","Spin"])

    ball_length = random.choice(["Full","Good","Short"])

    ball_line = random.choice(["Off","Middle","Leg"])

    if ball_length == "Full":
        footwork = random.choice(["Frontfoot","Frontfoot","Backfoot"])
    elif ball_length == "Short":
        footwork = random.choice(["Backfoot","Backfoot","Frontfoot"])
    else:
        footwork = random.choice(["Frontfoot","Backfoot"])

    # Shot selection based on conditions
    if ball_length == "Full" and ball_line == "Off":
        shot = random.choice(["Cover Drive","Straight Drive","Defensive"])
    elif ball_length == "Short":
        shot = random.choice(["Pull Shot","Cut Shot","Defensive"])
    elif ball_line == "Leg":
        shot = random.choice(["Flick","Pull Shot"])
    else:
        shot = random.choice(shots)

    # Shot angle ranges
    if shot == "Straight Drive":
        angle = np.random.normal(5,3)
    elif shot == "Cover Drive":
        angle = np.random.normal(30,5)
    elif shot == "Cut Shot":
        angle = np.random.normal(75,8)
    elif shot == "Pull Shot":
        angle = np.random.normal(115,10)
    elif shot == "Flick":
        angle = np.random.normal(150,8)
    else:
        angle = np.random.normal(20,20)

    angle = round(max(0,min(180,angle)),2)

    side = "Off" if angle < 90 else "Leg"

    runs = random.choices(
        [0,1,2,4,6],
        weights=[25,35,15,20,5]
    )[0]

    wicket_prob = round(random.uniform(0.01,0.35),3)

    rows.append([
        ball_speed,
        pace_spin,
        ball_length,
        ball_line,
        footwork,
        angle,
        side,
        shot,
        runs,
        wicket_prob
    ])

columns = [
"Ball Speed",
"Pace/Spin",
"Ball Length",
"Ball Line",
"Footwork",
"Shot Angle",
"Side",
"Prediction",
"Runs Scored",
"Wicket Probability"
]

df = pd.DataFrame(rows,columns=columns)

df.to_csv("realistic_cricket_dataset.csv",index=False)

print(df.head())