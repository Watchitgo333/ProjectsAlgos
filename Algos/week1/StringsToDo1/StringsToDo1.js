// const removeBlanks = (str) => {
//     let strArr = str.split(" ")
//     let newStr = '';
//     for(let i = 0; i <= strArr.length-1; i ++){
//         console.log(strArr[i])
//         newStr += strArr[i]
//     }
//     return newStr
// }

// console.log(removeBlanks("I can not BELIEVE it's not BUTTER"))

// const getDigits = (str) => {
//     let strArr = str.split('')
//     let num = ''
//     for(let i = 0; i <= strArr.length-1; i ++){
//         if(isNaN(strArr[i])){
//             null
//         } 
//         else {
//             // console.log(strArr[i])
//             num += strArr[i]
//         }
//     }
//     return num;
// }

// console.log(getDigits("0s1a3y5w7h9a2t4?6!8?0"))

// const acronyms = (str) => {
//     let strArr = str.split(' ');
//     let charArr = [];
//     let newStr = ''
//     for(let i = 0; i <= strArr.length-1; i ++){
//         if(strArr[i].split('')[0]!==undefined){
//             charArr.push(strArr[i].split('')[0])
//             newStr += strArr[i].split('')[0].toUpperCase()
//         }
//     }
//     return newStr
// }

// console.log(acronyms("Live from New York, it's Saturday Night!"))

// const countNonSpaces = (str) => {
//     let strArr = str.split(" ")
//     let newStr = ""
//     for(let i = 0; i <= strArr.length-1; i ++){
//         newStr += strArr[i]
//     }
//     return newStr.length
// }

// console.log(countNonSpaces("Hello world !"))

// const removeShorterStrings = (arr, val) => {
//     let newArr = [];
//     for(let i = 0; i <= arr.length-1; i ++){
//         console.log(arr[i].length)
//         if(arr[i].length >= val){
//             newArr.push(arr[i])
//         }
//     }
//     return newArr

// }

// console.log(removeShorterStrings(['There', 'is', 'a', 'bug', 'in', 'the', 'system'], 4))