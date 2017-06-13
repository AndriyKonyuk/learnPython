let xhttp = new XMLHttpRequest(),
    curFromElement = document.getElementById("cur_from"),
    curToElement = document.getElementById("cur_to"),
    curTextElement = document.getElementById("cur_text"),
    resultElement = document.getElementById("result");


let from = document.getElementById('cur_from'),
    to = document.getElementById('cur_to'),
    cur_text = document.getElementById('cur_text');

xhttp.open('GET', 'http://api.fixer.io/latest', false);

xhttp.send();

let cur_val = JSON.parse(xhttp.responseText),
    cur_keys = Object.keys(cur_val['rates']);

cur_text.value = cur_val['rates'];

cur_keys.forEach(function (key) {
    let opt = document.createElement("option");
    opt.text = key;

    curFromElement.add(opt);
});

function add_to_value() {
    curToElement.value = null;
    let sel = document.getElementById('cur_from').value,
        req = new XMLHttpRequest();

    req.open('GET', `http://api.fixer.io/latest?base=${sel}`, false);
    req.send();

    let keys = Object.keys(JSON.parse(req.responseText)['rates']);

    keys.forEach(function (key) {
        let opt = document.createElement("option");
        opt.text = key;

        curToElement.add(opt);
    });


}

/*
 Implement function that fills currency from/to select boxes with currency codes
 and fills scrolling text with rates against currencyBaseSymbol
 */
function loadCurrency() {
    /* your code goes here */
    curTextElement.innerHTML = JSON.stringify(cur_val['rates']);
}

/*
 Implement function that converts from one selected currency to another filling result text area.
 */
function getRates() {
    /* your code goes here */
    let from = document.getElementById('cur_from').value,
        to = document.getElementById('cur_to').value,
        amount = document.getElementById('cur_amount').value,
        xhr = new XMLHttpRequest();

    xhr.open('GET', `http://api.fixer.io/latest?base=${to}`, false);
    xhr.send();

    let my_cur = JSON.parse(xhr.responseText);
    resultElement.value = amount * my_cur['rates'][from];
}

let select = document.getElementById('cur_from');
select.addEventListener('change', add_to_value);

// Load currency rates when page is loaded
window.onload = function () {
    // Run loadCurrency func to fetch currencies data and set this function to run every 60 sec.
    (() => {
        loadCurrency();
        setInterval(loadCurrency, 1000 * 60);
    })();

    let btn = document.getElementById('run');
    btn.addEventListener("click", getRates);
};
