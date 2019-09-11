import os, glob, shutil, argparse

parser = argparse.ArgumentParser()
parser.add_argument('--src', nargs=1, required=True)
parser.add_argument('--dest',nargs=1, required=True)
args=parser.parse_args()

# args.src[0] = args.src[0].replace()

# dest = dest/path
# rootdir = root/path
# print(args.src[0])
# print(args.dest[0])
# args.src[0] = args.src[0].replace('\\','/')
print(args.src[0])
print(args.dest[0])
for filename in glob.iglob(args.src[0] + '/**', recursive=True):
    if os.path.isfile(filename) and filename.__contains__('.ispac') is True:
        print(filename)
        print(os.path.basename(filename))
        # print(dest + os.path.basename(filename))
        # os.rename(filename, dest + os.path.basename(filename))
        shutil.copy(filename, args.dest[0] + os.path.basename(filename))


# for subdirs, dirs, files in os.walk(rootdir):
#     for file in files:
#         print os.path.join(subdir, file)
