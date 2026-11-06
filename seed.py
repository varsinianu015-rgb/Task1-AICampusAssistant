from .models import Student, Staff
def seed(db):
    if db.query(Student).count() == 0:
        rows = [(1001,"Arun Kumar","Computer Science",3,"arun@example.edu",92.5),(1002,"Priya Sharma","Information Technology",2,"priya@example.edu",88),(1003,"Karthik Raj","Mechanical",1,"karthik@example.edu",79.5),(1004,"Divya S","Computer Science",4,"divya@example.edu",96),(1005,"Naveen K","Information Technology",3,"naveen@example.edu",84),(1006,"Meena R","Electronics",2,"meena@example.edu",91),(1007,"Sanjay P","Computer Science",2,"sanjay@example.edu",73),(1008,"Aishwarya M","Mechanical",4,"aishwarya@example.edu",81.5)]
        db.add_all([Student(student_id=a,name=b,department=c,year=d,email=e,attendance_percentage=f) for a,b,c,d,e,f in rows])
    if db.query(Staff).count() == 0:
        rows = [(501,"Dr. Lakshmi","Computer Science","Professor","lakshmi@example.edu",True),(502,"Mr. Suresh","Information Technology","Assistant Professor","suresh@example.edu",True),(503,"Dr. Kumar","Mechanical","Professor","kumar@example.edu",True),(504,"Ms. Nandhini","Electronics","Assistant Professor","nandhini@example.edu",True),(505,"Mr. Prakash","Computer Science","Associate Professor","prakash@example.edu",False)]
        db.add_all([Staff(staff_id=a,name=b,department=c,designation=d,email=e,is_class_teacher=f) for a,b,c,d,e,f in rows])
    db.commit()
