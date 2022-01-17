import pandas as pd
#from icecream import ic
import sqlite3

def BMI_Calculator(patient_df):

    bmi_df = pd.DataFrame({'Category': {0: 'Underweight', 1: 'Normal Weight', 2: 'Overweight', 
                                        3: 'Moderately obese', 4: 'Severely obese', 
                                        5: 'Very severely obese'},
                            'BMIRangeStart': {0: 0, 1: 18.5, 2: 25, 3: 30, 4: 35, 5: 40},
                            'BMIRangeStop': {0: 18.4, 1: 24.9, 2: 29.9, 3: 34.9, 4: 39.9, 5: float('inf')},
                            'HealthRisk': {0: 'Malnutrition risk', 1: 'Low risk', 2: 'Enhanced risk',
                                            3: 'Medium risk', 4: 'High risk', 5: 'Very high risk'}})

    patient_df['BodyMassIndex'] = (patient_df['WeightKg']/((patient_df['HeightCm']/100)**2)).round(1)

    conn = sqlite3.connect(':memory:')
    #write the tables
    patient_df.to_sql('patients', conn, index=False)
    bmi_df.to_sql('bmi', conn, index=False)

    query = '''
                select Gender, HeightCm, WeightKg, BodyMassIndex, Category as BMICategory, HealthRisk 
                from patients join bmi
                on BodyMassIndex between BMIRangeStart and BMIRangeStop
            '''

    result_df = pd.read_sql(query, conn)

    """ ic(patient_df.head(7))
    ic(bmi_df.head(7))
    ic(result_df.head(7)) """

    return result_df

if __name__ == "__main__":
    patient_df = pd.read_json('patient.json')
    result_df = BMI_Calculator(patient_df)
    print(result_df.head(10))


