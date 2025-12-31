AOS.init({
  duration: 900,
  easing: "ease-out-cubic",
  once: true,
  offset: 80
});

/* Evaluation Pipeline */
document.addEventListener("DOMContentLoaded", () => {
  const steps = document.querySelectorAll(".eval-step");
  const finalScore = document.querySelector(".final-score");
  const dashboard = document.querySelector(".dashboard-grid");
  const backBtn = document.querySelector(".back-btn");

  let current = 0;

  function runStep() {
    if (current >= steps.length) {
      revealResults();
      return;
    }

    setTimeout(() => {
      steps[current].classList.add("completed");
      current++;
      runStep();
    }, 900);
  }

  function revealResults() {
    finalScore.classList.remove("hidden");
    dashboard.classList.remove("hidden");
    backBtn.classList.remove("hidden");

    animateScore();
    AOS.refresh();
  }

  function animateScore() {
    const ring = document.querySelector(".score-ring");
    if (!ring) return;

    const target = parseInt(ring.dataset.score);
    const value = document.getElementById("scoreValue");
    let count = 0;

    const timer = setInterval(() => {
      count++;
      value.textContent = count;
      ring.style.background =
        `conic-gradient(#3b82f6 ${count * 3.6}deg, #0b1220 0deg)`;

      if (count >= target) clearInterval(timer);
    }, 16);
  }

  runStep();
});
