# 🌟 Synthetic Data Generator

This project is a **Streamlit app** that generates **synthetic data** using the **OpenAI GPT-4 API**. It allows users to specify parameters such as the number of rows, starting date, and subcategories, and provides the output as a downloadable Excel file.

---

## 🚀 Features

- **Customizable Synthetic Data**:
  - **State**: Random U.S. states.
  - **County**: Real counties corresponding to states.
  - **Value**: Random numerical data with a variance close to 1.
  - **Subcategory**: User-defined categories (e.g., Health, Education, Finance).
  - **Date**: Incremental dates starting from a user-defined start date.

- **Batch Processing**: Efficiently handles large datasets by batching API requests.
- **User-Friendly Interface**: Built with **Streamlit** for ease of use.
- **Downloadable Output**: Export the generated data to Excel.

---

## 🛠️ How It Works

### 🧠 **Core Functions**

1. **`extract_json_part(response_text)`**
   - Extracts JSON data from the API response using regex.
   - Handles potential errors in JSON decoding.

2. **`generate_synthetic_data_batch(start_date, batch_size, subcategories)`**
   - Creates a batch of synthetic data with incremental dates.
   - Sends a structured prompt to the OpenAI GPT-4 API.
   - Returns a DataFrame of the generated data.

3. **`generate_large_synthetic_data(total_rows, batch_size, start_date, subcategories, delay=5)`**
   - Splits the total rows into manageable batches.
   - Sends batch requests to the API and combines the results.
   - Adds a delay between API calls to avoid rate limits.

---

## 🎛️ **Streamlit App**

- **Inputs**:
  - **Number of Rows**: Choose between 10 and 1000 rows.
  - **Start Date**: Enter the start date in MM/DD/YYYY format.
  - **Subcategories**: Provide a comma-separated list of categories (e.g., `Health, Education`).

- **Outputs**:
  - Displays the generated synthetic data in a table.
  - Provides a button to download the data as an Excel file.

---

## 🧑‍💻 **Setup Instructions**

### **Prerequisites**
- Python 3.8 or higher
- OpenAI API key
- Streamlit
- dotenv for environment variables

### **Steps to Run the App**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-username>/synthetic-data-generator.git
   cd synthetic-data-generator
2. **Install dependencies**:
   pip install -r requirements.txt

3. **Add your OpenAI API key**:
   OPENAI_API=your-api-key in .env file or secrets.toml file

4. **Run the app**
   streamlit run app.py
