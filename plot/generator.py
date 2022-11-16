import os

if __name__ == "__main__":
    os.system("pip3 install -r requirements.txt")
    os.system("python create_scatter_plot.py")
    os.system("python create_flat_world_plot.py")
    os.system("python create_circle_world_plot.py")
    os.system("python create_2d_plot.py")
