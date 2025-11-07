import os,sys

BAD_HASH = "c1a4be04b972b6c17db242fc37752ad517c29402"
GOOD_HASH = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"


rc = os.system(f"git bisect start {BAD_HASH} {GOOD_HASH}")
if rc != 0:
    sys.exit(1)

os.system("git bisect run python manage.py test")
os.system("git bisect reset")
