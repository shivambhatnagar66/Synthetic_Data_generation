# Dataset: Cardiovascular Health Data
import pandas as pd                                      
import numpy as np   

def generate_cardiovascular_dataset(n_samples=3000):
    np.random.seed(42)

    # Demographics
    age = np.random.normal(55, 12, n_samples).astype(int)             
    age = np.clip(age, 30, 80)                                         
    gender = np.random.choice(['Male', 'Female'], n_samples, p=[0.55, 0.45])

    # Clinical measurements
    # Systolic BP (realistic correlation with age)
    systolic_bp = 110 + 0.4 * age + np.random.normal(0, 12, n_samples)    
    systolic_bp = np.clip(systolic_bp, 90, 180).round(0).astype(int)     
    # Cholesterol
    cholesterol = 170 + 0.5 * age + np.random.normal(0, 25, n_samples)    
    cholesterol = np.clip(cholesterol, 120, 300).round(0).astype(int)     
    # BMI
    bmi = 22 + np.random.exponential(2.5, n_samples)                      
    bmi = np.clip(bmi, 18, 40).round(1)

    # Lifestyle factors
    smoking = np.random.choice(['Never', 'Former', 'Current'], n_samples, p=[0.5, 0.35, 0.15])   
    exercise_hours = np.random.exponential(2, n_samples)                  
    exercise_hours = np.clip(exercise_hours, 0, 10).round(1)
    
    # Medical history
    diabetes = np.random.choice(['No', 'Yes'], n_samples, p=[0.85, 0.15])

    # Heart disease (target variable) - realistic relationships
    risk_score = (
        0.02 * age +                                                       
        0.008 * systolic_bp +                                            
        0.003 * cholesterol +                                             
        0.05 * bmi +                                                     
        (smoking == 'Current') * 0.8 +                                    
        (smoking == 'Former') * 0.3 +                                     
        (diabetes == 'Yes') * 0.7 +                                       
        (gender == 'Male') * 0.2 -                                        
        0.08 * exercise_hours +                                           
        np.random.normal(0, 0.8, n_samples)                               
    )
    #calculating heart disease probability using risk score
    heart_disease_prob = 1 / (1 + np.exp(-risk_score + 4))                
    heart_disease = np.random.binomial(1, heart_disease_prob, n_samples) 
    heart_disease = np.where(heart_disease == 1, 'Yes', 'No') 

    # Create DataFrame
    df = pd.DataFrame({                                          
        'patient_id': range(1, n_samples + 1),
        'age': age,
        'gender': gender,
        'systolic_bp': systolic_bp,
        'cholesterol': cholesterol,
        'bmi': bmi,
        'smoking_status': smoking,
        'exercise_hours_per_week': exercise_hours,
        'diabetes': diabetes,
        'heart_disease': heart_disease
    })

    df.to_csv("cardiovascular.csv", index=False)
    return df