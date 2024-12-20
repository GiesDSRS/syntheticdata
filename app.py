# -*- coding: utf-8 -*-
<<<<<<< HEAD
"""app
=======
"""appnew
>>>>>>> 7d850ab (Add Streamlit app for synthetic data generator)

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KJwbu3GiSFgcLRRyi5AEN2e08w5Fl3Ma

**Using OpenAI API Key to generate synthetic data**
"""

import openai
import time
from datetime import datetime, timedelta
import json
import re
import os
import io
from dotenv import load_dotenv
import streamlit as st

# Load environment variables
load_dotenv()

# Set OpenAI API key
openai.api_key = st.secrets.get("OPENAI_API") or os.getenv("OPENAI_API")

if not openai.api_key:
    st.error("OpenAI API key is not set. Please check Streamlit secrets or .env file.")
    st.stop()

<<<<<<< HEAD
=======
""" STATE | COUNTY | VALUE | SUBCATEGORY Data"""

>>>>>>> 7d850ab (Add Streamlit app for synthetic data generator)
import pandas as pd
import json
import re
import time
from datetime import datetime, timedelta

def extract_json_part(response_text):
    # Regular expression to match JSON arrays
    json_match = re.search(r'\[\s*\{.*?\}\s*\]', response_text, re.DOTALL)
    if json_match:
        json_data = json_match.group(0)  # Extract the JSON part
        try:
            return json.loads(json_data)  # Parse JSON into Python object
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None
    else:
        print("No valid JSON array found in the response.")
        return None

def generate_synthetic_data_batch(start_date, batch_size, subcategories):
    """
    Generates a batch of synthetic data using the API.
    Args:
        start_date (datetime): Starting date for the batch.
        batch_size (int): Number of rows in the batch.
        subcategories (list): List of subcategories to include.
    Returns:
        DataFrame: A DataFrame containing the generated data.
    """
    # Generate date range as strings
    date_list = [(start_date + timedelta(days=30 * i)).strftime("%m/%d/%Y") for i in range(batch_size)]
<<<<<<< HEAD
    
=======

>>>>>>> 7d850ab (Add Streamlit app for synthetic data generator)
    # Define the prompt
    prompt = f"""Generate synthetic data of {batch_size} observations with the following columns, Do not truncate the data, give complete data.:
    - State: Only U.S. states.
    - County: Real counties within the states.
    - Value: Random numerical data with a variance close to 1.
    - Subcategory: {subcategories}
    - Date: The dates should increment by 1 month starting from {date_list[0]}.

    Please output the data as a JSON array with each row as an object. The JSON format should look like this:
    [
        {{"state": "State Name", "county": "County Name", "value": some_number, "subcategory": "Some Category", "date": "some date"}},
        ...
    ]"""

    # Make the API call
    response = openai.chat.completions.create(
        model= "gpt-4",
        messages=[
            {"role": "system", "content": "You are a data analyst expert and will provide JSON formatted data"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=4000,
        temperature=0
    )

    # Extract and parse the response content
    response_text = response.choices[0].message.content
    data = extract_json_part(response_text)
    return pd.DataFrame(data) if data else None

def generate_large_synthetic_data(total_rows, batch_size, start_date, subcategories, delay=5):
    """
    Generates a large dataset by batching API requests.
    Args:
        total_rows (int): Total number of rows to generate.
        batch_size (int): Number of rows in each batch.
        start_date (str): Starting date in MM/DD/YYYY format.
        subcategories (list): List of subcategories to include.
        delay (int): Delay in seconds between API calls.
    Returns:
        DataFrame: A DataFrame containing the generated data.
    """
    start_date = datetime.strptime(start_date, "%m/%d/%Y")
    all_data = []

    for i in range(0, total_rows, batch_size):
        st.info(f"Generating batch {i // batch_size + 1}...")
        batch_data = generate_synthetic_data_batch(start_date, batch_size, subcategories)
        if batch_data is not None:
            all_data.append(batch_data)
        else:
            st.warning(f"Batch {i // batch_size + 1} failed. Skipping...")
        start_date += timedelta(days=30 * batch_size)

        time.sleep(delay)
<<<<<<< HEAD
        
    return pd.concat(all_data, ignore_index=True) if all_data else None

=======

    return pd.concat(all_data, ignore_index=True) if all_data else None

# Example usage
#subcategories = ["Health", "Education", "Finance"]
#total_rows = 200
#batch_size = 50
#start_date = "01/01/2010"

#final_data = generate_large_synthetic_data(total_rows, batch_size, start_date, subcategories)

#if final_data is not None:
    # Save to Excel
    #final_data.to_excel("synthetic_data.xlsx", index=False)
    #print("Synthetic data saved to synthetic_data.xlsx")
#else:
    #print("Failed to generate synthetic data.")

>>>>>>> 7d850ab (Add Streamlit app for synthetic data generator)
# Streamlit App
st.title("Synthetic Data Generator")

# Input fields
num_rows = st.number_input("Number of rows", min_value=10, max_value=1000, value=100, key="num_rows")
start_date = st.text_input("Start Date (MM/DD/YYYY)", "01/01/2020", key="start_date")
subcategories = st.text_area(
    "Subcategories (comma-separated, e.g., Health, Education, Finance)",
    "Health, Education, Finance",
    key="subcategories",
)

if st.button("Generate Data", key="generate_button"):
    with st.spinner("Generating synthetic data..."):
        try:
            subcategories_list = [s.strip() for s in subcategories.split(",")]
            start_date_parsed = datetime.strptime(start_date, "%m/%d/%Y")

            df = generate_large_synthetic_data(
                total_rows=num_rows,
                batch_size=50,  # Adjust batch size as needed
                start_date=start_date,
                subcategories=subcategories_list,
                delay=2
            )

            if df is not None:
                # Display data
                st.write("Generated Data:")
                st.dataframe(df)

                # Convert to Excel and provide download button
                output = io.BytesIO()
                with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                    df.to_excel(writer, index=False, sheet_name='Synthetic Data')
                output.seek(0)

                st.download_button(
                    label="Download data as Excel",
                    data=output,
                    file_name="synthetic_data.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
            else:
                st.error("Failed to generate data. Please try again.")
        except Exception as e:
<<<<<<< HEAD
            st.error(f"An error occurred: {e}")
=======
            st.error(f"An error occurred: {e}")
>>>>>>> 7d850ab (Add Streamlit app for synthetic data generator)
