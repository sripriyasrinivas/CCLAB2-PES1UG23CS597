from database import get_db

def checkout_logic():
    db = get_db()
    db.row_factory = None  

    events = db.execute("SELECT fee FROM events").fetchall()

    # Uncomment this line initially for the crash screenshot task
    #1 / 0

    total = 0
    for e in events:
        d=0
        for i in range(100000):
            d+=1
        total+=e[0]
    return total
