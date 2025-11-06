import pandas as pd
import sys

def generate_register():
    def map_risk_level(score):
        if score >= 6:
            return 'High'
        elif score >= 3:
            return 'Medium'
        else:
            return 'Low'

    try:
        assets_df = pd.read_csv('assets.csv')
        risks_df = pd.read_csv('risk_assessment.csv')
    except FileNotFoundError as e:
        print(f"Error: {e}. Make sure 'assets.csv' and 'risk_assessment.csv' are in the same folder.")
        sys.exit(1)

    merged_df = pd.merge(
        risks_df,
        assets_df,
        left_on='Affected_Asset_ID',
        right_on='Asset_ID',
        how='left'
    )

    merged_df['RiskScore'] = merged_df['Likelihood'] * merged_df['Impact']

    merged_df['RiskLevel'] = merged_df['RiskScore'].apply(map_risk_level)
    
    final_report_cols = [
        'Risk_ID',
        'Threat',
        'Vulnerability',
        'RiskLevel',
        'RiskScore',
        'Likelihood',
        'Impact',
        'Affected_Asset_ID',
        'AssetName',
        'DataClassification',
        'BusinessOwner'
    ]
    
    final_df = merged_df[final_report_cols]

    final_df_sorted = final_df.sort_values(by='RiskScore', ascending=False)

    output_filename = 'Prioritised_Risk_Register.csv'
    final_df_sorted.to_csv(output_filename, index=False)

 
    top_5_filename = 'Top_5_Risks_Summary.csv'
    final_df_sorted.head(5).to_csv(top_5_filename, index=False)

    print(f"A summary of the top 5 risks has been saved to '{top_5_filename}'.")

    print(f"Success! Your '{output_filename}' has been created.")
    print("\nTop 5 Risks:")
    print(final_df_sorted.head(5).to_string())

if __name__ == "__main__":
    generate_register()