const dataMatches = (first, second) => {
    const firstLowerCase = first.toString().toLowerCase();
    const secondLowerCase = second.toString().toLowerCase();
    if(firstLowerCase.includes(secondLowerCase) || secondLowerCase.includes(firstLowerCase)){
        return true;
    }
    return false;
}

module.exports = {
    dataMatches
}