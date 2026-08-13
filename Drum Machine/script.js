const display = document.getElementById("display");

const sounds = {
  Q: "Heater 1",
  W: "Heater 2",
  E: "Heater 3",
  A: "Heater 4",
  S: "Clap",
  D: "Open-HH",
  Z: "Kick-n'-Hat",
  X: "Kick",
  C: "Closed-HH"
};

function playSound(key) {
  const audio = document.getElementById(key);

  if (!audio) return;

  audio.currentTime = 0;
  audio.play();

  display.innerText = sounds[key];
}

document.querySelectorAll(".drum-pad").forEach(pad => {
  pad.addEventListener("click", () => {
    playSound(pad.innerText.trim());
  });
});

document.addEventListener("keydown", e => {
  const key = e.key.toUpperCase();

  if (sounds[key]) {
    playSound(key);
  }
});