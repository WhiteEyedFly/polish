f = open("words.txt")

wordDict = {}

def getURLsFromHTML(htmlBody, baseURL):
    const urls = []
    const dom = new JSDOM(htmlBody)

    // Returns an array of all the a tags in the doc
    const linkElements = dom.window.document.querySelectorAll("a")

    // Add links to the list
    for (const linkElement of linkElements){
        // Bind relative urls to the base
        if (linkElement.href.slice(0, 1) === "/"){
            // Relative
            try{
                const urlObj = new URL(`${baseURL}${linkElement.href}`)
                urls.push(urlObj.href)
            } catch(err){
                //console.log(`error with relative url: ${err.message}`)
            }
            
        } else {
            // Absolute
            try{
                const urlObj = new URL(linkElement.href)
                urls.push(urlObj.href)
            } catch(err){
                //console.log(`error with relative url: ${err.message}`)
                }
        }
    }

    return urls

# Validate word list
f = str(f.read()).split()

for word in range(len(f)):
    equalPos = f[word].index("=")
    f[word] = f[word][:equalPos]

for word in range(len(f)):
    link = "https://dictionary.cambridge.org/dictionary/polish-english/" + f[word]
    
    dict[f[word]] = 
    

#print(f)