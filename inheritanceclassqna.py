# class camera:
#     def take_photo(self):
#         print("Taking a photo...")
# # a = camera()
# # a.take_photo()

# class musicplayer:
#     def play_music(self):
#         print("Playing music...")
# # a = musicplayer()
# # a.play_music()

# class smartphone(camera , musicplayer):
#     def make_call(self):
#         print("Making a call...")

# a = smartphone()
# a.take_photo()
# a.play_music()
# a.make_call()

# class light:
#     def turn_on(self):
#         print("Light is turned on...")

# class fan:
#     def turn_on(self):
#         print("Fan is turned on...")

# class smarthome(light,fan):
#     def lock_door(self):
#         print("Door is locked...")

# home = smarthome()
# light.turn_on(home)
# fan.turn_on(home)
# home.lock_door()

# class employee:
#     def work(self):
#         print("Employee is working...")
# class manager(employee):
#     def manage_team(self):
#         print("Manager is managing the team...")
# class projectmanager(manager):
#     def assign_task(self):
#         print("Project manager is assigning the tasks...")

# office = projectmanager()
# office.work()
# office.manage_team()
# office.assign_task()

# class device:
#     def power_on(self):
#          print("Device is powered on...")
# class phone(device):
#     def make_call(self):
#             print("Making a phone call...")
# class smartphone(phone):
#     def use_internet(self):
#           print("Using the internet...")    
# myphone = smartphone()
# myphone.power_on()
# myphone.make_call()
# myphone.use_internet()

# class person:
#     def introduce(self):
#         print("I am a person...")
# class student(person):
#     def study(self):
#         print("Student is studying...")
# class teacher(person):
#     def teach(self):
#         print("Teacher is teaching...")
# class classmonitor(student,teacher):
#     def manage_class(self):
#         print("Class monitor is managing the class...")
# kid = classmonitor()
# kid.introduce()
# kid.study()
# kid.teach()
# kid.manage_class()   


class employee:
    def work(self):
        print("Employee is working...")
class developer(employee):
    def write_code(self):
        print("Developer is writing code...")
class designer(employee):
    def design(self):
        print("Designer is creating a design...")
class teamlead(developer,designer):
    def team_lead(self):
        print("Team lead is managing the team well...")
team = teamlead()
team.work()
team.write_code()
team.design()
team.team_lead()

