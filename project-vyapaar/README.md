# Project Vyapaar: Business Data Treasure Hunt

Team submission for the Project Vyapaar business analytics hackathon (BBA, 3rd year).

## What's in this folder

| File / folder | What it is |
|---|---|
| `colab/Vyapaar_Full_Analysis.ipynb` | **Simple version of the full analysis, ready for Google Colab.** Same findings, basic pandas code. This is the one to submit |
| `colab/01_Data_Cleaning.ipynb` … `04_Hidden_Mystery_and_Marketing.ipynb` | The same work split into 4 short notebooks, one per team role. Each one runs on its own |
| `Vyapaar_Analysis.ipynb` | Longer, more detailed version of the analysis (reference) |
| `Management_Summary.md` | One-page summary: 3 findings, hidden mystery, actions, plus a 3-minute pitch script |
| `charts/` | The 5 charts as interactive Plotly HTML and as PNG images |
| `data/` | Raw data we were given (orders, products, reviews, marketing) and the brief |
| `data/cleaned/vyapaar_master_clean.csv` | Cleaned orders + products + reviews in one table |
| `data/cleaned/cleaning_log.csv` | Every cleaning decision as Problem → Action → Reason |

## The 5 charts

| # | Chart | Business question it answers |
|---|---|---|
| 1 | `chart1_category_revenue_vs_profit` | Does high revenue mean high profit? (No, Electronics doesn't) |
| 2 | `chart2_discount_vs_margin` | Are discounts helping? (Margin falls and volume doesn't rise) |
| 3 | `chart3_east_region_service` | Where is customer experience breaking? (East delivery) |
| 4 | `chart4_profit_waterfall` | Where does the money go? (Marketing uses 98% of gross profit) |
| 5 | `chart5_campaign_tag_timing` | Can we trust campaign attribution? (Only 11% of tagged orders fall inside campaign dates) |

## How to run on Google Colab
1. Go to [colab.research.google.com](https://colab.research.google.com) → **File → Upload notebook** → choose a notebook from the `colab/` folder.
2. Click **Runtime → Run all**.
3. When the **Choose Files** button appears (under the "Load the data" step), select `orders.csv`, `products.csv`, `reviews.csv` and `marketing.csv` from the `data/` folder.

Colab already has pandas and plotly, so there's nothing to install. Charts are interactive; use the camera icon on a chart to download it as a PNG.

## How to run on your laptop (Jupyter)
```bash
pip install pandas numpy plotly jupyter kaleido   # kaleido is only needed to save PNGs
jupyter notebook Vyapaar_Analysis.ipynb          # then: Kernel -> Restart & Run All
```
Run it from this folder so the `data/` path works. The notebook rebuilds `charts/` and `data/cleaned/` every time it runs.

**Note:** `customers.csv` and `delivery.csv` were not in our data folder, so the notebook uses proxies for them (explained in Stage 1). If you add them to `data/`, the first cell will show them as "found".
