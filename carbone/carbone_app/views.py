# carbone_app/views.py
import json
import os
import carbone_sdk
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, FileResponse
from django.conf import settings
from .models import CarboneRender
from .forms import CarboneRenderForm

def home(request):
    if request.method == 'POST':
        form = CarboneRenderForm(request.POST, request.FILES)
        if form.is_valid():
            render_obj = form.save()
            
            # Process files with Carbone SDK
            try:
                # Initialize Carbone SDK
                csdk = carbone_sdk.CarboneSDK("test_eyJhbGciOiJFUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIxMTQxNjg4MTgxOTg0MTUwNjE0IiwiYXVkIjoiY2FyYm9uZSIsImV4cCI6MjQwNzgxNTAzNywiZGF0YSI6eyJ0eXBlIjoidGVzdCJ9fQ.AP760dvCZWsbCU8HRkP7twqML2_kkRAz7FkSAg_pj3GGxmCc_ayRAQnFxlmsMAJLmZfZVghCP0ezpF4jGwk6gOpVAa5An-2G6fsbtEqILuDCaONK_KdrcBinKKfOALmTq-bxH42nTu11JLUWP6zlmXv5eY3E-VfGd4mt-NpLOPJoePNG")
                
                # Get the template file path
                template_path = os.path.join(settings.MEDIA_ROOT, render_obj.template_file.name)
                
                # Read JSON data
                with open(os.path.join(settings.MEDIA_ROOT, render_obj.json_file.name), 'r') as f:
                    data = json.load(f)
                
                # Render options
                render_options = {
                    "data": data,
                    "convertTo": "pdf",
                }
                
                # Generate report
                report_bytes, report_name = csdk.render(template_path, render_options)
                
                # Save the PDF
                pdf_path = os.path.join('pdf', f"{render_obj.id}_{report_name}")
                full_pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_path)
                os.makedirs(os.path.dirname(full_pdf_path), exist_ok=True)
                
                with open(full_pdf_path, 'wb') as f:
                    f.write(report_bytes)
                
                # Update model with PDF location
                render_obj.pdf_file = pdf_path
                render_obj.save()
                
                return redirect('download_pdf', render_id=render_obj.id)
            
            except Exception as e:
                error_message = f"Error generating PDF: {str(e)}"
                return render(request, 'carbone_app/home.html', {'form': form, 'error': error_message})
    else:
        form = CarboneRenderForm()
    
    return render(request, 'carbone_app/home.html', {'form': form})

def generate(request):
    if request.method == 'POST':
        form = CarboneRenderForm(request.POST, request.FILES)
        if form.is_valid():
            render_obj = form.save()
            
            # Process files with Carbone SDK
            try:
                # Initialize Carbone SDK
                csdk = carbone_sdk.CarboneSDK("test_eyJhbGciOiJFUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIxMTM5NTkyOTkzODAzMDI4MDgzIiwiYXVkIjoiY2FyYm9uZSIsImV4cCI6MjQwNzU2NTI3MSwiZGF0YSI6eyJ0eXBlIjoidGVzdCJ9fQ.AZUwGpSwWJpfzvD0TzN1fRLry0MiPZAM6WG7XAYrFIoKk-8APx9s0vxSmVhtq6NZyIBWfQvX6Unvn1EzqZrzXPXVAbF3l6qIZ55FKStO6LpMwFc1ah4H0dUoMhUQHBf5_oXwEokrHtlmx3XFXIEVYl1p9M6G-wzZ4wZOR3DXYIGACYSF")
                
                # Get the template file path
                template_path = os.path.join(settings.MEDIA_ROOT, render_obj.template_file.name)
                
                # Read JSON data
                with open(os.path.join(settings.MEDIA_ROOT, render_obj.json_file.name), 'r') as f:
                    data = json.load(f)
                
                # Render options
                render_options = {
                    "data": data,
                    "convertTo": "pdf",
                }
                
                # Generate report
                report_bytes, report_name = csdk.render(template_path, render_options)
                
                # Save the PDF
                pdf_path = os.path.join('pdf', f"{render_obj.id}_{report_name}")
                full_pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_path)
                os.makedirs(os.path.dirname(full_pdf_path), exist_ok=True)
                
                with open(full_pdf_path, 'wb') as f:
                    f.write(report_bytes)
                
                # Update model with PDF location
                render_obj.pdf_file = pdf_path
                render_obj.save()
                
                return redirect('download_pdf', render_id=render_obj.id)
            
            except Exception as e:
                error_message = f"Error generating PDF: {str(e)}"
                return render(request, 'carbone_app/home.html', {'form': form, 'error': error_message})
    else:
        form = CarboneRenderForm()
    
    return render(request, 'carbone_app/home.html', {'form': form})

def download_pdf(request, render_id):
    render_obj = get_object_or_404(CarboneRender, id=render_id)
    if render_obj.pdf_file:
        pdf_path = os.path.join(settings.MEDIA_ROOT, render_obj.pdf_file.name)
        return FileResponse(open(pdf_path, 'rb'), as_attachment=True, filename=os.path.basename(pdf_path))
    else:
        return HttpResponse("PDF not found", status=404)