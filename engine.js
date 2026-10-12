(function (root) {
  "use strict";
  function plural(n, word, form) { return n + " " + (n === 1 ? word : (form || word + "s")); }
  function round1(x) { return Math.round(x * 10) / 10; }

  function railPlan(railCm, perItemCm) {
    if (!(railCm > 0) || !(perItemCm > 0)) return { error: "the rail length and the labeled width must be positive" };
    var items = Math.floor(railCm / perItemCm);
    if (items < 1) return { error: "the rail is shorter than one labeled item width" };
    var leftover = round1(railCm - items * perItemCm);
    var verdict;
    if (items <= 25) verdict = "a modest wardrobe";
    else if (items <= 50) verdict = "a working wardrobe";
    else verdict = "a serious wardrobe";
    return { items: items, leftover: leftover, verdict: verdict };
  }

  function doublePlan(railCm, levels) {
    if (!(railCm > 0)) return { error: "the rail length must be positive" };
    if (!(levels >= 1) || Math.floor(levels) !== levels) return { error: "the level count must be a whole number, one or more" };
    var total = round1(railCm * levels);
    var verdict;
    if (levels === 1) verdict = "a single rail";
    else if (levels === 2) verdict = "double-hang doubles the rail";
    else verdict = "a tall stack of rails";
    return { total: total, verdict: verdict };
  }

  function shelfPlan(heightCm, spacingCm) {
    if (!(heightCm > 0) || !(spacingCm > 0)) return { error: "the height and the labeled spacing must be positive" };
    var shelves = Math.floor(heightCm / spacingCm);
    if (shelves < 1) return { error: "the height fits less than one labeled spacing" };
    var topGap = round1(heightCm - shelves * spacingCm);
    var verdict;
    if (shelves <= 3) verdict = "a short column";
    else if (shelves <= 6) verdict = "a working column";
    else verdict = "a tall column";
    return { shelves: shelves, topGap: topGap, verdict: verdict };
  }

  function renderRail(r, railCm, perItemCm) {
    return "A rail " + railCm + " cm long at a labeled " + perItemCm + " cm an item hangs " + plural(r.items, "item") + " with " + r.leftover + " cm to spare - " + r.verdict + ".";
  }

  function renderDouble(r, railCm, levels) {
    return plural(levels, "rail") + " of " + railCm + " cm gives " + r.total + " cm of hanging - " + r.verdict + ".";
  }

  function renderShelf(r, heightCm, spacingCm) {
    return "A column " + heightCm + " cm tall at a labeled " + spacingCm + " cm of spacing fits " + plural(r.shelves, "shelf", "shelves") + " with " + r.topGap + " cm left at the top - " + r.verdict + ".";
  }

  var api = { railPlan: railPlan, doublePlan: doublePlan, shelfPlan: shelfPlan, renderRail: renderRail, renderDouble: renderDouble, renderShelf: renderShelf };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.ClosetMath = api;
})(this);
