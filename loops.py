my_variable = "hello"

for charc in my_variable:
	print(charc)

my_list = [4, 2, 1, 3]
for numbers in my_list:
	print(numbers ** 2)

user_answer = True
while user_answer == True:
	print(10)
	user_input = input("Should we print again? (y/n)")
	if user_input == 'n':
		user_answer = False


class Test():
	def __init__(self):
		print('Into Class')

def chummaTest(self):
	print(self.serviceObjectName)


object_type = ['service_object_6over4', 'service_object_ah', 'service_object_l2tp']
object_name = ['ServiceObjectForCreateSGWithMultipleObject1', 'ServiceObjectForCreateSGWithMultipleObject2', 'ServiceObjectForCreateSGWithMultipleObject3']

object = Test()
for count, name, type in zip(range (1,4),object_name,object_type):
	object = 'fw_obj'+str(count)
	object.serviceObjectName = name
	object.serviceObjectType = type
	object.chummaTest()

object_name = ['ServiceObjectForCreateSGWithMultipleObject1', 'ServiceObjectForCreateSGWithMultipleObject2',
                   'ServiceObjectForCreateSGWithMultipleObject3']
group_name = ['ServiceObjectForCreateSGWithMultipleGroup1', 'ServiceObjectForCreateSGWithMultipleGroup2',
                  'ServiceObjectForCreateSGWithMultipleGroup3']
obj_grp_name = object_name + group_name
print(obj_grp_name)