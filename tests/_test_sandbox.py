import coloredlogs
import imageio

from utoolbox.container.datastore import ImageFolderDatastore

coloredlogs.install(
    level="DEBUG", fmt="%(asctime)s  %(levelname)s %(message)s", datefmt="%H:%M:%S"
)

ds = ImageFolderDatastore("GH146ACV_power100_60ms_z3_split_converted", imageio.imread)

for k, v in ds.items():
    print("{}, {}".format(k, v.shape))
