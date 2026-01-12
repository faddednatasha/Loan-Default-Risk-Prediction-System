import pandas as pd
import numpy as np
import random

def generate_bulk_loan_data(n=1500):
    # Setup for consistent random generation
    data = []
    
    for i in range(n):
        loan_id = f"LP{10000 + i}"
        gender = random.choices(['Male', 'Female'], weights=[0.8, 0.2])[0]
        married = random.choices(['Yes', 'No'], weights=[0.65, 0.35])[0]
        dependents = random.choices(['0', '1', '2', '3+'], weights=[0.5, 0.2, 0.2, 0.1])[0]
        education = random.choices(['Graduate', 'Not Graduate'], weights=[0.75, 0.25])[0]
        self_employed = random.choices(['No', 'Yes'], weights=[0.85, 0.15])[0]
        
        # Applicant Income: Most between 2500-10000, some high earners
        applicant_income = int(np.random.lognormal(mean=8.4, sigma=0.5)) 
        
        # Coapplicant Income: 50% chance of being 0
        co_income = 0 if random.random() > 0.5 else int(random.uniform(1000, 5000))
        
        # Loan Amount: Linked to income (roughly 2.5x annual income / 12)
        total_income = (applicant_income + co_income)
        loan_amount = int((total_income * random.uniform(0.02, 0.04)))
        
        term = random.choices([360, 180, 480, 240, 120], weights=[0.8, 0.1, 0.05, 0.03, 0.02])[0]
        credit_history = random.choices([1.0, 0.0], weights=[0.85, 0.15])[0]
        property_area = random.choice(['Urban', 'Semiurban', 'Rural'])
        
        # Logic for Loan Status (Decision Engine)
        if credit_history == 1.0:
            status = random.choices(['Y', 'N'], weights=[0.9, 0.1])[0]
        else:
            status = random.choices(['Y', 'N'], weights=[0.1, 0.9])[0]
            
        data.append([loan_id, gender, married, dependents, education, self_employed, 
                     applicant_income, co_income, loan_amount, term, 
                     credit_history, property_area, status])

    cols = ['Loan_ID', 'Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 
            'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Term', 
            'Credit_History', 'Property_Area', 'Status']
    
    return pd.DataFrame(data, columns=cols)

# Generate 1500 entries
df = generate_bulk_loan_data(1500)

# Save to Excel-compatible CSV
df.to_csv('Loan_Entries_1500.csv', index=False)

print(f"Successfully generated {len(df)} entries.")
print("The file 'Loan_Entries_1500.csv' is ready for use in Excel.")
