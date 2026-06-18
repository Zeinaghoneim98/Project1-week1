
import pandas as pd

# Step 1: Load Dataset
df = pd.read_excel(r"C:\Users\User\Downloads\Dataset for Data Analytics.xlsx")

print("Dataset loaded successfully.\n")

# Step 2: Display basic information
print("First 5 rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nShape before cleaning:")
print(df.shape)

# Step 3: Identify Missing Values
print("\nMissing values in each column:")
print(df.isnull().sum())


# Handle missing CouponCode values
if "CouponCode" in df.columns:

    df["CouponCode"] = df["CouponCode"].fillna("No Coupon")
    print("\nMissing CouponCode values handled.")

# Step 4: Remove duplicate rows
duplicate_rows = df.duplicated().sum()
print("\nNumber of duplicate rows found:",
      duplicate_rows)
df = df.drop_duplicates()
print("Duplicate rows removed.")

# Step 5: Remove duplicate IDs
if "OrderID" in df.columns:

    duplicate_ids = df["OrderID"].duplicated().sum()

    print("\nDuplicate IDs before cleaning:",
          duplicate_ids)

    df = df.drop_duplicates(
        subset=["OrderID"]
    )
    duplicate_ids_after = (
        df["OrderID"]
        .duplicated()
        .sum()
    )

    print("Duplicate IDs after cleaning:",
          duplicate_ids_after)

# Step 6: Correct Date Format
if "Date" in df.columns:
    # convert mixed formats
    df["Date"] = pd.to_datetime(
        df["Date"],
        errors="coerce"
    )
    # convert to one standard format
    df["Date"] = (
        df["Date"]
        .dt.strftime("%Y-%m-%d")
    )

    print("\nDate format standardized.")

# Step 7: Final Verification

print("\nFinal checking")

print(
    "Remaining Missing Values:"
)

print(df.isnull().sum())


print(
    "\nDuplicate Rows Remaining:",
    df.duplicated().sum()
)


if "OrderID" in df.columns:

    print(
        "Duplicate IDs Remaining:",
        df["OrderID"]
        .duplicated()
        .sum()
    )
# count invalid dates

if "Date" in df.columns:

    invalid_dates = (
        df["Date"]
        .isnull()
        .sum()
    )

    print(
        "Incorrect Date Formats:",
        invalid_dates
    )

print("\nCleaning completed successfully.")

# Step 8: Save cleaned dataset
df.to_excel(
    "cleaned_dataset.xlsx",
    index=False
)
print(
    "\nCleaned dataset saved successfully."
) 