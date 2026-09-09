"""
Render the exact High-Level System Architecture topology matching docs/architecture/SYSTEM_DESIGN.md
with 6 Subgraphs: Sources, Ingest & Normalize, Event Spine, Detect & Reason, Surface, Storage Tier.
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

def draw_subgraph_box(ax, xy, width, height, title):
    rect = patches.Rectangle(xy, width, height, linewidth=1.5, linestyle="--", edgecolor="black", facecolor="white", zorder=1)
    ax.add_patch(rect)
    ax.text(xy[0] + width / 2.0, xy[1] + height - 0.25, title, ha='center', va='top', fontsize=9.0, fontweight='bold', color='black', zorder=2)

def draw_node(ax, center, width, height, title, subtitle="", is_cylinder=False):
    x = center[0] - width / 2.0
    y = center[1] - height / 2.0
    if is_cylinder:
        rect = patches.FancyBboxPatch((x, y), width, height, boxstyle="round,pad=0.03,rounding_size=0.15", linewidth=1.3, edgecolor="black", facecolor="white", zorder=3)
        ax.add_patch(rect)
    else:
        rect = patches.Rectangle((x, y), width, height, linewidth=1.3, edgecolor="black", facecolor="white", zorder=3)
        ax.add_patch(rect)

    cx, cy = center
    if subtitle:
        ax.text(cx, cy + 0.14, title, ha='center', va='center', fontsize=8.0, fontweight='bold', color='black', zorder=4)
        ax.text(cx, cy - 0.16, subtitle, ha='center', va='center', fontsize=7.0, color='black', zorder=4)
    else:
        ax.text(cx, cy, title, ha='center', va='center', fontsize=8.0, fontweight='bold', color='black', zorder=4)

def draw_wire(ax, start, end, label="", label_pos=0.5):
    ax.annotate('', xy=end, xytext=start, arrowprops=dict(arrowstyle="->", color="black", lw=1.2), zorder=5)
    if label:
        lx = start[0] + (end[0] - start[0]) * label_pos
        ly = start[1] + (end[1] - start[1]) * label_pos + 0.12
        ax.text(lx, ly, label, ha='center', va='center', fontsize=6.8, fontweight='bold', color='black', bbox=dict(boxstyle="square,pad=0.12", fc="white", ec="none"), zorder=6)

def gen_system_architecture():
    fig, ax = plt.subplots(figsize=(16, 9.5))
    ax.set_xlim(0, 22)
    ax.set_ylim(0, 13)
    ax.axis('off')

    # Subgraph 1: Sources (Top Left)
    draw_subgraph_box(ax, (0.4, 8.0), 3.2, 4.4, "Sources")
    draw_node(ax, (2.0, 11.4), 2.6, 0.55, "EDR / XDR")
    draw_node(ax, (2.0, 10.6), 2.6, 0.55, "SIEM")
    draw_node(ax, (2.0, 9.8), 2.6, 0.55, "Cloud APIs")
    draw_node(ax, (2.0, 9.0), 2.6, 0.55, "Identity")
    draw_node(ax, (2.0, 8.2), 2.6, 0.55, "Network")

    # Subgraph 2: Ingest & Normalize
    draw_subgraph_box(ax, (4.1, 8.0), 4.8, 4.4, "Ingest & Normalize")
    draw_node(ax, (5.4, 11.2), 2.2, 0.7, "Connectors", "(Python · 78 vendors)")
    draw_node(ax, (5.4, 9.5), 2.2, 0.7, "osquery-tls", "(Python · telemetry)")
    draw_node(ax, (7.6, 10.35), 1.8, 0.75, "Ingest worker", "(Go · OCSF)")
    draw_node(ax, (7.6, 8.7), 1.8, 0.7, "Enrichment", "(Go · IOC + Shodan)")

    # Connections in Ingest
    draw_wire(ax, (3.3, 10.2), (4.3, 10.2))
    draw_wire(ax, (6.5, 11.2), (6.7, 10.5))
    draw_wire(ax, (6.5, 9.5), (6.7, 10.2))
    draw_wire(ax, (7.6, 9.95), (7.6, 9.05))

    # Subgraph 3: Event Spine
    draw_subgraph_box(ax, (9.4, 8.0), 2.6, 4.4, "Event Spine")
    draw_node(ax, (10.7, 10.2), 2.0, 1.2, "Apache Kafka", "(Partitioned Spine)", is_cylinder=True)
    draw_wire(ax, (8.5, 8.7), (9.7, 9.8))

    # Subgraph 4: Detect & Reason
    draw_subgraph_box(ax, (12.5, 7.2), 4.2, 5.2, "Detect & Reason")
    draw_node(ax, (14.6, 11.4), 3.4, 0.65, "Fusion", "(Python · ML Scorer)")
    draw_node(ax, (14.6, 10.2), 3.4, 0.65, "UEBA", "(Python · baseline)")
    draw_node(ax, (14.6, 9.0), 3.4, 0.65, "Rule engine", "(Sigma · YARA · KQL)")
    draw_node(ax, (14.6, 7.8), 3.4, 0.65, "AI Agents", "(LangGraph DAG)")

    # Connections Spine -> Detect & Reason
    draw_wire(ax, (11.7, 10.6), (12.9, 11.4))
    draw_wire(ax, (11.7, 10.2), (12.9, 10.2))
    draw_wire(ax, (11.7, 9.8), (12.9, 9.0))
    draw_wire(ax, (11.7, 9.4), (12.9, 7.8))

    # Subgraph 5: Surface (Bottom Left-Center)
    draw_subgraph_box(ax, (4.1, 0.6), 7.9, 6.6, "Surface")
    draw_node(ax, (6.5, 5.2), 4.2, 0.8, "Web Console + Responder PWA", "(Next.js 14 / React 19)")
    draw_node(ax, (6.5, 3.2), 4.2, 0.8, "MCP Server", "(TypeScript · stdio / SSE)")
    draw_node(ax, (6.5, 1.4), 4.2, 0.8, "Investigation Rail & ChatOps", "(Slack / Teams Webhooks)")
    draw_node(ax, (10.6, 3.3), 2.2, 1.2, "Core API", "(FastAPI / Python)", is_cylinder=False)

    # Connections inside Surface
    draw_wire(ax, (8.6, 5.2), (9.6, 3.7))
    draw_wire(ax, (8.6, 3.2), (9.5, 3.3))
    draw_wire(ax, (8.6, 1.4), (9.6, 2.9))

    # Subgraph 6: Storage Tier (Bottom Right)
    draw_subgraph_box(ax, (12.5, 0.6), 9.0, 6.6, "Storage Tier")
    draw_node(ax, (14.2, 5.4), 2.6, 0.8, "PostgreSQL", "(Relational & RLS)", is_cylinder=True)
    draw_node(ax, (17.2, 5.4), 2.6, 0.8, "ClickHouse", "(Warm Telemetry)", is_cylinder=True)
    draw_node(ax, (20.2, 5.4), 2.6, 0.8, "OpenSearch", "(Log Search)", is_cylinder=True)
    draw_node(ax, (14.2, 2.4), 2.6, 0.8, "Neo4j", "(Knowledge Graph)", is_cylinder=True)
    draw_node(ax, (17.2, 2.4), 2.6, 0.8, "Qdrant", "(Vector DB / RAG)", is_cylinder=True)
    draw_node(ax, (20.2, 2.4), 2.6, 0.8, "Redis", "(Bloom & Simhash)", is_cylinder=True)

    # Connections Detect/Agents -> Storage Tier
    draw_wire(ax, (16.3, 7.8), (14.2, 6.0))
    draw_wire(ax, (16.3, 7.8), (14.2, 3.0))

    # Connections Surface/Core API -> Storage Tier
    draw_wire(ax, (11.7, 3.3), (12.9, 4.8))
    draw_wire(ax, (11.7, 3.3), (12.9, 2.4))

    p = os.path.join(FIG_DIR, "fig4_1_system_topology.png")
    plt.savefig(p, bbox_inches='tight')
    plt.close()
    print("Generated complete System Architecture Topology matching SYSTEM_DESIGN.md:", p)

if __name__ == "__main__":
    gen_system_architecture()
