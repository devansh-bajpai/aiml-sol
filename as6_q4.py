# # Solution 4:

# # Reading CSV:
# import csv
# with open('names.csv', 'r') as fobj:
#     csv_reader = csv.reader(fobj)

#     for line in csv_reader:
#         print(line)

# # Writing CSV:
# import csv
# with open('myCSV.csv', 'w', newline='') as fobj:
#     csv_writer = csv.writer(fobj, delimiter=',')
#     csv_writer.writerow(['devansh', 'bajpai', 'devansh@mnnit'])


# # Reading JPG File
# import cv2

# myImg = cv2.imread('rose.jpg')
# cv2.imshow("original image", myImg)
# cv2.waitKey(0)

# # Reading TSV File
# import csv

# with open('myTSV.tsv', 'r') as fobj:
#     csv_reader = csv.reader(fobj, delimiter='\t')
#     for line in csv_reader:
#         print(line)