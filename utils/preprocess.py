
import os 
from os import listdir
from os.path import isfile,join
import numpy as np
# the FMI_reader function reads the .las files that contain FMI resistivity values.
# the output of the function is two numpy arrays 
#1. data which is 2D array with 192 colums and rows equal to the number of depth samples 
#2. the depth array which is a 1D array and contains all the depth
# samples
def FMI_reader(path):
    # f = open(path, 'r')
    # content = f.readlines()
    # f.close()
    with open(path,'r') as file:
      content  = file.readlines()
    data = []
    depth = []
    rock_type = path.split('.')[0].split('_')[0].split('/')[-1]
    for L in content:
        L = L.split(' ')
        res = [st for st in L if st != "" and st != '\n']
        if res[0] == '~Ascii':
            continue
        elif res[0] == '~Version':
            break
        elif len(res) == 1:
            depth.append(float(res[0]))
        else:
            data.extend(list(map(float, res)))

    data = np.array(data)
    depth = np.array(depth)
    data = np.reshape(data, (-1, 192))

    return data, depth, rock_type


def read_all_data(path):
  """
  Path : path to where all your data folder 
  """
  # folder_location_in_drive= os.path.join(os.getcwd(),data_folder)
  file_names = [f for f in listdir(path) if( f.split('.')[-1]=='las' and isfile(join(path, f)))] #get list of the files with las extension 

  Data = []
  Depth = []
  Rock_Type = []

  for file in file_names:
    path_to_file = os.path.join( os.path.join(path,file))
    data,depth,rock_type = FMI_reader(path_to_file)
    Data.append(data)
    Depth.append(depth)
    Rock_Type.append(rock_type)
  return Data,Depth,Rock_Type