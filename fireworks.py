import random, time, os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

chars = r'✦✧✩✰✵✶✷✸✹✺✻✼✽✾✿❀❁❂❃❅❆❈❉❊'
rows = 18
cols = 60

while True:
    clear()
    for _ in range(rows):
        print(''.join(random.choice(chars) for _ in range(cols)))
    time.sleep(0.5)
