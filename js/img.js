window.onload = function() {
    let imgs = document.getElementsByTagName("img");

    for(let i of imgs) {
        i.onclick = () => {
            let s = document.getElementsByTagName("section")[0];
            
            let frame = document.createElement('div');
            frame.classList.add('img-frame');

            frame.onclick = () => {
                frame.parentElement.removeChild(frame);
            }

            let image = document.createElement('img');
            image.src = i.src;

            frame.appendChild(image);
            s.appendChild(frame);
        }
    }

};