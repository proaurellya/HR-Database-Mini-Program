# CASPTONE PROJECT 1
# CASE STUDY - EMPLOYEES DATA
# RAHMA AURELLYA
# JCDS 2204 007

import os
from datetime import date
import random

# Employee List
dummy4 = [
    {'employeeID':102145,
     'fullName':'Eli Utami',
     'age':29,
     'education':'S1',
     'position':'Data Engineer',
     'department':'IT',
     'salary': 9320000},

     {'employeeID':201985,
     'fullName':'Lucas Gunawan',
     'age':26,
     'education':'S2',
     'position':'Jr. Tax Audit',
     'department':'FINANCE',
     'salary': 8650000},

     {'employeeID':302243,
     'fullName':'Henrik Irawan',
     'age':30,
     'education':'S2',
     'position':'Head of Marketing',
     'department':'MARKETING',
     'salary':27800000},

     {'employeeID':502076,
     'fullName':'John Bonnie',
     'age':21,
     'education':'SMA',
     'position':'Staff Admin',
     'department':'ADMIN',
     'salary':4950000},

     {'employeeID':402218,
     'fullName':'Eza Hasbullah',
     'age':43,
     'education':'S3',
     'position':'Head of Talent',
     'department':'HR',
     'salary':55300000}
]

# Department List
deptList = [
    {'deptName': 'IT',
     'deptCode': 10},
     {'deptName': 'FINANCE',
     'deptCode': 20},
     {'deptName': 'MARKETING',
     'deptCode': 30},
     {'deptName': 'HR',
     'deptCode': 40},
     {'deptName': 'ADMIN',
     'deptCode': 50}
]

# Clear Screen Function for Windows
def clearScreen() :
    os.system('cls')

# Function mainMenu
def mainMenu() :
    print('+' + '-'*57 + '+')
    print('''   Selamat Datang di Program Employee Management System
                PT. Semoga Coding Lancar ''')
    print('+' + '-'*57 + '+')
    print('''Silahkan Pilih Angka Menu yang Tersedia:
    1. Tampilkan Data
    2. Menambahkan Data
    3. Update Data
    4. Hapus Data
    0. Exit Program''')

# Function Header Table
def headerTabl():
    gap = ' '*3
    header = f"{'ID':^6s}{gap}{'NAME':^20s}{gap}{'AGE':^3s}{gap}{'EDUCATION':^9s}{gap}{'POSITION':^20s}{gap}{'DEPARTMENT':11s}{gap}{'SALARY':^12}"
    print('='*100)
    print(header)
    print('='*100)

# Function Table Employee
def showListEmpl() :
    # Menampilkan Header Table
    headerTabl()
    # Menampilkan Isi Tabel Karyawan
    gap = ' '*3
    for i in range(len(dummy4)) :
        print(f"{dummy4[i]['employeeID']:6}{gap}{dummy4[i]['fullName']:20s}{gap}{dummy4[i]['age']:^3d}{gap}{dummy4[i]['education']:^9s}{gap}{dummy4[i]['position']:20s}{gap}{dummy4[i]['department']:^11s}{gap}{dummy4[i]['salary']:>12}")
    print('-'*100)

# Funcion Table Department
def showListDept():
    # Menampilkan Header Dept.
    gap = ' '*3
    header = f"{'NAME':^15}{gap}{'KODE DEPT.':^8}"
    print('='*29)
    print(header)
    print('='*29)

    # Menampilkan Isi Tabel Department
    for i in range(len(deptList)) :
        print(f"{deptList[i]['deptName']:<15}{gap}{deptList[i]['deptCode']:^8}")

# Function to Show a Certain Employee Data based on Their ID
def getEmplData(inputID) :
    found = False
    headerTabl()
    gap= ' '*3
    for i in dummy4:
        if i['employeeID'] == inputID:
            while True:
                print(f"{i['employeeID']:6d}{gap}{i['fullName']:20s}{gap}{i['age']:^3d}{gap}{i['education']:^9s}{gap}{i['position']:20s}{gap}{i['department']:^11s}{gap}{i['salary']:>12}")
                break
        elif found:
            print('EmployeeID Tidak Terdaftar.')

# Function to Generate ID based on Registration Date and Department
def generateID(deprt) :
    dCode = None 
    for i in deptList:
        if deprt == i['deptName']:
            dCode = i['deptCode']
            break
    if dCode is None:
        print('Departemen Tidak Terdaftar.')
        return
    
    global newID
    while True:
        tanggalMasuk = date.today()
        yearCode = str(tanggalMasuk.year)[-2:]
        randomID = f'{random.randint(0,99):2}'
        newID = f"{dCode}{yearCode}{randomID}"

        if newID not in dummy4:
            newID = int(newID)
            break
    
# ADD Employee // Menu 2
def addEmpl():
    while True: # NAMA
        nama = input('Masukkan Nama Karyawan: ').title()
        if not nama:
            print('Nama Wajib Diisi.')
            continue
        else:
            break
    while True: # USIA
        try:
            usia = int(input('Masukkan Usia Karyawan: '))
            if usia > 65:
                print('Karyawan sudah tua. Lebih baik pensiun!')
                continue
            elif usia < 15:
                print('Karyawan terlalu muda. Lebih baik sekolah!')
                continue
            else:
                break
        except ValueError :
            print('Masukkan Hanya Angka.')
    
    while True: # EDUCATION, POSITION
        education = input('Masukkan Pendidikan Terakhir: ').upper() 
        posisi = input('Masukkan Posisi Karyawan: ').title()
        break

    while True: # DEPARTMENT
        showListDept()
        department = input('Masukkan Nama Department Karyawan: ').upper()
        if not department:
            print('Department Wajib Diisi.')
            continue
        elif department not in [i['deptName'] for i in deptList]:
            print('Hanya Dapat Memasukkan Department yang Terdaftar.')
            continue
        else:
            break
    while True:
        salary = (input('Masukkan Gaji Karyawan: ')) # SALARY
        if not salary.isdigit() or len(salary) <= 10:
            print ('Gaji Karyawan dapat dimasukkan antara 10 sampai 999.999.999')
            continue
        else:
            break

    generateID(department)

    # Collecting data and add it to the table
    dummy4.append({
        'employeeID':newID,
        'fullName': nama,
        'age':usia,
        'education':education,
        'position':posisi,
        'department':department,
        'salary':int(salary)
        })
    showListEmpl()
    
# ADD New Department // Menu 2
def addDept():
    while True:
        namaDept = input('Masukkan Nama Departemen Baru: ').upper()
        add_con = True
        while add_con:
            kodeDept = int(input('Masukkan Kode Departemen Baru: '))
            for i in deptList:
                if i['deptCode'] == kodeDept:
                    print('Kode Departemen Sudah Terdaftar. Silahkan Masukan Kode Baru.')
                    break
                
                elif i['deptCode'] != kodeDept:
                    add_con = False
                    break

        deptList.append({
            'deptName': namaDept,
            'deptCode': kodeDept
        })
        showListDept()
        break

# UPDATE Employee Data // Menu 3
def updateEmpl() :
    update_con = True
    while update_con:
        inputID = int(input('Masukkan ID Karyawan: '))
        for i in dummy4:
            if i['employeeID'] == inputID :
                getEmplData(inputID)
                confirm = input('Apakah Data Karyawan Tersebut ingin Diupdate? (Y/N): ').upper()
                if confirm == 'Y':
                    print('Silahkan Pilih Informasi Karyawan yang ingin DiUpdate:')
                    print('1. Nama')
                    print('2. Age')
                    print('3. Education')
                    print('4. Position')
                    print('5. Department')
                    print('6. Salary')
                    
                    while True:
                        option = int(input('Masukkan Informasi yang Ingin Diupdate: '))
                        newValue = input('Masukkan Data Baru:')
                        if option == 1:     # Update Name
                                for i in dummy4:
                                    if i['employeeID'] == inputID:
                                        i['fullName'] = newValue.title()
                                        getEmplData(inputID)
                        elif option == 2: # Update Age
                            while True:
                                if int(newValue) > 65 :
                                    print('Usia Terlalu Tua. Saatnya Pensiun!')
                                    break
                                elif int(newValue) < 15 :
                                    print('Usia Terlalu Muda. Dilarang Bekerja!')
                                    break
                                elif newValue.isalpha():
                                    print('Tidak Dapat Memasukkan Alphabet.')
                                else:
                                    for i in dummy4:
                                        if i['employeeID'] == inputID:
                                            i['age'] = int(newValue)
                                            getEmplData(inputID)
                                    break              
                        elif option == 3:   # Update Education
                            for i in dummy4:
                                if i['employeeID'] == inputID:
                                    i['education'] = (newValue).upper()
                                    getEmplData(inputID)
                        elif option == 4:   # Update Position
                            for i in dummy4:
                                if i['employeeID'] == inputID:
                                    i['position'] = (newValue).title()
                                    getEmplData(inputID)
                        elif option == 5:   # Update Departemen
                            while True:
                                if newValue.upper() not in [i['deptName'] for i in deptList]:
                                    print('Hanya dapat Memasukkan Departemen yang Terdaftar Pada Tabel Berikut.')
                                    showListDept()
                                    newValue = input('Masukkan Data Baru: ').upper()
                                else:
                                    for empl in dummy4:
                                        if empl['employeeID'] == inputID:
                                            oldEmpl_Code = str(empl['employeeID'])[2:]
                                            for i in deptList:
                                                if i['deptName'] == newValue.upper():
                                                    newEmpl_Code = str(i['deptCode'])
                                                    empl['department'] = newValue.upper()
                                                    empl['employeeID'] = int(newEmpl_Code + oldEmpl_Code)
                                                    id_Updated = empl['employeeID']
                                                    getEmplData(id_Updated)
                                            break
                                    break
                        elif option == 6:   # Update Salary
                            while True:
                                for i in dummy4:
                                    if i['employeeID'] == inputID:
                                        i['salary'] = int(newValue)
                                        getEmplData(inputID)
                                break
                        update_con = False
                        break
                elif confirm == 'N':
                    continue
                else :
                    print("Hanya Dapat Memasukkan Pilihan 'Y' atau 'N'!")  
                break 
        else:
            print('ID Karyawan Tidak Ditemukan.')
            break

# DELETE Menu // Menu 4
def delEmpl(delID):
    while True:
        try:
            for i in range(len(dummy4)):
                if dummy4[i]['employeeID'] == delID:
                    getEmplData(delID)
                    confirm =input('Apakah Data Karyawan Tersebut ingin Dihapus? (Y/N): ')
                    if confirm.upper() == 'Y':
                        dummy4.pop(i)
                        print(f"Data Karyawan dengan ID {delID} berhasil dihapus.")
                        showListEmpl()
                        break
                    elif confirm.upper() == 'N':
                        break
            else:
                print(f"Data Karyawan dengan ID {delID} tidak ditemukan.")  
        except ValueError:
            print('Masukkan ID Karywan dengan Tepat')
        break

# SEARCH FEATURE //
def searchByName(full_name):
    found = False
    headerTabl() 
    gap = ' ' * 3
    for i in dummy4:
        if full_name.lower() in i['fullName'].lower():
            print(f"{i['employeeID']:6}{gap}{i['fullName']:20s}{gap}{i['age']:^3d}{gap}{i['education']:^9s}{gap}{i['position']:20s}{gap}{i['department']:^11s}{gap}{i['salary']:>12}")
            found = True

    if not found:
        print('Nama Karyawan Tidak Ditemukan pada Daftar.')

# # Run the Program
while True:
    try:
        mainMenu()
        chooseMenu = int(input('Masukkan Angka Menu yang Tersedia: '))
        if chooseMenu == 1:
             clearScreen()
             while True:
                try:
                    print('\nSilakan pilih menu yang diinginkan:')
                    print('\t1. Tabel Data Seluruh Karyawan')
                    print('\t2. Tampilkan Data Department')
                    print('\t3. Cari Data Karyawan by Nama')
                    print('\t0. Kembali ke Menu Utama')
                    subOpt = int(input('Pilih Angka Menu yang Dipilih: '))
                    if subOpt == 1 :
                        showListEmpl()
                        continue
                    elif subOpt == 2:
                        showListDept()
                        continue
                    elif subOpt == 3 :
                        inputChar = input('Masukkan Nama yang Ingin Dicari: ')
                        searchByName(inputChar)
                        continue
                    elif subOpt == 0 :
                        break
                except ValueError :
                    print('Hanya Dapat Menginput Angka Pada Menu!')
                    continue
             
        elif chooseMenu == 2:
            clearScreen()
            while True:
                try:
                    print('\nSilakan pilih menu yang diinginkan:')
                    print('\t1. Tambah Data Karyawan Baru')
                    print('\t2. Tambah Department Baru')
                    print('\t0. Kembali ke Menu Utama')
                    subOpt = int(input('Pilih Angka Menu yang Dipilih: '))
                    if subOpt == 1 :
                        addEmpl()
                        continue
                    elif subOpt == 2:
                        addDept()
                        continue
                    elif subOpt == 0:
                        break
                except ValueError :
                    print('Hanya Dapat Menginput Angka Pada Menu!')
                    continue

        elif chooseMenu == 3:
            clearScreen()
            while True:
                try:
                    print('\nSilakan pilih menu yang diinginkan:')
                    print('\t1. Update Data Karyawan')
                    print('\t0. Kembali ke Menu Utama')
                    subOpt = int(input('Pilih Angka Menu yang Dipilih: '))
                    if subOpt == 1 :
                        showListEmpl()
                        updateEmpl()
                        break
                    elif subOpt == 0:
                        break
                except ValueError:
                    print('Hanya Dapat Menginput Angka Pada Menu!')
                    continue

        elif chooseMenu == 4:
            clearScreen()
            while True:
                try:
                    print('\nSilakan pilih menu yang diinginkan:')
                    print('\t1. Hapus Data Karyawan')
                    print('\t0. Kembali ke Menu Utama')
                    subOpt = int(input('Pilih Angka Menu yang Dipilih: '))
                    if subOpt == 1 :
                        showListEmpl()
                        inputID = int(input('Masukkan ID Karyawan yang Ingin Dihapus: '))
                        delEmpl(inputID)
                        continue
                    elif subOpt == 0:
                        break
                except ValueError:
                    print('Hanya Dapat Menginput Angka Pada Menu!')
                    continue

        elif chooseMenu == 0:
            print('Anda Telah Keluar dari Program. Sampai Jumpa :)')
            break
        else:
            print('Hanya Dapat Memilih Angka Menu 1/2/3/4/0')
        input('Press enter untuk kembali ke menu utama...') #return to main menu
    except ValueError:
        print('Perintah yang Dimasukkan Tidak Tersedia. Silakan Coba Lagi.')
