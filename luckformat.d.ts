/** Just does it all, returning an element containing the calendar. */
declare function createIt(options: {
    backgroundImageUrl: string,
    windows: Array<WindowDescription>,
}): HTMLElement;

declare interface WindowDescription{
    position: Position;
    contentUrls?: ContentUrls;
}

/** Creates an advent calendar to which windows can be added. */
declare function createAdventCalendar(options: {
    container: HTMLElement,
    backgroundImageUrl: string,
}): Calendar;

declare interface Calendar {
    /**
     * Creates a CalendarWindow at the given `position` with the given
     * `contentUrls`. If no content is passed, the window is locked and cannot
     * be opened.
     *
     * If an attempt is made to add more than 24 windows, errors will be
     * thrown.
     *
     * Example:
     *   calendar.addWindow({
     *       position: {x: 10, y: 20, width: 100, height: 80},
     *       contentUrls: {imageUrl, linkUrl},
     *   });
     */
    addWindow(description: WindowDescription): CalendarWindow;
}

declare interface Position {
    x: number;
    y: number;
    width: number;
    height: number;
}

declare interface ContentUrls {
    /** The url of the image to display inside the window. Will be centered. */
    imageUrl: string;
    /** The url that the content image should link to. */
    linkUrl: string;
}

declare interface CalendarWindow {
    /** The calendar day. A number between 1 and 24. Yes, 24. Bite me! */
    readonly day: number;
}
