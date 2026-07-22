"""Render clean, readable horizontal toolkit cards for the GitHub profile README."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "toolkit-cards"
FONT = "C:/Windows/Fonts/segoeuib.ttf"
W, H = 1080, 190

CARDS = (
    (
        "toolkit-ai-llm-hover.gif",
        "AI & LLM",
        "RETRIEVAL, EVALUATION, AND AGENTIC APPLICATIONS",
        ("Python", "RAG", "LLM Apps", "Prompt Engineering", "AI Agents", "Embeddings", "Vector DBs", "Ragas"),
        "#22d3ee",
    ),
    (
        "toolkit-backend-data-hover.gif",
        "Backend & Data",
        "API DESIGN, PERSISTENCE, AND RELIABLE DATA FLOWS",
        ("FastAPI", "REST APIs", "PostgreSQL", "Pydantic", "SQLAlchemy", "Python venv"),
        "#a78bfa",
    ),
    (
        "toolkit-frontend-hover.gif",
        "Frontend",
        "INTERFACES FOR PRACTICAL AI PRODUCTS",
        ("React", "Vite", "Next.js", "TypeScript", "JavaScript", "HTML", "CSS"),
        "#f59e0b",
    ),
    (
        "toolkit-tools-quality-hover.gif",
        "Tools, Quality & Deployment",
        "BUILD, TEST, AUTOMATE, AND SHIP",
        ("Git", "GitHub", "Docker", "Railway", "Postman", "VS Code", "Codex", "pytest", "Camunda 7", "BPMN"),
        "#38bdf8",
    ),
    (
        "toolkit-robotics-hover.gif",
        "Robotics",
        "COMPUTER VISION, EMBEDDED CONTROL, AND SIMULATION",
        ("OpenCV", "PyTorch", "YOLOv8", "DeepSORT", "ESP32 / CAM", "Arduino", "ROS / Gazebo", "MATLAB", "PID / LQR"),
        "#2dd4bf",
    ),
)


def font(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT, size)


def tag_width(draw: ImageDraw.ImageDraw, value: str, tag_font: ImageFont.FreeTypeFont) -> int:
    return int(draw.textbbox((0, 0), value, font=tag_font)[2]) + 34


def render_base(title: str, subtitle: str, tags: tuple[str, ...], accent: str) -> tuple[Image.Image, list[tuple[int, int, int, int, str]]]:
    image = Image.new("RGB", (W, H), "#07111f")
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((1, 1, W - 2, H - 2), radius=22, outline="#1e506c", width=2)
    draw.rounded_rectangle((28, 29, 37, 77), radius=4, fill=accent)
    draw.text((58, 25), title, font=font(29), fill="#f8fafc")
    draw.text((60, 66), subtitle, font=font(13), fill="#94a3b8")

    tag_font = font(16)
    x, y = 32, 111
    tag_boxes = []
    for tag in tags:
        width = tag_width(draw, tag, tag_font)
        if x + width > W - 32:
            x, y = 32, y + 42
        draw.rounded_rectangle((x, y, x + width, y + 30), radius=15, fill="#0d2235", outline="#1d4f69", width=1)
        draw.text((x + 17, y + 6), tag, font=tag_font, fill="#dbeafe")
        tag_boxes.append((x, y, x + width, y + 30, tag))
        x += width + 10

    return image, tag_boxes


def render(filename: str, title: str, subtitle: str, tags: tuple[str, ...], accent: str) -> None:
    base, tag_boxes = render_base(title, subtitle, tags, accent)
    tag_font = font(16)
    frames = [base.copy()]
    for left, top, right, bottom, tag in tag_boxes:
        frame = base.copy()
        draw = ImageDraw.Draw(frame)
        draw.rounded_rectangle((left - 1, top - 1, right + 1, bottom + 1), radius=16, fill="#dbeafe")
        draw.rounded_rectangle((left, top, right, bottom), radius=15, fill=accent)
        draw.text((left + 17, top + 6), tag, font=tag_font, fill="#07111f")
        frames.extend((frame, frame.copy()))

    frames[0].save(
        OUT / filename,
        save_all=True,
        append_images=frames[1:],
        duration=220,
        loop=0,
        optimize=True,
        disposal=2,
    )


OUT.mkdir(parents=True, exist_ok=True)
for card in CARDS:
    render(*card)
    print(f"Wrote {card[0]}")
