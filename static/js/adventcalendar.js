class AdventCalendar {
  constructor(backgroundImageUrl, storage) {
    this.backgroundImageUrl = backgroundImageUrl;

    this.container = document.createElement("div");
    this.container.classList.add("calendar");

    this.background = document.createElement("img");
    this.background.src = backgroundImageUrl;
    this.background.setAttribute('draggable', false);
    this.container.appendChild(this.background);

    this.storage = storage;
    this.opened = new Set(JSON.parse(storage.getItem("opened") || "[]"));

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
      if (this.opened.has(label)) {
        hatch.classList.add("open");
        link.style.display = "block";
      } else {
        setTimeout(function(){ link.style.display = "block"; }, 500);
      }
      link.href = contentUrls.linkUrl;
      link.style.backgroundImage = `url(${contentUrls.imageUrl})`;
      window.appendChild(link);

      hatch.onclick = () => {
        hatch.classList.toggle("open");
        // If we couldn't remove the lable from opened, it wasn't open meaning
        // it is open now. So we should add it.
        if (!this.opened.delete(label)) {
          this.opened.add(label);
        }
        this.storage.setItem("opened", JSON.stringify(Array.from(this.opened)));
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
