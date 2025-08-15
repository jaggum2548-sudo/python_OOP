# AccessModifier
# คือระดับในการเข้าถึง class attribute method และอื่นๆ ในภาษาเชิงวัตถุ
# โดยมีประโยชน์อย่างมากในเรื่องของการกำหนดระดับในการเข้าถึง
# สิทธิในการเข้าใช้งาน การซ้อนข้อมูล และอื่ๆ

# Public คือการประกาศระดับการเข้าถึงที่เข้มงวดน้อยที่สุด หรือกล่าวว่าใครๆ
# ก็สามารถเข้าถึงและเรียกใช้งานได้

# Protected(_) เป็นการประกาศระดับการเข้าถึงเฉพาะคลาสของตัวมันเองและคลาสลูก
# ที่สืบทอดคุณสมบัติไปใช้เท่านั้น

# Private(_) เป็นการประกาศระดับการเข้าถึงที่เข้มงวดที่สุด กล่าวคือ จะมีแต่คลาสของ
# ตัวมันเองเท่านั้นที่มีสิทธิ์ใช้งานได้

class Employee:
    def __init__(self, name, salary, department):
        # public method
        self.__name = name
        self.__salary = salary
        self.__department = department


    # public method
    def _showData(self):
        print('ชื่อพนักงาน = {}'.format(self._name))
        print('เงินเดือน = {}'.format(self.__salary))
        print('แผนก = {}'.format(self.__department))



emp1 = Employee('พัชราภา', 12000, 'นักเรียน')
emp1._name = 'โนนแดง'
emp1.__salary = 12000
emp1._showData()
