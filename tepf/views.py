from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from fpdf import FPDF
import json

def downloadText(request):
    if request.method == 'POST':
        text = request.POST['text']
        download_file = open("downloadfile.txt", "w")
        download_file.write(text)
        return render(request, 'download.html')
    else:
        return render(request, 'index.html')    

def downloadPDF(request):
    if request.method == 'POST':
        text = request.POST['text']
        font_size = int(request.POST['font-size'])
        font_style = str(request.POST['font-style'])
        pdf = FPDF() 
        pdf.add_page() 
        pdf.set_font(font_style, size = font_size) 
        pdf.multi_cell(200, 10, text, align = 'L')
        pdf.output("downloadfile.pdf", 'F') 
        return render(request, 'download.html')
    else:
        return render(request, 'index.html')   

def index(request):
    return render(request, 'index.html')

def wordsLine(request):
    if request.method == 'POST':
        text = request.POST.get('text', None)
        words = len(text.split())
        lines = 0
        CoList = text.split("\n")
        for i in CoList:
            if i:
                lines += 1
        return JsonResponse(json.dumps({'words': words, 'lines': lines,}), safe=False) 
    else:
        return render(request, 'index.html') 