import import_admin_class 

greg = import_admin_class.Admin('ben', 'mathew', 'usa', 14)

print(f"{greg.whole_name.title()}'s privileges: ")
greg.privileges.show_privileges()
