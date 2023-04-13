import re
count = 1
with open('data/rsvp_agent_log.dat', 'r') as f:
    print('WARNINGS:')
    for line in f.readlines():
        if re.search('WARNING', line):
            print(re.sub(r'WARNING:\S+', '--', line), end='')
