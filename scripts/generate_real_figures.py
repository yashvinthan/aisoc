"""
Generate real high-resolution engineering and architectural diagrams, UML models, and benchmark charts for the AiSOC B. Tech report.
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from PIL import Image

FIG_DIR = r"c:\Users\yashv\dev\work in progress\mini project\AiSOC\docs\figures"
os.makedirs(FIG_DIR, exist_ok=True)

# Set global styles
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10
plt.rcParams['figure.dpi'] = 300

def draw_box(ax, xy, width, height, title, subtitle="", color="#1E293B", bg="#F8FAFC", border="#334155", title_color="#0F172A", subtitle_color="#475569", fontsize=10):
    rect = patches.FancyBboxPatch(xy, width, height, boxstyle="round,pad=0.03,rounding_size=0.05", linewidth=1.5, edgecolor=border, facecolor=bg)
    ax.add_patch(rect)
    cx = xy[0] + width / 2.0
    if subtitle:
        cy_title = xy[1] + height * 0.65
        cy_sub = xy[1] + height * 0.35
        ax.text(cx, cy_title, title, ha='center', va='center', fontsize=fontsize, fontweight='bold', color=title_color)
        ax.text(cx, cy_sub, subtitle, ha='center', va='center', fontsize=fontsize*0.8, color=subtitle_color)
    else:
        cy = xy[1] + height / 2.0
        ax.text(cx, cy, title, ha='center', va='center', fontsize=fontsize, fontweight='bold', color=title_color)

def draw_arrow(ax, start, end, label="", color="#2563EB", linestyle='-', lw=1.5):
    ax.annotate('', xy=end, xytext=start, arrowprops=dict(arrowstyle="->", color=color, lw=lw, ls=linestyle))
    if label:
        mx = (start[0] + end[0]) / 2.0
        my = (start[1] + end[1]) / 2.0 + 0.03
        ax.text(mx, my, label, ha='center', va='bottom', fontsize=8, fontweight='bold', color=color, bbox=dict(boxstyle="round,pad=0.1", fc="white", ec="none", alpha=0.8))

# -----------------------------------------------------------------------------
# Fig 1.1: Multi-Disciplinary Domain Mapping
# -----------------------------------------------------------------------------
def gen_fig1_1():
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')
    
    draw_box(ax, (3.5, 2.2), 3.0, 1.6, "AiSOC Platform", "Autonomous AI-Powered SOC", bg="#EEF2FF", border="#4F46E5", title_color="#312E81", fontsize=12)
    
    draw_box(ax, (0.5, 4.0), 2.5, 1.2, "Cybersecurity Engg.", "OCSF, ATT&CK, STIX 2.1", bg="#FEF2F2", border="#EF4444")
    draw_box(ax, (7.0, 4.0), 2.5, 1.2, "Distributed Systems", "Go Ingest, Kafka, Redis", bg="#F0FDF4", border="#22C55E")
    draw_box(ax, (0.5, 0.6), 2.5, 1.2, "Machine Learning", "Simhash, IsoForest, LightGBM", bg="#FFFBEB", border="#F59E0B")
    draw_box(ax, (7.0, 0.6), 2.5, 1.2, "Multi-Agent AI", "LangGraph DAG (4 Agents)", bg="#FAF5FF", border="#A855F7")
    
    draw_arrow(ax, (3.0, 4.2), (3.7, 3.6), "Standards & Rules")
    draw_arrow(ax, (7.0, 4.2), (6.3, 3.6), "Telemetry Stream")
    draw_arrow(ax, (3.0, 1.6), (3.7, 2.4), "Noise Filtering")
    draw_arrow(ax, (7.0, 1.6), (6.3, 2.4), "Closed-Loop Triage")
    
    plt.title("Figure 1.1: Multi-Disciplinary Domain Mapping of the AiSOC Platform", fontsize=11, fontweight='bold', pad=15)
    p = os.path.join(FIG_DIR, "fig1_1_domain_mapping.png")
    plt.savefig(p, bbox_inches='tight')
    plt.close()
    print("Generated:", p)

# -----------------------------------------------------------------------------
# Fig 1.2: The Alert Fatigue Funnel
# -----------------------------------------------------------------------------
def gen_fig1_2():
    fig, ax = plt.subplots(figsize=(8, 4.5))
    categories = ['Raw Security Logs', 'SIEM Rule Matches', 'Human Triage Queue', 'Investigated Incidents', 'Actual True Positives']
    values = [500000, 25000, 1200, 150, 12]
    colors = ['#64748B', '#F59E0B', '#EF4444', '#3B82F6', '#10B981']
    
    y_pos = np.arange(len(categories))
    bars = ax.barh(y_pos, values, color=colors, height=0.6)
    ax.set_xscale('log')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(categories, fontsize=10, fontweight='bold')
    ax.invert_yaxis()
    ax.set_xlabel('Daily Volume (Logarithmic Scale)', fontsize=10, fontweight='bold')
    
    for bar, val in zip(bars, values):
        ax.text(val * 1.3, bar.get_y() + bar.get_height()/2, f'{val:,}', va='center', fontsize=9, fontweight='bold', color="#0F172A")
        
    ax.set_xlim(1, 2000000)
    ax.grid(axis='x', linestyle='--', alpha=0.5)
    plt.title("Figure 1.2: The Tier-1 SOC Alert Fatigue Crisis and Alert Flow Funnel", fontsize=11, fontweight='bold', pad=15)
    p = os.path.join(FIG_DIR, "fig1_2_alert_fatigue.png")
    plt.savefig(p, bbox_inches='tight')
    plt.close()
    print("Generated:", p)

# -----------------------------------------------------------------------------
# Fig 2.1: Evolutionary Timeline
# -----------------------------------------------------------------------------
def gen_fig2_1():
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.set_xlim(1998, 2028)
    ax.set_ylim(0, 4)
    ax.axis('off')
    
    ax.axhline(2, color="#94A3B8", lw=3, zorder=1)
    
    milestones = [
        (2000, "Passive Log Aggregation", "Syslog (RFC 3164)\nText file archival", -1),
        (2006, "1st Gen SIEM", "ArcSight, QRadar\nRelational DB & CEF", 1),
        (2014, "Big Data SIEM", "Elasticsearch & Kafka\nHigh-volume indexing", -1),
        (2019, "1st Gen SOAR", "Static API Webhooks\nScript playbooks", 1),
        (2026, "Autonomous Multi-Agent SOC", "AiSOC: OCSF, LangGraph,\nNeo4j & Gated Actions", -1)
    ]
    
    for year, title, desc, direction in milestones:
        ax.plot(year, 2, 'o', color="#4F46E5", markersize=10, zorder=2)
        y_text = 2 + direction * 1.0
        draw_box(ax, (year - 2.2, y_text - 0.4), 4.4, 0.8, title, desc, bg="#EEF2FF" if year == 2026 else "#F8FAFC", border="#4F46E5" if year == 2026 else "#CBD5E1", fontsize=8.5)
        ax.plot([year, year], [2, y_text - 0.4 if direction > 0 else y_text + 0.4], color="#64748B", ls="--", lw=1)
        ax.text(year, 2 - direction * 0.25, str(year), ha='center', va='center', fontsize=9, fontweight='bold', color="#1E293B")
        
    plt.title("Figure 2.1: Evolutionary Timeline of Security Monitoring Architecture (2000–2026)", fontsize=11, fontweight='bold', pad=15)
    p = os.path.join(FIG_DIR, "fig2_1_evolution_timeline.png")
    plt.savefig(p, bbox_inches='tight')
    plt.close()
    print("Generated:", p)

# -----------------------------------------------------------------------------
# Fig 4.1: High-Level System Topology
# -----------------------------------------------------------------------------
def gen_fig4_1():
    fig, ax = plt.subplots(figsize=(10, 6.5))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # Layer 1: Data Sources
    draw_box(ax, (0.5, 6.2), 2.2, 1.4, "Telemetry Connectors", "EDR, CloudTrail, Okta,\nZeek, K8s (83+ feeds)", bg="#F1F5F9", border="#64748B")
    
    # Layer 2: Ingest & Normalization
    draw_box(ax, (3.5, 6.2), 2.4, 1.4, "services/ingest", "Go 1.21 Normalizer\nOCSF v1.1.0 & ATT&CK Trie", bg="#FEF3C7", border="#D97706")
    
    # Layer 3: Streaming Bus
    draw_box(ax, (6.7, 6.2), 2.2, 1.4, "Apache Kafka", "Topics: ocsf.events,\nfused.alerts", bg="#DCFCE7", border="#16A34A")
    
    # Layer 4: Fusion & ML
    draw_box(ax, (9.5, 6.2), 2.2, 1.4, "services/fusion", "Simhash 64-bit\nIsoForest + LambdaRank", bg="#FEE2E2", border="#DC2626")
    
    # Layer 5: Knowledge Graph & DBs
    draw_box(ax, (9.5, 3.2), 2.2, 1.8, "Stateful Storage", "Neo4j Property Graph\nPostgreSQL (RLS)\nRedis Cache / Bloom", bg="#E0E7FF", border="#4338CA")
    
    # Layer 6: LangGraph Multi-Agent DAG
    draw_box(ax, (4.5, 3.2), 4.2, 1.8, "services/agents (LangGraph DAG)", "DetectAgent -> TriageAgent -> HuntAgent -> RespondAgent\nRAG STIX Bundles, NL -> ES|QL/SPL/KQL", bg="#F3E8FF", border="#9333EA", fontsize=9.5)
    
    # Layer 7: Safety Gating & SOAR
    draw_box(ax, (0.5, 3.2), 3.2, 1.8, "services/actions", "Blast-Radius Gating Engine\nL0–L4 Maturity Model\nSlack/Teams ChatOps", bg="#FFEDD5", border="#EA580C")
    
    # Layer 8: Web Console
    draw_box(ax, (2.5, 0.6), 7.0, 1.6, "SOC Analyst Console (Next.js 14 / React 19)", "Real-time WebSocket Rail | Cytoscape Graph | Monaco Editor | Executive PDF Export", bg="#ECFEFF", border="#0891B2", fontsize=10)
    
    # Connectors
    draw_arrow(ax, (2.7, 6.9), (3.5, 6.9), "Raw Logs")
    draw_arrow(ax, (5.9, 6.9), (6.7, 6.9), "OCSF JSON")
    draw_arrow(ax, (8.9, 6.9), (9.5, 6.9), "Streaming")
    draw_arrow(ax, (10.6, 6.2), (10.6, 5.0), "Upsert Graph")
    draw_arrow(ax, (9.5, 4.1), (8.7, 4.1), "Graph Context")
    draw_arrow(ax, (4.5, 4.1), (3.7, 4.1), "Containment Plan")
    draw_arrow(ax, (6.0, 3.2), (6.0, 2.2), "State & Ledger")
    draw_arrow(ax, (2.1, 3.2), (3.5, 2.2), "Approval Hook")
    
    plt.title("Figure 4.1: High-Level End-to-End System Topology of AiSOC", fontsize=11, fontweight='bold', pad=15)
    p = os.path.join(FIG_DIR, "fig4_1_system_topology.png")
    plt.savefig(p, bbox_inches='tight')
    plt.close()
    print("Generated:", p)

# -----------------------------------------------------------------------------
# Fig 4.2: UML Use Case Diagram
# -----------------------------------------------------------------------------
def gen_fig4_2():
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # System Boundary
    rect = patches.Rectangle((2.8, 0.5), 6.5, 7.0, fill=False, edgecolor="#475569", lw=1.5, ls="--")
    ax.add_patch(rect)
    ax.text(6.0, 7.2, "AiSOC Autonomous Platform Boundary", ha='center', fontsize=11, fontweight='bold', color="#1E293B")
    
    # Actors
    draw_box(ax, (0.3, 5.5), 1.8, 1.2, "SOC Analyst\n(Tier-1/2)", bg="#EFF6FF", border="#3B82F6", fontsize=8.5)
    draw_box(ax, (0.3, 3.0), 1.8, 1.2, "SOC Lead /\nAdministrator", bg="#EFF6FF", border="#3B82F6", fontsize=8.5)
    draw_box(ax, (0.3, 0.8), 1.8, 1.2, "Detection\nEngineer", bg="#EFF6FF", border="#3B82F6", fontsize=8.5)
    
    # Use Cases (Ovals)
    ucs = [
        (6.0, 6.2, "UC1: Monitor Real-Time Alert Stream"),
        (6.0, 5.1, "UC2: Inspect Investigation Rail & Graph"),
        (6.0, 4.0, "UC3: Approve / Deny Gated Actions"),
        (6.0, 2.9, "UC4: Execute Autonomous Triage & Hunt"),
        (6.0, 1.8, "UC5: Tune Detection Rules & Benchmarks"),
        (6.0, 0.8, "UC6: Generate Compliance & PDF Reports")
    ]
    
    for x, y, title in ucs:
        ellipse = patches.Ellipse((x, y + 0.2), 4.8, 0.7, facecolor="#F8FAFC", edgecolor="#4F46E5", lw=1.2)
        ax.add_patch(ellipse)
        ax.text(x, y + 0.2, title, ha='center', va='center', fontsize=8.5, fontweight='bold', color="#1E1B4B")
        
    # Association Lines
    ax.plot([2.1, 3.6], [6.1, 6.4], color="#64748B", lw=1.2)
    ax.plot([2.1, 3.6], [6.1, 5.3], color="#64748B", lw=1.2)
    ax.plot([2.1, 3.6], [3.6, 4.2], color="#64748B", lw=1.2)
    ax.plot([2.1, 3.6], [3.6, 1.0], color="#64748B", lw=1.2)
    ax.plot([2.1, 3.6], [1.4, 2.0], color="#64748B", lw=1.2)
    
    plt.title("Figure 4.2: UML Use Case Diagram for Enterprise SOC Actors and Autonomous Engine", fontsize=11, fontweight='bold', pad=15)
    p = os.path.join(FIG_DIR, "fig4_2_use_case_diagram.png")
    plt.savefig(p, bbox_inches='tight')
    plt.close()
    print("Generated:", p)

# -----------------------------------------------------------------------------
# Fig 4.3: UML Class Diagram
# -----------------------------------------------------------------------------
def gen_fig4_3():
    fig, ax = plt.subplots(figsize=(10, 6.5))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    draw_box(ax, (0.5, 4.5), 3.2, 3.0, "OcsfEvent", "- id: UUID\n- class_uid: Int\n- category_uid: Int\n- time: DateTime\n- observables: List\n+ normalize(): Event\n+ tagMitre(): List", bg="#F8FAFC", border="#334155", fontsize=8.5)
    
    draw_box(ax, (4.5, 4.5), 3.2, 3.0, "Alert", "- id: UUID\n- title: String\n- severity: Enum\n- confidence: Int\n- simhash: Int64\n+ fuse(): Alert\n+ scoreRisk(): Float", bg="#F8FAFC", border="#334155", fontsize=8.5)
    
    draw_box(ax, (8.5, 4.5), 3.0, 3.0, "Case", "- id: UUID\n- title: String\n- status: Enum\n- priority: Enum\n- analyst: UUID\n+ closeCase(): Bool\n+ exportPdf(): File", bg="#F8FAFC", border="#334155", fontsize=8.5)
    
    draw_box(ax, (0.5, 0.5), 3.2, 3.0, "EntityNode (Neo4j)", "- id: String\n- type: Enum\n- risk_score: Float\n- blast_radius: Int\n+ getBlastRadius(): Int\n+ getAttackPath(): Path", bg="#F8FAFC", border="#334155", fontsize=8.5)
    
    draw_box(ax, (4.5, 0.5), 3.2, 3.0, "AgentLedgerStep", "- step_idx: Int\n- agent_name: String\n- action: String\n- rationale: String\n- tool_calls: List\n+ serialize(): JSON", bg="#F8FAFC", border="#334155", fontsize=8.5)
    
    draw_box(ax, (8.5, 0.5), 3.0, 3.0, "ActionExecution", "- id: UUID\n- action_type: String\n- target: String\n- blast_tier: Enum\n+ validateGating(): Bool\n+ execute(): Status", bg="#F8FAFC", border="#334155", fontsize=8.5)
    
    draw_arrow(ax, (3.7, 6.0), (4.5, 6.0), "fused into 1..*")
    draw_arrow(ax, (7.7, 6.0), (8.5, 6.0), "grouped in 1")
    draw_arrow(ax, (6.1, 4.5), (6.1, 3.5), "recorded in")
    draw_arrow(ax, (6.1, 0.5), (8.5, 1.5), "executes")
    draw_arrow(ax, (2.1, 4.5), (2.1, 3.5), "projects to")
    
    plt.title("Figure 4.3: UML Class Diagram of Core Entity Model and System Constraints", fontsize=11, fontweight='bold', pad=15)
    p = os.path.join(FIG_DIR, "fig4_3_class_diagram.png")
    plt.savefig(p, bbox_inches='tight')
    plt.close()
    print("Generated:", p)

# -----------------------------------------------------------------------------
# Fig 4.4: Sequence Diagram
# -----------------------------------------------------------------------------
def gen_fig4_4():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    lifelines = [
        (1.0, "Sensor / EDR"),
        (2.8, "services/ingest"),
        (4.6, "services/fusion"),
        (6.4, "LangGraph DAG"),
        (8.2, "services/actions"),
        (9.5, "SOC Analyst")
    ]
    
    for x, name in lifelines:
        ax.text(x, 7.5, name, ha='center', va='center', fontsize=8.5, fontweight='bold', bbox=dict(boxstyle="round,pad=0.2", fc="#EEF2FF", ec="#4F46E5"))
        ax.plot([x, x], [0.5, 7.0], color="#94A3B8", ls="--", lw=1)
        
    messages = [
        (1.0, 2.8, 6.5, "1. Ingest Raw JSON"),
        (2.8, 4.6, 5.6, "2. Normalized OCSF (Kafka)"),
        (4.6, 6.4, 4.7, "3. Fused Alert (Simhash + ML)"),
        (6.4, 6.4, 3.8, "4. Triage & Hunt (ES|QL)"),
        (6.4, 8.2, 2.9, "5. Propose Containment"),
        (8.2, 9.5, 2.0, "6. Blast Radius Approval"),
        (9.5, 8.2, 1.2, "7. Approve Action (ChatOps)"),
        (8.2, 1.0, 0.6, "8. Execute Containment (Isolate)")
    ]
    
    for x1, x2, y, text in messages:
        if x1 == x2:
            ax.annotate('', xy=(x1+0.6, y-0.3), xytext=(x1, y), arrowprops=dict(arrowstyle="->", color="#4338CA", lw=1.2))
            ax.plot([x1, x1+0.6, x1+0.6, x1], [y, y, y-0.3, y-0.3], color="#4338CA", lw=1.2)
            ax.text(x1 + 0.7, y - 0.15, text, fontsize=7.5, color="#1E1B4B", va='center')
        else:
            draw_arrow(ax, (x1, y), (x2, y), text, color="#2563EB" if x1 < x2 else "#DC2626")
            
    plt.title("Figure 4.4: UML Sequence Diagram: Telemetry Ingest to Gated Action Containment", fontsize=11, fontweight='bold', pad=15)
    p = os.path.join(FIG_DIR, "fig4_4_sequence_diagram.png")
    plt.savefig(p, bbox_inches='tight')
    plt.close()
    print("Generated:", p)

# -----------------------------------------------------------------------------
# Fig 6.3: Dual Stage MLScorer
# -----------------------------------------------------------------------------
def gen_fig6_3():
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')
    
    draw_box(ax, (0.5, 2.2), 2.2, 1.6, "Deduplicated Alert\nFeature Vector x", "Severity, CMDB Asset,\nHour, MITRE Tactic", bg="#F8FAFC", border="#475569")
    
    draw_box(ax, (3.8, 3.5), 2.8, 1.8, "Stage 1: Isolation Forest\n(Unsupervised)", "100 iTrees\nPath Length h(x)\ns(x, n) = 2^(-E(h)/c(n))", bg="#FEF2F2", border="#EF4444")
    
    draw_box(ax, (3.8, 0.7), 2.8, 1.8, "Stage 2: LambdaRank\n(Supervised GBDT)", "LightGBM Pairwise Loss\nNDCG Optimization\nAnalyst Feedback Loop", bg="#F0FDF4", border="#22C55E")
    
    draw_box(ax, (7.6, 2.2), 2.0, 1.6, "Fused Priority\nScore (1-100)", "Enriched Severity\nConfidence Tier\nQueue Position", bg="#EEF2FF", border="#4F46E5")
    
    draw_arrow(ax, (2.7, 3.4), (3.8, 4.2), "x_anomaly")
    draw_arrow(ax, (2.7, 2.6), (3.8, 1.8), "x_rank")
    draw_arrow(ax, (6.6, 4.2), (7.6, 3.4), "Anomaly Score")
    draw_arrow(ax, (6.6, 1.8), (7.6, 2.6), "Rank Score")
    
    plt.title("Figure 6.3: Dual-Stage MLScorer Architecture (Isolation Forest & LambdaRank)", fontsize=11, fontweight='bold', pad=15)
    p = os.path.join(FIG_DIR, "fig6_3_dual_stage_ml.png")
    plt.savefig(p, bbox_inches='tight')
    plt.close()
    print("Generated:", p)

# -----------------------------------------------------------------------------
# Fig 6.5: LangGraph Multi-Agent DAG Flow
# -----------------------------------------------------------------------------
def gen_fig6_5():
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')
    
    draw_box(ax, (0.5, 2.2), 1.8, 1.6, "DetectAgent", "Signature Matches\nMITRE ATT&CK TTPs\nOpens Intake Alert", bg="#EFF6FF", border="#3B82F6")
    draw_box(ax, (2.8, 2.2), 1.8, 1.6, "TriageAgent", "Confidence Scoring\nFalse-Pos Suppression\nSemantic Memory RAG", bg="#FEF3C7", border="#D97706")
    draw_box(ax, (5.1, 2.2), 1.8, 1.6, "HuntAgent", "Query Synthesis\nWarm Lake Sweeps\nES|QL / SPL / KQL", bg="#F3E8FF", border="#9333EA")
    draw_box(ax, (7.4, 2.2), 2.1, 1.6, "RespondAgent", "Containment Plan\nBlast Radius Gating\nGraduated Action", bg="#DCFCE7", border="#16A34A")
    
    draw_arrow(ax, (2.3, 3.0), (2.8, 3.0), "Evaluate")
    draw_arrow(ax, (4.6, 3.0), (5.1, 3.0), "Conf >= 30")
    draw_arrow(ax, (6.9, 3.0), (7.4, 3.0), "Artifacts")
    
    # Conditional edge to END
    draw_box(ax, (2.8, 0.2), 1.8, 1.0, "END (Auto-Suppress)", "Benign False Positive", bg="#F1F5F9", border="#64748B")
    draw_arrow(ax, (3.7, 2.2), (3.7, 1.2), "Conf < 30", color="#EF4444")
    
    plt.title("Figure 6.5: LangGraph Multi-Agent Directed Acyclic Graph (DAG) Execution Flow", fontsize=11, fontweight='bold', pad=15)
    p = os.path.join(FIG_DIR, "fig6_5_langgraph_dag.png")
    plt.savefig(p, bbox_inches='tight')
    plt.close()
    print("Generated:", p)

# -----------------------------------------------------------------------------
# Fig 7.1: Benchmark Charts (Noise & MTTR)
# -----------------------------------------------------------------------------
def gen_fig7_1():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5))
    
    # Chart 1: Noise Reduction
    scenarios = ['Lateral Mvt', 'AWS Exfil', 'GitHub Theft', 'K8s PrivEsc', 'Phishing', 'Full Corpus']
    raw_events = [24, 48, 18, 32, 55, 124500]
    fused_alerts = [1, 2, 1, 1, 2, 18052]
    reduction_pct = [(1 - f/r)*100 for r, f in zip(raw_events, fused_alerts)]
    
    x = np.arange(len(scenarios))
    bars = ax1.bar(x, reduction_pct, color='#3B82F6', width=0.55, edgecolor='#1E40AF')
    ax1.set_xticks(x)
    ax1.set_xticklabels(scenarios, rotation=25, ha='right', fontsize=8.5, fontweight='bold')
    ax1.set_ylabel('Alert Noise Reduction (%)', fontsize=9.5, fontweight='bold')
    ax1.set_ylim(0, 110)
    ax1.grid(axis='y', linestyle='--', alpha=0.5)
    ax1.set_title("Noise Reduction Ratio by Scenario", fontsize=10, fontweight='bold')
    
    for bar in bars:
        h = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., h + 2, f'{h:.1f}%', ha='center', va='bottom', fontsize=8, fontweight='bold')
        
    # Chart 2: MTTR Comparison
    categories = ['Traditional SOC', 'SIEM Only', 'AiSOC Autonomous']
    mttr_seconds = [3300, 1800, 1.08]
    colors = ['#EF4444', '#F59E0B', '#10B981']
    
    bars2 = ax2.bar(categories, mttr_seconds, color=colors, width=0.5, edgecolor='#334155')
    ax2.set_yscale('log')
    ax2.set_ylabel('Investigation MTTR (Seconds, Log Scale)', fontsize=9.5, fontweight='bold')
    ax2.grid(axis='y', linestyle='--', alpha=0.5)
    ax2.set_title("MTTR: Traditional vs. AiSOC", fontsize=10, fontweight='bold')
    
    for bar, val in zip(bars2, mttr_seconds):
        label = f"{val/60:.0f} min" if val >= 60 else f"{val:.2f} s"
        ax2.text(bar.get_x() + bar.get_width()/2., val * 1.4, label, ha='center', va='bottom', fontsize=8.5, fontweight='bold')
        
    plt.suptitle("Figure 7.1: Comparative Alert Noise Reduction and MTTR Compression Chart", fontsize=11, fontweight='bold')
    plt.tight_layout()
    p = os.path.join(FIG_DIR, "fig7_1_benchmark_charts.png")
    plt.savefig(p, bbox_inches='tight')
    plt.close()
    print("Generated:", p)

if __name__ == "__main__":
    gen_fig1_1()
    gen_fig1_2()
    gen_fig2_1()
    gen_fig4_1()
    gen_fig4_2()
    gen_fig4_3()
    gen_fig4_4()
    gen_fig6_3()
    gen_fig6_5()
    gen_fig7_1()
    print("All real engineering and architectural figures generated successfully.")
