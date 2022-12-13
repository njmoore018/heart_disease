import pandas as pd

DISEASE_COUNT = 120
CLEAN_COUNT = 150

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

def main():
    df = pd.read_csv('archive/Heart_Disease_Prediction.csv')
    df = df[['Age', 'Sex', 'Chest pain type', 'BP', 'Cholesterol',
        'Max HR', 'Heart Disease']]
    df_disease = df.loc[df['Heart Disease'] == 'Presence']
    df_clean = df.loc[df['Heart Disease'] == 'Absence']
    avg_disease_age = calc_avg_age(df_disease,DISEASE_COUNT)
    min_disease_age = df_disease['Age'].min()
    avg_disease_pain = calc_avg_pain(df_disease,DISEASE_COUNT)
    avg_clean_pain = calc_avg_pain(df_clean,CLEAN_COUNT)
    avg_disease_bp = calc_avg_bp(df_disease,DISEASE_COUNT)
    avg_clean_bp = calc_avg_bp(df_clean,CLEAN_COUNT)
    avg_disease_chol = calc_avg_chol(df_disease,DISEASE_COUNT)
    avg_clean_chol = calc_avg_chol(df_clean,CLEAN_COUNT)
    avg_disease_hr = calc_avg_hr(df_disease,DISEASE_COUNT)
    avg_clean_hr = calc_avg_hr(df_clean,CLEAN_COUNT)
    print(f'Average Age of Person with Heart Disease: {avg_disease_age}')
    print(f'Lowest Age of Person with Heart Disease: {min_disease_age}')
    print()
    print(f'Average Max Heart Rate of Person with Heart Disease: {avg_disease_hr}')
    print(f'Average Max Heart Rate of Person without Heart Disease: {avg_clean_hr}')
    print()
    print(avg_disease_bp)
    print(avg_clean_bp)
    print()
    print(avg_disease_pain)
    print(avg_clean_pain)
    print()
    print(avg_disease_chol)
    print(avg_clean_chol)
    return

if __name__ == '__main__':
    main()