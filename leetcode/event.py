def event(arr,arr1):
    h = arr[0]
    sliceH=h[slice(0,2)]
    h1 = arr1[0]
    sliceH1 = h1[slice(0,2)]
    return [sliceH,sliceH1]


print(event(["01:15","02:00"],["02:00","03:00"]))

