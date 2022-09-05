// const pushFront = (arr, val) => {
//     let newArr = arr;
//     newArr[arr.length] = val;
//     //or
//     // let newArr = [val]
//     // console.log(newArr)
//     // for(let i = 0; i <= arr.length-1; i++){
//     //     console.log(arr[i]);
//     //     newArr.push(arr[i]);
//     // }
//     return newArr
// }

// console.log(pushFront([5,7,2,3], 8))

// const popFront = (arr, val) => {
//     let newArr = [];
//     val = arr[0];
//     for(let i = 1; i <= arr.length-1; i++){
//         // console.log(arr[i]);
//         newArr.push(arr[i]);
//     }
//     console.log(newArr)
//     return val;
// }

// console.log(popFront([4,5,7,9]))

// const insertAt = (arr, index, val) => {
//     let newArr = [];
//     for(let i = 0; i <= arr.length-1; i++){
//         if(i === index){
//             newArr.push(val);
//         }
//         newArr.push(arr[i]);
//     }
//     return newArr
// }

// console.log(insertAt([100,200,5], 1, 311));

// const removeAt = (arr, index) => {
//     let newArr = [];
//     let val = arr[index];
//     for(let i = 0; i <= arr.length-1; i ++){
//         if(i !== index){
//             newArr.push(arr[i]);
//         }
//     }
//     console.log(newArr)
//     return val
// }

// console.log(removeAt([8,20,55,44,98], 3))

// const swapPairs = (arr) => {
//     console.log(arr)
//     let temp;
//     for(let i = 0; i <= arr.length-1; i++){
//         if(i % 2 === 1){
//             temp = arr[i]
//             arr[i] = arr[i-1]
//             arr[i-1] = temp
//         }
//     }
//     console.log(arr)
// }

// console.log(swapPairs(["Sox",true,"Kitty",true]))

//Only works if its sorted!
// const removeDuplicates = (arr) => {
//     let newArr = [];
//     let val = 0;
//     for(let i = 0; i <= arr.length-1; i++){
//         if(arr[i]===arr[i+1]){
//             val = arr[i]
//         }
//         if(arr[i]!==arr[i+1]){
//             newArr.push(arr[i])
//         }
//     }
//     return newArr
// }

// console.log(removeDuplicates([-2,-2,3.14,5,5,10]))