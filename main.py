class Student:
    def __init__ (self, name, age, tracks, score) :
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
        
    print("Details of new student: ")

    def change_name (self, new_name) :
        self.name = new_name
        print("New Name: ", self.name)

    def change_age (self, new_age) :
        self.age = new_age
        print("New Age: ", self.age)

    def add_track (self, tracks) :
        self.tracks = tracks
        print("New Tracks: ", self.tracks)
        
    def get_score (self) :
        print("Score: ", self.score)
    
   

Bob = Student(name="Bob", age=26, tracks=["FE","BE"], score=99.99)

Bob.change_name("Verike")
Bob.change_age(21)
Bob.add_track("FullStack")
Bob.get_score()
