let mobilenet;
let model;
const webcam = new Webcam(document.getElementById('wc'));
const dataset = new RPSDataset();
var rockSamples = 0, paperSamples = 0, scissorsSamples = 0, spockSamples = 0, lizardSamples = 0;
let isPredicting = false;

let start_button = document.querySelector("#startPredicting");
let train_button = document.querySelector("#train");

function disable_sample_buttons() {
    document.querySelector("#\\30 ").disabled = true
    document.querySelector("#\\31 ").disabled = true
    document.querySelector("#\\32 ").disabled = true
    document.querySelector("#\\33 ").disabled = true
    document.querySelector("#\\34 ").disabled = true
}

async function loadMobilenet() {
    const mobilenet = await tf.loadLayersModel('https://storage.googleapis.com/tfjs-models/tfjs/mobilenet_v1_1.0_224/model.json');
    const layer = mobilenet.getLayer('conv_pw_13_relu');
    return tf.model({ inputs: mobilenet.inputs, outputs: layer.output });
}

async function train() {
    dataset.ys = null;
    dataset.encodeLabels(5);

    // In the space below create a neural network that can classify hand gestures
    // corresponding to rock, paper, scissors, lizard, and spock. The first layer
    // of your network should be a flatten layer that takes as input the output
    // from the pre-trained MobileNet model. Since we have 5 classes, your output
    // layer should have 5 units and a softmax activation function. You are free
    // to use as many hidden layers and neurons as you like.  
    // HINT: Take a look at the Rock-Paper-Scissors example. We also suggest
    // using ReLu activation functions where applicable.
    model = tf.sequential({
        layers: [

            // YOUR CODE HERE
            tf.layers.flatten({ inputShape: mobilenet.outputs[0].shape.slice(1) }),
            tf.layers.dense({ units: 100, activation: 'relu' }),
            tf.layers.dense({ units: 5, activation: 'softmax' })
        ]
    });


    // Set the optimizer to be tf.train.adam() with a learning rate of 0.0001.
    const optimizer = tf.train.adam(0.0001);


    // Compile the model using the categoricalCrossentropy loss, and
    // the optimizer you defined above.
    model.compile({ optimizer: optimizer, loss: 'categoricalCrossentropy' });

    let loss = 0;
    model.fit(dataset.xs, dataset.ys, {
        epochs: 10,
        callbacks: {
            onBatchEnd: async (batch, logs) => {
                loss = logs.loss.toFixed(5);
                console.log('LOSS: ' + loss);
            }
        }
    });
}


function handleButton(elem) {
    switch (elem.id) {
        case "0":
            rockSamples++;
            document.getElementById("rocksamples").innerText = "Rock Samples: " + rockSamples;
            break;
        case "1":
            paperSamples++;
            document.getElementById("papersamples").innerText = "Paper Samples: " + paperSamples;
            break;
        case "2":
            scissorsSamples++;
            document.getElementById("scissorssamples").innerText = "Scissors Samples: " + scissorsSamples;
            break;
        case "3":
            spockSamples++;
            document.getElementById("spocksamples").innerText = "Spock Samples: " + spockSamples;
            break;
        case "4":
            lizardSamples++;
            document.getElementById("lizardsamples").innerText = "Lizard Samples: " + lizardSamples;
            break;
    }

    label = parseInt(elem.id);
    const img = webcam.capture();
    dataset.addExample(mobilenet.predict(img), label);

    if (rockSamples &&
        paperSamples && scissorsSamples &&
        spockSamples && lizardSamples) {
            train_button.disabled = false;
    }

}

async function predict() {
    while (isPredicting) {
        const predictedClass = tf.tidy(() => {
            const img = webcam.capture();
            const activation = mobilenet.predict(img);
            const predictions = model.predict(activation);
            return predictions.as1D().argMax();
        });
        const classId = (await predictedClass.data())[0];
        var predictionText = "";
        switch (classId) {
            case 0:
                predictionText = "I see Rock";
                break;
            case 1:
                predictionText = "I see Paper";
                break;
            case 2:
                predictionText = "I see Scissors";
                break;
            case 3:
                predictionText = "I see Spock";
                break;
            case 4:
                predictionText = "I see lizard";
                break;
        }
        document.getElementById("prediction").innerText = predictionText;
        predictedClass.dispose();
        await tf.nextFrame();
    }
    if (!isPredicting) {
        document.getElementById("prediction").innerText = "\xa0"; //&nbsp
    }
}


async function doTraining() {
    await train();
    start_button.disabled = false;
    train_button.disabled = true;
    disable_sample_buttons();
    alert("Training Done!")
}

function startPredicting() {
    if (isPredicting == false) {
        start_button.innerText = "Stop predicting";
        isPredicting = true;
    } else {
        start_button.innerText = "Start predicting";
        isPredicting = false;
    }

    predict();
}

async function init() {
    await webcam.setup();
    mobilenet = await loadMobilenet();
    tf.tidy(() => mobilenet.predict(webcam.capture()));
}

init();