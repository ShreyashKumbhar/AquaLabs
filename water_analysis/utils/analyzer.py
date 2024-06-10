def water_quality_analysis(pH, hardness, alkalinity, turbidity, tds):
    # Analyzing the data and generating the text result
    pH_status = "Within Standard" if 6.5 <= pH <= 8.5 else "Outside Standard"
    hardness_status = "Within Standard" if hardness <= 200 else "Outside Standard"
    alkalinity_status = "Within Standard" if alkalinity <= 200 else "Outside Standard"
    turbidity_status = "Within Standard" if turbidity <= 1 else "Outside Standard"
    tds_status = "Within Standard" if tds <= 500 else "Outside Standard"

    # Constructing the result text
    result_text = f"Water Quality Analysis:\n"
    result_text += f"pH: {pH} - {pH_status}\n"
    result_text += f"Hardness: {hardness} - {hardness_status}\n"
    result_text += f"Alkalinity: {alkalinity} - {alkalinity_status}\n"
    result_text += f"Turbidity: {turbidity} - {turbidity_status}\n"
    result_text += f"TDS: {tds} - {tds_status}\n"

    return result_text
