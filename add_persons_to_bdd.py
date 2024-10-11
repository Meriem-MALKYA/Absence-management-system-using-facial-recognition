
import cv2
import face_recognition
import os
import sqlite3

print("Start\n")
path = 'persons'
images = []
classNames = []
personsList = os.listdir(path)

for cl in personsList:
    curPersonn = cv2.imread(f'{path}/{cl}')
    images.append(curPersonn)
    classNames.append(os.path.splitext(cl)[0])


def findEncodeings(image):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

list_known = findEncodeings(images)

db = sqlite3.connect('database.db')


cur = db.cursor()
for element in classNames:
    tr = element.split(",")
    cur.execute(f"insert into infos values ('{tr[0]}','{tr[1]}','{tr[2]}','{tr[3]}')")

cr = db.cursor()
for a in list_known:
    cr.execute(f"insert into data values({a[0]},{a[1]},{a[2]},{a[3]},{a[4]},{a[5]},{a[6]},{a[7]},{a[8]},{a[9]},{a[10]},{a[11]},{a[12]},{a[13]},{a[14]},{a[15]},{a[16]},{a[17]},{a[18]},{a[19]},{a[20]},{a[21]},{a[22]},{a[23]},{a[24]},{a[25]},{a[26]},{a[27]},{a[28]},{a[29]},{a[30]},{a[31]},{a[32]},{a[33]},{a[34]},{a[35]},{a[36]},{a[37]},{a[38]},{a[39]},{a[40]},{a[41]},{a[42]},{a[43]},{a[44]},{a[45]},{a[46]},{a[47]},{a[48]},{a[49]},{a[50]},{a[51]},{a[52]},{a[53]},{a[54]},{a[55]},{a[56]},{a[57]},{a[58]},{a[59]},{a[60]},{a[61]},{a[62]},{a[63]},{a[64]},{a[65]},{a[66]},{a[67]},{a[68]},{a[69]},{a[70]},{a[71]},{a[72]},{a[73]},{a[74]},{a[75]},{a[76]},{a[77]},{a[78]},{a[79]},{a[80]},{a[81]},{a[82]},{a[83]},{a[84]},{a[85]},{a[86]},{a[87]},{a[88]},{a[89]},{a[90]},{a[91]},{a[92]},{a[93]},{a[94]},{a[95]},{a[96]},{a[97]},{a[98]},{a[99]},{a[100]},{a[101]},{a[102]},{a[103]},{a[104]},{a[105]},{a[106]},{a[107]},{a[108]},{a[109]},{a[110]},{a[111]},{a[112]},{a[113]},{a[114]},{a[115]},{a[116]},{a[117]},{a[118]},{a[119]},{a[120]},{a[121]},{a[122]},{a[123]},{a[124]},{a[125]},{a[126]},{a[127]})")
db.commit()
db.close()

print("End ! Add Successful ")