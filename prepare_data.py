import pandas as pd

# Define the column names based on the header in the image
columns = [
    'Account name', 'Ad Set Name', 'Ad name', 'Campaign name', 'Month',
    'Reach', 'Impressions', 'Frequency', 'Currency', 'Amount spent',
    'Attribution source', 'Purchases', 'Link clicks', 'CPC (cost per click)',
    'Clicks (all)', 'CPC (all)', 'CPM (cost per thousand impressions)',
    'Views', 'Reporting starts', 'Reporting ends'
]

# Create data from the screenshot
data = [
    ['Aion Wellness Verbisz', 'Leat Verbisz', 'Leat Verbisz', 'Leat Verbisz', '2024-12-01-2024-12-31', 86, 100, 1.1627907, 'USD', 27.52, '7-day click or 1-day view', None, 3, 9.17333333, 3, 9.17333333, 275.2, 100, '1/1/24', '12/31/24'],
    ['Aion Wellness Verbisz', 'Leat Verbisz', 'Leat Verbisz', 'Leat Verbisz', '2024-12-01-2024-12-31', 380, 493, 1.3947368, 'USD', 116.62, '7-day click or 1-day view', None, 19, 6.13789474, 22, 5.30090909, 236.55736, 493, '1/1/24', '12/31/24'],
    ['Aion Wellness Verbisz', 'Leat Verbisz', 'Leat Verbisz', 'Leat Verbisz', '2024-12-01-2024-12-31', 376, 493, 1.3111702, 'USD', 132.17, '7-day click or 1-day view', None, 12, 11.0141667, 23, 5.74652174, 268.09539, 493, '1/1/24', '12/31/24'],
    ['Aion Wellness Verbisz', 'Leat Verbisz', 'Leat Verbisz', 'Wet Verbisz', '2024-12-01-2024-12-31', 63, 73, 1.1587302, 'USD', 13.17, '7-day click or 1-day view', None, 4, 3.2925, 3, 4.39, 180.41096, 73, '1/1/24', '12/31/24'],
    ['Aion Wellness Verbisz', 'Leat Verbisz', 'Leat Verbisz', 'Wet Verbisz', '2024-12-01-2024-12-31', 725, 976, 1.3462069, 'USD', 186.44, '7-day click or 1-day view', None, 29, 6.42896552, 40, 4.661, 191.02459, 976, '1/1/24', '12/31/24']
]

# Create DataFrame
df = pd.DataFrame(data, columns=columns)

# Save to CSV
df.to_csv('ad_data.csv', index=False)
print("Data saved to ad_data.csv") 