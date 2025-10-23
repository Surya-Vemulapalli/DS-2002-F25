#!/usr/bin/env python3
import pandas as pd
import os
import json
import sys
import csv

def list_size(list):
    count = 0
    for x in list:
        count+=1
    return count
    

def _load_lookup_data(lookup_dir):
    all_lookup_df = []
    for json_file in os.listdir(lookup_dir):
        splitted = os.path.splitext(json_file)
        extension = splitted[1]
        if extension != ".json":
            return "Incompatible type"
        filepath = os.path.join(lookup_dir,json_file);
        with open(filepath,'r') as j:
            data = json.load(j)
        df = pd.json_normalize(data["data"])
        df_col_1 = df['tcgplayer.prices.holofoil.market']
        df_col_2 = df['tcgplayer.prices.normal.market']
        df_col_1_new = df_col_1.where(df_col_1.isna() == False,0.0)
        df_col_2_new = df_col_2.where(df_col_1.isna() == True,0.0)
        df['card_market_value'] = df_col_1_new + df_col_2_new
        df = df.rename(columns={"id":"card_id","name":"card_name","number":"card_number","set.id":"set_id","set.name":"set_name","tcgplayer.prices.holofoil.market":"holofoil_card_prices","tcgplayer.prices.normal.market":"normal_card_prices"})
        required_cols = ['card_id','card_name','card_number','set_id','set_name','card_market_value']
        all_lookup_df.append(df[required_cols].copy())
    
    lookup_df = pd.concat(all_lookup_df,ignore_index=True)
    lookup_df.sort_values(by=['card_id'])
    lookup_df.drop_duplicates(subset=['card_id'], keep='first')
    return lookup_df

def _load_inventory_data(inventory_dir):
    inventory_data = []
    for file in os.listdir(inventory_dir):
        if file.endswith('csv'):
            filepath = os.path.join(inventory_dir,file)
            df = pd.read_csv(filepath)
            inventory_data.append(df)
    if list_size(inventory_data) == 0:
        return pd.Dataframe({})
    inventory_df = pd.concat(inventory_data)
    inventory_df['card_id'] = inventory_df['set_id'].astype(str) + '-' + inventory_df['card_number'].astype(str)
    return inventory_df

def update_portfolio(inventory_dir, lookup_dir, output_file):
    lookup_df = _load_lookup_data(lookup_dir)
    inventory_df = _load_inventory_data(inventory_dir)
    if list_size(inventory_dir) <= 0:
        print("No file present", file=sys.stderr)
        with open('empty.csv','w', newline='') as empty_file:
            fieldnames = ['card_name','set_id','card_number','binder_name','page_number','slot_number','card_id']
            writer = csv.DictWriter(empty_file, fieldnames=fieldnames)

            writer.writeheader();
        return empty_file;
    df = pd.merge(inventory_df,lookup_df[['card_id', 'set_name','card_market_value']],on=['card_id'],how='left')
    cf = df['card_market_value']
    sf = df['set_name']
    df['card_market_value'] = cf.where(cf.isnull() == False,0.0)
    df['set_name'] = sf.where(sf.isnull() == False,'NOT FOUND')
    df['index'] = df['binder_name'].astype(str) + df['page_number'].astype(str) + df['slot_number'].astype(str)
    final_cols = ['index','card_id','card_name','card_market_value']
    df[final_cols].to_csv(output_file)
    print("New csv file created")

def main():
    update_portfolio('./card_inventory/','./card_set_lookup/','card_portfolio.csv')

def test():
    update_portfolio('./card_inventory_test/','./card_set_lookup_test/','test_card_portfolio.csv')

if __name__ == "__main__":
    print("Going to test mode", file=sys.stderr)
    test()


            

