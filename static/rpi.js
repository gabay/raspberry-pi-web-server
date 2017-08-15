
function ajax(method, url, callback, data) {
    request = new XMLHttpRequest();
    request.open(method, url, true);
    request.onreadystatechange = function() {
        if (this.readyState == 4 && callback instanceof Function) {
            callback(this.status, this.responseText);
        }
    }
    request.send(data);
}

function poll(url, callback) {
    f = function(status, text) {
        if (status == 200) {
            callback(text);
        }
        ajax('GET', url, f);
    }
    ajax('GET', url, f);
}
