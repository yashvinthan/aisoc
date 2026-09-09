"""
Script to generate an expanded, professional, multi-actor UML Use Case Diagram for AiSOC.
Features 5 distinct actors:
- SOC Analyst / Responder
- Detection Engineer / Threat Hunter
- SOC Lead / Incident Commander
- Compliance Auditor / CISO
- Autonomous AI Agent Engine (System Actor)
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

FIG_DIR = r"c:\Users\yashv\dev\work in progress\mini project\AiSOC\docs\figures"
os.makedirs(FIG_DIR, exist_ok=True)

def generate_multi_actor_use_case_diagram():
    fig, ax = plt.subplots(figsize=(14, 11), dpi=300)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 14)
    ax.axis('off')

    # System boundary box (dashed)
    sys_box = patches.Rectangle((3.8, 0.6), 8.4, 12.8, linewidth=1.5, linestyle="--", edgecolor="black", facecolor="white")
    ax.add_patch(sys_box)
    ax.text(8.0, 13.0, "AiSOC Autonomous Security Operations Platform", ha='center', va='center', fontsize=11, fontweight='bold')

    def draw_actor(cx, cy, label, is_system=False):
        if is_system:
            # System / Robot actor (Box with icon/tag)
            rect = patches.FancyBboxPatch((cx - 0.75, cy - 0.45), 1.5, 0.9, boxstyle="round,pad=0.08", edgecolor="black", facecolor="white", linewidth=1.4)
            ax.add_patch(rect)
            ax.text(cx, cy, "«System Actor»\nAutonomous\nAI Engine", ha='center', va='center', fontsize=7.5, fontweight='bold')
            return
            
        # Human stick figure
        ax.plot([cx], [cy + 0.45], 'o', color="black", markersize=11)
        ax.plot([cx, cx], [cy + 0.35, cy - 0.15], color="black", lw=1.5)
        ax.plot([cx - 0.28, cx + 0.28], [cy + 0.15, cy + 0.15], color="black", lw=1.5)
        ax.plot([cx, cx - 0.22], [cy - 0.15, cy - 0.55], color="black", lw=1.5)
        ax.plot([cx, cx + 0.22], [cy - 0.15, cy - 0.55], color="black", lw=1.5)
        ax.text(cx, cy - 0.75, label, ha='center', va='top', fontsize=8.2, fontweight='bold')

    # Left Actors
    draw_actor(1.8, 10.2, "SOC Analyst\n(Tier-1 / Tier-2)")
    draw_actor(1.8, 3.8, "Detection Engineer /\nThreat Researcher")

    # Right Actors
    draw_actor(14.2, 10.5, "SOC Lead /\nIncident Commander")
    draw_actor(14.2, 6.6, "Compliance Auditor\n/ CISO")
    draw_actor(14.2, 2.6, "", is_system=True)

    # Use Cases (Ellipses)
    # cx = 8.0
    use_cases = [
        # (id, cy, text, w, h)
        ("uc1", 12.1, "Authenticate & Manage MFA Session", 4.6, 0.70),
        ("uc2", 11.0, "Monitor Real-Time Alert Triage Queue", 4.6, 0.70),
        ("uc3", 9.9, "Inspect AI Investigation Dossier & Timeline", 4.8, 0.70),
        ("uc4", 8.8, "Execute Natural Language Threat Hunt (ES|QL/KQL)", 5.2, 0.70),
        ("uc5", 7.7, "Approve High-Blast-Radius Containment (L2-L4)", 5.0, 0.70),
        ("uc6", 6.6, "Audit Immutable Agent CoT Governance Ledger", 5.0, 0.70),
        ("uc7", 5.5, "Generate & Sign Compliance Incident PDF Dossier", 5.0, 0.70),
        ("uc8", 4.4, "Manage & Benchmark Detection Rules (Sigma/YARA)", 5.2, 0.70),
        ("uc9", 3.3, "Submit Disposition Feedback & ML Noise Tuning", 5.0, 0.70),
        ("uc10", 2.2, "Autonomously Ingest, Score & Normalize (OCSF)", 5.0, 0.70),
        ("uc11", 1.1, "Execute Multi-Agent DAG & Blast-Radius Traversal", 5.2, 0.70)
    ]

    uc_dict = {}
    for uid, cy, text, w, h in use_cases:
        ellipse = patches.Ellipse((8.0, cy), w, h, linewidth=1.3, edgecolor="black", facecolor="white")
        ax.add_patch(ellipse)
        ax.text(8.0, cy, text, ha='center', va='center', fontsize=8.0)
        uc_dict[uid] = (8.0 - w/2.0, 8.0 + w/2.0, cy)

    # Connecting Lines: Actor -> Use Case
    # Actor 1: SOC Analyst (1.8, 10.2)
    ax.plot([2.2, uc_dict["uc1"][0]], [10.4, uc_dict["uc1"][2]], color="black", lw=1.1)
    ax.plot([2.2, uc_dict["uc2"][0]], [10.3, uc_dict["uc2"][2]], color="black", lw=1.1)
    ax.plot([2.2, uc_dict["uc3"][0]], [10.2, uc_dict["uc3"][2]], color="black", lw=1.1)
    ax.plot([2.2, uc_dict["uc4"][0]], [10.0, uc_dict["uc4"][2]], color="black", lw=1.1)
    ax.plot([2.2, uc_dict["uc9"][0]], [9.8, uc_dict["uc9"][2]], color="black", lw=1.1)

    # Actor 2: Detection Engineer (1.8, 3.8)
    ax.plot([2.2, uc_dict["uc1"][0]], [4.2, uc_dict["uc1"][2]], color="black", lw=1.1)
    ax.plot([2.2, uc_dict["uc4"][0]], [4.0, uc_dict["uc4"][2]], color="black", lw=1.1)
    ax.plot([2.2, uc_dict["uc8"][0]], [3.8, uc_dict["uc8"][2]], color="black", lw=1.1)
    ax.plot([2.2, uc_dict["uc9"][0]], [3.6, uc_dict["uc9"][2]], color="black", lw=1.1)

    # Actor 3: SOC Lead (14.2, 10.5)
    ax.plot([13.8, uc_dict["uc1"][1]], [10.7, uc_dict["uc1"][2]], color="black", lw=1.1)
    ax.plot([13.8, uc_dict["uc2"][1]], [10.6, uc_dict["uc2"][2]], color="black", lw=1.1)
    ax.plot([13.8, uc_dict["uc3"][1]], [10.5, uc_dict["uc3"][2]], color="black", lw=1.1)
    ax.plot([13.8, uc_dict["uc5"][1]], [10.3, uc_dict["uc5"][2]], color="black", lw=1.1)
    ax.plot([13.8, uc_dict["uc7"][1]], [10.1, uc_dict["uc7"][2]], color="black", lw=1.1)

    # Actor 4: Compliance Auditor / CISO (14.2, 6.6)
    ax.plot([13.8, uc_dict["uc1"][1]], [6.8, uc_dict["uc1"][2]], color="black", lw=1.1)
    ax.plot([13.8, uc_dict["uc6"][1]], [6.6, uc_dict["uc6"][2]], color="black", lw=1.1)
    ax.plot([13.8, uc_dict["uc7"][1]], [6.4, uc_dict["uc7"][2]], color="black", lw=1.1)

    # Actor 5: Autonomous AI Engine (14.2, 2.6)
    ax.plot([13.4, uc_dict["uc10"][1]], [2.8, uc_dict["uc10"][2]], color="black", lw=1.1)
    ax.plot([13.4, uc_dict["uc11"][1]], [2.4, uc_dict["uc11"][2]], color="black", lw=1.1)
    ax.plot([13.4, uc_dict["uc3"][1]], [2.9, uc_dict["uc3"][2]], color="black", lw=1.1, ls=":")

    # Relationship stereotypes: «include» between Monitor Queue & Inspect Dossier
    ax.annotate('', xy=(8.0, 10.25), xytext=(8.0, 10.65), arrowprops=dict(arrowstyle="->", color="black", lw=1.1, ls="--"))
    ax.text(8.45, 10.45, "«include»", fontsize=7.2, fontstyle='italic', va='center')

    # «extend» between Inspect Dossier & Approve Containment
    ax.annotate('', xy=(8.0, 8.05), xytext=(8.0, 9.55), arrowprops=dict(arrowstyle="->", color="black", lw=1.1, ls="--"))
    ax.text(8.45, 8.8, "«extend»", fontsize=7.2, fontstyle='italic', va='center')

    out_file = os.path.join(FIG_DIR, "fig4_2_use_case_diagram.png")
    plt.savefig(out_file, bbox_inches='tight', dpi=300)
    plt.close()
    print("Generated multi-actor use case diagram successfully at:", out_file)

if __name__ == "__main__":
    generate_multi_actor_use_case_diagram()
