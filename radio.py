import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Dictionary of radioactive elements and their corresponding half-lives
element_half_lives = {
    "Uranium-238": 4.468e9,
    "Carbon-14": 5730,
    "Radium-226": 1602,
    # Add more elements as needed
}

def radioactive_decay(initial_amount, decay_constant, time):
    return initial_amount * np.exp(-decay_constant * time)

def main():
    st.title("Radioactive Decay Calculator")

    # User input
    initial_amount = st.number_input("Initial Amount of Radioactive Substance:", min_value=0.0, step=0.1)

    # Dropdown menu for selecting the radioactive element
    selected_element = st.selectbox("Select Radioactive Element:", list(element_half_lives.keys()))

    # Get the decay constant for the selected element
    decay_constant = np.log(2) / element_half_lives[selected_element]

    time = st.number_input("Time (in years):", min_value=0.0, step=0.1)

    # Calculate remaining amount
    remaining_amount = radioactive_decay(initial_amount, decay_constant, time)

    # Plot the radioactive decay curve
    times = np.linspace(0, time, 100)
    decay_curve = radioactive_decay(initial_amount, decay_constant, times)

    # Display result
    st.write(f"Remaining Amount of {selected_element} after {time} years: {remaining_amount:.4f}")

    # Plotting
    plt.figure(figsize=(8, 6))
    plt.plot(times, decay_curve, label=f"{selected_element} Decay Curve")
    plt.xlabel("Time (years)")
    plt.ylabel("Remaining Amount")
    plt.legend()
    st.pyplot(plt)

if __name__ == "__main__":
    main()
