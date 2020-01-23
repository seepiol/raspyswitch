# Stats for raspiswitch
import sqlite3


conn = sqlite3.connect("actions.db", check_same_thread=False)

data = conn.execute('''
                    SELECT ID, ACTION, DATETIME FROM SWITCHCRON
                    ''')
actions = []
onCounter = 0
offCounter = 0
for row in data:
    action = [row[0], row[1], row[2]]
    actions.append(action)
    if action[1] == "ON":
        onCounter+=1
    else:
        offCounter+=1



print(f"""
{len(actions)} actions.
Light on {onCounter} times.
Light off {offCounter} times.
""")
