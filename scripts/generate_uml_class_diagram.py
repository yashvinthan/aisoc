"""
Generate standard 3-compartment UML Class Diagram with clean layout and no internal title.
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

FIG_DIR = r"c:\Users\yashv\dev\work in progress\mini project\AiSOC\docs\figures"
os.makedirs(FIG_DIR, exist_ok=True)

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 8.5
plt.rcParams['figure.dpi'] = 300

def draw_uml_class(ax, xy, width, h_title, h_attr, h_meth, class_name, attributes, methods):
    x, y = xy
    total_h = h_title + h_attr + h_meth

    # Main outer rectangle
    rect = patches.Rectangle((x, y), width, total_h, linewidth=1.5, edgecolor="black", facecolor="white", zorder=2)
    ax.add_patch(rect)

    # Dividing horizontal lines
    y_line1 = y + h_meth + h_attr
    y_line2 = y + h_meth
    ax.plot([x, x + width], [y_line1, y_line1], color="black", lw=1.2, zorder=3)
    ax.plot([x, x + width], [y_line2, y_line2], color="black", lw=1.2, zorder=3)

    # Class Name (Title Compartment)
    cy_title = y_line1 + h_title / 2.0
    ax.text(x + width / 2.0, cy_title, class_name, ha='center', va='center', fontsize=9.0, fontweight='bold', color='black', zorder=4)

    # Attributes Compartment
    attr_start_y = y_line1 - 0.22
    for idx, attr in enumerate(attributes):
        ax.text(x + 0.12, attr_start_y - idx * 0.25, f"+{attr}", ha='left', va='center', fontsize=7.8, color='black', zorder=4)

    # Methods Compartment
    meth_start_y = y_line2 - 0.22
    for idx, meth in enumerate(methods):
        ax.text(x + 0.12, meth_start_y - idx * 0.25, f"+{meth}", ha='left', va='center', fontsize=7.8, color='black', zorder=4)

def gen_uml_class_diagram():
    fig, ax = plt.subplots(figsize=(12, 7.2))
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 9.5)
    ax.axis('off')

    # Class 1: Analyst / User (Top Left)
    c1_attrs = ["UserID: UUID", "Username: Str", "TenantID: Str", "Role: Enum", "Email: Str"]
    c1_meths = ["Login()", "ViewAlerts()", "InspectDossier()", "ExecuteHunt()", "ApproveAction()", "ExportReport()"]
    draw_uml_class(ax, (0.6, 5.0), 3.1, 0.45, 1.45, 1.7, "Analyst / User", c1_attrs, c1_meths)

    # Class 2: AiSOC Core System (Top Center)
    c2_attrs = ["SystemID: UUID", "Version: 1.5.0", "MaturityLevel", "BlastRadiusLimit", "ActiveConnectors"]
    c2_meths = ["IngestEvent()", "NormalizeOCSF()", "SimhashDedup()", "ScoreRisk()", "RouteToAgents()", "ValidateGating()"]
    draw_uml_class(ax, (4.6, 5.0), 3.3, 0.45, 1.45, 1.7, "AiSOC System", c2_attrs, c2_meths)

    # Class 3: Knowledge Graph (Top Right-Center)
    c3_attrs = ["GraphID: UUID", "HostNodes", "UserNodes", "AlertNodes", "TechniqueNodes"]
    c3_meths = ["UpsertEntity()", "GetAttackPath()", "GetBlastRadius()", "GetNeighbors()", "VerifyIsolation()"]
    draw_uml_class(ax, (8.8, 5.2), 2.9, 0.45, 1.45, 1.5, "Knowledge Graph", c3_attrs, c3_meths)

    # Class 4: Storage Tier (Top Right)
    c4_attrs = ["DatabaseID: UUID", "PostgresDB", "OpenSearchIndex", "RedisCache", "QdrantVector"]
    c4_meths = ["PersistState()", "QueryLake()", "CacheBloom()", "SemanticSearch()"]
    draw_uml_class(ax, (12.3, 5.4), 2.4, 0.45, 1.45, 1.3, "Storage Engine", c4_attrs, c4_meths)

    # Class 5: Incident Case / Alert (Bottom Left)
    c5_attrs = ["CaseID: UUID", "AlertID: UUID", "Severity: Enum", "Confidence: Int", "Status: Enum", "MitreTTPs: List", "SimhashFingerprint"]
    c5_meths = ["Fuse()", "CalculatePriority()", "AssignAnalyst()", "CloseCase()", "GeneratePDF()"]
    draw_uml_class(ax, (1.8, 0.6), 3.4, 0.45, 1.95, 1.45, "Incident Case", c5_attrs, c5_meths)

    # Class 6: SOAR Action Execution (Bottom Right-Center)
    c6_attrs = ["ActionID: UUID", "ActionType: Enum", "TargetEntity: Str", "BlastRadiusTier: Int", "ApprovalStatus: Enum", "ExecutionTimestamp"]
    c6_meths = ["CheckBlastRadius()", "DispatchIsolateHost()", "RevokeTokens()", "SendSlackModal()", "ConfirmRemediation()"]
    draw_uml_class(ax, (8.4, 0.6), 3.4, 0.45, 1.7, 1.45, "Action Execution", c6_attrs, c6_meths)

    # Connecting Associative Lines
    # Analyst <-> AiSOC System
    ax.plot([3.7, 4.6], [6.8, 6.8], color="black", lw=1.3)

    # AiSOC System <-> Knowledge Graph
    ax.plot([7.9, 8.8], [6.8, 6.8], color="black", lw=1.3)

    # Knowledge Graph <-> Storage Engine
    ax.plot([11.7, 12.3], [6.8, 6.8], color="black", lw=1.3)

    # Analyst / System <-> Incident Case
    ax.plot([2.5, 2.5], [5.0, 4.45], color="black", lw=1.3)

    # Knowledge Graph <-> Action Execution
    ax.plot([10.2, 10.2], [5.2, 4.2], color="black", lw=1.3)

    # Incident Case <-> Action Execution
    ax.plot([5.2, 8.4], [2.4, 2.4], color="black", lw=1.3)

    p = os.path.join(FIG_DIR, "fig4_3_class_diagram.png")
    plt.savefig(p, bbox_inches='tight')
    plt.close()
    print("Generated clean UML Class Diagram:", p)

if __name__ == "__main__":
    gen_uml_class_diagram()
