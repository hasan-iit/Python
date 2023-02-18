import csv
with open("python.csv",'w',newline='') as csvfile:
    fld = ['firstname','lastname','age']
    wri = csv.DictWriter(csvfile,fieldnames=fld)
    wri.writeheader()
    wri.writerow({'firstname':'Shahed','lastname':'Imam','age':31})
    wri.writerow({'age':30,'firstname':'Jahed'})


#=================================================================
# import csv
# with open("python.txt",newline='') as csv_file:
#     csv_reader = csv.DictReader(csv_file,delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count==0:
#             print(f'{",".join(row)}')
#             line_count = line_count+1
#         # print(list(row.keys()))
#         print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')


#===================================================
# import csv
# with open('python.txt') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#     print(line_count)