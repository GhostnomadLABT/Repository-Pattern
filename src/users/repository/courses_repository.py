import abc
from users.model.courses_model import Courses
class CoursesRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, name: str, descripcion: str)-> Courses:
        raise NotImplementedError
    
    @abc.abstractmethod
    def get(self, id:int) -> Courses:
        raise NotImplementedError

class LocalCoursesRepository(CoursesRepository):
    
    def __init__(self):
        self.courses = []

    def add(self, name: str, descripcion: str) -> Courses:
        courses = Courses(
        id = len(self.courses) + 1,
        name = name,
        descripcion = descripcion
    )
        self.courses.append(courses)
        return courses
    
    def get(self, id:int) -> Courses:
        courses_found = None
        for courses in self.courses:
            if courses.id == id:
                courses_found = courses
                break
        return courses_found
    
    def find_by_name(self, name: str) -> Courses:
        for course in self.courses:
            if course.name == name:
                return course
        return None