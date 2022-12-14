import pandas as pd

# Constant set up for displaying data with nice format 
LINE = '-'*40


'''
These calculate functions take in the dataframes for either
people with heart disease or without and calculate average
values for the selected columns of data.
'''
def calc_avg_age(df, count):
    avg = df['Age'].sum()/count
    return avg

# See comment above
def calc_avg_pain(df, count):
    avg = df['Chest pain type'].sum()/count
    return avg

# See comment above
def calc_avg_bp(df, count):
    avg = df['BP'].sum()/count
    return avg

# See comment above
def calc_avg_chol(df, count):
    avg = df['Cholesterol'].sum()/count
    return avg

# See comment above
def calc_avg_hr(df, count):
    avg = df['Max HR'].sum()/count
    return avg

'''
This function takes in all the calculated data from the main
function and outputs the values in a pretty format for the user
to read.
'''
def display(disease_age, min_disease_age, disease_hr,
        clean_hr, disease_bp, clean_bp, disease_chol, clean_chol):
    
    # Creates a nice outline around the data for easy viewing and
    # reading of the data
    print(' '+LINE)
    
    # Introduction to data; not a selected question for answering
    print('| Ages:'.ljust(41)+'|')
    print(f'| Average with Heart Disease: {disease_age:.2f}'.ljust(41)+'|')
    print(f'| Lowest with Heart Disease: {min_disease_age}'.ljust(41)+'|')
    
    # Part of data outlines
    print('|'+LINE+'|')

    # First question selected to answer: How do peoples max heart
    # rates change based on disease presence/absence?
    print('| Average Max Heart Rates:'.ljust(41)+'|')
    print(f'| With Heart Disease: {disease_hr:.2f}'.ljust(41)+'|')
    print(f'| Without Heart Disease: {clean_hr:.2f}'.ljust(41)+'|')
    
    # Part of data outlines
    print('|'+LINE+'|')

    # Second question selected to answer: How do peoples blood
    # pressure change based on disease presence/absence?
    print('| Average Blood Pressure:'.ljust(41)+'|')
    print(f'| With Heart Disease: {disease_bp:.2f}'.ljust(41)+'|')
    print(f'| Without Heart Disease: {clean_bp:.2f}'.ljust(41)+'|')
    
    # Part of data outlines
    print('|'+LINE+'|')

    # Third question selected to answer: How do peoples cholesterol
    # levels vary based on disease presence/absence?
    print('| Average Cholesterol Level:'.ljust(41)+'|')
    print(f'| With Heart Disease: {disease_chol:.2f}'.ljust(41)+'|')
    print(f'| Without Heart Disease: {clean_chol:.2f}'.ljust(41)+'|')
    
    # Part of data outlines
    print(' '+LINE)
    return

# Main function, sets up pandas dataframe, calls all calculate
# functions and finally passes values to display function
def main():
    # Set up DataFrame for Pandas
    df = pd.read_csv('archive/Heart_Disease_Prediction.csv')
    
    # Narrow down columns to simplest ones
    df = df[['Age', 'Sex', 'Chest pain type', 'BP', 'Cholesterol',
        'Max HR', 'Heart Disease']]

    # Create separate DataFrames for individuals with and without
    # Heart Disease
    df_disease = df.loc[df['Heart Disease'] == 'Presence']
    df_clean = df.loc[df['Heart Disease'] == 'Absence']
    
    # Count number of people in each new DataFrame for use with
    # average calculations
    disease_count = df_disease.shape[0]
    clean_count = df_clean.shape[0]

    # Perform all calculations
    disease_age = calc_avg_age(df_disease,disease_count)
    min_disease_age = df_disease['Age'].min()
    disease_bp = calc_avg_bp(df_disease,disease_count)
    clean_bp = calc_avg_bp(df_clean,clean_count)
    disease_chol = calc_avg_chol(df_disease,disease_count)
    clean_chol = calc_avg_chol(df_clean,clean_count)
    disease_hr = calc_avg_hr(df_disease,disease_count)
    clean_hr = calc_avg_hr(df_clean,clean_count)

    # Call display and pass all calculated values
    display(disease_age, min_disease_age, disease_hr, clean_hr,
            disease_bp, clean_bp, disease_chol, clean_chol)
    return

if __name__ == '__main__':
    main()