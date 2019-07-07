/**
 * Create a function that takes a 2D array as an input, and outputs another array that contains the average values for the numbers in the nested arrays at the corresponding indexes.
 * For Example:
 * ================================================================================================================================
 * avgArray([[1, 2, 3, 4], [5, 6, 7, 8]]); // => [3, 4, 5, 6]
 * avgArray([[2, 3, 9, 10, 7], [12, 6, 89, 45, 3], [9, 12, 56, 10, 34], [67, 23, 1, 88, 34]]); // => [22.5, 11, 38.75, 38.25, 19.5]
 * ================================================================================================================================
 */


// my First solution.
function avgArray(arr) {
  console.log(arr, 'arr');
  const tmp = {};
  const result = [];
  
  for (let lt of arr) {
    lt.forEach(function (value, i) {
    console.log(value, i);
      if (tmp[i] === undefined) {
        tmp[i] = [];
      }
      tmp[i].push(value);
    });
  }
  for (let i = 0; i < Object.keys(tmp).length; i++) {
    sum = 0;
    console.log(tmp[i]);
    for (let j of tmp[i]) {
      sum += j
    }
    result.push(sum / tmp[i].length);
  }
  return result;
}

// Improving
function avgArray(arr) {
  var result=[];
  for(var i in arr[0]){
    var num=0;
    for(var j in arr){
      num+=arr[j][i];
    }
    result.push(num/arr.length);
  }
  return result;
}

