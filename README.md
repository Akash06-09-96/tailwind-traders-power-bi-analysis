# Tailwind Traders — Sales & Profitability Analysis (Power BI)

**Author:** Akash Kaliramna
**Tools Used:** Microsoft Power BI Desktop · Power Query · DAX · Python (Pandas) · Power BI Service

---

## Project Overview

Tailwind Traders is a fictional global retail company selling products across multiple countries and product categories. This project is a capstone case study demonstrating an end-to-end Business Intelligence solution built in Microsoft Power BI, transforming raw sales, purchase, country, and currency data into actionable business insights.

The project covers the complete analytics workflow:

```
Raw Data → Data Extraction → Data Cleaning → Data Transformation →
Data Modeling → DAX Calculations → Data Analysis → Interactive Reports →
Power BI Service → Executive Dashboard
```

The final solution contains two interactive report pages — **Sales Performance Overview** and **Profit Performance Overview** — published to Power BI Service, where selected KPIs and visuals were combined into an **Executive Dashboard**.

<p align="center">
  <img src="./screenshots/sales-performance-overview.png" alt="Sales Performance Overview report page" width="800"/>
</p>

---

## Business Task

> **Can a single Power BI solution give stakeholders a consolidated view of sales and profitability performance across Tailwind Traders' international markets?**

Tailwind Traders needed a consolidated reporting solution to understand overall sales and profitability performance, revenue by product, geographic differences in sales and margin, customer loyalty patterns, product demand, and sales trends over time. The goal was not simply to visualize data, but to build an analytical solution that lets decision-makers quickly identify performance drivers, trends, and geographic patterns.

---

## 📂 Repository Structure

```
tailwind-traders-power-bi-analysis/
│
├── README.md                          ← You are here — project overview & findings
├── Case_Study_Complete.docx           ← Full detailed report (all phases)
├── Tailwind-Traders-Power-BI.pbix     ← Power BI Desktop file
│
├── dax/
│   ├── 01_calendar_table.dax          ← Calculated CalendarTable for time intelligence
│   ├── 02_sales_in_usd_table.dax      ← Calculated 'Sales in USD' table (currency standardization)
│   ├── 03_profit_measures.dax         ← Profit, Yearly/Quarterly/YTD margin measures
│   └── 04_additional_measures.dax     ← Median Sales and supporting KPI measures
│
├── python/
│   └── exchange_rate_extraction.py    ← Pandas script preparing exchange-rate lookup data
│
├── screenshots/
│   ├── sales-performance-overview.png
│   ├── profit-performance-overview.png
│   └── executive-dashboard.png
│
├── data/
│   └── README.md                      ← Notes on the (excluded) raw datasets
│
└── documentation/
    └── project-notes.md
```

---

## Dataset

The project integrates multiple business datasets rather than a single flat table:

| Dataset | Description |
|---|---|
| **Sales** | 55 transaction-level records, 22 fields (Order ID, Product Name, Gross Product Price, Quantity Purchased, Country ID, Customer ID, Loyalty Points, etc.) |
| **Purchases** | Transaction and purchase-date information, used for time-based analysis (quarterly, YTD) |
| **Countries** | Geographic lookup covering 5 markets: UK, USA, Australia, France, UAE |
| **Exchange Data** | Currency exchange rates used to standardize revenue into USD |

**Exchange rates used:**

| Currency | Exchange Rate |
|---|---|
| USD | 1.00 |
| GBP | 0.75 |
| EUR | 0.85 |
| AED | 3.67 |
| AUD | 1.30 |

---

## Tools & Workflow

| Phase | Tool | Purpose |
|---|---|---|
| Extract | Python · Pandas | Preparing exchange-rate lookup data in a tabular structure |
| Prepare | Power Query | Cleaning and transforming Sales, Purchases, Countries, Exchange Data |
| Model | Power BI Desktop | Building relationships, Calendar table, currency standardization |
| Analyze | DAX | Profit, margin, YTD/quarterly time-intelligence measures |
| Share | Power BI Desktop | Two interactive report pages |
| Publish | Power BI Service | Publishing the report and building the Executive Dashboard |

**Why Python?** Exchange-rate information wasn't already available in the main source system, so Python and Pandas were used to prepare it as a lookup table before loading it into the Power BI model — an example of incorporating an external data-processing step into a BI workflow.

---

## Data Modeling & DAX

A structured data model connected `Sales → Purchases → Countries → Exchange Data → Calendar` using business keys (Order ID, Country ID, Exchange ID, Purchase Date). A dedicated `CalendarTable` was added to support time intelligence, and a calculated `Sales in USD` table standardized international transactions into a single reporting currency.

Key DAX measures (full definitions in [`/dax`](./dax)):

- **Profit in USD** — Net Revenue USD minus Total Tax USD
- **Yearly Profit Margin** — `DIVIDE()` of Profit over Net Revenue, for safe divide-by-zero handling
- **Quarterly Profit** — `CALCULATE()` + `DATESQTD()` for cumulative quarter-to-date profit
- **YTD Profit** — `TOTALYTD()` for cumulative year-to-date profit
- **Median Sales** — `MEDIAN()` of Gross Revenue USD, less sensitive to outlier transactions than an average

---

## Key Findings

### Finding 1 — UAE Has the Highest Typical Sales Value

| Country | Median Sales |
|---|---|
| **UAE** | **~$680.79** |
| Australia | $234.00 |
| USA | $230.00 |
| France | $221.85 |
| UK | $144.00 |

UAE transactions tend to involve significantly higher-value purchases than every other market.

### Finding 2 — Profitability Is Extremely Consistent Across Countries

| Country | Profit Margin |
|---|---|
| Australia | ~62.37% |
| UAE | ~62.37% |
| UK | ~62.37% |
| USA | ~62.17% |
| France | ~62.12% |

Margins range only from ~62.12% to ~62.37% — no single market is materially underperforming.

### Finding 3 — Product Revenue Is Concentrated Among a Few Leading Products

The **Modular Sofa Set** generated the highest net revenue at approximately **$928.36**, well ahead of the rest of the top 10:

| Rank | Product | Net Revenue (USD) |
|---|---|---|
| 1 | Modular Sofa Set | $928.36 |
| 2 | Motion Sensor Alarm | $716.75 |
| 3 | Bamboo Plant Pot | $709.92 |
| 4 | LED Garden Lights | $682.62 |
| 5 | Organic Potting Soil | $583.64 |
| 6 | Vintage Wall Mirror | $580.23 |
| 7 | Luxury Chandelier | $471.01 |
| 8 | Electric Screwdriver | $409.57 |
| 9 | Brass Coat Rack | $398.97 |
| 10 | Velvet Cushion Cover | $374.79 |

### Finding 4 — Sales and Profitability Are Not Constant Over Time

Profit margins stayed close to ~62% for most periods, but the trend visuals show temporary declines — highlighting the value of monitoring performance over time rather than relying on annual aggregates alone.

---

## 📊 Report Pages & Executive Dashboard

**Sales Performance Overview** — KPI cards (Total Stock 14K, Units Sold 152, Median Sales $222.50), Customer Loyalty Points by Country, Median Sales by Country, Top-Selling Products by Units Sold, Median Sales Trend, and a Country slicer for interactivity.

<p align="center">
  <img src="./screenshots/profit-performance-overview.png" alt="Profit Performance Overview report page" width="800"/>
</p>

**Profit Performance Overview** — KPI cards (YTD Profit Margin 62.27%, Gross Revenue $14.97K, Net Revenue $13.89K), Top Products by Net Revenue (Top 10 filter), Yearly Profit Margin by Country, Profit Margin Trend, and a Year/Quarter/Month slicer for time-based filtering.

<p align="center">
  <img src="./screenshots/executive-dashboard.png" alt="Executive Dashboard published to Power BI Service" width="800"/>
</p>

The **Executive Dashboard**, published to Power BI Service, pins the most important visuals from both pages into a single view: Executive KPIs (Gross Revenue, Net Revenue, Units Sold, YTD Profit Margin), Geographic Performance (Customer Loyalty Points by Country, Yearly Profit Margin by Country), Product Performance (Top Products by Net Revenue, Top-Selling Products by Units Sold), and Trend Analysis (Median Sales Trend, Profit Margin Trend).

---

## Top Recommendations

**1. Prioritize High-Revenue Products** — Use net-revenue ranking (not just units sold) to guide inventory, placement, and promotional decisions, since the highest-volume product isn't always the highest-revenue product.

**2. Investigate UAE Customer Behavior** — Dig into product mix, average quantity purchased, and pricing to understand why UAE transaction values are so much higher, and whether that pattern is transferable to other markets.

**3. Monitor Geographic Margin Stability** — Track the currently narrow country-margin range over time, since divergence could signal changes in pricing, tax, currency effects, or product mix.

**4. Investigate Temporary Profit-Margin Declines** — Drill into the specific periods where the trend dipped below ~62% to identify whether product mix, lower-value transactions, or currency movements were the cause.

---

## Challenges & Solutions

| Challenge | Solution |
|---|---|
| Exchange rates with decimals were initially misread due to decimal-format differences | Reviewed and corrected data types/decimal formatting before use in financial calculations |
| Transactions across countries used different currencies and weren't directly comparable | Built a currency-conversion layer (`Sales in USD`) standardizing all financial calculations into USD |
| A custom lollipop visual for country profit-margin comparison required a paid license in Power BI Service | Replaced it with a native Power BI column chart, keeping the project free of paid third-party visual dependencies |

---

## Skills Demonstrated

Power BI Desktop & Service · Power Query · DAX · Data cleaning & transformation · Data modeling & relationships · Calendar tables & time intelligence · Currency conversion · Python & Pandas · KPI development · Sales & profitability analysis · Geographic & trend analysis · Top-N analysis · Interactive slicers · Dashboard design · Business storytelling

---

## Full Report

For the complete analysis including all methodology details, DAX walkthroughs, and design decisions, see [`Case_Study_Complete.docx`](./Case_Study_Complete.docx).

---

## 👤 About

**Akash Kaliramna**
Data Analyst | Power BI · SQL · Python · Excel · Tableau
