import pandas as pd
import matplotlib.pyplot as plt

assets_df = pd.read_csv('assets.csv')

assets_df['Annual_Depreciation'] = (assets_df['Purchase_Cost'] - assets_df['Salvage_Value'])/assets_df['Useful_Life']

#print(assets_df)

#print(max((assets_df['Useful_Life'])))

assets_df = assets_df.reset_index() #matches indices with number of rows

def straight_line(cost, salvage, useful_life):
    schedule = []
    depr_amount = (cost - salvage)/useful_life
    years = []
    bv_schedule = []
    depr_schedule = []
    for year in range(0,useful_life+1):
        bv_schedule.append(round(cost,2))
        depr_schedule.append(round(depr_amount,2))
        cost -= depr_amount
    schedule.append(bv_schedule)
    schedule.append(depr_schedule)
    return schedule




def reducing_balance_schedule(cost, salvage, useful_life):
    rate = 1 - (salvage/cost)**(1/useful_life)
    schedule = []

    bv_schedule = [] #book value schedule
    depr_schedule = [] #depreciation schedule
    book_value = cost
    for year in range(0, useful_life + 1):
        bv_schedule.append(round(book_value, 2))
        depreciation = book_value * rate
        depr_schedule.append(round(depreciation, 2))
        book_value -= depreciation
        

    schedule.append(bv_schedule)
    schedule.append(depr_schedule)
        
    return schedule


Year = []
bv_schedule_table = [{'Year':Year}] #book value for compound method
depr_schedule_table = [{'Year':Year}] #depr amounts for compound method
bv_str_line = [{'Year':Year}]
depr_str_line = [{'Year':Year}]
iter = 0



for row in assets_df.itertuples():
    #appends the schedule tables with the data from what the function returns
    #itertuples() iterates through the DF row by row and returns them as a tuple, quick and not heavy on the memory
    if iter == 0:

        Year.append(int(iter))
    elif iter == 9:
        Year.append(int(iter))
        Year.append(int(iter+1))
    else:
        Year.append(int(iter))

    bv_str_line.append({
        row.Asset_Name: straight_line(row.Purchase_Cost, row.Salvage_Value, row.Useful_Life)[0]
    })
    depr_str_line.append({
            row.Asset_Name: straight_line(row.Purchase_Cost, row.Salvage_Value, row.Useful_Life)[1]
        })
    
    bv_schedule_table.append({
        row.Asset_Name: reducing_balance_schedule(row.Purchase_Cost, row.Salvage_Value, row.Useful_Life)[0]
    })

    depr_schedule_table.append({
            row.Asset_Name: reducing_balance_schedule(row.Purchase_Cost, row.Salvage_Value, row.Useful_Life)[1]
        })
    iter +=1 #iteration for loop for years

#The tables as a DF
bv_schedule_table = pd.concat([pd.DataFrame(d) for d in bv_schedule_table], axis=1)
depr_schedule_table = pd.concat([pd.DataFrame(d) for d in depr_schedule_table], axis=1)
str_table = pd.concat([pd.DataFrame(d) for d in bv_str_line], axis=1)
depr_str_table = pd.concat([pd.DataFrame(d) for d in depr_str_line], axis=1)

print(str_table)
print(depr_str_table)
print()
print(bv_schedule_table)
print(depr_schedule_table)