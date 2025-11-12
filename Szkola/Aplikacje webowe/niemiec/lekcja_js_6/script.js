console.log("Loaded js!");

function arrToUl(arr){
    const url = document.createElement('ul');
    arr.forEach(item => {
        const li = document.createElement('li');
        li.textContent = item;
        url.appendChild(li);
    });
    return url;
}

const buttonNode = document.querySelector('#guzik')

if (buttonNode){
    buttonNode.addEventListener('click', async () => {
        const url  = "/ajax"

        try {
            const resp = await fetch(url)

            const text = await resp.json()
            console.log("Response from AJAX:", text)

            const ul = arrToUl([text])
            document.body.appendChild(ul)
        }
        catch (error){
            console.error("Error:", error)
        }
    });
}