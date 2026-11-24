import json, re, datetime, random
random.seed(7)
def slug(s): return re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')
DAYS=[
 ("upper-power","Upper Power","power",[("Barbell Bent-Over Row",3,185,5),("Weighted Pull-Up",2,45,8),("Rack Chin",2,25,10),("Flat Dumbbell Press",3,85,5),("Weighted Dip",2,45,8),("Seated DB Shoulder Press",3,55,8),("EZ-Bar Curl",3,75,8),("Skull Crusher",3,65,8)]),
 ("lower-power","Lower Power","power",[("Back Squat",3,275,5),("Hack Squat",2,230,8),("Leg Extension",2,140,10),("Stiff-Leg Deadlift",3,225,6),("Lying Leg Curl",2,100,8),("Standing Calf Raise",3,200,10),("Seated Calf Raise",2,135,10)]),
 ("back-shoulders","Back & Shoulders","hyper",[("Speed Barbell Row",6,135,3),("Rack Chin",3,0,10),("Seated Cable Row",3,150,10),("One-Arm DB Row",2,70,12),("Close-Grip Pulldown",2,130,15),("Seated DB Press",3,45,10),("Upright Row",2,65,12),("Lateral Raise",3,20,15)]),
 ("lower-hyper","Lower Hypertrophy","hyper",[("Speed Squat",6,185,3),("Hack Squat",3,180,10),("Leg Press",2,360,12),("Leg Extension",3,110,15),("Romanian Deadlift",3,185,10),("Lying Leg Curl",2,80,12),("Seated Leg Curl",2,90,15),("Donkey Calf Raise",4,180,12),("Seated Calf Raise",3,115,15)]),
 ("chest-arms","Chest & Arms","hyper",[("Speed Bench Press",6,155,3),("Incline DB Press",3,65,10),("Machine Chest Press",3,140,12),("Incline Cable Fly",2,30,15),("Preacher Curl",3,55,10),("Seated Overhead Tricep Ext",3,60,10),("Concentration Curl",2,30,12),("Cable Pressdown",2,60,12),("Spider Curl",2,25,15),("Tricep Kickback",2,20,15)]),
]
# weekdays from Oct 7 2026 to Nov 20 2026
d=datetime.date(2026,10,5); end=datetime.date(2026,11,20); dates=[]
while d<=end:
    if d.weekday()<5: dates.append(d)
    d+=datetime.timedelta(days=1)
dates=[x for x in dates if not (x==datetime.date(2026,10,30) or x==datetime.date(2026,11,11))]  # couple of skipped days
n=len(dates); start=(1-(n-1))%5
hist=[]
for i,dt in enumerate(dates):
    di=(start+i)%5; did,dname,typ,exs=DAYS[di]; wk=i//5
    entries={}; names={}
    for name,sets,w,r in exs:
        k=slug(name); names[k]=name
        step=5 if w>=100 else 2.5
        ww=w+step*(wk//1) if w else 0
        lastwk=(n-1)//5
        if wk>=lastwk-1: ww=w+step*(lastwk-2)   # final two weeks repeat a weight: no new PR, so Recall advises
        miss = (wk==lastwk and name in ("Seated Cable Row","Close-Grip Pulldown","Lateral Raise"))
        entries[k]=[{"w":(str(int(ww)) if ww==int(ww) else str(ww)) if w else "","r":str((r-2) if (miss and j==sets-1) else r)} for j in range(sets)]
    hh=random.choice([5,5,6,11,12]); mm=random.choice([5,12,20,35,41])
    iso=f"{dt.isoformat()}T{hh+6:02d}:{mm:02d}:00.000Z"
    hist.append({"id":f"s{i:03d}x","client_id":f"00000000-0000-4000-8000-{i:012d}","date":iso,"programId":"phat","dayId":did,"dayName":dname,"type":typ,"entries":entries,"names":names,"durationMin":random.choice([52,58,61,64,67,71,74])})
hist.reverse()
cyc={"phat":{}}
for h in hist[:5]:
    pass
# current pass: last session indexes ending with D2 -> D1,D2 done this pass
last=[h for h in hist[:2]]
for h in last: cyc["phat"][h["dayId"]]={"completedAt":h["date"],"sessionId":h["id"]}
weights=[]
wd=datetime.date(2026,10,5); bw=192.4
while wd<=end:
    weights.append({"date":wd.isoformat(),"weight":round(bw,1),"unit":"lbs"}); bw-=random.choice([0.1,0.3,0.4,-0.2,0.5]); wd+=datetime.timedelta(days=random.choice([2,3,4]))
ls={"phat:history":json.dumps(hist),"phat:settings":json.dumps({"split":"5","volume":"standard","manualProgramId":"phat","programChosen":True}),
"phat:userGoal":json.dumps({"goal":"muscle","days":"5","experience":"advanced"}),"phat:seenInstallTip":"true","mm:arrow-hint-seen":"1","mm:onb-backup-asked":"1",
"phat:cycleByProgram":json.dumps(cyc),"phat:weightLog":json.dumps(weights)}
json.dump(ls,open("seed.json","w"))
print(n,"sessions; last",hist[0]["dayName"],hist[0]["date"][:10], "| next", hist[1]["dayName"])
