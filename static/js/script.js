/* =====================================================
   CLASSICAL CRYPTOGRAPHY SIMULATOR
   MODERN UI/UX SCRIPT
===================================================== */

/* =====================================================
   ELEMENTS
===================================================== */

const algorithmSelect =
    document.getElementById("algorithm");

const actionSelect =
    document.getElementById("action");

const cryptoForm =
    document.getElementById("crypto-form");

const processBtn =
    document.getElementById("process-btn");

const darkModeBtn =
    document.getElementById("theme-toggle");

/* =====================================================
   ALGORITHM FIELD
===================================================== */

const caesarField =
    document.getElementById("caesar-field");

const vigenereField =
    document.getElementById("vigenere-field");

const affineField =
    document.getElementById("affine-field");

const hillField =
    document.getElementById("hill-field");

const playfairField =
    document.getElementById("playfair-field");

/* =====================================================
   HIDE ALL FIELDS
===================================================== */

function hideAllFields() {

    document
        .querySelectorAll(".option-field")
        .forEach(field => {

            field.classList.add("d-none");

        });

}

/* =====================================================
   SHOW FIELD BASED ON ALGORITHM
===================================================== */

function showFields() {

    const value = algorithmSelect.value;

    hideAllFields();

    switch (value) {

        case "caesar":

            caesarField.classList.remove("d-none");

            break;

        case "vigenere":

            vigenereField.classList.remove("d-none");

            break;

        case "affine":

            affineField.classList.remove("d-none");

            break;

        case "hill":

            hillField.classList.remove("d-none");

            break;

        case "playfair":

            playfairField.classList.remove("d-none");

            break;
    }

    updateAlgorithmInfo();

}

/* =====================================================
   ALGORITHM EDUCATION INFO
===================================================== */

function updateAlgorithmInfo() {

    const infoBox =
        document.getElementById("algorithm-info");

    if (!infoBox) return;

    const algorithm =
        algorithmSelect.value;

    let html = "";

    if (algorithm === "caesar") {

        html = `
            <div class="alert alert-primary">
                <strong>Caesar Cipher</strong><br>
                Menggeser setiap huruf berdasarkan
                nilai shift tertentu.
                <br><br>
                Rumus:
                <code>E(x) = (x + k) mod 26</code>
            </div>
        `;
    }

    else if (algorithm === "vigenere") {

        html = `
            <div class="alert alert-success">
                <strong>Vigenère Cipher</strong><br>
                Menggunakan kata kunci untuk
                melakukan pergeseran huruf.
                <br><br>
                Rumus:
                <code>Ci = (Pi + Ki) mod 26</code>
            </div>
        `;
    }

    else if (algorithm === "affine") {

        html = `
            <div class="alert alert-warning">
                <strong>Affine Cipher</strong><br>
                Menggunakan fungsi matematika linear.
                <br><br>
                Rumus:
                <code>E(x) = (ax + b) mod 26</code>
            </div>
        `;
    }

    else if (algorithm === "hill") {

        html = `
            <div class="alert alert-info">
                <strong>Hill Cipher</strong><br>
                Menggunakan perkalian matriks
                dalam proses enkripsi.
                <br><br>
                Rumus:
                <code>C = K × P mod 26</code>
            </div>
        `;
    }

    else if (algorithm === "playfair") {

        html = `
            <div class="alert alert-danger">
                <strong>Playfair Cipher</strong><br>
                Menggunakan tabel matriks 5x5
                dan pairing huruf.
                <br><br>
                Teknik:
                <code>Bigram Encryption</code>
            </div>
        `;
    }

    infoBox.innerHTML = html;

}

/* =====================================================
   FORM VALIDATION
===================================================== */

function validateForm(event) {

    const algorithm =
        algorithmSelect.value;

    const text =
        document.getElementById("text").value;

    if (text.trim() === "") {

        event.preventDefault();

        showToast(
            "Input text tidak boleh kosong!",
            "danger"
        );

        return false;
    }

    /* =========================
       CAESAR VALIDATION
    ========================= */

    if (algorithm === "caesar") {

        const shift =
            document.getElementById("shift").value;

        if (
            shift < 1 ||
            shift > 25
        ) {

            event.preventDefault();

            showToast(
                "Shift Caesar harus 1 - 25",
                "warning"
            );

            return false;
        }

    }

    /* =========================
       VIGENERE VALIDATION
    ========================= */

    if (algorithm === "vigenere") {

        const key =
            document.getElementById("key").value;

        if (key.trim() === "") {

            event.preventDefault();

            showToast(
                "Key Vigenère wajib diisi!",
                "warning"
            );

            return false;
        }

    }

    return true;

}

/* =====================================================
   PROCESS BUTTON LOADING
===================================================== */

function loadingButton() {

    if (!processBtn) return;

    processBtn.innerHTML = `
        <span class="spinner-border spinner-border-sm">
        </span>
        Processing...
    `;

    processBtn.disabled = true;

}

/* =====================================================
   TOAST NOTIFICATION
===================================================== */

function showToast(message, type) {

    const toastContainer =
        document.getElementById("toast-container");

    if (!toastContainer) return;

    const toast =
        document.createElement("div");

    toast.className =
        `alert alert-${type} shadow-lg`;

    toast.innerHTML = `
        ${message}
    `;

    toast.style.animation =
        "fadeIn 0.3s ease";

    toastContainer.appendChild(toast);

    setTimeout(() => {

        toast.remove();

    }, 3000);

}

/* =====================================================
   DARK / LIGHT MODE
===================================================== */

function toggleTheme() {

    const body =
        document.body;

    if (
        body.classList.contains("dark-mode")
    ) {

        body.classList.remove("dark-mode");

        body.classList.add("light-mode");

        localStorage.setItem(
            "theme",
            "light"
        );

    }

    else {

        body.classList.remove("light-mode");

        body.classList.add("dark-mode");

        localStorage.setItem(
            "theme",
            "dark"
        );

    }

}

/* =====================================================
   LOAD SAVED THEME
===================================================== */

function loadTheme() {

    const savedTheme =
        localStorage.getItem("theme");

    if (savedTheme === "light") {

        document.body.classList.remove("dark-mode");

        document.body.classList.add("light-mode");

    }

    else {

        document.body.classList.add("dark-mode");

    }

}

/* =====================================================
   CARD ANIMATION
===================================================== */

function animateCards() {

    const cards =
        document.querySelectorAll(".card");

    cards.forEach((card, index) => {

        card.style.opacity = "0";

        card.style.transform =
            "translateY(20px)";

        setTimeout(() => {

            card.style.transition =
                "all 0.5s ease";

            card.style.opacity = "1";

            card.style.transform =
                "translateY(0px)";

        }, index * 150);

    });

}

/* =====================================================
   MATRIX HOVER EFFECT
===================================================== */

function matrixAnimation() {

    const cells =
        document.querySelectorAll(".matrix-cell");

    cells.forEach(cell => {

        cell.addEventListener(
            "mouseenter",
            () => {

                cell.style.transform =
                    "scale(1.08) rotate(2deg)";
            }
        );

        cell.addEventListener(
            "mouseleave",
            () => {

                cell.style.transform =
                    "scale(1)";
            }
        );

    });

}

/* =====================================================
   TYPEWRITER EFFECT
===================================================== */

function typeWriterEffect() {

    const title =
        document.querySelector(".hero-title");

    if (!title) return;

    const text =
        title.innerText;

    title.innerText = "";

    let i = 0;

    const interval = setInterval(() => {

        title.innerText += text.charAt(i);

        i++;

        if (i >= text.length) {

            clearInterval(interval);

        }

    }, 40);

}

/* =====================================================
   COPY RESULT BUTTON
===================================================== */

function copyResult() {

    const resultBox =
        document.getElementById("result-text");

    if (!resultBox) return;

    navigator.clipboard.writeText(
        resultBox.innerText
    );

    showToast(
        "Hasil berhasil disalin!",
        "success"
    );

}

/* =====================================================
   EVENT LISTENER
===================================================== */

algorithmSelect.addEventListener(
    "change",
    showFields
);

if (cryptoForm) {

    cryptoForm.addEventListener(
        "submit",
        (event) => {

            const valid =
                validateForm(event);

            if (valid) {

                loadingButton();

            }

        }
    );

}

if (darkModeBtn) {

    darkModeBtn.addEventListener(
        "click",
        toggleTheme
    );

}

/* =====================================================
   INIT
===================================================== */

document.addEventListener(
    "DOMContentLoaded",
    () => {

        loadTheme();

        showFields();

        animateCards();

        matrixAnimation();

        typeWriterEffect();

    }
);