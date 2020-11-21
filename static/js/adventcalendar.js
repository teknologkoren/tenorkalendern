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
      throw new Error("Only 24 windows in an advent calendar, yao!");
    }
    const { offset, size } = position;

    console.log(offset, size);

    const window = document.createElement("div");
    this.container.appendChild(window);

    window.classList.add("window");
    window.style.left = offset.x + "px";
    window.style.top = offset.y + "px";
    window.style.width = size.width + "px";
    window.style.height = size.height + "px";

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
    hatch.style.backgroundPosition = `-${offset.x + 1}px -${offset.y + 1}px`;

    hatch.classList.add("left");

    hatch.innerText = label;
    ++this.windows;
  }
}
