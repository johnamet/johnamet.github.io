#!/usr/bin/env python3
"""
The scripts wrangles a dataset into different sets
and saves it as a csv file
"""
import pandas as pd
import sys
import matplotlib.pyplot as plt
from fpdf import FPDF

def wrangle_dataset(df):
    # select columns to keep
    columns_to_keep = ["Country/Region"] + list(df.columns)[4:]
    df = df[columns_to_keep]

    # List of the countries
    countries = df["Country/Region"].unique()

    for country in countries:
        print("----------------------------------------------------")
        print(f"Wrangling: {country}")
        print("----------------------------------------------------")
        country_df = df[df["Country/Region"] == country]
        # Transpose the data to have cases and time in columns for the country
        country_df = country_df.T

        # Reset index
        country_df.reset_index(inplace=True)

        # Set the column to the first row of the data
        country_df.columns = country_df.iloc[0]

        # rename the columns
        country_df.rename(columns={"Country/Region": "timestamp", f"{country_df.iloc[0][1]}": "Cases"}, inplace=True)

        # remove the first row
        country_df = country_df[1:]

        # Convert the timestamp to datatime datatype
        country_df["timestamp"] = pd.to_datetime(country_df["timestamp"])
        country_df["timestamp"] = country_df["timestamp"].dt.tz_localize("UTC")

        # Convert the Number of cases to int data type
        country_df["Cases"] = country_df["Cases"].astype(int)

        # drop rows where the cases are zero
        try:
            country_df.drop(country_df[country_df["Cases"] == 0].index, inplace=True)
        except ValueError:
            pass

        # set the index of the index of the dataset as timestamp
        country_df.set_index("timestamp", inplace=True)

        # Resample the data to monthly average cases
        try:
            country_df = country_df["Cases"].resample("M").mean().fillna(method="ffill").to_frame()
        except AttributeError:
            country_df = country_df["Cases"].resample("M").mean().fillna(method="ffill")

        # Round the number of cases to
        country_df["Cases"] = country_df["Cases"].apply(lambda x: round(x, 0))

        # Reset the index
        country_df.reset_index(inplace=True)
        # Convert the date time to Month Year format
        country_df["timestamp"] = country_df["timestamp"].dt.strftime("%b, %Y")
        country_df.set_index("timestamp", inplace=True)

        country_df = country_df[1:]
        print(country_df.head())
        # Save to csv
        # country_df.to_pdf(f"{country}.xlsx", index=True)

        # Save to pdf
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, f"{country} COVID 19 data (Monthly Average Cases)")

        pdf.cell(200, 10, txt="", ln=True)
        pdf.set_font("Arial", size=10)
        pdf.cell(200, 10, country_df.to_string(), ln=True, align="center")
        pdf.output(f"{country}.pdf")
        break


    print("-------------------------------------------------------------------")
    print("Wrangled")
    print("-------------------------------------------------------------------")


if __name__ == "__main__":
    file_path = sys.argv[1]

    df = pd.read_csv(file_path)

    wrangle_dataset(df)