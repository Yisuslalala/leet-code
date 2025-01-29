const validAnagrams = (s, t) => {
  // console.log(s, t);
  const splitS = s.split(``);
  const splitT = t.split(``);
  const sortedS = splitS.sort();
  const sortedT = splitT.sort();
  const joinedS = sortedS.join(``);
  const joinedT = sortedT.join(``);
  return joinedS === joinedT ? true : false;
};

const s = `racecaer`;
const t = `carrace`;

console.log(validAnagrams(s, t));
