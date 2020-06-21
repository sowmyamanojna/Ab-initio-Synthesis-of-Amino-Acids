import os
import csv
from calculate_G_S_H import *

def get_lib_data(libraries_list, temperature, path):
    # libraries_list = rmg_link_lists()

    H_lists = []
    S_lists = []
    G_lists = []

    H_list = []
    S_list = []
    G_list = []

    for lib in libraries_list:
        os.chdir(path)

        compound_list = os.listdir()        

        directory = f"{lib}_data"
        if os.path.exists(f"{directory}/csv"):
            print("Initial data is available")
            os.chdir(f"{directory}/csv")
        
            compound_list = os.listdir()

            for file_name in compound_list:
                fin = open(file_name)
                reader = csv.reader(fin)
                data = []
                if (temperature > 100 and temperature < 1074.56):
                    for i in reader:
                        data.append(float(i[0]))
                else:
                    for i in reader:
                        data.append(float(i[1]))

                H = calculate_H(data, temperature)
                S = calculate_S(data, temperature)
                G = calculate_G(S, H, temperature)

                H_list.append(H)
                S_list.append(S)
                G_list.append(G)

            H_lists.append(H_list)
            S_lists.append(S_list)
            G_lists.append(G_list)

    return [H_lists, S_lists, G_lists]


def get_single_compound_data(lib, temperature, path, file_name):
    # Code to calculate the H, S and G values for specific compound
    os.chdir(path)
    os.chdir('..')  

    directory = f"{lib}_data"    
    if os.path.exists(f"{directory}/csv"):
        os.chdir(f"{directory}/csv")
        
        fin = open(file_name)
        reader = csv.reader(fin)
        data1 = []
        data2 = []

        for row in reader:
            data1.append(float(row[0]))
            data2.append(float(row[1]))
            
        if (temperature > data1[0] and temperature < data1[1]):
            # print('Choosing from data 1')
            data = data1[2:]
        elif (temperature > data2[0] and temperature < data2[1]):
            # print('Choosing from data 2')
            data = data2[2:]
        else:
            print("The enquired compound doesn't have data for the temperature provided.")

        H = calculate_H(data, temperature)
        S = calculate_S(data, temperature)
        G = calculate_G(H, S, temperature)
        
        os.chdir(path)
        return (H, S, G)
    else:
        print("The file requested is unavailable")

if __name__ == '__main__':
    lib = "GRI-Mech3.0"
    temperature = 700 
    path = os.getcwd()
    file_name = "13.csv"
    (_, _, G) = get_single_compound_data(lib, temperature, path, file_name)
    print(G)