// ============================================================
// LAYOUT THRASHING DEMO
// ============================================================

// Create the demo section
const demo = document.createElement("section");

demo.style.padding = "40px 20px";
demo.style.background = "#f1f1f1";
demo.style.marginTop = "40px";

demo.innerHTML = `
    <h2>Layout Thrashing Demo</h2>

    <p>
        Compare the intentionally bad version with the optimized version.
    </p>

    <button id="badButton">
        Run Bad Version
    </button>

    <button id="goodButton">
        Run Good Version
    </button>

    <div id="demoBox"
         style="
            width: 200px;
            height: 50px;
            margin-top: 20px;
            padding: 10px;
            background: white;
            border: 1px solid #999;
            box-sizing: border-box;
         ">
        Demo Box
    </div>

    <p id="result"></p>
`;

document.body.appendChild(demo);


// Get our single demo box
const box = document.getElementById("demoBox");

const result = document.getElementById("result");


// ============================================================
// ❌ BAD VERSION — LAYOUT THRASHING
// ============================================================

function runBadVersion() {

    console.clear();

    console.log("❌ BAD VERSION STARTED");

    const start = performance.now();

    for (let i = 0; i < 100; i++) {

        // WRITE
        box.style.width = `${200 + i}px`;

        // READ
        // This can force the browser to calculate layout
        // immediately after the style change.
        const height = box.offsetHeight;

        console.log(
            `Iteration ${i + 1}: height = ${height}px`
        );
    }

    const end = performance.now();

    console.log(
        `❌ Bad version: ${(end - start).toFixed(2)} ms`
    );

    result.textContent =
        `❌ Bad version completed in ${(end - start).toFixed(2)} ms`;
}


// ============================================================
// ✅ GOOD VERSION — BATCHED READS AND WRITES
// ============================================================

function runGoodVersion() {

    console.clear();

    console.log("✅ GOOD VERSION STARTED");

    const start = performance.now();

    // --------------------------------------------------------
    // STEP 1 — READ
    // --------------------------------------------------------

    const height = box.offsetHeight;

    console.log(
        `Initial height: ${height}px`
    );


    // --------------------------------------------------------
    // STEP 2 — WRITE
    // --------------------------------------------------------

    for (let i = 0; i < 100; i++) {

        box.style.width = `${200 + i}px`;
    }


    const end = performance.now();

    console.log(
        `✅ Good version: ${(end - start).toFixed(2)} ms`
    );

    result.textContent =
        `✅ Good version completed in ${(end - start).toFixed(2)} ms`;
}


// ============================================================
// BUTTONS
// ============================================================

document
    .getElementById("badButton")
    .addEventListener("click", runBadVersion);

document
    .getElementById("goodButton")
    .addEventListener("click", runGoodVersion);