import glob
import os
from random import shuffle
from shutil import copyfile
import argparse
input_dir = 'input/'
output_dir = 'output/'
DIV_INTO = 5

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Merge and shuffle dataset")
    parser.add_argument('--inpdir', dest='inpdir', default= 'input/')
    parser.add_argument('--outdir', dest='outdir', default= 'output/')

    args = parser.parse_args()
    input_dir = args.inpdir
    output_dir = args.outdir

    if (not os.path.exists(output_dir)):
        os.makedirs(output_dir)
        print('created')

    def saveList2File(lst, filename):
        fo = open(filename,"w")
        for file_name in lst:
            fo.write(file_name+'\n')

        fo.close()

    labels = glob.glob(input_dir+'/*')

    # list all files in folders _ labels
    all_files = []
    labels_dict = {}

    fo = open(output_dir+'dict.txt',"w")
    for i, label in enumerate(labels):
        print(label)
        labels_dict[os.path.basename(label)] = i
        fo.write(str(i) +' '+ os.path.basename(label)+'\n')
        files = glob.glob(label+'/*.jpg')
        all_files += files
        # lab_name = os.path.basename(label)
        # fo = open(lab_name+'.txt',"w")
        # for file_name in files:
        #     fo.write(file_name+'\n')
        # fo.close()
    fo.close()
    print('Total files: '+ str(len(all_files)))
    saveList2File(all_files,'all_files.txt')
    shuffle(all_files)



    n = len(all_files)/DIV_INTO
    r = len(all_files)%DIV_INTO
    for i in range(DIV_INTO):
        tmp = all_files[i:i+n+int(i<r)]
        print('part '+str(i)+' have '+str(len(tmp))+' images' )
        saveList2File(tmp,str(i).zfill(2)+'.txt')
        out_folder = output_dir+str(i).zfill(2)
        if (not os.path.exists(out_folder)):
            os.makedirs(out_folder)
        
        fo = open(output_dir+'labels_'+str(i).zfill(2)+'.txt',"w")
        for i, file_name in enumerate(tmp):
            copyfile(file_name,out_folder+'/'+str(i).zfill(5)+'.JPG')
            lb = os.path.basename(os.path.dirname(file_name))
            fo.write(str(labels_dict[lb])+'\n')
        fo.close()