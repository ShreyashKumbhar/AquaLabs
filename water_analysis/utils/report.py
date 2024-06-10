import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from water_analysis.models import CalculatedParameter
import io
import matplotlib.pyplot as plt

def generate_water_quality_report(buffer):
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()

    # Adding a title
    title_style = ParagraphStyle('title', fontSize=18, alignment=1, spaceAfter=12)
    title = Paragraph("Water Quality Analysis Report", title_style)
    elements.append(title)

    # Adding parameter details
    parameter_data = [['Parameter', 'Value', 'Status']]
    parameters = CalculatedParameter.objects.all()
    for parameter in parameters:
        status = "Within Standard" if parameter.within_standard() else "Outside Standard"
        parameter_data.append([parameter.parameter_name, str(parameter.value), status])

    parameter_table = Table(parameter_data)
    parameter_table.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,0), styles['Heading1'].textColor),
                                         ('TEXTCOLOR', (0,0), (-1,0), styles['Heading1'].textColor),
                                         ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                                         ('FONTSIZE', (0,0), (-1,0), 12),
                                         ('BOTTOMPADDING', (0,0), (-1,0), 12),
                                         ('GRID', (0,0), (-1,-1), 0.5, colors.black),  
                                         ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black)])) 
    elements.append(parameter_table)

    # Generating the report
    doc.build(elements)
