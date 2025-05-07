let currentChapter = "";

const videos = {
  "Chapter 1:": { 
    oneshots: [
      
    ],
    course: [
    ]
  },
  
  "Chapter 2:": {
    oneshots: [
    ],
    course: []
  },

  "Chapter 3:": { 
    oneshots: [
        "https://www.youtube.com/embed/p5rcchZ1JH4?si=H51SetVa3AkZSX0P"
    ],
    course: [
    ] 
  },
  
  "Chapter 4:": { 
    oneshots: [
    ], 
    course: [] 
  },
  
  "Chapter 5:": { 
    oneshots: [
    ], 
    course: [] 
  },

  "Chapter 6:": { 
    oneshots: [
    ],
    course: [
    ]
  },

  "Others:": { oneshots: [
    "https://www.youtube.com/embed/z5EEuYEc6bQ?si=MmKbcXVrDNra8BPY",
    "https://www.youtube.com/embed/z5s5G-J3Z7c?si=fVZzfWSxXL43nRF3"
  ],
  course: [
    "https://www.youtube.com/embed/a8LdEvd7Pwc?si=PQoT7i1oa-sTmlTG",
    "https://www.youtube.com/embed/b9CUI5SS6RA?si=qZvJV0eN0GB2DOHz"
  ] 
},
};

const problemsPhotos = {
  "Chapter 1:": {
    mcq: [],
    cq: []
  },
  "Chapter 2:": { mcq: [], cq: [] },
  "Chapter 3:": { mcq: [], cq: [] },
  "Chapter 4:": { mcq: [], cq: [] },
  "Chapter 5:": { mcq: [], cq: [] },
  "Chapter 6:": { mcq: [], cq: [] },
  "Others:": { mcq: [], cq: [] },
};

const notes = {
  "Chapter 1:": {
    videos: [],
    images: [],
    pdfs: []
  },
  "Chapter 2:": { videos: [], images: [], pdfs: [] },
  "Chapter 3:": { videos: [], images: [], pdfs: [] },
  "Chapter 4:": { videos: [], images: [], pdfs: [] },
  "Chapter 5:": { videos: [], images: [], pdfs: [] },
  "Chapter 6:": { videos: [], images: [], pdfs: [] },
  "Others:": { videos: [], images: [], pdfs: [] }
};

function goTo(section, data = "") {
  if (section === "chapter") currentChapter = data;
  history.pushState({ section, data }, "", "#" + section);
  renderSection(section, data);
}

function goBack() {
  history.back();
}

function renderSection(section, data = "") {
  document.querySelectorAll("main > div").forEach(div => div.classList.add("hidden"));

  const showItems = (items, container, type = "iframe") => {
    container.innerHTML = items.length === 0
      ? "<p>No items available for this chapter.</p>"
      : "";
    items.forEach(url => {
      const el = document.createElement(type === "img" ? "img" : "iframe");
      el.src = url;
      if (type === "iframe") el.allowFullscreen = true;
      container.appendChild(el);
    });
  };

  switch (section) {
    case "chapter":
      document.getElementById("chapter-title").textContent = data;
      document.getElementById("options-section").classList.remove("hidden");
      break;
    case "videos":
      document.getElementById("video-options").classList.remove("hidden");
      break;
    case "notes":
      document.getElementById("notes-options").classList.remove("hidden");
      break;
    case "problems":
      document.getElementById("problems-options").classList.remove("hidden");
      break;
    case "photos":
      showItems(problemsPhotos[currentChapter] || [], document.querySelector("#photos .photo-list"), "img");
      document.getElementById("photos").classList.remove("hidden");
      break;
    case "oneshots":
    case "course":
      document.getElementById("video-title").textContent = section === "oneshots" ? "🎯 One Shots Videos" : "📘 Course Videos";
      showItems(videos[currentChapter]?.[section] || [], document.querySelector(".video-list"));
      document.getElementById("video-page").classList.remove("hidden");
      break;
    case "notes-section":
      showItems(notes[currentChapter]?.pdfs || [], document.querySelector(".notes-list"));
      break;
    default:
      break;
  }
}

window.addEventListener("popstate", (event) => {
  const state = event.state;
  renderSection(state?.section, state?.data);
});
