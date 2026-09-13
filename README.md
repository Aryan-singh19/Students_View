<div align="center">

# 🎓 Theory of Computation: Intelligent Tracker

**A YouTube-style learning environment with integrated attention-tracking and academic integrity enforcement.**

[![Launch App](https://img.shields.io/badge/Launch-Live_Demo-success?style=for-the-badge&logo=githubpages&logoColor=white)](https://aryan-singh19.github.io/Students_View/)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)](https://github.com/aryan-singh19/Students_View)
[![Focus](https://img.shields.io/badge/Focus-Academic-blue?style=for-the-badge)](https://github.com/aryan-singh19/Students_View)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

<p>
  <a href="#-overview">Overview</a> •
  <a href="#-key-features">Key Features</a> •
  <a href="#-technical-architecture">Technical Architecture</a> •
  <a href="#-getting-started">Getting Started</a> •
  <a href="#-troubleshooting">Troubleshooting</a>
</p>

</div>

---

## 📖 Overview

The **Theory of Computation Tracker** is a compliance-focused **Learning Management System (LMS) module** designed to solve the problem of passive video consumption in online learning.

By integrating directly with modern browser lifecycle events, the tracker measures user engagement with second-by-second granularity. It prevents background playback, enforces continuous focus, and verifies that students actively watch lecture material before producing an exportable proof-of-completion report.

---

## 🎯 Key Features

### 🖥️ Immersive Interface
* **Dark Mode Native:** A sleek, high-contrast UI inspired by modern streaming platforms, engineered to reduce visual fatigue during dense proof-and-code lectures.
* **Responsive Playlist:** Dynamic sidebar navigation with real-time video thumbnail updates and completion indicators.

### 🛡️ Academic Integrity (Anti-Cheat)
* **Visibility-Based Auto-Pause:** Utilizes the **Page Visibility API** (`document.hidden`) to automatically freeze playback whenever the user switches tabs, minimizes the browser, or covers the window.
* **No-Skip Policy:** Manages scrubber behavior to encourage linear consumption of complex theoretical topics.

### 📊 Granular Analytics
* **Real-Time Persistence:** Saves playback position and metrics to `localStorage` every second—safeguarding against accidental tab closure.
* **Visual Feedback:** Dynamic progress bars overlay on video thumbnails in the sidebar.
* **Verifiable Reports:** Generates a downloadable `.txt` report card summarizing viewed intervals for class submission.

---

## 🛠️ Technical Architecture

Built purely with **Vanilla JavaScript** to ensure maximum performance and zero external dependencies.

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Frontend** | HTML5 / CSS3 | Responsive Flexbox/Grid layout with custom CSS variables for theming. |
| **Logic** | ES6+ JavaScript | Handles state management, lifecycle event listeners, and DOM updates. |
| **Video Engine** | YouTube IFrame API | Programmatic control over playback states, timing loops, and auto-pause triggers. |
| **State** | `localStorage` | Persists user session and progress timestamps across reloads without a backend database. |
| **Sensors** | `document.hidden` | Detects tab-switching and window-blur events to trigger the auto-pause mechanic. |

---

## 🚀 Getting Started

### Prerequisites
No installation is required to use the tracker; it is a fully client-side web application.

### Usage Guide
1. **Launch:** Access the [Hosted Tracker](https://aryan-singh19.github.io/Students_View/).
2. **Select:** Choose a lecture from the "Theory of Computation" playlist on the right.
3. **Watch:** Keep the tab **focused**.
   > *Note: If you switch tabs to check Discord or Instagram, the video will pause immediately.*
4. **Track:** Observe the progress bar filling up on the sidebar thumbnail in real time.
5. **Export:** Navigate to the **Analytics & Download** tab and click **Download Progress Report** to generate your submission file.

### Local Development (Optional)

If you wish to modify the code or contribute:

# Clone the repository
git clone https://github.com/aryan-singh19/Students_View.git

# Navigate to the directory
cd Students_View

# Open index.html in your browser OR use a local server (recommended for API origin stability)
npx serve .

```

## 📂 Project Structure

Students_View/
├── index.html       # Main entry point and layout structure
├── style.css        # Custom dark-mode styling and animations
├── script.js        # Core logic: API integration, focus tracking, and analytics
├── assets/          # Icons and static resources
└── README.md        # Documentation

```

## ⚠️ Troubleshooting

* **Progress not saving?** Ensure you are not using **Incognito/Private Mode**, as `localStorage` is cleared automatically when the tab closes in private sessions.
* **Video not playing?** Some ad-blockers or privacy extensions interfere with the YouTube IFrame API. Whitelist the domain or temporarily disable blockers if playback fails to initialize.

---

<div align="center">

Made with ❤️ for the Theory of Computation Class  
**[View Developer Profile](https://github.com/aryan-singh19)**

</div>


