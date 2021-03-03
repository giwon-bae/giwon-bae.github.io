import subprocess
subprocess.SW_HIDE = 1
r = subprocess.Popen(r'D:\DevProg\HFC3.0\resource\Distrib-x64-2017-08-21\hfAnalyzer -o'+inputFileName, shell=True).wait()
if r == 1: 
    print('running error')