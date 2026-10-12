import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def plural(n, word, form=None): return str(jsnum(n)) + " " + (word if n == 1 else (form or word + "s"))
def fmt(x): return str(jsnum(x))
def round1(x): return jsnum(math.floor(x * 10 + 0.5) / 10)

def rail_plan(railCm, perItemCm):
    if not (railCm > 0) or not (perItemCm > 0):
        return {"error": "the rail length and the labeled width must be positive"}
    items = math.floor(railCm / perItemCm)
    if items < 1:
        return {"error": "the rail is shorter than one labeled item width"}
    leftover = round1(railCm - items * perItemCm)
    if items <= 25: verdict = "a modest wardrobe"
    elif items <= 50: verdict = "a working wardrobe"
    else: verdict = "a serious wardrobe"
    return {"items": items, "leftover": leftover, "verdict": verdict}

def double_plan(railCm, levels):
    if not (railCm > 0):
        return {"error": "the rail length must be positive"}
    if not (levels >= 1) or math.floor(levels) != levels:
        return {"error": "the level count must be a whole number, one or more"}
    total = round1(railCm * levels)
    if levels == 1: verdict = "a single rail"
    elif levels == 2: verdict = "double-hang doubles the rail"
    else: verdict = "a tall stack of rails"
    return {"total": total, "verdict": verdict}

def shelf_plan(heightCm, spacingCm):
    if not (heightCm > 0) or not (spacingCm > 0):
        return {"error": "the height and the labeled spacing must be positive"}
    shelves = math.floor(heightCm / spacingCm)
    if shelves < 1:
        return {"error": "the height fits less than one labeled spacing"}
    top_gap = round1(heightCm - shelves * spacingCm)
    if shelves <= 3: verdict = "a short column"
    elif shelves <= 6: verdict = "a working column"
    else: verdict = "a tall column"
    return {"shelves": shelves, "topGap": top_gap, "verdict": verdict}

def render_rail(r, railCm, perItemCm):
    return ("A rail " + fmt(railCm) + " cm long at a labeled " + fmt(perItemCm) + " cm an item hangs "
            + plural(r["items"], "item") + " with " + fmt(r["leftover"]) + " cm to spare - " + r["verdict"] + ".")

def render_double(r, railCm, levels):
    return plural(levels, "rail") + " of " + fmt(railCm) + " cm gives " + fmt(r["total"]) + " cm of hanging - " + r["verdict"] + "."

def render_shelf(r, heightCm, spacingCm):
    return ("A column " + fmt(heightCm) + " cm tall at a labeled " + fmt(spacingCm) + " cm of spacing fits "
            + plural(r["shelves"], "shelf", "shelves") + " with " + fmt(r["topGap"]) + " cm left at the top - " + r["verdict"] + ".")

cases = []
def add(fn, f, rf, args):
    r = f(*args)
    c = {"fn": fn, "args": args, "result": r}
    if "error" not in r: c["render"] = rf(r, *args)
    cases.append(c)

for a in [[120,3],[150,3],[200,3],[2,3],[0,3],[120,0],[122,3],[127,3],[95.5,3],[80,4]]:
    add("railPlan", rail_plan, render_rail, a)
for a in [[120,1],[120,2],[120,3],[0,2],[120,0],[120,2.5],[95.5,2],[120,4],[60,1],[80,3]]:
    add("doublePlan", double_plan, render_double, a)
for a in [[200,30],[100,30],[300,30],[20,30],[0,30],[200,0],[205.5,30],[210,30],[95,25],[180,30]]:
    add("shelfPlan", shelf_plan, render_shelf, a)
json.dump(cases, open("expected.json", "w"), separators=(",", ":"))
print(len(cases), "cases")
