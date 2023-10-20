import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
from matplotlib.backends.backend_pdf import PdfPages
from fpdf import FPDF

# Read the CSV file into a pandas DataFrame
csv_file = './YOUR CSV FILE.csv'  # Replace with the path to your CSV file
df = pd.read_csv(csv_file)

# Define a function to convert grain size in mm to Phi


def mm_to_phi(mm):
    return -1 * np.log2(mm)


# Apply the mm_to_phi function to the 'Grain_Size_mm' column and create a new 'Phi' column
df['Phi'] = df['Grain_Size_mm'].apply(mm_to_phi)

# Calculate the total weight
total_weight = df['Weight_gram'].sum()

# Calculate the weight percentage of each grain size
df['Weight_Percentage'] = (df['Weight_gram'] / total_weight) * 100

# Calculate the cumulative weight percentage
df['Cumulative_Weight_Percentage'] = df['Weight_Percentage'].cumsum()

# Format the table to display numbers with two decimal places
df['Weight_gram'] = df['Weight_gram'].apply(lambda x: f"{x:.2f}")
df['Phi'] = df['Phi'].apply(lambda x: f"{x:.2f}")
df['Weight_Percentage'] = df['Weight_Percentage'].apply(lambda x: f"{x:.2f}")
df['Cumulative_Weight_Percentage'] = df['Cumulative_Weight_Percentage'].apply(
    lambda x: f"{x:.2f}")

# Create a table to show the calculations
calculation_table = tabulate(
    df, headers='keys', tablefmt='pretty', showindex=False)

# Print the table
print("Calculations:")
print(calculation_table)

# Save the table as a PDF


class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Grain Size Analysis', align='C', ln=True)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')


pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, calculation_table)
pdf.output("grain_size_calculation.pdf")

# Plot a histogram of grain size in Phi with weight percentage
plt.figure(figsize=(10, 6))
plt.bar(df['Phi'].astype(float), df['Weight_Percentage'].astype(
    float), width=0.5, align='center', label='Weight Percentage')
plt.xlabel('Grain Size (Phi)')
plt.ylabel('Weight Percentage')
plt.title('Grain Size Distribution in Phi Scale')
plt.legend()
plt.grid(True)

# Save the plot as a PDF file
with PdfPages('grain_size_distribution.pdf') as pdf:
    pdf.savefig()
    plt.close()

# Plot the cumulative weight percentage with each grain size
plt.figure(figsize=(10, 6))
plt.plot(df['Phi'].astype(float), df['Cumulative_Weight_Percentage'].astype(
    float), marker='o', linestyle='-', color='b')
plt.xlabel('Grain Size (Phi)')
plt.ylabel('Cumulative Weight Percentage')
plt.title('Cumulative Grain Size Distribution in Phi Scale')
plt.grid(True)

# Save the plot as a PDF file
with PdfPages('cumulative_grain_size_distribution.pdf') as pdf:
    pdf.savefig()
    plt.close()
