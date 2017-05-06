# crm_scraper
from __future__ import print_function
import os
import sys
import pandas as pd
import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
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
    df = df[df['t']<=0.01]  # restrict to tmax = 0.01
    ary = df.as_matrix(columns=['t','T','U','p'])
    t = ary[:,0]
    T = ary[:,1]
    U = ary[:,2]
    p = ary[:,3] / 1.0e5  # convert Pa to bar
    return t, T, U, p


def single_plot(x, y, var_, imgFmt='.eps'):
    opts = {
        'p': {
            'ylim': [np.min(y)*0.95,np.max(y)*1.05],
            'ylabel': r'P [bar]'
        },
        'U': {
            'ylim': [-5, np.max(y)*1.05],
            'ylabel': r'|U| [m/s]'
        },
        'T': {
            'ylim': [np.min(y)*0.95, np.max(y)*1.05],
            'ylabel': r'T [K]'
        }
    }
    varOpts = opts.get(var_)
    plt.figure()
    plt.plot(x, y, linewidth=2.0)
    plt.xlabel('t [sec]', family='serif', fontsize=16)
    plt.ylabel(varOpts['ylabel'], family='serif', fontsize=16)
    # plt.title(r'Pressure over time at x={0}'.format(x0), fontsize=20)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(True)
    plt.xlim([0,0.01])
    plt.ylim(varOpts['ylim'])
    # plt.show()
    plt.savefig(var_+'_plot'+imgFmt)


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


if __name__ == "__main__":
    dir_ = os.getcwd()
    csvFileName = 'data3.csv'
    subdir = 'postProcessing/sample'
    outPath = os.path.join(dir_,csvFileName)
    dirPath = os.path.join(dir_,subdir)
    csvPath = foam2csv(dirPath, outPath)
    # ---- Extract time plots from data ----
    x0 = 0.705  # position to plot values over time
    csvPath = os.path.join(dir_,csvFileName)
    df = pd.read_csv(csvPath)
    t, T, U, p = get_plot_data(df, x0)
    print('t=',t)
    print('p=',p)
    print('T=',T)
    print('U=',U)
    imgFmt = '.eps'
    single_plot(t, p, 'p', imgFmt)
    single_plot(t, T, 'T', imgFmt)
    single_plot(t, U, 'U', imgFmt)
