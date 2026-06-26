import pandas as pd

from google.colab import files

uploaded = files.upload()

df = pd.read_csv("multi_touch_attribution_dataset_cleaned .csv")

df.head()

print(df.columns)

total_spend = df["ad_spend"].sum()

print("Total Spend =", total_spend)

attributed_revenue = df["conversion_value"].sum()

print("Attributed Revenue =", attributed_revenue)

attributed_conversions = df["is_conversion"].sum()

print("Attributed Conversions =", attributed_conversions)

ROAS = attributed_revenue / total_spend

print("ROAS =", round(roas,2))

CAC = total_spend / attributed_conversions




