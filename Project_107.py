import pandas as pd
import csv
import plotly.express as px

fd = pd.read_csv("data4.csv")
#std = fd.loc[fd["student_id"]=="TRL_xyz"]
m = fd.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
graph = px.scatter(m, x = "student_id", y = "level", size = "attempt", color = "attempt")
graph.show()