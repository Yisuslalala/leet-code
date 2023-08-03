var str = "Jesús";
var strVolteada = "súseJ"
var otraString = "Jiijijia"
var otraOtraString = "aoiwjaw";

const IsPalindrome = (original, str) => {
    let splitArray = str.split("");
    let reverseArray = splitArray.reverse(); 
    let joinStr = reverseArray.join("");
    reversedString = joinStr.toLowerCase();
    originalLower = original.toLowerCase();
    return originalLower === reversedString ? true : false
};

console.log(IsPalindrome(strVolteada, str));
console.log(IsPalindrome(otraString, otraOtraString));