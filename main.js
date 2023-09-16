var urlArray = [
    "http://www.woodnshop.com/index.htm",
    "https://www.spacejam.com/1996/",
    "https://www.reddit.com/r/wallstreetbets/",
    "https://www.arsenal.com/"
];

function randomUrl() {
    var randomNumber = Math.floor(Math.random() * urlArray.length);
    var newUrl = urlArray[randomNumber];
    window.location.href = newUrl;
}