import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

print("AI-Powered Customer Churn Prediction & Customer Analytics Platform")

print("Current Folder:", os.getcwd())
print("Files:", os.listdir())

df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

print(df.head())
print(df.shape)