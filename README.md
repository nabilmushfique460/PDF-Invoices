# 📄 Automated Excel-to-PDF Invoice Generator (Python)

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Automation](https://img.shields.io/badge/Workflow-Automation-blueviolet?style=for-the-badge)](#)

A high-performance Python automation utility that dynamically ingests raw tabular invoice data from Microsoft Excel spreadsheets (`.xlsx`) and renders polished, print-ready, professional corporate PDF invoices in bulk.

---

## 🎯 Business Problem Solved
Small businesses, e-commerce stores, and accounting departments often waste hours manually formatting and exporting invoices. This automation script processes hundreds of client invoices in seconds with zero manual intervention.

---

## ✨ Features
- **Batch Processing:** Scans any directory of `.xlsx` invoice sheets and transforms each file into a structured PDF.
- **Dynamic Table Formatting:** Computes sub-totals, items purchased, unit costs, and overall totals dynamically.
- **Custom Corporate Branding:** Embed your company logo, typography, invoice numbering, and issuance dates automatically.
- **Modular & Extensible:** Easily customize layout dimensions, fonts, currency symbols, and multi-page tables using `fpdf2`.

---

## 📁 Project Structure
```text
PDF-Invoices/
├── invoices/              # Input directory for Excel spreadsheets (.xlsx)
│   ├── 10001-2026.07.15.xlsx
│   └── 10002-2026.07.18.xlsx
├── PDFs/                  # Output directory where generated invoices land
│   ├── 10001-2026.07.15.pdf
│   └── 10002-2026.07.18.pdf
├── main.py                # Core PDF generator & automation script
├── requirements.txt       # Project dependencies
└── README.md              # Documentation
```

---

## 🚀 Quickstart Guide

### 1. Clone the Repository
```bash
git clone https://github.com/nabilmushfique460/PDF-Invoices.git
cd PDF-Invoices
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Automation
Place your `.xlsx` files into the `invoices/` directory following the naming pattern `[invoice_number]-[date].xlsx` (e.g. `10001-2026.11.08.xlsx`) and execute:
```bash
python main.py
```
Your compiled invoices will immediately appear inside the `PDFs/` folder!

---

## 📊 Expected Excel Schema (`Sheet 1`)
| product_id | product_name | amount_purchased | price_per_unit | total_price |
|:---:|:---|:---:|:---:|:---:|
| 1 | Professional Web Audit | 1 | 250 | 250 |
| 2 | Python Automation Script | 2 | 100 | 200 |

---

## 💼 Commercial Services & Inquiries
Need this tailored for your ERP, CRM (Stripe, QuickBooks, Xero), or web dashboard? 
Feel free to reach out for custom automation pipelines or freelance work:

- **Developer:** S.M. Nabil Mushfique
- **Email:** [nabilmushfique460@gmail.com](mailto:nabilmushfique460@gmail.com)
- **Fiverr / Upwork:** Available for direct contracting & custom Python automations.
