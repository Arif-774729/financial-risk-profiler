import pandas as pd
import random

random.seed(42)

def generate_data(num_samples=150):
    data = []

    for _ in range(num_samples):
        age = random.randint(18, 60)
        income = random.randint(15000, 150000)
        employment_status = random.choice(['employed', 'self-employed', 'student', 'unemployed'])
        spending_score = random.randint(1, 100)
        credit_score = random.randint(300, 850)

       
        if credit_score < 580 or income < 30000 or employment_status == 'unemployed':
            risk = 1  # High risk
        else:
            risk = 0  # Low risk

        data.append([age, income, employment_status, spending_score, credit_score, risk])

    df = pd.DataFrame(data, columns=[
        'age', 'income', 'employment_status', 'spending_score', 'credit_score', 'risk'
    ])

    df.to_csv('financial_data.csv', index=False)
    print(f"✅ Generated {num_samples} records in 'financial_data.csv'")

if __name__ == "__main__":
    generate_data()
