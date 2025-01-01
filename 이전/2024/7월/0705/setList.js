let n = 1000000;
let start, end;

// for문 사용
start = performance.now();
let visited1 = [];
for (let i = 0; i < n; i++) {
    visited1.push(0);
}
end = performance.now();
console.log(`for문 사용: ${end - start}ms`);

// fill 사용
start = performance.now();
let visited2 = Array(n).fill(0);
end = performance.now();
console.log(`fill 사용: ${end - start}ms`);