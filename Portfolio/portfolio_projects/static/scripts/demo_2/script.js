let text_field = document.querySelector('textarea#text');
let result_field = document.querySelector('p#result');

function preLoad() {
    text_field.backgroundColor = "grey";
    text_field.disabled = true;
}

function init() {
    text_field.backgroundColor = "white";
    text_field.disabled = false;
}


async function run() {
    preLoad();
    const threshold = 0.5;

    const model = toxicity.load(threshold).then(model => {
        init();

        text_field.oninput = () => {
            let timer;
            clearTimeout(timer);
            timer = setTimeout(() => {
                const sentence = [text_field.value];
                model.classify(sentence).then(prediction => {
                    let result = "";
                    prediction.forEach(element => {
                        if (element.results[0].match) {
                            let num = parseFloat(element.results[0].probabilities[1] * 100).toFixed(2);
                            result += `- ${element.label} with probalility: ${num}%\n`
                        }
                    });
                    if (result === "") {
                        result += "no harm";
                    }
                    result_field.textContent = result;
                });
            }, 300);
        }
    });
}

run();
