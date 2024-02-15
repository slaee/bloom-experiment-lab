let a = 'Simple String';
function query(a) {
    console.log(a)
}
query(a);


// read from query param in url q=
let url = new URL(window.location.href);
let b = url.searchParams.get("q");
let sql = `SELECT * FROM table WHERE id = ${b}`;

function SQLQuery(sql) {
    console.log(sql)
}