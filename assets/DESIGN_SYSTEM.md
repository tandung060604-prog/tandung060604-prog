# GitHub Profile Design System

## Direction

The profile uses an **AI × Robotics × Futuristic Engineering** direction: dark, precise, and technical without looking like a generic neon template. Projects and evidence take priority over decoration.

## Color palette

| Token | Hex | Use |
| --- | --- | --- |
| Deep space | `#050B18` | Banner background |
| Deep navy | `#07111F` | Cards and interface surfaces |
| Surface blue | `#0A2137` | Diagram surfaces |
| Electric blue | `#38BDF8` | Primary accents and links |
| Cyan | `#22D3EE` | Data-flow nodes and active states |
| Soft purple | `#A78BFA` | Secondary accents |
| Main text | `#F4F8FC` | High-emphasis text in SVG assets |
| Muted text | `#9FB3C8` | Supporting text in SVG assets |

All text/background pairs used in the SVG assets are designed for strong contrast on GitHub's light and dark page themes because the text is rendered inside the dark artwork.

## Typography

- SVG assets use only the system stack: `Segoe UI, Arial, sans-serif`.
- README content relies on GitHub's native typography.
- Headings use sentence case and a shallow hierarchy: `##` for sections, `###` for categories/projects.
- Body paragraphs stay short; technical detail is expressed with lists and compact stack lines.

## Components

- **Hero:** 1200 × 360 desktop SVG plus a 720 × 480 mobile SVG selected through `<picture>`; both use the same identity and robotics/network language.
- **Project visual:** 1280 × 720 SVG architecture diagram, explicitly a system overview rather than a fabricated UI screenshot.
- **Badges:** flat-square for the compact hero row; for-the-badge only for the two CV actions. Badge backgrounds stay deep navy with cyan/purple accents.
- **Project entries:** native Markdown headings, a one-sentence outcome, and one concise stack line. No dense HTML card grid.
- **GitHub activity:** native profile/repository links instead of external statistics cards; this keeps the README reliable when third-party renderers are unavailable.

## Responsive rules

- Images use relative repository paths and `width="100%"` where the artwork should scale with the content column.
- The hero switches to the taller mobile asset at widths up to 600 px so the identity and tagline remain readable instead of shrinking the wide desktop artwork.
- Technology groups are separate lines instead of one long badge wall.
- Tables are avoided in the main README because they can force horizontal scrolling on mobile.
- No fixed-height HTML containers, custom CSS, JavaScript, animation, or external fonts are used.

## Asset rules

- Keep the banner under 100 KB and project diagrams under 150 KB when possible.
- Prefer SVG for diagrams and decorative graphics; use optimized PNG/WebP only for approved photos or real screenshots.
- Every image referenced by the README must include meaningful alt text.
- Never place secrets, student IDs, document numbers, private addresses, or unapproved personal photos in an asset.
