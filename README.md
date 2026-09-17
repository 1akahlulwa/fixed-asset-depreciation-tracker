# fixed-asset-depreciation-tracker
Small tool that models fixed asset depreciation schedules (straight-line, reducing balance) from a sample dataset.
The data in "assets.csv" is fictional as this type of information is usually not disclosed to the public.
Assumes that Asset_Name,Purchase_Date,Purchase_Cost,Useful_Life,Salvage_Value are known before making calculations.
The first table adds the annual deprecition values for each asset to the initial table from "assets.csv"
The second table displays the value of the assets over time using the deminishing balance method
The third table displays the depriciation amounts over time using the deminishing balance method