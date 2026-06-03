const {JSDOM} = require('jsdom')

function findTranslation(link, word){
    const urls = []
    const dom = new JSDOM(link)

    // Returns an array of all the a tags in the doc
    const linkElements = dom.window.document.querySelectorAll("span")

    return linkElements
}

console.log(findTranslation("https://dictionary.cambridge.org/dictionary/polish-english/się", "się"))