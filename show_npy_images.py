import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import argparse

import warnings
# filter warnings
warnings.filterwarnings('ignore')

def show_image_grid(npy_file, rows, columns):
    x_l = np.load(npy_file)
    img_size = x_l.shape[1]
    N = x_l.shape[0]

    if rows*columns >= N:
        print(f'Error:  invalid number of rows and columns, > number of images {rows*columns} >= {N}')
        return
        
    for i in range(0, rows):
        for j in range(0, columns):
            index = (i*columns + j)
            print(f'I: {i}, J: {j}, Index: {index}')
            plt.subplot(rows, columns, j + i*columns + 1)
            plt.imshow(x_l[index])
            plt.axis('off')

    plt.show()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file')
    parser.add_argument('-r', '--rows', type=int, default=5)
    parser.add_argument('-c', '--columns', type=int, default=5)

    args = parser.parse_args()

    if args.file is None:
        print(f'Requires an output file path')
        sys.exit(1)

    show_image_grid(args.file, args.rows, args.columns)

if __name__ == "__main__":
    main()
