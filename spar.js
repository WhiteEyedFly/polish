// Add links to the list
    for (const linkElement of linkElements){
        // Bind relative urls to the base
        if (linkElement.href.slice(0, 1) === "/"){
            // Relative
            try{
                const urlObj = new URL(`${baseURL}${linkElement.href}`)
                urls.push(urlObj.href)
            } catch(err){
                console.log(`error with relative url: ${err.message}`)
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