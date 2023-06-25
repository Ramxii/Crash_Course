from multiple_modules_admin import Admin

stephanie = Admin('stephanie', 'gustave', 'brazil', 21)

print(f"{stephanie.whole_name.title()}'s privileges: ")
stephanie.privileges.show_privileges()

