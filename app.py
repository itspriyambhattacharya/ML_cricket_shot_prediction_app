import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Load trained objects
# -----------------------------
model = joblib.load("shot_model.pkl")
scaler = joblib.load("scaler.pkl")
le = joblib.load("label_encoder.pkl")
feature_columns = joblib.load("feature_columns.pkl")

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🏏 Cricket Shot Prediction System")
st.write("Developed by Priyam Bhattacharya")
st.write(
    "Enter the ball characteristics below to predict which cricket shot "
    "the batsman is likely to play."
)

# -----------------------------
# User Inputs
# -----------------------------

ball_speed = st.slider(
    "Ball Speed (km/h)",
    min_value=70,
    max_value=160,
    value=130
)

pace_spin = st.selectbox(
    "Bowling Type",
    ["Pace", "Spin"]
)

ball_length = st.selectbox(
    "Ball Length",
    ["Full", "Good Length", "Short", "Yorker", "Half Volley", "Bouncer"]
)

ball_line = st.selectbox(
    "Ball Line",
    ["Off", "Middle", "Leg"]
)

footwork = st.selectbox(
    "Footwork",
    ["Frontfoot", "Backfoot"]
)

shot_angle = st.slider(
    "Shot Angle (degrees)",
    min_value=0,
    max_value=180,
    value=30
)

side = st.selectbox(
    "Side",
    ["Off", "On"]
)

# -----------------------------
# Create Input DataFrame
# -----------------------------

input_data = pd.DataFrame({
    "Ball_Speed": [ball_speed],
    "Pace_Spin": [pace_spin],
    "Ball_Length": [ball_length],
    "Ball_Line": [ball_line],
    "Footwork": [footwork],
    "Shot_Angle": [shot_angle],
    "Side": [side]
})

# -----------------------------
# One-Hot Encoding
# -----------------------------

input_encoded = pd.get_dummies(input_data)

# Ensure same columns as training
input_encoded = input_encoded.reindex(columns=feature_columns, fill_value=0)

# -----------------------------
# Scaling
# -----------------------------

input_scaled = scaler.transform(input_encoded)

# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict Shot"):

    with st.spinner("Predicting shot..."):

        prediction = model.predict(input_scaled)
        shot_name = le.inverse_transform(prediction)

        st.success(f"🏏 Predicted Shot: **{shot_name[0]}**")

        # -----------------------------
        # Show prediction probabilities
        # -----------------------------
        # if hasattr(model, "predict_proba"):

        #     probs = model.predict_proba(input_scaled)

        #     prob_df = pd.DataFrame({
        #         "Shot": le.classes_,
        #         "Probability": probs[0]
        #     }).sort_values(by="Probability", ascending=False)

        #     st.subheader("Prediction Probabilities")

        #     st.bar_chart(
        #         prob_df.set_index("Shot")
        #     )

# -----------------------------
# Footer
# -----------------------------

st.markdown("---")
st.write("Machine Learning based Cricket Shot Prediction")