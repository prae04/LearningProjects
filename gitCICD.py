import os
import subprocess

# gitraw = os.system('git diff-tree --no-commit-id --name-only -r 308280ea')
# gitrawCall = subprocess.call('git diff-tree --no-commit-id --name-only -r 308280ea', shell=True)
gitrawChk = subprocess.run('git diff-tree / --no-commit-id --name-only -r 308280ea', shell=True,stdout=subprocess.PIPE)

print(gitrawChk.stdout.split())
filst = gitrawChk.stdout.split()
filst.pop()
for f in filst:
    if '.sql' in f:
        print(f)
# # lw = gitrawChk.stdout.split('\n')
# for f in fil

#sqlcmd -S myServer\instanceName -i C:\myScript.sql
