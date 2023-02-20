import pandas as pd

df = pd.read_excel("文具商品採購清單.xlsx",
                        engine="openpyxl")
pivot_products = df.pivot_table(columns=["分類","項目"],
                                values="數量",
                                aggfunc="sum")
print(pivot_products)
pivot_products.to_excel("文具商品採購清單樞紐分析表2.xlsx",
                        engine="openpyxl")
