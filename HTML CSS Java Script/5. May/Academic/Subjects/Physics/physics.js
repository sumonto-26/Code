let currentChapter = "";

const videos = {
  "Chapter 1:": { 
    oneshots: [
      "https://www.youtube.com/embed/yeBjLwKutl0?si=csM0mec9ybDoNhHo",
      "https://www.youtube.com/embed/2rH8yLsNOvI?si=tgWpprZBE2NHPRzB", 
      "https://www.youtube.com/embed/ldGRYoWoJFc?si=0H6X8lSv_YHqzRln",
      "https://www.youtube.com/watch?v=F6gMQiEykh0",
      "https://www.youtube.com/embed/4eE-6RKTPN0?si=Wb93qfOFe3Bs4caF",
      "https://www.youtube.com/embed/pbUbXE4BHV8?si=ZVilngop8B_t6Laj"
    ],
    course: [
      "https://www.youtube.com/embed/46GKKXG95-g?si=SSuXjaPQBS_p_mjU",
      "https://www.youtube.com/embed/hzYEL77Mv4w?si=Su6WdOTWeQ98OquB",
      "https://www.youtube.com/embed/mRBSRATONhQ?si=qSUfOrK6eQiReJm4"
    ]
  },
  
  "Chapter 2:": {
    oneshots: [
      "https://www.youtube.com/embed/1lSGS9JAAFw", 
      "https://www.youtube.com/embed/ldGRYoWoJFc?si=MEb5YsM7OZgCuAZ_"
    ],
    course: []
  },

  "Chapter 3:": { 
    oneshots: [
      "https://www.youtube.com/embed/WOvcFM2cBAo", 
      "https://www.youtube.com/embed/g6zVrmArqWQ?si=EXgmkDSc41zIRe_0", 
      "https://www.youtube.com/embed/jeN_EttA9-4?si=iBXhzGnC8fHl56qK",
    ],
    course: [] 
  },
  
  "Chapter 4:": { 
    oneshots: [
      "https://www.youtube.com/embed/KiFedKyPp8Y", 
      "https://www.youtube.com/embed/zpvcxlONIOE?si=5otajNJM9e1O12dw",
    ], 
    course: [] 
  },
  
  "Chapter 5:": { 
    oneshots: [
      "https://www.youtube.com/embed/oeH5ZUVARv4?si=RgzTFac1TicKr0L4",
      "https://www.youtube.com/embed/GBto5bgkQe0?si=ntOHfL35pAISmVsA"
    ], 
    course: [] 
  },

  "Chapter 6:": { 
    oneshots: [
      "https://www.youtube.com/embed/15fwTfSeW1o?si=02TPAgexq44_5nfc",
      "https://www.youtube.com/embed/GnTelD_J9nk?si=pKAev40q7KvN5-ka"
    ],
    course: [
      "https://www.youtube.com/embed/UDxnYnZuaHU?si=dfzdO0G3A2huXXV-",
      "https://www.youtube.com/embed/RPyEeHyCMik?si=_w9BzZr5SRpLxROS",
      "https://www.youtube.com/embed/wLqtOcbFCoA?si=j8mwpXSJr8nYlIgx"
    ]
  },

  "Others:": { oneshots: [
    "https://www.youtube.com/embed/MveoyYPz4lA?si=cT21avP-xeQh3a3T",
    "https://www.youtube.com/embed/Vh8y8ZcKSNs?si=JEjNPkDHewhfXdZR",
    "https://www.youtube.com/embed/SNGe6hLycow?si=x_dX5FMhvyXJLXBQ",
    "https://www.youtube.com/embed/eQqB8aOQiFU?si=ZHJicm2WtWs7lDzs",
    "https://www.youtube.com/embed/qo3VECVLQYc?si=m1rmwmBd7PHIOPrd",
    "https://www.youtube.com/embed/LlARlgfileE?si=UTu5irt64UEaE4k6",
    "https://www.youtube.com/embed/zhC3z_CnEZ4?si=m9bz4reqRyOE4QUf",
    "https://www.youtube.com/embed/2MM7mEkNgRQ?si=oh1-LxKrfjhXMeES",
    "https://www.youtube.com/embed/nzGIy6nM2qo?si=cCPWm1NMKp97kPBF",
    "https://www.youtube.com/embed/UeEiKwyTQWw?si=ttKvUqP_FI04x7R9"
  ],
  course: [
    "https://www.youtube.com/embed/dakEp10n0HU?si=RAOiC6tYj2ubMkJ1",
    "https://www.youtube.com/embed/vNhuM-PxLVE?si=aCvYRWCVLmj4ifk1",
    "https://www.youtube.com/embed/79pwA2xxu_M?si=_-ikFyvV8ctuztRW",
    
    "https://www.youtube.com/embed/PfgG0iCSx0I?si=laLstLn9gilaeBYf",
    "https://www.youtube.com/embed/mktmipqA_CM?si=3KDkYzvEA5CQwPmS",
    "https://www.youtube.com/embed/vXFQaPMpIxU?si=kWmYfkX-nK1M31uI"
  ] 
},
};

const problemsPhotos = {
  "Chapter 1:": {
    mcq: ["https://via.placeholder.com/300x200?text=MCQ+1"],
    cq: ["https://via.placeholder.com/300x200?text=CQ+1"]
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
    videos: ["https://www.youtube.com/embed/1lSGS9JAAFw"],
    images: ["https://via.placeholder.com/300x200?text=Note+Image+1"],
    pdfs: ["https://drive.google.com/file/d/1IehDVA91kQe9r2fYqsbTZO7JgcPWi2JY/view?usp=sharing"]
  },
  "Chapter 2:": { videos: [], images: [], pdfs: ["https://drive.google.com/file/d/1E1HaFI7QkXUieufXbcapm5CSC3LU_8Jr/view?usp=sharing"] },
  "Chapter 3:": { videos: [], images: [], pdfs: ["https://drive.google.com/file/d/1nLb43NUS2endyJb9dy6nANMf4eQqbnpF/view?usp=sharing"] },
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
