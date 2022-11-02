safety = int(input())
roadrunner_speed = int(input())
coyote_speed = int(input())
rs = safety / roadrunner_speed
cs = (safety + 50) / coyote_speed
if rs < cs:
    print("Meep Meep")
else:
    print("Yum")





