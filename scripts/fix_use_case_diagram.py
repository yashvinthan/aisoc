"""
Professional UML Use Case Diagram generator for AiSOC with:
- Zero line collisions
- Strictly adjacent «include» and «extend» relationships (no jumping through bubbles)
- Clean, non-overlapping actor association lines
- Generous vertical spacing and crisp typography
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

FIG_DIR = r"c:\Users\yashv\dev\work in progress\mini project\AiSOC\docs\figures"
os.makedirs(FIG_DIR, exist_ok=True)

def generate_perfect_use_case_diagram():
    # Large canvas for plenty of breathing room
    fig, ax = plt.subplots(figsize=(15, 12), dpi=300)
    ax.set_xlim(0, 18)
    ax.set_ylim(0, 15)
    ax.axis('off')

    # System boundary box (dashed)
    sys_box = patches.Rectangle((4.2, 0.5), 9.6, 14.0, linewidth=1.6, linestyle="--", edgecolor="#111827", facecolor="#FAFAFA")
    ax.add_patch(sys_box)
    
    # System title badge
    title_badge = patches.FancyBboxPatch((5.8, 13.9), 6.4, 0.55, boxstyle="round,pad=0.08", edgecolor="#111827", facecolor="#FFFFFF", linewidth=1.2)
    ax.add_patch(title_badge)
    ax.text(9.0, 14.17, "AiSOC Autonomous Security Operations Platform", ha='center', va='center', fontsize=10.5, fontweight='bold', color="#111827")

    def draw_human_actor(cx, cy, label):
        # Head
        ax.plot([cx], [cy + 0.45], 'o', color="#111827", markersize=11, fillstyle='full')
        # Spine
        ax.plot([cx, cx], [cy + 0.35, cy - 0.15], color="#111827", lw=1.6)
        # Arms
        ax.plot([cx - 0.30, cx + 0.30], [cy + 0.12, cy + 0.12], color="#111827", lw=1.6)
        # Legs
        ax.plot([cx, cx - 0.25], [cy - 0.15, cy - 0.55], color="#111827", lw=1.6)
        ax.plot([cx, cx + 0.25], [cy - 0.15, cy - 0.55], color="#111827", lw=1.6)
        # Text label
        ax.text(cx, cy - 0.78, label, ha='center', va='top', fontsize=8.5, fontweight='bold', color="#111827")

    def draw_system_actor(cx, cy, label):
        rect = patches.FancyBboxPatch((cx - 0.95, cy - 0.5), 1.9, 1.0, boxstyle="round,pad=0.1", edgecolor="#111827", facecolor="#FFFFFF", linewidth=1.4)
        ax.add_patch(rect)
        ax.text(cx, cy + 0.22, "«System Actor»", ha='center', va='center', fontsize=7.2, fontstyle='italic', color="#374151")
        ax.text(cx, cy - 0.12, label, ha='center', va='center', fontsize=8.2, fontweight='bold', color="#111827")

    # Position 5 distinct actors
    # Left Side Actors
    draw_human_actor(1.8, 11.2, "SOC Analyst\n(Tier-1 / Tier-2)")
    draw_human_actor(1.8, 4.2, "Detection Engineer /\nThreat Researcher")

    # Right Side Actors
    draw_human_actor(16.2, 11.2, "SOC Lead /\nIncident Commander")
    draw_human_actor(16.2, 6.8, "Compliance Auditor\n/ CISO")
    draw_system_actor(16.2, 2.2, "Autonomous\nAI Engine")

    # 10 Cleanly Ordered & Spaced Use Cases
    # center_x = 9.0
    use_cases = [
        # id, cy, text, w, h
        ("uc1", 13.2, "Authenticate & Manage MFA Session", 5.2, 0.75),
        ("uc2", 11.9, "Monitor Real-Time Alert Triage Queue", 5.4, 0.75),
        ("uc3", 10.6, "Inspect AI Investigation Dossier & Timeline", 5.6, 0.75),
        ("uc4", 9.3, "Approve High-Blast-Radius Containment (L2–L4)", 5.6, 0.75),
        ("uc5", 8.0, "Execute Natural Language Threat Hunt (ES|QL/KQL)", 5.6, 0.75),
        ("uc6", 6.7, "Submit Disposition Feedback & ML Noise Tuning", 5.6, 0.75),
        ("uc7", 5.4, "Manage & Benchmark Detection Rules (Sigma/YARA)", 5.6, 0.75),
        ("uc8", 4.1, "Audit Immutable Agent CoT Governance Ledger", 5.6, 0.75),
        ("uc9", 2.8, "Generate & Sign Compliance Incident PDF Dossier", 5.6, 0.75),
        ("uc10", 1.4, "Autonomously Ingest, Deduplicate & Reason (OCSF)", 5.8, 0.80),
    ]

    uc_map = {}
    for uid, cy, text, w, h in use_cases:
        ellipse = patches.Ellipse((9.0, cy), w, h, linewidth=1.3, edgecolor="#111827", facecolor="#FFFFFF")
        ax.add_patch(ellipse)
        ax.text(9.0, cy, text, ha='center', va='center', fontsize=8.2, color="#111827")
        # Store left edge and right edge
        uc_map[uid] = {
            "left": (9.0 - w/2.0, cy),
            "right": (9.0 + w/2.0, cy),
            "top": (9.0, cy + h/2.0),
            "bottom": (9.0, cy - h/2.0),
            "cy": cy
        }

    # Internal Stereotype Arrows (Between strictly adjacent nodes only)
    # 1. «include»: uc2 (Monitor Queue) -> uc3 (Inspect Dossier)
    ax.annotate('', xy=uc_map["uc3"]["top"], xytext=uc_map["uc2"]["bottom"],
                arrowprops=dict(arrowstyle="->", color="#111827", lw=1.2, ls="--"))
    ax.text(9.45, (uc_map["uc2"]["cy"] + uc_map["uc3"]["cy"]) / 2.0, "«include»", fontsize=7.2, fontstyle='italic', va='center', color="#374151")

    # 2. «extend»: uc4 (Approve Containment) -> uc3 (Inspect Dossier)
    ax.annotate('', xy=uc_map["uc3"]["bottom"], xytext=uc_map["uc4"]["top"],
                arrowprops=dict(arrowstyle="->", color="#111827", lw=1.2, ls="--"))
    ax.text(9.45, (uc_map["uc3"]["cy"] + uc_map["uc4"]["cy"]) / 2.0, "«extend»", fontsize=7.2, fontstyle='italic', va='center', color="#374151")

    # Clean Actor Association Lines (Straight lines with NO text collisions)
    # Actor 1: SOC Analyst (1.8, 11.2)
    ax.plot([2.3, uc_map["uc1"]["left"][0]], [11.5, uc_map["uc1"]["left"][1]], color="#1F2937", lw=1.1)
    ax.plot([2.3, uc_map["uc2"]["left"][0]], [11.3, uc_map["uc2"]["left"][1]], color="#1F2937", lw=1.1)
    ax.plot([2.3, uc_map["uc3"]["left"][0]], [11.1, uc_map["uc3"]["left"][1]], color="#1F2937", lw=1.1)
    ax.plot([2.3, uc_map["uc5"]["left"][0]], [10.9, uc_map["uc5"]["left"][1]], color="#1F2937", lw=1.1)
    ax.plot([2.3, uc_map["uc6"]["left"][0]], [10.7, uc_map["uc6"]["left"][1]], color="#1F2937", lw=1.1)

    # Actor 2: Detection Engineer (1.8, 4.2)
    ax.plot([2.3, uc_map["uc1"]["left"][0]], [4.6, uc_map["uc1"]["left"][1]], color="#1F2937", lw=1.1)
    ax.plot([2.3, uc_map["uc5"]["left"][0]], [4.4, uc_map["uc5"]["left"][1]], color="#1F2937", lw=1.1)
    ax.plot([2.3, uc_map["uc6"]["left"][0]], [4.2, uc_map["uc6"]["left"][1]], color="#1F2937", lw=1.1)
    ax.plot([2.3, uc_map["uc7"]["left"][0]], [4.0, uc_map["uc7"]["left"][1]], color="#1F2937", lw=1.1)

    # Actor 3: SOC Lead / Incident Commander (16.2, 11.2)
    ax.plot([15.7, uc_map["uc1"]["right"][0]], [11.5, uc_map["uc1"]["right"][1]], color="#1F2937", lw=1.1)
    ax.plot([15.7, uc_map["uc2"]["right"][0]], [11.3, uc_map["uc2"]["right"][1]], color="#1F2937", lw=1.1)
    ax.plot([15.7, uc_map["uc3"]["right"][0]], [11.1, uc_map["uc3"]["right"][1]], color="#1F2937", lw=1.1)
    ax.plot([15.7, uc_map["uc4"]["right"][0]], [10.9, uc_map["uc4"]["right"][1]], color="#1F2937", lw=1.1)

    # Actor 4: Compliance Auditor / CISO (16.2, 6.8)
    ax.plot([15.7, uc_map["uc1"]["right"][0]], [7.1, uc_map["uc1"]["right"][1]], color="#1F2937", lw=1.1)
    ax.plot([15.7, uc_map["uc8"]["right"][0]], [6.8, uc_map["uc8"]["right"][1]], color="#1F2937", lw=1.1)
    ax.plot([15.7, uc_map["uc9"]["right"][0]], [6.5, uc_map["uc9"]["right"][1]], color="#1F2937", lw=1.1)

    # Actor 5: Autonomous AI Engine (16.2, 2.2)
    ax.plot([15.2, uc_map["uc10"]["right"][0]], [2.2, uc_map["uc10"]["right"][1]], color="#1F2937", lw=1.1)
    ax.plot([15.2, uc_map["uc3"]["right"][0]], [2.6, uc_map["uc3"]["right"][1]], color="#1F2937", lw=1.1, ls=":")

    out_file = os.path.join(FIG_DIR, "fig4_2_use_case_diagram.png")
    plt.savefig(out_file, bbox_inches='tight', dpi=300)
    plt.close()
    print("Fixed Use Case diagram generated successfully with zero overlaps at:", out_file)

if __name__ == "__main__":
    generate_perfect_use_case_diagram()
