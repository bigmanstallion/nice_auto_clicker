import os

dir_path = os.path.dirname(os.path.realpath(__file__)) # dir of python file
os.chdir(dir_path)

os.system("mkdir ../build")
os.system("cd ../build && cmake .. && cmake --build .")
os.system("mv ../build/compile_commands.json ../")
