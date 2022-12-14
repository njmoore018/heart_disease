import pandas as pd

DISEASE_COUNT = 120
CLEAN_COUNT = 150
LINE = '-'*40
LENGTH = 42

def calc_avg_age(df, count):
    avg = df['Age'].sum()/count
    return avg

def calc_avg_pain(df, count):
    avg = df['Chest pain type'].sum()/count
    return avg

def calc_avg_bp(df, count):
    avg = df['BP'].sum()/count
    return avg

def calc_avg_chol(df, count):
    avg = df['Cholesterol'].sum()/count
    return avg

def calc_avg_hr(df, count):
    avg = df['Max HR'].sum()/count
    return avg

def display(disease_age, min_disease_age, disease_hr,
        clean_hr, disease_bp, clean_bp, disease_chol, clean_chol):
    print(' '+LINE)
    print('| Ages:'.ljust(41)+'|')
    print(f'| Average with Heart Disease: {disease_age:.2f}'.ljust(41)+'|')
    print(f'| Lowest with Heart Disease: {min_disease_age}'.ljust(41)+'|')
    print('|'+LINE+'|')
    print('| Average Max Heart Rates:'.ljust(41)+'|')
    print(f'| With Heart Disease: {disease_hr:.2f}'.ljust(41)+'|')
    print(f'| Without Heart Disease: {clean_hr:.2f}'.ljust(41)+'|')
    print('|'+LINE+'|')
    print('| Average Blood Pressure:'.ljust(41)+'|')
    print(f'| With Heart Disease: {disease_bp:.2f}'.ljust(41)+'|')
    print(f'| Without Heart Disease: {clean_bp:.2f}'.ljust(41)+'|')
    print('|'+LINE+'|')
    print('| Average Cholesterol Level:'.ljust(41)+'|')
    print(f'| With Heart Disease: {disease_chol:.2f}'.ljust(41)+'|')
    print(f'| Without Heart Disease: {clean_chol:.2f}'.ljust(41)+'|')
    print(' '+LINE)
    return

def main():
    df = pd.read_csv('archive/Heart_Disease_Prediction.csv')
    df = df[['Age', 'Sex', 'Chest pain type', 'BP', 'Cholesterol',
        'Max HR', 'Heart Disease']]
    df_disease = df.loc[df['Heart Disease'] == 'Presence']
    df_clean = df.loc[df['Heart Disease'] == 'Absence']
    disease_age = calc_avg_age(df_disease,DISEASE_COUNT)
    min_disease_age = df_disease['Age'].min()
    disease_bp = calc_avg_bp(df_disease,DISEASE_COUNT)
    clean_bp = calc_avg_bp(df_clean,CLEAN_COUNT)
    disease_chol = calc_avg_chol(df_disease,DISEASE_COUNT)
    clean_chol = calc_avg_chol(df_clean,CLEAN_COUNT)
    disease_hr = calc_avg_hr(df_disease,DISEASE_COUNT)
    clean_hr = calc_avg_hr(df_clean,CLEAN_COUNT)
    display(disease_age, min_disease_age, disease_hr, clean_hr,
            disease_bp, clean_bp, disease_chol, clean_chol)
    return

if __name__ == '__main__':
    main()