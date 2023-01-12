import glob
import shutil
import os
from zipfile import ZipFile

source_path = '../source/*'
destination_path = '../destination'

postfix = [1,2,3]
while True:
    source_object = glob.glob(source_path)
   

    if len(source_object) > 0:
        object_path = source_object[0]
        object_name = object_path.split('\\')[-1].split('.')
        prefix = object_name[0]
        postfix2 = object_name[1]
        

        if(postfix2 == 'txt'):
            my_file=[]
            allFile=[] 
            create_zip_file=prefix
            zip_fileName=create_zip_file+'.zip'
            my_src_file=prefix+'.'+postfix2
            shutil.copy(object_path,'.')

            with open(my_src_file,'r') as files:
                my_file=files.readlines()
                files.close

            for item in range(len(postfix)):
                filename = prefix + '_' + str(item+1) + '.' + postfix2
                allFile.append(filename)
                with open(filename,'w') as files:
                        for items in range(0,(item+1)*10):
                            itm=my_file[items]
                            files.write(itm)

            with ZipFile(zip_fileName,'w') as zip:
                for file in allFile:
                    zip.write(file)
                    os.remove(file)
                shutil.copy(object_path,f'{destination_path}/{zip_fileName}')
                zip.extractall(destination_path)

            os.remove(object_path)
            os.remove(object_path.split('\\')[-1])
            os.remove(zip_fileName)
            os.remove(f'{destination_path}/{zip_fileName}')
        if(postfix2 =='py'):
            try:
                exec(open(object_path).read())
            except Exception as ex:
                print(ex)
            os.remove(object_path)
    
    