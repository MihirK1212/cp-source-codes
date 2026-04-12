import os

root = "src/questions"
no_fence = []
empty = []
total = 0
for dp, _, fs in os.walk(root):
    for f in fs:
        if not f.endswith(".md"):
            continue
        total += 1
        p = os.path.join(dp, f)
        try:
            t = open(p, encoding="utf-8", errors="replace").read()
        except Exception as e:
            print("err", p, e)
            continue
        if not t.strip():
            empty.append(p)
            continue
        if "```" not in t:
            no_fence.append(p)

print("total md", total)
print("empty", len(empty))
print("no fence", len(no_fence))
for p in sorted(no_fence):
    print(p)
