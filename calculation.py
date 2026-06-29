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
kpi = pd.DataFrame({

    "KPI":[
        "Total Spend",
        "Attributed Revenue",
        "Attributed Conversions",
        "ROAS",
        "CAC"
    ],

    "Value":[
        total_spend,
        attributed_revenue,
        attributed_conversions,
        round(roas,2),
        round(cac,2)
    ]

})

kpi

kpi.to_csv("week3_kpi_summary.csv", index=False)

print("KPI Summary Saved Successfully")

fact_table = df[[
    "user_id",
    "campaign",
    "channel",
    "event_timestamp_utc",
    "ad_spend",
    "conversion_value",
    "is_conversion"
]]

fact_table.head()

dim_campaign = df[[
    "campaign",
    "channel"
]].drop_duplicates()

dim_campaign.head()

dim_user = df[[
    "user_id",
    "device",
    "region"
]].drop_duplicates()

dim_user.head()

df["event_timestamp_utc"] = pd.to_datetime(df["event_timestamp_utc"])

dim_date = pd.DataFrame()

dim_date["Date"] = df["event_timestamp_utc"]

dim_date["Year"] = df["event_timestamp_utc"].dt.year
dim_date["Month"] = df["event_timestamp_utc"].dt.month
dim_date["Day"] = df["event_timestamp_utc"].dt.day

dim_date = dim_date.drop_duplicates()

dim_date.head()

fact_table.to_csv("fact_table.csv", index=False)

dim_campaign.to_csv("dim_campaign.csv", index=False)

dim_user.to_csv("dim_user.csv", index=False)

dim_date.to_csv("dim_date.csv", index=False)

print("All tables saved successfully!")

print("week3_kpi_summary.csv")
print("fact_table.csv")
print("dim_campaign.csv")
print("dim_user.csv")
print("dim_date.csv")



