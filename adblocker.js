chrome.webRequest.onBeforeRequest.addlistener(
    function (details) {
        return {
            cancel: true
        };
    },
    { urls: ["*://*.doubleclick.net/*"] },
    ["blocking"]
);

window.onload = function () {
    function updateLabel() {
        var enabled = chrome.extension.getBackgroundPage().enabled;
        document.getElementById('toggle_button').value = enabled ? "Disable" : enabled;
    }
    document.getElementById('toggle_button').onclick = function () {
        var background = chrome.extension.getBackgroundPage();
        background.enabled = !background.enabled;
        updateLabel();
    };
    updateLabel();
}