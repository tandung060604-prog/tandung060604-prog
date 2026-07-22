# GitHub Profile Redesign Report

Audit date: **July 22, 2026**
Target account: **`tandung060604-prog`**

## Summary

A complete GitHub profile repository was scaffolded as a recruiter-focused landing page for a recent Robotics and Artificial Intelligence graduate. The result emphasizes practical RAG/LLM work, AI agents, robotics, workflow automation, honest project status, traceable evidence, and clear contact/CV calls to action.

The starting workspace contained no profile repository, README, assets, resume files, or approved personal images. Because there was no existing README, no `README.backup.md` was created.

## Files created

- `README.md` — redesigned profile landing page.
- `assets/github-profile-banner.svg` — 1200 × 360 custom hero banner.
- `assets/github-profile-banner-mobile.svg` — 720 × 480 responsive hero variant for narrow screens.
- `assets/project-images/haui-admission-ai-architecture.svg` — 1280 × 720 architecture visual.
- `assets/profile-avatar-placeholder.svg` — abstract 512 × 512 non-photo placeholder.
- `assets/DESIGN_SYSTEM.md` — palette, typography, components, and responsive rules.
- `assets/IMAGE_GUIDE.md` — safe photo/screenshot replacement guidance.
- `resume/README.md` — public CV inventory and publishing guidance.
- `resume/Nguyen-Bui-Tan-Dung-CV-EN.pdf` — English CV supplied by the profile owner.
- `resume/Nguyen-Bui-Tan-Dung-CV-VI.pdf` — Vietnamese CV supplied by the profile owner.
- `GITHUB_PROFILE_UPDATE_COMMANDS.md` — safe, unexecuted metadata update proposal.
- `PROFILE_REDESIGN_REPORT.md` — this implementation and handoff report.
- `.gitignore` — blocks common local secret/environment files and OS clutter.

## Files modified

None. The deliverable was created in a new directory because the workspace did not contain an existing profile repository.

## Main profile sections

1. Custom AI/robotics hero banner.
2. Concise professional introduction.
3. “What I'm working on” focus list.
4. Evidence-based technical toolkit grouped by discipline.
5. Featured HaUI Admission AI case study with architecture, differentiators, demo, and repository.
6. Four selected projects with one-sentence descriptions, stacks, links, and honest status labels.
7. Native links to GitHub repositories and public activity without vanity metrics.
8. Direct English/Vietnamese CV actions.
9. Confirmed email, Instagram, Discord, location, and GitHub contact section.
10. Minimal personal footer.

## Repository audit and project selection

The public account exposed **35 repositories** during the audit. Forked course materials, small daily labs, and repositories without enough context were excluded.

Selected projects:

- **HaUi-Admission-Chatbot** — featured because its README documents a RAG admissions system, citations, year filtering, handoff, an admin/advisor dashboard, FastAPI, PostgreSQL, and Docker setup. Status confirmed as Completed.
- **Camunda-Quest-Academy** — selected for its unusually complete product scope, modular FastAPI architecture, content validation, test/quality tooling, and practical BPMN/Camunda focus.
- **Human-Following-Robot** — selected as the strongest cross-disciplinary perception/embedded robotics project; confirmed as an individual project and labeled Prototype.
- **Esp32-self-balancing-robot** — selected for control-system depth spanning PID, LQR, Kalman filtering, ESP32 firmware, and MATLAB/Simulink; labeled Prototype.
- **NexaRead-AI** — selected for its documented full-stack architecture and engineering quality; labeled In Progress, with OCR/RAG/LLM work explicitly described as planned rather than complete.

The **Robot-Vision-System** repository was reviewed but not listed to keep the profile concise and avoid overlapping heavily with the two selected robotics entries.

## Link and availability findings

- GitHub profile: `https://github.com/tandung060604-prog`
- HaUI repository: `https://github.com/tandung060604-prog/HaUi-Admission-Chatbot`
- HaUI demo: `https://c2-app-028.up.railway.app`
- The demo returned a page titled “Tư vấn tuyển sinh” during the audit. The README includes a dated availability note and does not claim production uptime.
- Both tested GitHub statistics-card endpoints returned HTTP 503 during final validation. They were removed and replaced with native GitHub activity/repository links, leaving no broken statistics image dependency.

## Confirmed profile information

- Email: `tandung060604@gmail.com`
- Instagram: `@_saxichuongduong_`
- Discord: `.harunguyen`
- Location: `Ha Noi, Vietnam`
- HaUI Admission AI: Completed
- Human-Following Mobile Robot: individual project
- Confirmed tools: Ragas, Railway, Postman, Codex, and Camunda
- Introduction: “Recent Robotics and Artificial Intelligence Graduate”

LinkedIn, portfolio website, and a HaUI demo-video URL were not provided, so they are intentionally omitted from the public README.

The supplied CV PDFs still label HaUI Admission AI as `Jun 2026 – Present`. The profile README uses **Completed** based on the owner's confirmation; update the CV PDFs before publishing if they must show the same final status.

## Content requiring confirmation

- Optional: provide a public LinkedIn URL, portfolio URL, or HaUI demo-video URL when available.

## Missing assets

- Approved 512 × 512 personal avatar/photo.
- Approved 1280 × 720 product screenshot for HaUI Admission AI, if desired.
- HaUI demo video URL, if one is intended for public release.

No fake PDF, random portrait, or fabricated product screenshot was created.

## Security and honesty checks

- No API key, access token, `.env` content, phone number, home address, student ID, or private invite was added.
- No unverifiable employer, certificate, benchmark, user count, accuracy, latency, or uptime claim was added.
- Public repository READMEs were used as the evidence boundary for technology and project claims.
- Forks and weak lab repositories were excluded from featured work.
- The metadata command file contains no token and keeps unknown values as explicit placeholders.
- The supplied public CVs include a phone number with the profile owner's explicit approval.
- GitHub account metadata was not changed because CLI authentication was invalid and placeholders remain.

## Preview instructions

1. Open `README.md` in VS Code and use Markdown Preview.
2. Open both SVG files directly in a browser or image viewer and inspect them at full width and around 360 px wide.
3. Push only after replacing or deliberately accepting every placeholder.
4. After publishing, test every link in an incognito window to confirm it is public.
5. Check the GitHub profile on both desktop and a real mobile device.

## Validation results

- All four SVG assets parsed as valid XML and rendered successfully.
- The desktop hero, mobile hero, and HaUI architecture artwork were visually checked at 1200 px and 360 px viewport widths.
- The mobile `<picture>` source switched correctly at the 600 px breakpoint.
- Every README `<img>` has non-empty alt text.
- All relative README references resolve to files in the repository.
- No unsupported `<script>` or `<style>` block appears in the README.
- GitHub profile, selected repository, HaUI demo, and Shields URLs returned HTTP 200 during final validation.
- Third-party statistics endpoints returned HTTP 503 and were removed before commit.
- Secret-pattern scan found no API key, GitHub token, private key, or unexpected `.env` file.
- UTF-8 validation found no replacement characters or mojibake in the deliverable.

## Deployment commands

The target GitHub profile repository must be named exactly `tandung060604-prog`.

After authenticating the correct GitHub account:

```powershell
gh auth login -h github.com
gh auth status
gh repo create tandung060604-prog --public --source . --remote origin
git push -u origin main
```

If the remote repository is created separately:

```powershell
git remote add origin https://github.com/tandung060604-prog/tandung060604-prog.git
git push -u origin main
```

Do not push until the account identity is confirmed.

## Git status

The deliverable is initialized as an independent local Git repository on `main` and committed after validation with:

```text
feat: redesign GitHub profile and personal branding
```

The working tree is clean at handoff. No remote, push, or GitHub account mutation is part of this handoff.
