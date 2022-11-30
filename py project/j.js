const numbs = [2,5,8];
const sum = numbs.reduce(function(sum, number) {
    const updatedsum = sum + number;
    return updatedsum; }, 0);
    sum;
document.write(sum);