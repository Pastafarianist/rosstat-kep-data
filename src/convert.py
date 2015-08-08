# -*- coding: utf-8 -*-
"""
"""

from batch import doc_to_database
from batch import make_csv_with_labels, csv_to_database
from batch import make_csv_in_stei_folder
from database import wipe_db_tables
from label_csv_by_specification import check_vars_not_in_labelled_csv 
import os

src_doc = ["../data/1-07/1-07.doc", "../data/ind06/tab.doc", "../data/minitab/minitab.doc"] 

def batch1():
    print("\n### Trial 1")
    p = os.path.abspath("../data/1-07/1-07.doc")
    doc_to_database(p)    
    check_vars_not_in_labelled_csv(p)
    
def batch2():
    print("\n### Trial 2")
    # omit making raw csv - as it is long 
    c = os.path.abspath("../data/minitab/minitab.csv")
    t = make_csv_with_labels(c)
    csv_to_database(t) 
    check_vars_not_in_labelled_csv(c)

    
def batch3():
    print("\n### Trial 3")
    # omit making raw csv - as it is long 
    c = os.path.abspath("../data/ind06/all_tab.csv") #all_tab got.csv
    t = make_csv_with_labels(c)
    csv_to_database(t) 
    check_vars_not_in_labelled_csv(c)
    
def batch4():
    folder = "../data/ind06/"
    make_csv_in_stei_folder(folder)
    
if __name__ == "__main__":
    wipe_db_tables()   
    batch4()
    # TODO - import from single table
    # import query   