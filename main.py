class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name=name
        self.age = age
        self.tracks = tracks
        self.score = score

        print("Student's details:His name is",name, "age is", age, "while his track is", tracks, "and he scored", score)


       #method
    def change_name(self,new_name):
        self.name = new_name
        print("Name:", self.name)

    def change_age(self,new_age):
        self.age = new_age
        print("Age:", self.age)

    def add_tracks(self,new_tracks):
        self.tracks = new_tracks
        print("Tracks:", self.tracks) 

    def get_score(self):
        print("Score:", self.score)   

                
Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_tracks("UI/UX")
Bob.get_score()
 