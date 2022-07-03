
# class declaration 

class Student: 

    #Initializes the Student Object 
    def __init__ (self, name, age, track, score) :
        self.name = name
        self.age = age 
        self.track = track 
        self.score = score 

    #Function that changes the students name
    def change_name (self, new_name) :
        self.name = new_name
        print(f"Changed name to :{new_name}")

    #Function that changes the students age 
    def change_age (self, new_age) :
        try: #validate if the new age is an integer
            new_age = int(new_age)
        except:
            print("Failed to change age, Input Valid DataType")
            raise Exception

        self.age = new_age
        print(f"Changed age to : {new_age}")

    #Function that changes the students track
    def change_track (self, new_track) :
        self.track = new_track
        print(f"Changed track to : {new_track}")

    #Function that returns the students score
    def get_score (self) :
        score = print(f"Score remains : {self.score}")
        return score

Bob = Student (name = "Bobin", age = 35, track = ["FE","BE"], score = 95.6)

Bob.change_name ("Verike")
Bob.change_age (22)
Bob.change_track ("Full Stack/ DevOps")
Bob.get_score()