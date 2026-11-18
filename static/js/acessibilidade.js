(() => {
    const root = document.documentElement;
    const contrastButton = document.getElementById("contrast-toggle");
    const increaseButton = document.getElementById("font-increase");
    const decreaseButton = document.getElementById("font-decrease");
    const resetButton = document.getElementById("font-reset");
    const status = document.getElementById("accessibility-status");

    if (!contrastButton || !increaseButton || !decreaseButton || !resetButton) return;

    let fontScale = 100;

    contrastButton.addEventListener("click", () => {
        const enabled = root.classList.toggle("high-contrast");
        contrastButton.setAttribute("aria-pressed", String(enabled));
        status.textContent = enabled ? "Alto contraste ativado." : "Alto contraste desativado.";
    });

    increaseButton.addEventListener("click", () => {
        fontScale = Math.min(fontScale + 10, 150);
        root.style.fontSize = fontScale + "%";
        status.textContent = "Tamanho da fonte: " + fontScale + "%.";
    });

    decreaseButton.addEventListener("click", () => {
        fontScale = Math.max(fontScale - 10, 80);
        root.style.fontSize = fontScale + "%";
        status.textContent = "Tamanho da fonte: " + fontScale + "%.";
    });

    resetButton.addEventListener("click", () => {
        fontScale = 100;
        root.style.fontSize = "100%";
        status.textContent = "Tamanho da fonte restaurado.";
    });
})();