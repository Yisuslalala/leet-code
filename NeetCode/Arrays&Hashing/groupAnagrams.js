const groupAnagrams = (strs) => {
  const res = {};

  for (let s of strs) {
    const count = new Array(26).fill(0);
    for (let c of s) {
      count[c.charCodeAt(0) - `a`.charCodeAt(0)] += 1;
    }
    console.log(`count:`, count);
    const key = count.join(`,`);
    if (!res[key]) {
      res[key] = [];
    }
    res[key].push(s);
  }
  return Object.values(res);
};

const strs = ["act", "pots", "tops", "cat", "stop", "hat"];
console.log(groupAnagrams(strs));
