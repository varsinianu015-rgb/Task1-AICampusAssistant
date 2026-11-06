from langchain_core.tools import tool
from .erp_client import get
@tool
def get_student_count()->dict:
    'Get the total student count in the college.'
    return get('/api/students/count')
@tool
def get_student_by_id(student_id:int)->dict:
    'Get details for a student using their numeric student ID.'
    return get(f'/api/students/{student_id}')
@tool
def get_students_by_department(department:str)->list:
    'List students belonging to a department.'
    return get('/api/students',{'department':department})
@tool
def get_staff_by_department(department:str)->list:
    'List staff members belonging to a department.'
    return get('/api/staff',{'department':department})
@tool
def get_class_teacher(department:str)->dict:
    'Find the class teacher for a department.'
    return get('/api/staff/class-teacher',{'department':department})
@tool
def get_attendance_report()->dict:
    'Get college attendance summary and department averages.'
    return get('/api/attendance/report')
TOOLS=[get_student_count,get_student_by_id,get_students_by_department,get_staff_by_department,get_class_teacher,get_attendance_report]
TOOL_MAP={x.name:x for x in TOOLS}
