// How can you make this more scalable and reusable later?

exports.findArmstrongNumbers = function(arr) {
    //empty array to push answer to
    let ansArr = [];
    /* creating an array taking original num to string then splitting them, then mapping and taking each num to pow of length and a final map to 
    reduce the inner arrays taking whole thing back to one array filled with numbers same length as input array */
    let testArr = arr.map(element => element.toString().split('').map((num, _, a) =>  num ** a.length)).map(elem => elem.reduce((a, b) => a + b) );
    //looping through both arrays and pushing any matching cases to ansArray
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === testArr[i]) {
            ansArr.push(arr[i])
        }
    }
    return ansArr
};

