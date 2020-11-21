class AdventCalendar {
  constructor(backgroundImageUrl) {
    this.backgroundImageUrl = backgroundImageUrl;

    this.container = document.createElement("div");
    this.container.classList.add("calendar");

    this.background = document.createElement("img");
    this.background.src = backgroundImageUrl;
    this.container.appendChild(this.background);

    this.windows = 0;
  }

  createWindow(label, { position, contentUrls }) {
    if (this.windows >= 24) {
      throw new Error("Only 24 windows in an advent calendar yao!");
    }

    const window = document.createElement("div");
    this.container.appendChild(window);

    window.classList.add("window");
    window.style.left = position.x + "px";
    window.style.top = position.y + "px";
    window.style.width = position.width + "px";
    window.style.height = position.height + "px";

    const hatch = document.createElement("div");
    window.appendChild(hatch);

    if (contentUrls) {
      const link = document.createElement("a");
      link.classList.add("link");
      link.href = contentUrls.linkUrl;
      link.style.backgroundImage = `url(${contentUrls.imageUrl})`;
      window.appendChild(link);

      hatch.onclick = () => {
        hatch.classList.toggle("open");
      };
    }

    hatch.classList.add("hatch");

    hatch.style.backgroundImage = `url(${this.backgroundImageUrl})`;
    hatch.style.backgroundPosition = `-${position.x + 1}px -${position.y +
      1}px`;

    hatch.classList.add("left");

    hatch.innerText = label;
    ++this.windows;
  }
}
