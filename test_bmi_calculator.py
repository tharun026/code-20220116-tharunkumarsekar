from cmath import exp
from bmi_calculator.bmi_calculator import BMI_Calculator
import pandas as pd
from pandas._testing import assert_frame_equal

patient_df = pd.DataFrame({'Gender': {0: 'Male', 1: 'Male', 2: 'Male', 
                                        3: 'Female'},
                            'HeightCm': {0: 171, 1: 0, 2: 204, 3: 183.5},
                            'WeightKg': {0: 0, 1: 85, 2: 77, 3: 62}})

actual_df = BMI_Calculator(patient_df)

expected_df = pd.DataFrame({'Gender': {0: 'Male', 1: 'Male', 2: 'Male', 
                                        3: 'Female'},
                            'HeightCm': {0: 171, 1: 0, 2: 204, 3: 183.5},
                            'WeightKg': {0: 0, 1: 85, 2: 77, 3: 62},
                            'BodyMassIndex': {0: 0, 1: float('inf'), 2: 18.5, 3: 18.4},
                            'BMICategory': {0: "Underweight", 1: "Very severely obese",
                                            2: "Normal Weight", 3: "Underweight"},
                            'HealthRisk': {0: "Malnutrition risk", 1: "Very high risk",
                                            2: "Low risk", 3: "Malnutrition risk"}})

assert_frame_equal(actual_df,expected_df)