from django.shortcuts import render, redirect
from django.http import HttpResponse

import os
import numpy
import scipy
import requests
from mdr import MDR
from lxml import etree
from urlparse import urlparse
import sys, getopt
# Create your views here.

from django.http import HttpResponse

def index(request):
    return render(request, 'autoscrapper/index.html')

def extract(request):
    if request.GET.get('url'):
        url = request.GET['url']

        mdr = MDR()
        try:
            r = requests.get(url)
            parsed_uri = urlparse(url)
        except:
            return redirect(index)

        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)

        candidates, doc = mdr.list_candidates(r.text)

        seed, mappings = mdr.extract(candidates[0])

        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        rel_path = "templates/autoscrapper/output.html"
        abs_file_path = os.path.join(script_dir, rel_path)
        f = open(rel_path,'w')
        x = seed.trees[0]
        # print "seed : ",x

        values = list(mappings.viewvalues())

        f.write("{%  load static %}")
        f.write("<html><h1>Extracted Data<h1>")
        f.write('<link href="bootstrap.min.css" rel="stylesheet" >')
        f.write("""<link href="{%  static 'bootstrap.min.css' %} " rel="stylesheet" >""")
        f.write("""<link href="{%  static 'cover.css' %} " rel="stylesheet">""")
        f.write('<table class="table table-bordered ">')

        key = x.iterdescendants()
        while(True):
            try:
                k = key.next()
                f.write("<th>")
                try:
                    classname = k.attrib['class']
                    f.write(classname)
                except:
                    f.write("_"+k.tag+"</th>")
                f.write("</th>")
            except:
                break

        for i, value in enumerate(values):
            f.write("<tr>")
            print "data item", i
            print "=============="
            key = x.iterdescendants()
            while(True):
                try:
                    k = key.next()
                    try:
                        val = value[k]
                    except:
                        f.write("<td></td>")
                        continue
                    f.write("<td>")
                    print k.tag, " --------> ", val.tag
                    if k.tag == 'a':
                        valattrib = val.attrib
                        href = valattrib['href']
                        # print href
                        try:
                            atext = a.text
                            print "atext = ", atext
                        except:
                            atext = href
                        # print href[:4]
                        if href[:4] != 'http':
                            # print "rel"
                            f.write('<a href="'+domain+href+'" >'+atext+'</a>')
                        else:
                            # print "abs"
                            f.write('<a href="'+valattrib['href']+'" >'+atext+'</a>')
                        # print "href = ", valattrib['href']
                        
                    elif k.tag == 'img':
                        
                        valattrib = val.attrib

                        href = valattrib['src']
                        if href[:4] != 'http':
                            f.write('<img height="100" src="'+domain+href+'" >')
                        else:
                            f.write('<img height="100" src="'+valattrib['src']+'" >')

                        # print "img = ", valattrib['src'] 
                        
                    else:  
                        try:
                            f.write(val.text)     
                            ktext = k.text
                            # valtext = val.text
                            valtext = etree.tostring(val, pretty_print=True)
                            # print ktext, " --------> ", valtext
                        except:
                            pass
                    f.write("</td>")    
                    
                except:
                    break
            f.write("</tr>")
        f.write("</table>")
        f.write("</html>")
        f.close()



        # return HttpResponse(url)
        return redirect('/output/')
    else:
        return redirect(index)
    
    

def output(request):
    return render(request, 'autoscrapper/output.html')