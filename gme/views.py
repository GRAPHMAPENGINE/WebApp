from flask import Flask, render_template, request, redirect, url_for
# IMPORT LIBRARIES
import string
import os
import urllib.request
import patoolib

from functools import reduce
from toolz.itertoolz import sliding_window
import os


app = Flask(__name__)

@app.route('/' , methods = ['GET','POST'])
def index():

    if request.method == 'POST':

        github_link = request.form['github_link']
        user_input_url = github_link
        url_download_extension = '/archive/master.zip'
        download_url = user_input_url+url_download_extension
        url=download_url
        test_url = user_input_url
        zip_list = '.zip'
        zip_file_name = "_".join(test_url.split('/')[-2:]).lower()
        zip_file_name = zip_file_name+zip_list
        urllib.request.urlretrieve( url, zip_file_name)
        patoolib.extract_archive(zip_file_name,outdir='unpack')
        engine_root = os.getcwd()
        concatenator = '/unpack/'
        extracted_file_name = test_url.split('/')[-1:][0]
        ending_concatanator = "-master"
        final_url = engine_root+concatenator+extracted_file_name+ending_concatanator
        os.chdir(final_url)
        DIRS = os.getcwd()
        f=0
        door_list=[]
        data=[]
        cypher_graph = []
        for root, folder, files in os.walk(DIRS):
            while f==0:
                    split_root = root.split('/')
                    len_split_root =len(split_root)-1
                    f=+1
            new_root = root.split('/')[len_split_root:]
            s = []
            for r in reversed(new_root):
                r =''.join([i for i in r if not i.isdigit()])
                for c in string.punctuation:
                    r=r.replace(c,"")
                s.append(r)
            s = '_'.join(s)
            for fol in folder:
                t =''.join([i for i in fol if not i.isdigit()])
                for f in string.punctuation:
                    t=t.replace(f,"")
                print("CREATE ({b})-[:CONTAINS]->({a}_{b})".format(a=t,b=s))
                cypher_graph.append("CREATE ({b})-[:CONTAINS]->({a}_{b})".format(a=t,b=s))
            for fil in files:
                t =''.join([i for i in fil if not i.isdigit()])
                for f in string.punctuation:
                    t=t.replace(f,"")
                print("CREATE ({b})-[:CONTAINS]->({a}_{b})".format(a=t,b=s))
                cypher_graph.append("CREATE ({b})-[:CONTAINS]->({a}_{b})".format(a=t,b=s))

        data=cypher_graph


        return render_template('engine.html', data=data)

    else:
        return render_template('index.html')


@app.route('/gme')
def gme():
    return render_template('test2.html', message=message)
