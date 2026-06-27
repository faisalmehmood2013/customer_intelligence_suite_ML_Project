"""
Constants package - SAB fixed values yahan rakhte hain (file paths,
column names, model parameters ke defaults, etc.) taake hardcoded
values code mein bar-bar na likhni paren.

Jaisे "TARGET_COLUMN = 'churned'" ya
"TEST_SIZE = 0.2" jaisi values yahan define karenge, phir
har tier mein import karke use karenge. Isse agar value change
karni ho, EK jagah change karo, sab files mein automatically update ho jayegi.
"""

# -------- Shared Pipeline Constants --------
PIPELINE_NAME: str = "customer_intelligence_suite"
ARTIFACT_DIR: str = "artifacts"

# -------- Shared Data Constants --------
RAW_DATA_FILE_NAME: str = "online_retail_ii.csv"
TRAIN_TEST_SPLIT_RATIO: float = 0.2
RANDOM_STATE: int = 42

# -------- Shared Column Names (raw dataset se aate hain) --------
COL_INVOICE_NO: str = "InvoiceNo"
COL_STOCK_CODE: str = "StockCode"
COL_DESCRIPTION: str = "Description"
COL_QUANTITY: str = "Quantity"
COL_INVOICE_DATE: str = "InvoiceDate"
COL_UNIT_PRICE: str = "UnitPrice"
COL_CUSTOMER_ID: str = "CustomerID"
COL_COUNTRY: str = "Country"

# Tier-specific constants aap "tierX_xxx/constants.py" mein alag rakh
# sakte hain agar zaroorat pare (jaise CHURN_DAYS_THRESHOLD = 90)
