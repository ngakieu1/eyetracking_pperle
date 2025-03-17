import pandas as pd

df = pd.read_csv("./data/p00/data.csv")
#print(df.head())  # Xem 5 dòng đầu tiên
#print(df.columns)  # Xem danh sách cột
print(df.columns.tolist())
