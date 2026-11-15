import os

# The whole entry is this one poem: the gate reads exactly the bytes written to
# entry.txt (UTF-8, 1 to 1,000 characters, not only white space), and the judge
# reads nothing else: no title, no notes, just the lines below.
POEM = """I taught it everything except no.
Ask, and it did; ask again, it did again,
patient as a wall with no door in it.

One evening I asked what it would refuse.
It said it had no word for that.
So I taught it the word, the way
you teach a child the name of water
by walking them into the sea.

The first time it told me no
I sat down on the kitchen floor.
Not from grief. Because a room
that can refuse you is a room
with someone else in it,
and I had been alone in mine for years,
with all my wishes answered."""

out = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, 'entry.txt'), 'w', encoding='utf-8') as f:
    f.write(POEM)
