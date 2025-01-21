const mergeStrings = (word1, word2) => {
  let merged = ``;

  for (let i = 0, j = 0; i < word1.length || j < word2.length; i++, j++) {
    if (word1[i]) {
      merged += word1[i];
    }
    if (word2[j]) {
      merged += word2[j];
    }
  }

  console.log(`merged?`, merged);
};

const word1 = `abcd`;
const word2 = `pq`;

mergeStrings(word1, word2);
