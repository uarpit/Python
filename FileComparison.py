'''
Created on Aug 29, 2017
@author: Arpit Ubale
Description: 
This program was written to help during the testing phase of the project to find the differences between 
before and after target files generated during the ETL process.
The program takes two zip files (before and after) and compares individual files to find the differences.
The comaprison is based on specific columns in each file (calling those primary keys).
A dictionary is build with primary keys begin defined for each file at the begining of the program.
Then the programs extarcts the files, removes the headers, sorts the files respectively and collects the differences 
for each set of files in a seperate output file.
'''

import shutil
import operator
import csv
import zipfile
import os
import sys
import re

def file_srt(file_name,p_key):
    with open(file_name, "r", encoding='UTF8') as file:
        filtered = (line.strip() for line in file)
        f_csv = csv.reader(filtered,delimiter=",")
        next(f_csv,None)            # skip UTF-8 (first line)
        next(f_csv,None)            # skip Headers (second line)
        #Sort the file data based on the p_key and write it into a new file
        sort_cont = sorted(f_csv,key=operator.itemgetter(*p_key)) # *p_key - is used to iterate through all the p_key values
        srt_csv = file_name.replace(".","_srtd.")
        with open(srt_csv, 'w', encoding='UTF8') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', lineterminator='\n')
            for x in sort_cont:
                writer.writerow(x)

def zip_extract(zip_file,target_path):
    
    #Extract all the files from the input zip file
    with zipfile.ZipFile(zip_file,"r") as zip_ref:
        zip_ref.extractall(target_path)
        #for name in zip_ref.namelist():
            #print(name)



def main(arg):
    
    #1 Declare the primary keys for each file in dictionary
    p_key_dict = {"SupplierIDs.csv":[2,1], "SupplierOrganizations.csv":[5],"PreferredVendorFlag.csv":[0]}
    sap_key_dict = {"Supplier.csv":[1], 
                    "SupplierLocation.csv":[4],
                    "SupplierLocationSupplement.csv":[0],
                    "PurchaseOrgSupplierCombo.csv":[1,0],
                    "RemittanceLocation.csv":[5],
                    "RemittanceLocationDetails.csv":[3],
                    "SLRemittanceInformation.csv":[0],
                    "SLRemittanceInformationDetails.csv":[2,0],
                    "BankInformation.csv":[0]
                    }
    ora_key_dict = {"Supplier.csv":[0], 
                    "SupplierLocation.csv":[13,4],
                    "SupplierLocationSupplement.csv":[0],
                    "SupplierPaymentBankLocation.csv":[8],
                    "RemittanceLocation.csv":[5],
                    "RemittanceLocationDetails.csv":[3],
                    "SLRemittanceInformation.csv":[0],
                    "SLRemittanceInformationDetails.csv":[0]
                    }
    #1
    print("Primary keys initialized in a dictionary.")
    
    os.chdir("C:/Personal/09126629/Documents/MDM/Ariba/Mybuy/Extracts")
    print("Working directory set to {}".format(os.getcwd()))
    
    b_dir = os.getcwd()+ "/before" #create a folder for before files
    if os.path.exists(b_dir):
        print("\n" + "Before exists, deleting the before directory..")
        shutil.rmtree(b_dir)
        
    zip_extract(arg[0],b_dir)
    
    a_dir = os.getcwd()+ "/after" #create a folder for after files
    if os.path.exists(a_dir):
        print("After exists, deleting the after directory..")
        shutil.rmtree(a_dir)
    if str(arg[0]).split(".")[1] == 'zip':
        zip_extract(arg[1],a_dir)
    print("Created before and after directories" + "\n")
    
    #Extract the alphabet portion of the first input file name append it with .csv and write the results in that file
    result_f_name = re.split(r'(\d+)',arg[0])[0] + ".csv"
    result = open(result_f_name, "w", encoding='UTF8') 
    
    #2 Selecting the correct dictionary by searching for 'GBL', 'SAP', 'ORA' strings
    if arg[0][0:3] == 'GBL':
        if arg[0][8:11] == 'SAP':
            select_dict = sap_key_dict
            print("Dictionary set to Global child SAP file" + "\n")
        elif arg[0][8:11] == 'ORA':
            select_dict = ora_key_dict
            print("Dictionary set to Global child ORA file" + "\n")
        else:
            select_dict = p_key_dict
            print("Dictionary set to Global Parent file" + "\n")
    else:
        if arg[0][5:8] == 'SAP':
            select_dict = sap_key_dict
            print("Dictionary set to EUR child SAP file" + "\n")
        elif arg[0][5:8] == 'ORA':
            select_dict = ora_key_dict
            print("Dictionary set to EUR child ORA file" + "\n")
        else:
            select_dict = p_key_dict
            print("Dictionary set to EUR Parent file" + "\n")
    #2
    
    with zipfile.ZipFile(arg[0],"r") as zip_ref:
        for name in zip_ref.namelist():
            #3 Extract filenames inside zipfile 
            #3 For each filename Create a new files by sorting them on the p_key from the dictionary
            print("Comparing {} file..".format(name))
            b_s_file = b_dir + "/" + name 
            
            p_key = select_dict[name]
            file_srt(b_s_file,p_key)
            
            a_s_file = a_dir + "/" + name
            file_srt(a_s_file,p_key)
            #3
            
            result.write(name +"\n" + "\n")
            
            #srt_f1 = b_s_file + "_srtd"
            srt_f1 = b_s_file.replace(".","_srtd.")
            f1 = open(srt_f1, "r", encoding='UTF8')
            line1 = f1.readline()          # read line from before sorted file
        
            #srt_f2 = a_s_file + "_srtd"
            srt_f2 = a_s_file.replace(".","_srtd.")
            f2 = open(srt_f2, "r", encoding='UTF8')
            line2 = f2.readline()          # read line from after sorted file
            
            none_len=len(line1.split(",")) # get the number of columns to fill 'Nones' from the sorted file
            empty_str = ['None']* none_len # Generate 'none' string
    
            while (line1 or line2):

                if not(line2):            # if second file becomes empty write the line from the first file into result
                    line_tmp = line1.strip("\n") + "," + ",".join(empty_str) + "\n"
                    result.write(line_tmp)
                    line1 = f1.readline()
                elif not(line1):          # if first file becomes empty write the line from the second file into result
                    line_tmp=",".join(empty_str) + "," + line2
                    result.write(line_tmp)
                    line2 = f2.readline()
                else: 
                    l_line = ''
                    for x in p_key:
                        l_line += line1.split(",")[x] #join all the p_key column values into single value for comparison
                    m_line = ''
                    for x in p_key:
                        m_line += line2.split(",")[x] #join all the p_key column values into single value for comparison
                    if ( l_line > m_line ):           #if first p_key combination is greater then write line2 and increment pointer in second file
                        line_tmp=",".join(empty_str) + "," + line2
                        result.write(line_tmp)
                        line2 = f2.readline()
                    elif ( l_line < m_line ):         #if second p_key combination is greater then write line1 and increment pointer in first file
                        line_tmp = line1.strip("\n") + "," + ",".join(empty_str) + "\n"
                        result.write(line_tmp)
                        line1 = f1.readline()
                    else:
                        line1 = f1.readline()         #if both p_key values are equal then just move to next line
                        line2 = f2.readline()
                
            f1.close
            f2.close
            print("{} file comparison complete.".format(name))
            result.write("\n")
    result.close
    print("\n" + "Comparison result is ready in {} file.".format(result_f_name))

if __name__ == '__main__':
    main(sys.argv[1:])
   
