# Closet math

Closet math plans the organizer before the shopping trip: the rail length at
a labeled width an item becomes the hanging count, the rail times the level
count becomes the total hanging, and the column height at a labeled spacing
becomes the shelf count with the gap at the top.

Live site: https://ilanis-agent.github.io/closetmath/

## The three tools

- **Rail plan** - `floor(rail / labeled width an item (3 cm))` items and the
  centimeters left over, with a modest / working / serious wardrobe verdict.
- **Level plan** - `rail x levels`, the total hanging, with a single /
  double-hang / tall-stack verdict.
- **Shelf plan** - `floor(height / labeled spacing (30 cm))` shelves and the
  gap at the top, with a short / working / tall column verdict.

## Limits

Every default is labeled and illustrative. Wardrobes vary from silk shirts
to winter coats, and organizers rate their own rails and fixings. This is
planning arithmetic, not a fitting: measure the real closet and count the
real clothes.

## Files

- `index.html` - landing page with the labeled norms
- `app.html` - the three calculators
- `engine.js` - shared calculation and render logic (browser + node)
- `oracle.py` - python mirror of the engine, writes `expected.json`
- `test.js` - runs the engine against `expected.json` (30 cases, 137 checks)

Run the tests: `python3 oracle.py && node test.js`
