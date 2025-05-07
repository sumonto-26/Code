let currentChapter = "";

function goTo(section, data = "") {
  if (section === "chapter") currentChapter = data;
  history.pushState({ section: section, data: data }, "", "#" + section);
  renderSection(section, data);
}

function goBack() {
  history.back(); // triggers onpopstate
}

function renderSection(section, data = "") {
  document.querySelectorAll("main > div").forEach(div => div.classList.add("hidden"));

  if (section === "chapter") {
    document.getElementById("chapter-title").textContent = data;
    document.getElementById("options-section").classList.remove("hidden");
  } else if (section === "videos") {
    document.getElementById("video-options").classList.remove("hidden");
  } else if (section === "notes") {
    document.getElementById("notes-options").classList.remove("hidden");
  } else if (section === "problems") {
    document.getElementById("problems-options").classList.remove("hidden");
  } else if (section === "oneshots" || section === "course") {
    const videoTitle = section === "oneshots" ? "🎯 One Shots Videos" : "📘 Course Videos";
    document.getElementById("video-title").textContent = videoTitle;

    const videoContainer = document.querySelector(".video-list");
    videoContainer.innerHTML = "";

    const chapterVideos = videos[currentChapter]?.[section] || [];
    if (chapterVideos.length === 0) {
      videoContainer.innerHTML = "<p>No videos available for this chapter.</p>";
    } else {
      chapterVideos.forEach(url => {
        const iframe = document.createElement("iframe");
        iframe.src = url;
        iframe.allowFullscreen = true;
        videoContainer.appendChild(iframe);
      });
    }

    document.getElementById("video-page").classList.remove("hidden");
  } else {
    document.getElementById("chapter-section").classList.remove("hidden");
  }
}

window.onpopstate = function(event) {
  if (event.state) {
    renderSection(event.state.section, event.state.data);
  } else {
    renderSection("home");
  }
};
