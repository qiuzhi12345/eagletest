#!/usr/bin/env python

import os, sys
import shutil
import getopt
import platform

def check_target_path(path=""):
    if not os.path.exists(path):
        print path + " is not exists"
        return False, False, False
    else:
        if os.path.isdir(path):
            file_list = os.listdir(path)
            if "index.rst" in file_list:
                return path, os.path.split(path)[1], "index"
            else:
                print "can't find index.rst in " + path
                return False, False, False
        else:
            return os.path.split(path)[0], os.path.splitext(os.path.split(path)[1])[0], os.path.splitext(os.path.split(path)[1])[0]

def new_conf(target_path, docname, master_doc):
    with open("./script/conf.py") as fid, open("./_build/%s/conf.py"%(os.path.split(target_path)[1]), 'w') as ofid:
        for line in fid.readlines():

            if line.find("root_path=\"../../\"") != -1:
                ofid.write("root_path=\"../../../../\"\n")
            elif line.find("eagletest") != -1:
                ofid.write(line.replace("eagletest", docname))
            elif line.find("master_doc = \'index\'") != -1:
                ofid.write(line.replace("index", master_doc))
            else:
                ofid.write(line)

    with open("./script/Makefile") as fid, open("./_build/Makefile", 'w') as ofid:
        for line in fid.readlines():
            if line.find("source") != -1:
                ofid.write(line.replace("source", os.path.split(target_path)[1]))
            elif line.find("eagletest") != -1:
                ofid.write(line.replace("eagletest", docname))
            else:
                ofid.write(line)

    with open("./script/make.bat") as fid, open("./_build/make.bat", 'w') as ofid:
        for line in fid.readlines():
            if line.find("source") != -1:
                ofid.write(line.replace("source", os.path.split(target_path)[1]))
            elif line.find("eagletest") != -1:
                ofid.write(line.replace("eagletest", docname))
            else:
                ofid.write(line)



def main():
    spath = os.path.split(os.getcwd())
    if spath[1] != "docs" or os.path.split(spath[0])[1] != "rftest":
        print spath
        print "PATH %s"%os.getcwd()
        print "Please goto directory \"py_script/docs\", then run"
        exit(-1)


    opts,args = getopt.getopt(sys.argv[1:],'-h-p-f:-d:-m:',['html','pdf', 'format', "docname", "masterdoc"])
    t_type = "html"
    docname_autodec = True
    masterdoc_autodec = True
    for opt_name,opt_value in opts:
        if opt_name in ('-h','--html'):
            t_type = "html"
        elif opt_name in ('-p','--pdf'):
            t_type = "latexpdf"
        elif opt_name in ('-f','--format'):
            t_type = opt_value
        elif opt_name in ('-d','--docname'):
            docname_autodec = False
            argv_doc_name = opt_value
        elif opt_name in ('-m','--masterdoc'):
            masterdoc_autodec = False
            argv_master_doc = opt_value

    target_list = args

    if len(target_list) == 0:
        print "errror: too few arguments"
        exit(-2)

    if not os.path.exists("_build"):
        os.mkdir("_build")
        print "mkdir _build"

    for target in target_list:
        print "*"*10
        print target
        print "*"*10
        if target == "clean":
            shutil.rmtree("./_build/")
            continue

        # ==============
        doc_path, doc_name, master_doc = check_target_path(target)
        if not docname_autodec:
            doc_name = argv_doc_name
        if not masterdoc_autodec:
            master_doc = argv_master_doc

        # ==============
        if doc_path == False:
            exit(-3)
        print "DOC   name:", doc_name
        print "DOC   path:", doc_path
        print "DOC Master:", master_doc
        cpSRC = doc_path
        cpTAG = "./_build/" + os.path.split(doc_path)[1]
        if os.path.exists(cpTAG):
            shutil.rmtree(cpTAG)
        shutil.copytree(cpSRC, cpTAG)

        new_conf(doc_path, doc_name, master_doc)
        os.chdir("./_build/")
        try:
            if platform.platform().find("Win") != -1:
                os.system("make.bat %s"%(t_type))
            else:
                os.system("make %s"%(t_type))
        except:
            print "fail"
        os.chdir("../")

if __name__ == "__main__":
    main()
