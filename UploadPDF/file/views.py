from django.shortcuts import render,redirect
from .forms import DocumentForm
import os
from django.conf import settings

import os
import sys
import re
import time
import PyPDF2


def getPageCount(pdf_file):
    pdfFileObj = open(pdf_file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pages = pdfReader.numPages
    return pages


def extractData(pdf_file, page):
    pdfFileObj = open(pdf_file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(page)
    data = pageObj.extractText()
    return data


def getWordCount(data):
    data = data.split()
    return len(data)


def uploadFile(request):

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        pdf = request.FILES.get('document')
        if form.is_valid():
            form.save()

            file_root = os.path.join(settings.MEDIA_ROOT, 'documents')
            pdf_document = str(file_root) + "\\" + str(pdf)

            # get the word count in the pdf file
            totalWords = 0
            numPages = getPageCount(pdf_document)
            for i in range(numPages):
                text = extractData(pdf_document, i)
                totalWords += getWordCount(text)
            time.sleep(1)

            print("total words -->", totalWords)
            print("number of pages  -->", numPages)

            return render(request, 'file/upload_file.html', {
                'form': form,'totalWords':totalWords,'numPages':numPages,'pdf': str(pdf),'uploaded':True
            })

    else:
        form = DocumentForm()
    return render(request, 'file/upload_file.html', {
        'form': form,'uploaded':False
    })



def home(request):
    form = DocumentForm()
    return render(request, 'file/upload_file.html', {
        'form': form
    })