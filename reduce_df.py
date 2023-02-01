import pandas as pd

df = pd.read_csv("C:\\Users\\richa\\OneDrive\\Bureau\\Formation GEPP\\Python_training_perso\\test_files\\LA_Crime_clean.csv")

df= df.sample(100000)

df.to_csv("LA_Crime_clean.csv")