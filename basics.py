from taipy import Gui
import pandas as pd

data = {
    "Date": pd.date_range("2023-01-01", periods=4, freq="D"),
    "Min": [222,419.7,662.7,323.5],
    "Max": [28.6,68.2,666,173.5]
}

# Parameters for the GUI
title = "Stock Simulator By Ishan"
path = "logo.png"  # Ensure this path is correct
company_name = "TATA"
company_minp = 340
company_maxp = 740

# Action function for the button
def ishan(state):
    print("Hey hello Ishan")
    print(state.path)
    print(state.company_minp)

    with open("data.txt","w") as f:
        f.write(f"{state.company_name}, {state.company_minp}, {state.company_maxp}")

# GUI layout
page = """
<|text-center |
<|{path}|image|>

<|{title}|hover_text=welcome to stock screener|>

Name of Stock: <|{company_name}|input|>

Min Price: <|{company_minp}|input|>

Max Price: <|{company_maxp}|input|>

<|Run Simulation|button|on_action=ishan|>

<|{title}|hover_text=your simulation|>

<|{data}|chart|mode=lines|x=Date|y[1]=Min|y[2]=Max|line[1]=dash|color[2]=blue|>

>
"""

# Run the app
if __name__ == "__main__":
    app = Gui(page)
    app.run(use_reloader=True)
