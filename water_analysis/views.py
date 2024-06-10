from django.shortcuts import render
from django.http import HttpResponse
from .models import pHReading, HardnessMeasurement, TurbidityMeasurement, AlkalinityMeasurement, TDSMeasurement, CalculatedParameter
from .utils import ph, tds, turbidity, alkalinity, hardness
from .utils.analyzer import water_quality_analysis
from .utils.report import generate_water_quality_report
import io

def home(request):
    return render(request, 'water_analysis/home.html')

def aboutus(request):
    return render(request, 'water_analysis/aboutus.html')

def procedure(request):
    return render(request, 'water_analysis/procedure.html')

def analyze(request):
    if request.method == 'POST':
        # Clearing existing CalculatedParameter objects
        CalculatedParameter.objects.all().delete()

        # Handling form submission
        ph_value = request.POST.get('ph_value')
        volume_hcl_phenolphthalein = request.POST.get('volume_hcl_phenolphthalein')
        volume_hcl_methyl_orange = request.POST.get('volume_hcl_methyl_orange')
        depth_cm = request.POST.get('depth_cm')
        weight_dish_filtrate = request.POST.get('weight_dish_filtrate')
        weight_dish = request.POST.get('weight_dish')
        volume_sample = request.POST.get('volume_sample')
        znso4_volume = request.POST.get('znso4_volume')
        edta_volume = request.POST.get('edta_volume')
        edta_volume_B = request.POST.get('edta_volume_B')

        # Model instances with the submitted readings
        pHReading.objects.create(value=ph_value)
        AlkalinityMeasurement.objects.create(volume_hcl_phenolphthalein=volume_hcl_phenolphthalein, volume_hcl_methyl_orange=volume_hcl_methyl_orange)
        TurbidityMeasurement.objects.create(depth_cm=depth_cm)
        TDSMeasurement.objects.create(weight_dish_filtrate=weight_dish_filtrate, weight_dish=weight_dish, volume_sample=volume_sample)
        HardnessMeasurement.objects.create(znso4_volume=znso4_volume, edta_volume=edta_volume)

        # Performing calculations using the Python programs
        alkalinity_value = alkalinity.calculate_alkalinity(float(volume_hcl_phenolphthalein), float(volume_hcl_methyl_orange))
        alkalinity_value = round(alkalinity_value[0], 2)
        ntu_measurement = round(turbidity.depth_to_ntu(float(depth_cm)),2)
        tds_measurement = round(tds.calculate_tds(float(weight_dish_filtrate), float(weight_dish), float(volume_sample)))

        znso4_concentration = 0.01  # Default value
        edta_molarity = hardness.calculate_edta_molarity(float(znso4_volume) / 1000, znso4_concentration, float(edta_volume) / 1000)
        water_hardness = hardness.calculate_hardness(edta_molarity, float(edta_volume_B))

        # Instances of CalculatedParameter model with calculated values
        CalculatedParameter.objects.create(parameter_name='pH', value=ph_value)
        CalculatedParameter.objects.create(parameter_name='hardness', value=water_hardness)
        CalculatedParameter.objects.create(parameter_name='turbidity', value=ntu_measurement)
        CalculatedParameter.objects.create(parameter_name='alkalinity', value=alkalinity_value)
        CalculatedParameter.objects.create(parameter_name='tds', value=tds_measurement)

        # Generating the text analysis result
        result_text = water_quality_analysis(float(ph_value), float(water_hardness), float(alkalinity_value), float(ntu_measurement), float(tds_measurement))

        # Generating the PDF report
        buffer = io.BytesIO()
        generate_water_quality_report(buffer)
        buffer.seek(0)

        # Returning the report as a response
        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="water_quality_report.pdf"'
        return response

    # Rendering the analysis form if the request method is not POST
    return render(request, 'water_analysis/analyze.html')

def download_report(request):
    # Generating the PDF report
    buffer = io.BytesIO()
    generate_water_quality_report(buffer)
    buffer.seek(0)

    # Returning the report as a response
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="water_quality_report.pdf"'
    return response