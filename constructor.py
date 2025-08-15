# Constructor
# เป็น Method พิเศษที่จะถูกใช้งานเมื่อตอนเริ่มสร้างวัตถุ (ไม่ระบุก็ได้)
# โครงสร้าง Constructor
# def __init__(self):
#     pass

# Destructor
# เป็น method พิเศษที่ตรงข้างกับ constructor จะถูกใช้งานเมื่อ
# สิ้นสุดการทำงานของ class หรือถูกทำก่อนจะสลาย object
# ส่วนใหญ่จะเป็นกลุ่มคำสั่งที่ทำหน้าที่คืนหน่วยความจำให้ระบบ (ไม่ระบุก็ได้)
# โครงสร้าง
# def __del__(self):
#   pass

class Employee:
    def __init__(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department


    def showData(self):
        print('ชื่อพนักงาน = {}'.format(self.name))
        print('เงินเดือน = {}'.format(self.salary))
        print('แผนก = {}'.format(self.department))

# มีหรือไม่มีก็ได้ destructor
def __del__(self):
    print('call destructor')

emp1 = Employee('พัชราภา',1200,'นักเรียน')
emp1.showData()

emp1 = Employee('โนนแดง',250,'กีฬา')
emp2.showData()

emp3 = Employee('gumm',250,'กิจกรรม')
emp3.showData()

emp4 = Employee('plim',2000,'HR')
emp4.salary = 21000
emp4.showData()
