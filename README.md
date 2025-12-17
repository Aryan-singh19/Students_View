🎓 Student Playlist Tracker
A simple, client-side tool to track student engagement on YouTube playlists. This tool embeds a specific YouTube playlist and monitors whether the viewer is actually watching the content or skipping through it.
It generates a Progress Report that students can copy and submit to verify their work.
🚀 Live Demo
Click here to view the Tracker > (Note: Replace the link above with your actual GitHub Pages URL once setup is complete)
✨ Features
Anti-Cheat System: The video automatically pauses if the user switches tabs or minimizes the window (uses the Page Visibility API).
Precision Tracking: Tracks every second watched. Dragging the slider (skipping) leaves "gaps" in the data, resulting in a low score.
Playlist Support: Automatically loads the assigned YouTube playlist.
Auto-Save: Progress is saved to the browser's Local Storage, so students can refresh the page or come back later without losing their grades.
Report Generation: One-click button to copy a text-based report card to the clipboard for submission.
📋 How It Works
The Student opens the hosted webpage.
They watch the videos in the playlist.
The script tracks which specific seconds of the video were played.
If they try to "scrub" (skip ahead), those skipped seconds are not counted.
Once finished, they click "Copy Report to Send".
They paste the report (Ctrl+V) into an email, WhatsApp, or LMS assignment to send to the instructor.
Example Report Output
My Video Progress Report:
-------------------------
Video 1: 98.5%
Video 2: 12.0%
Video 3: 100.0%

Sent from Class Tracker.
🛠️ Configuration
To use this for your own classes, you only need to edit one line in index.html.
Open index.html.
Find the configuration section near the bottom script:
// --- CONFIGURATION ---
const PLAYLIST_ID = 'PL424dCM7s48ngY-ylr6rKDhZC-eojZyOT'; // <--- Replace this ID with your own
Replace the ID with your own YouTube Playlist ID.
Commit the changes to GitHub.
📦 How to Host (Free)
This project is designed to run on GitHub Pages.
Create a public repository on GitHub.
Upload the index.html file to your repository.
Go to Settings > Pages (in the left sidebar).
Under Branch, select main (or master) and ensure the folder is /(root).
Click Save.
Wait 1-2 minutes. Your site will be live at:
https://<your-username>.github.io/<repository-name>/
⚠️ Disclaimer
This is a client-side tool designed for low-stakes accountability (e.g., verifying homework or training compliance).
Is it hackable? Yes. A tech-savvy student who knows JavaScript could inspect the code and manually modify their score variables.
Is it effective? For 99% of general students, it is highly effective at preventing "lazy skipping" and background playing.
📄 License
This project is open source. Feel free to modify and use it for educational or commercial purposes.
