# crm_scraper
from __future__ import print_function
import os
import sys
import pandas as pd
import csv
import numpy as np
# import matplotlib
# matplotlib.use('cairo')
import matplotlib.pyplot as plt


def main(dir_=os.getcwd()):
            # ----  Get data ----
    # Loop through post processed files
    subdir = 'postProcessing/sample'
    outPath = os.path.join(dir_,'data.csv')
    print('outpath=',outPath)
    print('dir_+subdir=',dir_+subdir)
    dirPath = os.path.join(dir_,subdir)
    csvPath = foam2csv(dirPath, outPath)

    # ---- Extract time plots from data ----
    x0 = 4.995  # position to plot values over time
    df = pd.read_csv(csvPath)
    t, T, U, p = get_plot_data(df, x0)
    plot_data(t, T, U, p, x0)


def get_plot_data(df, x0):
    df = df[df['x']==x0]  # restrict data to that spatial location
    print(df)
    df = df.sort_values(['t'])  # sort by increasing
    ary = df.as_matrix(columns=['t','T','U','p'])
    t = ary[:,0]
    T = ary[:,1]
    U = ary[:,2]
    p = ary[:,3]
    return t, T, U, p


def plot_data(t, T, U, p, x0):
    plt.plot(t, p)
    plt.xlabel('t', fontsize=22)
    plt.ylabel('p', fontsize=22)
    plt.title(r'Pressure over time at x={0}'.format(x0), fontsize=20)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.ylim([20000,100000])
    plt.show()


def foam2csv(dirPath, outPath):
    data = pd.DataFrame()
    for root, dirs, filenames in os.walk(dirPath):
        for fname in filenames:
            fpath = os.path.join(root, fname)
            t = os.path.basename(os.path.dirname(fpath))  # the directory name is the time step
            # print('fpath=',fpath,'  t=',t)
            with open(fpath,'r') as inFile:
                # print('t=',t,'  fpath=',fpath)
                if t == '0':  # initial condition, also set U=0.0
                    # print('init!')
                    tmpdf = pd.read_table(inFile, sep='\t', header=None, names=['x','T','p']) # read tab-delimited text file into tmp
                    tmpdf['U'] = 0.0
                else:
                    tmpdf = pd.read_table(inFile, sep='\t', header=None, names=['x','T','U','p']) # read tab-delimited text file into tmp
                tmpdf['t'] = float(t)  # add time step column
                data = data.append(tmpdf, ignore_index=True)
    # save dataframe to csv
    print(data)
    data = data.sort_values(['t','x'], ascending=[True, False])
    with open(outPath, 'w') as outFile:
        data.to_csv(outFile, index=False)
    return outPath

def convert_to_csv(ext='.xy', dir_=None):
    if not dir_:
        dir_ = os.getcwd()  # use default pwd
    fileList = []
    for root, dirs, filenames in os.walk(dir_):
        for fname in filenames:
            if fname.endswith(ext):
                fileList.append(fname)
                parse_text(os.path.join(root,fname))
    return fileList

def concatenate_files(ext='.xy', dir_=None, out_fname=None):
    if not dir_:
        dir_ = os.getcwd()  # use default pwd
    fileList = []
    if not out_fname:
        out_fname = 'data.txt'
    # outFile = open(os.path.join(dir_,out_fname),'w')
    i = 0
    for root, dirs, filenames in os.walk(dir_):
        i += 1
        print(i)
        print(root)
        print(dirs)
        print(filenames)
        for fname in filenames:
            if fname.endswith(ext):
                fileList.append(fname)
                fpath = os.path.join(root, fname)
                dirname = os.path.basename(os.path.dirname(fpath))
                print(dirname)
                # print('PATH=',fpath,'DIRNAME=',os.path.dirname(fpath),'BASENAME=',os.path.basename(fpath))
                with open(fpath, 'r') as f:
                    pass
                    # outFile.write(f.read())
    # outFile.close()

if __name__ == "__main__":

    main()
    # return
    # # ---- Extract time plots from data ----
    # x0 = 0.995  # position to plot values over time
    # csvPath = os.path.join(os.getcwd(),'data.csv')
    # df = pd.read_csv(csvPath)
    # t, T, U, p = get_plot_data(df, x0)
    # plt.plot(t, p)
    # plt.xlabel('t', fontsize=22)
    # plt.ylabel('p', fontsize=22)
    # plt.title(r'Pressure over time at x={0}'.format(x0), fontsize=20)
    # plt.xticks(fontsize=16)
    # plt.yticks(fontsize=16)
    # plt.ylim([20000,100000])
    # plt.show()
    # # plt.savefig('plot.png')
    # # print('t=',t)
    # # print('T=',T)
    # # print('U=',U)
    # print('p=',p)
