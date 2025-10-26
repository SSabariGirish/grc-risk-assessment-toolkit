import pandas as pd
import sys

def generate_register():
    # --- 1. Define Risk Methodology ---
    # Define the scoring and levels. This makes it easy to change later.
    def map_risk_level(score):
        if score >= 6:
            return 'High'
        elif score >= 3:
            return 'Medium'
        else:
            return 'Low'

    # --- 2. Load Data ---
    try:
        assets_df = pd.read_csv('assets.csv')
        risks_df = pd.read_csv('risk_assessment.csv')
    except FileNotFoundError as e:
        print(f"Error: {e}. Make sure 'assets.csv' and 'risk_assessment.csv' are in the same folder.")
        sys.exit(1)

    # --- 3. Process & Merge Data ---
    # Merge the risk data with the asset data to get asset names
    # We use a 'left' merge to keep all risks, even if an Asset_ID was mistyped
    merged_df = pd.merge(
        risks_df,
        assets_df,
        left_on='Affected_Asset_ID',
        right_on='Asset_ID',
        how='left'
    )

    # --- 4. Calculate Risk ---
    # Calculate the RiskScore (Likelihood * Impact)
    merged_df['RiskScore'] = merged_df['Likelihood'] * merged_df['Impact']

    # Apply the mapping function to create the 'RiskLevel' column
    merged_df['RiskLevel'] = merged_df['RiskScore'].apply(map_risk_level)
    
    # --- 5. Finalise the Report ---
    # Select and reorder the columns for the final report
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
    
    # Filter the DataFrame to only include our desired columns
    final_df = merged_df[final_report_cols]

    # Sort the final report by RiskScore (highest first)
    final_df_sorted = final_df.sort_values(by='RiskScore', ascending=False)

    # --- 6. Save the Report ---
    output_filename = 'Prioritised_Risk_Register.csv'
    final_df_sorted.to_csv(output_filename, index=False)

    # --- 7. Save Top 5 Summary Report ---
    top_5_filename = 'Top_5_Risks_Summary.csv'
    final_df_sorted.head(5).to_csv(top_5_filename, index=False)

    print(f"✅ A summary of the top 5 risks has been saved to '{top_5_filename}'.")

    print(f"✅ Success! Your '{output_filename}' has been created.")
    print("\nTop 5 Risks:")
    print(final_df_sorted.head(5).to_string()) # .to_string() formats it nicely

# --- Run the function ---
if __name__ == "__main__":
    generate_register()