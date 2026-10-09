
async function RunSentimentAnalysis() {
    const input = document.getElementById("textToAnalyze");
    const output = document.getElementById("system_response");
    const text = input.value;

    if (!text.trim()) {
        output.textContent = "Please enter some text to analyze.";
        return;
    }

    output.textContent = "Analyzing...";

    try {
        const response = await fetch(
            "/emotionDetector?textToAnalyze=" +
            encodeURIComponent(text)
        );

        const result = await response.text();
        output.textContent = result;

    } catch (error) {
        output.textContent =
            "Unable to connect to the emotion detection server.";
    }
}
