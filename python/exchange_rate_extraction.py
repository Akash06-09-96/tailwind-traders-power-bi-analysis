"""
exchange_rate_extraction.py

Prepares foreign exchange-rate data in a tabular structure so it can be
imported into the Power BI data model as the 'Exchange Data' table.

Tailwind Traders operates across five markets (UK, USA, Australia, France,
UAE), so transactions were standardized into USD before analysis.
"""

import pandas as pd

exchange_data = {
    "Currency": ["USD", "GBP", "EUR", "AED", "AUD"],
    "Exchange Rate": [1.00, 0.75, 0.85, 3.67, 1.30]
}

exchange_df = pd.DataFrame(exchange_data)

print(exchange_df)
