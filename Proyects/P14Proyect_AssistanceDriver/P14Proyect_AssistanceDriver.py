import os
import cv2
import face_recognition as fr
import numpy as np

# Data Base

dir_employees = 'Proyects\P14Proyect_AssistanceDriver\Employees'

employees_list = os.listdir(dir_employees)

db_employees = []

print(employees_list)

for name in employees_list:
    
    actual_image = cv2.imread(f'{dir_employees}\\{name}')

    actual_image_cvt = cv2.cvtColor(actual_image, cv2.COLOR_BGR2RGB)
    
    actual_image_encoded = fr.face_encodings(actual_image_cvt)[0]
    
    db_employees.append(dict([('name',os.path.splitext(name)[0]),('img_code',actual_image_encoded),('img',actual_image),('assist_log',0)]))

print([f'{emp['name'],emp['assist_log']}' for emp in db_employees])

# Function

def face_search():

    captureimg = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    succesimg, cam_img = captureimg.read() 
    if not succesimg:
        
        print('No image taken')
        
        face_in_cam_select = [cv2.imread('Proyects\\P14Proyect_AssistanceDriver\\Employees\\Brad Pitt.jpg'), cv2.imread('Practices\\Practice 14\\FotoB.jpg')]

        face_select = int(input(f'Select face from directory, 1 or 2: '))

        face_in_cam = face_in_cam_select[face_select-1]
        
        face_in_cam_cvt = cv2.cvtColor(face_in_cam, cv2.COLOR_BGR2RGB)

        face_map = fr.face_locations(face_in_cam_cvt)[0]

        face_encoded = fr.face_encodings(face_in_cam_cvt)[0]

        cv2.rectangle(face_in_cam, (face_map[3],face_map[0]),(face_map[1],face_map[2]),(0,255,0),3)

        employee_exist = False

        for emp in db_employees:    

            if fr.compare_faces([emp['img_code']], face_encoded, 0.4) == np.True_:
            
                print(f'Employee: {emp["name"]}')

                emp['assist_log'] += 1

                match_value = fr.face_distance([face_encoded],emp['img_code'])

                cv2.putText(face_in_cam,f'Match: {match_value*100}%',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

                cv2.imshow('Data Base Match',emp['img'])
                cv2.imshow('Face', face_in_cam)
                employee_exist = True

        if employee_exist == False:
            print('No match with any registered employee')


        for emp in db_employees:
            print(f'''
                Name: {emp['name']}
                Assistance: {emp['assist_log']}
                *******************************
                ''')
    else:
        face_in_cam = cam_img

        #face_in_cam = cv2.imread('Proyects\\P14Proyect_AssistanceDriver\\Employees\\Brad Pitt.jpg')
        #face_in_cam = cv2.imread('Practices\\Practice 14\\FotoB.jpg')
        
        face_in_cam_cvt = cv2.cvtColor(face_in_cam, cv2.COLOR_BGR2RGB)

        face_map = fr.face_locations(face_in_cam_cvt)[0]

        face_encoded = fr.face_encodings(face_in_cam_cvt)[0]

        cv2.rectangle(face_in_cam, (face_map[3],face_map[0]),(face_map[1],face_map[2]),(0,255,0),3)

        employee_exist = False

        for emp in db_employees:    

            if fr.compare_faces([emp['img_code']], face_encoded, 0.4) == np.True_:
            
                print(f'Employee: {emp["name"]}')

                emp['assist_log'] += 1

                match_value = fr.face_distance([face_encoded],emp['img_code'])

                cv2.putText(face_in_cam,f'Match: {match_value*100}%',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

                cv2.imshow('Data Base Match',emp['img'])
                cv2.imshow('Face', face_in_cam)
                employee_exist = True

        if employee_exist == False:
            print('No match with any registered employee')


        for emp in db_employees:
            print(f'''
                Name: {emp['name']}
                Assistance: {emp['assist_log']}
                *******************************
                ''')

face_search()

cv2.waitKey(0)