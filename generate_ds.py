import pandas as pd
import numpy as np


def generate_cricket_dataset(num_records):
    # Ensuring consistent results for professional use
    np.random.seed(42)

    data = []
    lengths = ['Yorker', 'Full', 'Half Volley',
               'Good Length', 'Short', 'Bouncer']
    lines = ['Wide Outside Off', 'Outside Off', 'Stumps', 'Leg Side']

    for _ in range(num_records):
        speed = np.random.randint(70, 161)
        # Rule: 70-110 is Spin, 111-160 is Pace
        pace_spin = 'Spin' if speed <= 110 else 'Pace'

        length = np.random.choice(lengths)
        line = np.random.choice(lines)

        # Physics Logic: Back foot only for short/bouncers
        if length in ['Short', 'Bouncer']:
            footwork = 'Back Foot'
        else:
            footwork = 'Front Foot'

        # Mapping Shot Predictions and Angles
        if line in ['Wide Outside Off', 'Outside Off']:
            side = 'Off Side'
            if length in ['Short', 'Bouncer']:
                prediction = 'Square Cut'
                angle = np.random.randint(45, 90)
            else:
                prediction = 'Cover Drive'
                angle = np.random.randint(20, 60)
        else:
            side = 'On Side'
            if length in ['Short', 'Bouncer']:
                prediction = 'Pull'
                angle = np.random.randint(120, 175)
            elif length in ['Yorker', 'Full'] and line == 'Leg Side':
                prediction = 'Sweep'
                angle = np.random.randint(140, 170)
            elif line == 'Leg Side' or length == 'Good Length':
                prediction = 'Flick'
                angle = np.random.randint(100, 140)
            else:
                prediction = 'Straight Drive'
                angle = np.random.randint(80, 100)

        # Logic for Professional Metrics: Runs and Wicket Probability
        if length == 'Half Volley':
            runs = np.random.choice([4, 6], p=[0.8, 0.2])
            wicket_prob = round(np.random.uniform(0.01, 0.08), 2)
        elif length == 'Yorker':
            runs = np.random.choice([0, 1], p=[0.7, 0.3])
            wicket_prob = round(np.random.uniform(0.60, 0.85), 2)
        elif length == 'Bouncer':
            runs = np.random.choice([0, 1, 4], p=[0.4, 0.4, 0.2])
            wicket_prob = round(np.random.uniform(0.30, 0.60), 2)
        else:
            runs = np.random.choice([1, 2, 4], p=[0.4, 0.3, 0.3])
            wicket_prob = round(np.random.uniform(0.10, 0.40), 2)

        data.append([speed, pace_spin, length, line, footwork,
                    angle, side, prediction, runs, wicket_prob])

    # Creating the DataFrame
    df = pd.DataFrame(data, columns=[
        'Ball Speed', 'Pace/Spin', 'Ball Length', 'Ball Line',
        'Footwork', 'Shot Angle', 'Side', 'Prediction',
        'Runs Scored', 'Wicket Probability'
    ])
    return df


# Generating and saving the dataset
df_700 = generate_cricket_dataset(700)
df_700.to_csv('ds700.csv', index=False)
print("File 'ds700.csv' has been generated with 700 records.")
