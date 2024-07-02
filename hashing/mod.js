function get(n){
    let nums =[]
    if(n>0){
        for(let i=n;i<=n+2;i++){
                nums.push(i)
        }
    }
    else{
        for(let i=n;i<=n*(-1);i++){
            nums.push(i)
        }
    }
    return nums
}


console.log(get(-2))
