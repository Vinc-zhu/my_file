"""
"""
import pandas as pd

## Export Curves
shock_curve = []
base_curve  = []
shock_curve = pd.DataFrame(shock_curve)
base_curve  = pd.DataFrame(base_curve)

for i in range(1, 361, 1):
    shock_curve = shock_curve.append([shocked_irCurve_GBP_up.zeroRate(i/12)])
    base_curve = base_curve.append([base_irCurve_GBP.zeroRate(i/12)])

shock_curve = shock_curve.reset_index(drop=True)
shock_curve.columns = ['Shock']

base_curve = base_curve.reset_index(drop=True)    
base_curve.columns = ['Base']

curve = shock_curve.join(base_curve)

base_asset['Category'].unique()