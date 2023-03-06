let icon;
let url;
let request;

document.addEventListener('DOMContentLoaded', init, false);

function init() {
    icon = document.querySelector('.icon');
    icon.innerHTML = 'I &#10084';
    icon.addEventListener('click', change_icon, false);
}

function change_icon(){
    let url = 'addtofav.py';
    request = new XMLHttpRequest();
    request.addEventListener('readystatechange', handle_response, false);
    request.open('GET', url, true);
    request.send(null);
}

function handle_response() {
    // Check that the response has fully arrived
    if ( request.readyState === 4 ) {
        // Check the request was successful
        if ( request.status === 200 ) {
            if ( request.responseText.trim() === 'I &#10084' ) {
                icon.innerHTML = 'I &#10084';
                } else if ( request.responseText.trim() === '&#x1F494' ) {
                icon.innerHTML = '&#x1F494';
            }
        }
    }
}
