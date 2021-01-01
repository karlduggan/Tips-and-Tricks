# Snippets of code that are useful

'''
>> PRINT ALL THE METHODS WITHIN THE OBJECT <<

Very simply and useful tool for inspecting modules with very little documentation.
Enter the object into the parameter and execute.
'''

def print_obj_methods(obj):
    	object_methods = []
    	for method_name in dir(obj):
    		if callable(getattr(obj, method_name)):
    			object_methods.append(method_name)
    	for method_name in object_methods:
    		print(method_name)
