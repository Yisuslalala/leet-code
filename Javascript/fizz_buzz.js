const obj = {};
obj["1"] = "Hello";

console.log(obj);

const FizzBuzz = (max) => {
    for (let i = 1; i < max; i++) {
        let out = "";
        if (i % 3 === 0)
            out += "Fizz";
        if (i % 5 === 0)
            out += "Buzz";
        if (i % 7 ===0)
            out += "Bazz";

        console.log(out || i);
    }
};

FizzBuzz(101);