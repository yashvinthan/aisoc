"""
Academic style diagrams generator with clean layout, ample padding, no title inside image, and zero text/arrow overlapping.
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

FIG_DIR = r"c:\Users\yashv\dev\work in progress\mini project\AiSOC\docs\figures"
os.makedirs(FIG_DIR, exist_ok=True)

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 9.0
plt.rcParams['figure.dpi'] = 300

def draw_pill(ax, center, width, height, text, fontsize=9.5, bold=True):
    x = center[0] - width / 2.0
    y = center[1] - height / 2.0
    rect = patches.FancyBboxPatch((x, y), width, height, boxstyle="round,pad=0.04,rounding_size=0.25", linewidth=1.5, edgecolor="black", facecolor="white")
    ax.add_patch(rect)
    ax.text(center[0], center[1], text, ha='center', va='center', fontsize=fontsize, fontweight='bold' if bold else 'normal', color='black')

def draw_box(ax, center, width, height, text, fontsize=8.5, bold=False):
    x = center[0] - width / 2.0
    y = center[1] - height / 2.0
    rect = patches.Rectangle((x, y), width, height, linewidth=1.5, edgecolor="black", facecolor="white")
    ax.add_patch(rect)
    ax.text(center[0], center[1], text, ha='center', va='center', fontsize=fontsize, fontweight='bold' if bold else 'normal', color='black', multialignment='center')

def draw_diamond(ax, center, width, height, text, fontsize=8.0, bold=False):
    cx, cy = center
    hw = width / 2.0
    hh = height / 2.0
    pts = [[cx, cy + hh], [cx + hw, cy], [cx, cy - hh], [cx - hw, cy]]
    poly = patches.Polygon(pts, closed=True, linewidth=1.5, edgecolor="black", facecolor="white")
    ax.add_patch(poly)
    ax.text(cx, cy, text, ha='center', va='center', fontsize=fontsize, fontweight='bold' if bold else 'normal', color='black', multialignment='center')

def draw_arrow(ax, start, end, label="", label_pos=0.5, offset=(0, 0.08)):
    ax.annotate('', xy=end, xytext=start, arrowprops=dict(arrowstyle="->", color="black", lw=1.3))
    if label:
        lx = start[0] + (end[0] - start[0]) * label_pos + offset[0]
        ly = start[1] + (end[1] - start[1]) * label_pos + offset[1]
        ax.text(lx, ly, label, ha='center', va='center', fontsize=7.5, fontweight='bold', color='black', bbox=dict(boxstyle="square,pad=0.15", fc="white", ec="none"))

# 4.4 Methodology — Complete System Workflow
def gen_methodology_flowchart():
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 12)
    ax.axis('off')

    # Column 1: Ingest & Scoring (x = 3.2)
    draw_pill(ax, (3.2, 11.2), 2.4, 0.65, "Start")
    draw_box(ax, (3.2, 9.7), 4.2, 0.85, "Raw Telemetry Ingestion\n(83 Connectors / Webhooks)")
    draw_box(ax, (3.2, 8.1), 4.2, 0.85, "OCSF Normalization &\nATT&CK Tagging (Go)")
    draw_box(ax, (3.2, 6.5), 4.2, 0.85, "Kafka Event Bus &\nPartitioned Streams")
    draw_box(ax, (3.2, 4.9), 4.2, 0.85, "Simhash LSH Dedup &\nMLScorer (Isolation Forest)")
    draw_diamond(ax, (3.2, 3.0), 3.6, 1.4, "Anomalous\n/ Risk >= 30?")
    draw_box(ax, (3.2, 1.0), 4.2, 0.85, "Auto-Suppress Alert\n& Update Baseline")

    # Connectors Col 1
    draw_arrow(ax, (3.2, 10.85), (3.2, 10.15))
    draw_arrow(ax, (3.2, 9.25), (3.2, 8.55))
    draw_arrow(ax, (3.2, 7.65), (3.2, 6.95))
    draw_arrow(ax, (3.2, 6.05), (3.2, 5.35))
    draw_arrow(ax, (3.2, 4.45), (3.2, 3.75))
    draw_arrow(ax, (3.2, 2.3), (3.2, 1.45), "No", offset=(0.25, 0))

    # Column 2: Multi-Agent DAG (x = 8.5)
    draw_diamond(ax, (8.5, 10.5), 3.4, 1.3, "Choose Agent\nTriage Action")
    draw_box(ax, (8.5, 8.9), 4.0, 0.8, "DetectAgent:\nSignature & Rule Check")
    draw_box(ax, (8.5, 7.3), 4.0, 0.8, "TriageAgent:\nGeo-Velocity & Risk Score")
    draw_box(ax, (8.5, 5.7), 4.0, 0.8, "HuntAgent:\nWarm-Lake Query (ES|QL)")
    draw_box(ax, (8.5, 4.1), 4.0, 0.8, "RespondAgent:\nPlan Containment Actions")

    # Connectors Col 1 -> Col 2
    # Anomalous Yes -> Agent DAG
    ax.plot([5.0, 8.5], [3.0, 3.0], color="black", lw=1.3)
    ax.plot([8.5, 8.5], [3.0, 3.7], color="black", lw=1.3)
    draw_arrow(ax, (8.5, 3.0), (8.5, 3.7), "Yes (True Threat)", offset=(-0.8, 0.2))
    
    # Diamond to DetectAgent loop
    draw_arrow(ax, (8.5, 9.85), (8.5, 9.3))
    draw_arrow(ax, (8.5, 8.5), (8.5, 7.7))
    draw_arrow(ax, (8.5, 6.9), (8.5, 6.1))
    draw_arrow(ax, (8.5, 5.3), (8.5, 4.5))

    # Column 3: Blast Radius & Containment (x = 13.5)
    draw_diamond(ax, (13.5, 8.5), 3.6, 1.4, "Blast Radius\n<= Limit (L3/L4)?")
    draw_box(ax, (13.5, 6.3), 3.8, 0.8, "Autonomous Execution\n(Isolate Host / Revoke)")
    draw_box(ax, (13.5, 4.5), 3.8, 0.8, "Dispatch Approval Modal\n(Slack / Web Console)")
    draw_box(ax, (13.5, 2.6), 4.2, 0.9, "Update Neo4j & Postgres\nGenerate PDF Dossier")

    # Connect RespondAgent to Blast Radius
    ax.plot([10.5, 13.5], [4.1, 4.1], color="black", lw=1.3)
    draw_arrow(ax, (13.5, 4.1), (13.5, 7.8))

    # Decision branches Col 3
    draw_arrow(ax, (11.7, 8.5), (11.7, 6.7), "Yes", offset=(-0.25, 0))
    ax.plot([11.7, 11.7], [8.5, 6.7], color="black", lw=1.3)
    draw_arrow(ax, (11.7, 6.7), (11.6, 6.3)) # into auto exec

    draw_arrow(ax, (13.5, 7.8), (13.5, 4.9), "No", offset=(0.25, 1.0))
    draw_arrow(ax, (13.5, 4.1), (13.5, 3.05))

    # Bottom End Pill (x = 8.5, y = 1.0)
    draw_pill(ax, (8.5, 1.0), 2.4, 0.65, "End")
    draw_arrow(ax, (5.3, 1.0), (7.3, 1.0))
    
    ax.plot([13.5, 13.5], [2.15, 1.0], color="black", lw=1.3)
    draw_arrow(ax, (13.5, 1.0), (9.7, 1.0))

    p = os.path.join(FIG_DIR, "fig4_0_complete_methodology.png")
    plt.savefig(p, bbox_inches='tight')
    plt.close()
    print("Cleaned methodology flowchart:", p)

# 4.6.1 Use Case Diagram
def gen_use_case_diagram():
    fig, ax = plt.subplots(figsize=(11, 7.5))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 9.5)
    ax.axis('off')

    # System boundary box (dashed)
    sys_box = patches.Rectangle((3.2, 0.6), 6.6, 8.3, linewidth=1.5, linestyle="--", edgecolor="black", facecolor="white")
    ax.add_patch(sys_box)
    ax.text(6.5, 8.6, "AiSOC Autonomous Platform", ha='center', va='center', fontsize=10, fontweight='bold')

    def draw_actor(cx, cy, label):
        ax.plot([cx], [cy + 0.45], 'o', color="black", markersize=12)
        ax.plot([cx, cx], [cy + 0.35, cy - 0.15], color="black", lw=1.6)
        ax.plot([cx - 0.3, cx + 0.3], [cy + 0.15, cy + 0.15], color="black", lw=1.6)
        ax.plot([cx, cx - 0.25], [cy - 0.15, cy - 0.55], color="black", lw=1.6)
        ax.plot([cx, cx + 0.25], [cy - 0.15, cy - 0.55], color="black", lw=1.6)
        ax.text(cx, cy - 0.8, label, ha='center', va='top', fontsize=8.5, fontweight='bold')

    draw_actor(1.4, 5.0, "SOC Analyst /\nResponder")
    draw_actor(11.6, 5.0, "SOC Lead /\nAdministrator")

    use_cases = [
        (6.5, 7.6, "Authenticate / MFA Login", 4.2, 0.75),
        (6.5, 6.3, "Monitor Real-Time Alert Queue", 4.4, 0.75),
        (6.5, 5.0, "Inspect AI Investigation Dossier", 4.4, 0.75),
        (6.5, 3.7, "Execute Natural Language Hunt", 4.4, 0.75),
        (6.5, 2.4, "Approve Gated Containment Action", 4.6, 0.75),
        (6.5, 1.2, "Generate Compliance PDF Report", 4.4, 0.75)
    ]

    for cx, cy, text, w, h in use_cases:
        ellipse = patches.Ellipse((cx, cy), w, h, linewidth=1.3, edgecolor="black", facecolor="white")
        ax.add_patch(ellipse)
        ax.text(cx, cy, text, ha='center', va='center', fontsize=8.0)

    # Actor lines
    ax.plot([1.8, 4.3], [5.0, 7.6], color="black", lw=1.2)
    ax.plot([1.8, 4.3], [5.0, 6.3], color="black", lw=1.2)
    ax.plot([1.8, 4.3], [5.0, 5.0], color="black", lw=1.2)
    ax.plot([1.8, 4.3], [5.0, 3.7], color="black", lw=1.2)

    ax.plot([11.2, 8.8], [5.0, 7.6], color="black", lw=1.2)
    ax.plot([11.2, 8.8], [5.0, 2.4], color="black", lw=1.2)
    ax.plot([11.2, 8.8], [5.0, 1.2], color="black", lw=1.2)

    # Include relationship
    ax.annotate('', xy=(6.5, 5.38), xytext=(6.5, 6.0), arrowprops=dict(arrowstyle="->", color="black", lw=1.2, ls="--"))
    ax.text(6.85, 5.65, "«include»", fontsize=7, fontstyle='italic')

    p = os.path.join(FIG_DIR, "fig4_2_use_case_diagram.png")
    plt.savefig(p, bbox_inches='tight')
    plt.close()
    print("Cleaned academic use case diagram:", p)

# 4.6.2 Activity Diagram
def gen_activity_diagram():
    fig, ax = plt.subplots(figsize=(9, 9.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 11)
    ax.axis('off')

    # Start circle
    ax.plot(5.0, 10.3, 'o', color="black", markersize=14)

    draw_pill(ax, (5.0, 9.2), 3.6, 0.7, "Ingest Telemetry (Connectors)")
    draw_diamond(ax, (5.0, 7.8), 2.8, 1.1, "Is Duplicate\nSimhash?")
    draw_pill(ax, (5.0, 6.3), 3.6, 0.7, "Score Risk (MLScorer)")
    draw_diamond(ax, (5.0, 4.9), 2.8, 1.1, "Risk >= 30?")
    draw_pill(ax, (5.0, 3.4), 3.8, 0.7, "Multi-Agent AI Investigation")
    draw_pill(ax, (5.0, 2.0), 3.8, 0.7, "Execute Safe Containment")

    # Bullseye end node
    ax.plot(5.0, 0.8, 'o', color="black", markersize=16)
    ax.plot(5.0, 0.8, 'o', color="white", markersize=12)
    ax.plot(5.0, 0.8, 'o', color="black", markersize=8)

    # Arrows
    draw_arrow(ax, (5.0, 10.1), (5.0, 9.55))
    draw_arrow(ax, (5.0, 8.85), (5.0, 8.35))
    draw_arrow(ax, (5.0, 7.25), (5.0, 6.65), "No", offset=(0.25, 0))
    draw_arrow(ax, (5.0, 5.95), (5.0, 5.45))
    draw_arrow(ax, (5.0, 4.35), (5.0, 3.75), "Yes", offset=(0.25, 0))
    draw_arrow(ax, (5.0, 3.05), (5.0, 2.35))
    draw_arrow(ax, (5.0, 1.65), (5.0, 0.95))

    # Duplicate loopback
    ax.plot([6.4, 8.4, 8.4, 6.8], [7.8, 7.8, 9.2, 9.2], color="black", lw=1.2)
    draw_arrow(ax, (8.4, 9.2), (6.8, 9.2), "Yes (Drop)", offset=(0.45, 0.2))

    # Low risk bypass
    ax.plot([3.6, 1.8, 1.8, 5.0], [4.9, 4.9, 0.8, 0.8], color="black", lw=1.2)
    draw_arrow(ax, (1.8, 0.8), (4.7, 0.8), "No (Suppress)", offset=(0.5, 0.2))

    p = os.path.join(FIG_DIR, "fig4_5_activity_diagram.png")
    plt.savefig(p, bbox_inches='tight')
    plt.close()
    print("Cleaned academic activity diagram:", p)

# 4.6.3 Sequence Diagram
def gen_sequence_diagram():
    fig, ax = plt.subplots(figsize=(11, 7.5))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 8.5)
    ax.axis('off')

    lifelines = [
        (1.2, "User / Analyst"),
        (3.4, "Web Console"),
        (5.8, "Core API"),
        (8.2, "LangGraph Agents"),
        (10.4, "Neo4j / DB"),
        (12.0, "SOAR API")
    ]

    for x, name in lifelines:
        draw_box(ax, (x, 7.8), 1.8, 0.6, name, fontsize=8.0, bold=True)
        ax.plot([x, x], [7.5, 0.8], color="black", linestyle="--", lw=1.2)

    messages = [
        (1.2, 3.4, 6.8, "1. Open console", False),
        (3.4, 5.8, 6.2, "2. GET /alerts/{id}", False),
        (5.8, 8.2, 5.6, "3. Trigger LangGraph triage", False),
        (8.2, 10.4, 5.0, "4. Query blast radius & path", False),
        (10.4, 8.2, 4.4, "5. Return graph context", True),
        (8.2, 5.8, 3.8, "6. Propose containment plan", False),
        (5.8, 3.4, 3.2, "7. Push live dossier over WS", False),
        (1.2, 3.4, 2.6, "8. Click 'Approve Action'", False),
        (3.4, 5.8, 2.0, "9. POST /actions/execute", False),
        (5.8, 12.0, 1.4, "10. Dispatch host isolation", False),
        (12.0, 5.8, 0.9, "11. Isolation confirmed", True)
    ]

    for x1, x2, y, text, is_return in messages:
        ls = "--" if is_return else "-"
        draw_arrow(ax, (x1, y), (x2, y), text, label_pos=0.5, offset=(0, 0.12))

    p = os.path.join(FIG_DIR, "fig4_4_sequence_diagram.png")
    plt.savefig(p, bbox_inches='tight')
    plt.close()
    print("Cleaned academic sequence diagram:", p)

# 4.8.1 ER Model
def gen_er_model():
    fig, ax = plt.subplots(figsize=(11, 7.5))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 8.5)
    ax.axis('off')

    draw_box(ax, (2.2, 4.5), 2.4, 1.1, "USER / TENANT", fontsize=9.0, bold=True)
    draw_diamond(ax, (5.8, 4.5), 2.0, 1.1, "MANAGES\n(1:M)", fontsize=7.5)
    draw_box(ax, (9.4, 4.5), 2.4, 1.1, "INCIDENT_CASE", fontsize=9.0, bold=True)
    draw_diamond(ax, (9.4, 2.2), 2.0, 1.1, "TRIGGERS\n(1:N)", fontsize=7.5)
    draw_box(ax, (9.4, 0.7), 2.4, 0.85, "ACTION_EXEC", fontsize=8.5, bold=True)

    ax.plot([3.4, 4.8], [4.5, 4.5], color="black", lw=1.3)
    ax.plot([6.8, 8.2], [4.5, 4.5], color="black", lw=1.3)
    ax.plot([9.4, 9.4], [3.95, 2.75], color="black", lw=1.3)
    ax.plot([9.4, 9.4], [1.65, 1.12], color="black", lw=1.3)

    user_attrs = [
        (1.0, 6.8, "user_id (PK)", True),
        (2.8, 6.8, "username", False),
        (1.0, 2.5, "tenant_id", False),
        (2.8, 2.5, "role", False)
    ]
    for cx, cy, text, is_pk in user_attrs:
        el = patches.Ellipse((cx, cy), 1.6, 0.65, linewidth=1.1, edgecolor="black", facecolor="white")
        ax.add_patch(el)
        ax.text(cx, cy, text, ha='center', va='center', fontsize=7.0)
        ax.plot([cx, 2.2], [cy + (0.32 if cy < 4.5 else -0.32), 4.5 + (-0.55 if cy < 4.5 else 0.55)], color="black", lw=1.0)

    case_attrs = [
        (8.2, 6.8, "case_id (PK)", True),
        (10.6, 6.8, "severity", False),
        (12.0, 4.5, "status", False),
        (12.0, 5.8, "created_at", False)
    ]
    for cx, cy, text, is_pk in case_attrs:
        el = patches.Ellipse((cx, cy), 1.6, 0.65, linewidth=1.1, edgecolor="black", facecolor="white")
        ax.add_patch(el)
        ax.text(cx, cy, text, ha='center', va='center', fontsize=7.0)
        ax.plot([cx + (-0.8 if cx > 9.4 else 0), 9.4 + (1.2 if cx > 9.4 else 0)], [cy + (-0.32 if cy > 4.5 else 0), 4.5 + (0.55 if cy > 4.5 else 0)], color="black", lw=1.0)

    p = os.path.join(FIG_DIR, "fig4_8_er_model.png")
    plt.savefig(p, bbox_inches='tight')
    plt.close()
    print("Cleaned academic ER model diagram:", p)

if __name__ == "__main__":
    gen_methodology_flowchart()
    gen_use_case_diagram()
    gen_activity_diagram()
    gen_sequence_diagram()
    gen_er_model()
