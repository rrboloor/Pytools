import socket
import sys
import string
import datetime

#read parameters.
successCount=0
failCount=0
invalidCount=0
invalidDataLines=[]



def prep_params(inputFile):
    """ This function reads input file and returns a list of tuples. each tuple containing host and port.
    [(host1,port1),(host2,port2)]
    """
    global invalidCount,invalidDataLines
    items =[]
    currLine=0  #lineCounter
    try:
        with open(inputFile,'r') as ip :
            temp_lines= ip.readlines()
            for line in temp_lines:
                currLine=currLine+1
                if(":" not in line):
                    invalidCount=invalidCount+1
                    invalidDataLines.append(currLine)
                    continue
                host,port = line.strip().split(":")
                if(host == "" or port == ""):
                    invalidCount=invalidCount+1
                    invalidDataLines.append(currLine)
                    continue
                items.append((host,port,currLine))
                
    except Exception as e:
        print("There was some error reading file or data")
        print(e)
        


    
    return items

def connect_to_port(ip,port):
    result="Failed"
    parameter=(ip,int(port))
    mysoc=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        mysoc.connect(parameter)
        return "Success"
    except:
        return "Failed"
    finally:
        mysoc.close()




#main program
#check if filename is given as argument.
if(len(sys.argv)) ==1 :
    print("Please give me the filename")
    exit(1)

#have the parameter file now.
data=prep_params(sys.argv[1])
outputfile=sys.argv[1]+".result.log"

try :
    with open(outputfile,'a') as op:
        op.write("\n----------------------------------------------\n")
        op.write("Beginning Tests from file {}\n".format(sys.argv[1]))
        op.write("Run at {}\n".format(datetime.datetime.now()))
        op.write("----------------------------------------------\n")
        for d in data:
            host,port,lineNo=d
            print("{} Checking Connection to {} on port {}".format(lineNo,host,port))
            result=connect_to_port(host,port)
            if(result=="Success"):
                successCount=successCount+1
            else:
                failCount=failCount+1
            op.write( "{} Checking connection on host {}, and port {} ==> {}".format(lineNo,host,port,result))
            op.write("\n")
        op.write("---------------summary--------------\n")
        op.write(" Total Success = {}\n Total Failed={}\n Invalid Data count={}\n in lines {}".format(successCount,failCount,invalidCount,invalidDataLines))
        op.write("\n=============end===================n")
except Exception as e:
    print(e)    