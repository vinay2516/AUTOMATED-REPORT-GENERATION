import csv
from statistics import mean
from fpdf import FPDF

# Read and analyze data
def read_and_analyze_data(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = []
        for row in reader:
            name = row['Name']
            sales = int(row['Sales'])
            data.append({'name': name, 'sales': sales})
    
    total_sales = sum(d['sales'] for d in data)
    avg_sales = mean(d['sales'] for d in data)
    max_sale = max(data, key=lambda x: x['sales'])
    min_sale = min(data, key=lambda x: x['sales'])

    return data, total_sales, avg_sales, max_sale, min_sale

# Generate PDF report
def generate_pdf_report(data, total, average, max_sale, min_sale, filename='report.pdf'):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Sales Report", ln=True, align='C')
    pdf.ln(10)

    # Summary
    pdf.set_font("Arial", size=11)
    pdf.cell(200, 10, f"Total Sales: {total}", ln=True)
    pdf.cell(200, 10, f"Average Sales: {average:.2f}", ln=True)
    pdf.cell(200, 10, f"Highest Sale: {max_sale['name']} - {max_sale['sales']}", ln=True)
    pdf.cell(200, 10, f"Lowest Sale: {min_sale['name']} - {min_sale['sales']}", ln=True)
    pdf.ln(10)

    # Table header
    pdf.set_font("Arial", 'B', 11)
    pdf.cell(100, 10, "Name", 1)
    pdf.cell(50, 10, "Sales", 1)
    pdf.ln()

    # Table rows
    pdf.set_font("Arial", '', 11)
    for entry in data:
        pdf.cell(100, 10, entry['name'], 1)
        pdf.cell(50, 10, str(entry['sales']), 1)
        pdf.ln()

    pdf.output(filename)
    print(f"PDF report generated: {filename}")

if __name__ == "__main__":
    data, total, avg, max_sale, min_sale = read_and_analyze_data("data.csv")
    generate_pdf_report(data, total, avg, max_sale, min_sale)
