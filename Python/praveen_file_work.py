import random

def create_result_file(file_path):
    with open(file_path, 'w') as file:
        
        for i in range(1, 31):
            
            name = f"Student{i}"
            reg_no = f"Reg{i:04}"
            grades = ['O', 'A', 'B', 'C', 'D', 'U']  
            points = {'O': 10, 'A': 9, 'B': 8, 'C': 7, 'D': 6, 'U': 0}
            grd=[]
            
            for i in range(5):
                g=random.choice(grades)
                grd.append(g)
            total_points = sum(points[grade] for grade in grd[:5])
            percentage = (total_points / 50) * 100  
            file.write(f"{name},{reg_no},{','.join(grd)},{total_points},{percentage:.2f}%\n")


def read_result_file(file_path):
    with open(file_path, 'r') as file:
        print(file.read())

def analyze_results(input_file, output_file):
    I=[]
    II=[]
    III=[]
    IV=[]
    V=[]
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            data = line.strip().split(',')
            
            percentage = float(data[-1].rstrip('%'))
            
            if percentage >= 90:
                I.append(data[0])
                
            elif 80 <= percentage < 90:
                II.append(data[0])
                
            elif 70 <= percentage < 80:
                III.append(data[0])
                
            elif 'U' in data[2:7]: 
                V.append(data[0])
                
            else:
                IV.append(data[0])
        
        
        outfile.write("\n--------------------------------------------------------------------------------------------------------------------------\n")
        outfile.write("--------------------------------------------------------------------------------------------------------------------------\n")        
        outfile.write("\nStudents scoring 90% and above :\n\n")
        for x in I:
            outfile.write(f"{x}\n")
        else:
            outfile.write("......")
               
        outfile.write("\n--------------------------------------------------------------------------------------------------------------------------\n")
        outfile.write("--------------------------------------------------------------------------------------------------------------------------\n")
        outfile.write('\nStudents scoring 80% and above but below 90% :\n\n')
        for x in II:
            outfile.write(f"{x}\n")
        else:
            outfile.write("......")
                
        outfile.write("\n--------------------------------------------------------------------------------------------------------------------------\n")
        outfile.write("--------------------------------------------------------------------------------------------------------------------------\n")
        outfile.write('\nStudents scoring 70% and above but below 80% :\n\n')
        for x in III:
            outfile.write(f"{x}\n")
        else:
            outfile.write("......")
              
        outfile.write("\n--------------------------------------------------------------------------------------------------------------------------\n")
        outfile.write("--------------------------------------------------------------------------------------------------------------------------\n")
        outfile.write('\nStudents scoring below 70% :\n\n')
        for x in IV:
            outfile.write(f"{x}\n")
        else:
            outfile.write("......")
            
        outfile.write("\n--------------------------------------------------------------------------------------------------------------------------\n")
        outfile.write("--------------------------------------------------------------------------------------------------------------------------\n")
        outfile.write('\nStudents having arrear :\n\n')
        for x in V:
            outfile.write(f"{x}\n")
        else:
            outfile.write("......")
               
        outfile.write("\n--------------------------------------------------------------------------------------------------------------------------\n")
        outfile.write("--------------------------------------------------------------------------------------------------------------------------\n")
         
file_path = 'result.txt'
create_result_file(file_path)
read_result_file(file_path)
analyze_results(file_path, 'analysis.txt')
