import subprocess, sys

cp = subprocess.run(['python','learning/logma_and_dow.py'])
if cp.returncode != 0:
    print('ls failed.', file=sys.stderr)
    sys.exit(1)
print("finish logma_and_dow")

'''
cp = subprocess.run(['python','learning/lgbm.py'])
if cp.returncode != 0:
    print('ls failed.', file=sys.stderr)
    sys.exit(1)
print("finish lgbm")


cp = subprocess.run(['python','learning/cat_boost.py'])
if cp.returncode != 0:
    print('ls failed.', file=sys.stderr)
    sys.exit(1)
print("finish catboost")
'''
cp = subprocess.run(['python','ensemble.py'])
if cp.returncode != 0:
    print('ls failed.', file=sys.stderr)
    sys.exit(1)
print("finish ensemble")