# Data Analysis With Pandas – Python Project

## Project Roadmap

### Step 1: What is Pandas?

Pandas is a powerful Python library for data manipulation and analysis, built on top of NumPy.

### Step 2: Starting With Pandas and IPython

Install Pandas and IPython:

```bash
pip install pandas ipython
```

Start IPython shell or use Jupyter for an interactive experience:

```bash
ipython
```

### Step 3: Working with Jupyter Notebooks

Install Jupyter and launch it:

```bash
pip install notebook
jupyter notebook
```

### Step 4: Important Jupyter Notebook Commands

- `Shift + Enter`: Run a cell.
- `A`/`B`: Add a cell Above/Below.
- `DD`: Delete a cell.
- `%matplotlib inline`: Display plots in the notebook.

### Step 5: Working with CSV, Excel, TXT, and JSON Files

```python
import pandas as pd

# CSV
df_csv = pd.read_csv("data.csv")

# Excel
df_excel = pd.read_excel("data.xlsx")

# TXT (tab-delimited)
df_txt = pd.read_csv("data.txt", delimiter="\t")

# JSON
df_json = pd.read_json("data.json")
```

### Step 6: Working with API Response

```python
import requests

response = requests.get("https://api.example.com/data")
data = response.json()
df_api = pd.DataFrame(data)
```

### Step 7: Indexing and Slicing Dataframe Tables

```python
df.head()         # First 5 rows
df.tail()         # Last 5 rows
df["column_name"] # Access column
df.iloc[0]        # Access row by index
df.loc[0]         # Access row by label
```

### Step 8: Deleting Columns and Rows

```python
df.drop("column_name", axis=1, inplace=True)  # Delete column
df.drop(index=0, inplace=True)                # Delete row
```

### Step 9: Adding and Updating New Columns and Rows

```python
df["new_column"] = df["column1"] + df["column2"]  # New column
df.loc[len(df.index)] = ["val1", "val2", "val3"]  # Add new row

