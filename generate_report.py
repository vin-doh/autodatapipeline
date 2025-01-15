import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def generate_report(processed_csv, report_file_txt, report_file_xlsx, report_file_img, report_file_html):
    # Read the processed data CSV
    df = pd.read_csv(processed_csv)

    # Calculate statistics
    report = df.describe()

    # Save statistics to the text file
    with open(report_file_txt, 'w') as f:
        f.write("Weather Data Report\n\n")
        f.write("Temperature (°C)  Wind Speed (km/h)  Humidity (%)\n")
        f.write(str(report))

    print(f"Text report saved to {report_file_txt}")
    
    # Generate Excel report
    with pd.ExcelWriter(report_file_xlsx, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Weather Data')

        # Access the worksheet to format it
        worksheet = writer.sheets['Weather Data']

        # Adjust column widths based on the maximum content length
        for idx, col in enumerate(df.columns):
            # Find the maximum length of the column content
            max_len = max(df[col].astype(str).apply(len).max(), len(col))
            worksheet.set_column(idx, idx, max_len + 2)  # Adding extra space for readability

    print(f"Excel report saved to {report_file_xlsx}")

    # Generate a bar plot for temperature, wind speed, and humidity for each location (static)
    plt.figure(figsize=(10, 6))
    df_melted = df.melt(id_vars="Location", value_vars=["Temperature (°C)", "Wind Speed (km/h)", "Humidity (%)"], 
                        var_name="Metric", value_name="Value")
    sns.barplot(x="Location", y="Value", hue="Metric", data=df_melted)
    plt.title('Weather Data by Location')
    plt.xlabel('Location')
    plt.ylabel('Value')
    plt.xticks(rotation=45, ha='right')

    # Save the static plot as a PNG image
    plt.tight_layout()
    plt.savefig(report_file_img)
    plt.close()

    print(f"Static visualization saved to {report_file_img}")

    # Generate interactive bar plot with Plotly
    fig = px.bar(df_melted, x="Location", y="Value", color="Metric", 
                 title="Weather Data by Location",
                 labels={"Value": "Value", "Location": "Location"})
    
    # Save the interactive plot as an HTML file
    fig.write_html(report_file_html)

    print(f"Interactive visualization saved to {report_file_html}")
