# ชื่อ ,เงินเดือน
class Employee: #การสร้าง class
  # สร้าง method
    def detail(self,name,salary,department):
  # สร้าง Attrlbute
        self.name = name
        self.salary = salary
        self.department = department

    def showData(self):
        print('ชื่อพนักงาน = {}'.format(self.name))
        print('เงินเดือน = {}'.format(self.salary))
        print('เเผนก = {}'.format(self.salary))

# Attrlbute เป็นกลไกที่กำหนดคุณสมบัติ class
#การสร้าง Attrlbute
# self.name = ชื่อพนักงาน
# self.salary = เงินเดือน
# self.age = อายุของพนักงาน

# Method เป็นกลไกที่กำหนดพฤติกรรมให้กับ class
# การสร้าง Method
#   def getName(self):
#    return self.name
# การเรียกใช้งาน
#  ชื่อวัตถุ.getName()

# คี์ย์เวิร์ด self
#  การใช้คีย์เวิร์ด self จะเป็นตัวชี้หรือบ่งบอกว่าตอนนี้เราทำงานกับวัตถุใด
#  ให้บอกตัวตนของวัตถุนั้นๆ เช่น การกำหนดคุณสมบัติต่างๆ ในวัตถุ

# Constructor
# เป็น method พิเศษที่จะถูกใช้งานเมื่อตอนเริ่มสร้างวัตถุ (ไม่ระบุก็ได้)
# โครงสร้าง constructor
#  def__init__(self):

# การสร้างวัตถุ
emp1 = Employee()
emp1.detail('พัชราภา',1200,'นักเรียน')
emp1.showData()

emp2 = Employee()
emp2.detail('โนนแดง',250,'กีฬา')
emp2.showData()

emp3 = Employee()
emp3.detail('gumm',250,'กิจกรรม')
emp3.showData()


