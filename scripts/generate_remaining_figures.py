"""
Generate the remaining real figures for the AiSOC B. Tech report.
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
# Fig 3.1: Traditional Multi-Tier SOC Operational Funnel
# -----------------------------------------------------------------------------
def gen_fig3_1():
    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis('off')
    
    draw_box(ax, (1.0, 5.0), 8.0, 1.4, "SIEM Detection Rule Evaluation", "10,000 – 50,000 raw daily alerts | 85%+ False Positives", bg="#FEF2F2", border="#EF4444", title_color="#991B1B")
    
    draw_box(ax, (2.0, 3.2), 6.0, 1.4, "Tier-1 Human Monitoring & Triage", "Swivel-chair across 5-10 tabs | 3-5 mins/alert | Backlog Latency: 15-45m", bg="#FFFBEB", border="#F59E0B", title_color="#92400E")
    
    draw_box(ax, (3.0, 1.4), 4.0, 1.4, "Tier-2 Incident Response", "Manual SPL queries | Scope forensics | MTTR: 45-60 mins", bg="#EFF6FF", border="#3B82F6", title_color="#1E40AF")
    
    draw_box(ax, (4.0, 0.1), 2.0, 0.9, "Tier-3 Escalation", "Lead Hunters / Admins", bg="#F5F3FF", border="#8B5CF6", title_color="#5B21B6", fontsize=8.5)
    
    draw_arrow(ax, (5.0, 5.0), (5.0, 4.6), "Escalate (10%)")
    draw_arrow(ax, (5.0, 3.2), (5.0, 2.8), "Escalate (2%)")
    draw_arrow(ax, (5.0, 1.4), (5.0, 1.0), "Escalate (0.2%)")
    
    plt.title("Figure 3.1: Traditional Multi-Tier SOC Operational Funnel and Hand-off Delays", fontsize=11, fontweight='bold', pad=15)
    p = os.path.join(FIG_DIR, "fig3_1_traditional_soc_funnel.png")
    plt.savefig(p, bbox_inches='tight')
    plt.close()
    print("Generated:", p)

# -----------------------------------------------------------------------------
# Fig 4.5: UML Activity Diagram
# -----------------------------------------------------------------------------
def gen_fig4_5():
    fig, ax = plt.subplots(figsize=(9, 6.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 9)
    ax.axis('off')
    
    # Start node
    ax.plot(5.0, 8.4, 'o', color="#1E293B", markersize=14)
    
    draw_box(ax, (3.2, 7.0), 3.6, 0.9, "DetectAgent: Match Signatures", bg="#EEF2FF", border="#4F46E5", fontsize=9)
    draw_box(ax, (3.2, 5.6), 3.6, 0.9, "TriageAgent: Score Confidence", bg="#FEF3C7", border="#D97706", fontsize=9)
    
    # Decision Diamond
    diamond = patches.Polygon([[5.0, 4.8], [6.2, 4.3], [5.0, 3.8], [3.8, 4.3]], closed=True, facecolor="#F8FAFC", edgecolor="#334155", lw=1.5)
    ax.add_patch(diamond)
    ax.text(5.0, 4.3, "Confidence >= 30?", ha='center', va='center', fontsize=8, fontweight='bold')
    
    draw_box(ax, (0.5, 3.8), 2.6, 1.0, "Auto-Suppress Alert", "Log Benign FP", bg="#F1F5F9", border="#64748B", fontsize=8.5)
    draw_box(ax, (3.2, 2.4), 3.6, 0.9, "HuntAgent: Data Lake Sweep", bg="#F3E8FF", border="#9333EA", fontsize=9)
    draw_box(ax, (3.2, 1.0), 3.6, 0.9, "RespondAgent: Plan Gating", bg="#DCFCE7", border="#16A34A", fontsize=9)
    
    # End node
    ax.plot(5.0, 0.3, 'o', color="#1E293B", markersize=14)
    ax.plot(5.0, 0.3, 'o', color="white", markersize=10)
    ax.plot(5.0, 0.3, 'o', color="#1E293B", markersize=6)
    
    draw_arrow(ax, (5.0, 8.2), (5.0, 7.9))
    draw_arrow(ax, (5.0, 7.0), (5.0, 6.5))
    draw_arrow(ax, (5.0, 5.6), (5.0, 4.8))
    draw_arrow(ax, (3.8, 4.3), (3.1, 4.3), "No", color="#DC2626")
    draw_arrow(ax, (5.0, 3.8), (5.0, 3.3), "Yes", color="#16A34A")
    draw_arrow(ax, (5.0, 2.4), (5.0, 1.9))
    draw_arrow(ax, (5.0, 1.0), (5.0, 0.5))
    draw_arrow(ax, (1.8, 3.8), (1.8, 0.3))
    draw_arrow(ax, (1.8, 0.3), (4.7, 0.3))
    
    plt.title("Figure 4.5: UML Activity Diagram: Autonomous Multi-Agent Investigation Loop", fontsize=11, fontweight='bold', pad=15)
    p = os.path.join(FIG_DIR, "fig4_5_activity_diagram.png")
    plt.savefig(p, bbox_inches='tight')
    plt.close()
    print("Generated:", p)

# -----------------------------------------------------------------------------
# Fig 4.6: UML State Machine Diagram
# -----------------------------------------------------------------------------
def gen_fig4_6():
    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis('off')
    
    ax.plot(0.8, 5.8, 'o', color="#1E293B", markersize=12)
    
    draw_box(ax, (1.6, 5.2), 1.8, 1.2, "Ingested", "Raw OCSF Event", bg="#F8FAFC", border="#64748B", fontsize=8.5)
    draw_box(ax, (4.2, 5.2), 1.8, 1.2, "Fused", "Simhash & Scored", bg="#EFF6FF", border="#3B82F6", fontsize=8.5)
    draw_box(ax, (6.8, 5.2), 2.2, 1.2, "Investigating", "LangGraph DAG Active", bg="#F3E8FF", border="#9333EA", fontsize=8.5)
    
    draw_box(ax, (6.8, 2.2), 2.2, 1.2, "PendingApproval", "Blast Radius > Limit", bg="#FEF3C7", border="#D97706", fontsize=8.5)
    draw_box(ax, (4.2, 2.2), 1.8, 1.2, "AutoRemediating", "SOAR API Executing", bg="#DCFCE7", border="#16A34A", fontsize=8.5)
    draw_box(ax, (1.6, 2.2), 1.8, 1.2, "Resolved / Closed", "Ledger Finalized", bg="#F1F5F9", border="#334155", fontsize=8.5)
    
    draw_arrow(ax, (1.0, 5.8), (1.6, 5.8))
    draw_arrow(ax, (3.4, 5.8), (4.2, 5.8), "Deduplicated")
    draw_arrow(ax, (6.0, 5.8), (6.8, 5.8), "Risk >= Threshold")
    draw_arrow(ax, (7.9, 5.2), (7.9, 3.4), "High Blast Radius")
    draw_arrow(ax, (6.8, 2.8), (6.0, 2.8), "Approved")
    draw_arrow(ax, (7.4, 5.2), (5.5, 3.4), "Low Blast Radius", color="#16A34A")
    draw_arrow(ax, (4.2, 2.8), (3.4, 2.8), "Remediated")
    
    plt.title("Figure 4.6: UML State Machine Diagram: Incident and Alert Lifecycle State Transitions", fontsize=11, fontweight='bold', pad=15)
    p = os.path.join(FIG_DIR, "fig4_6_state_machine.png")
    plt.savefig(p, bbox_inches='tight')
    plt.close()
    print("Generated:", p)

# -----------------------------------------------------------------------------
# Fig 6.1: OCSF Normalization Pipeline
# -----------------------------------------------------------------------------
def gen_fig6_1():
    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis('off')
    
    draw_box(ax, (0.5, 1.8), 2.2, 1.8, "Raw Telemetry Ingest", "Syslog / CEF / HEC\nWebhooks / CloudTrail", bg="#F8FAFC", border="#64748B")
    draw_box(ax, (3.6, 1.8), 2.8, 1.8, "Go Normalizer Engine", "OCSF v1.1.0 Taxonomy\nAho-Corasick ATT&CK Trie\nLatency: < 2 ms", bg="#FEF3C7", border="#D97706")
    draw_box(ax, (7.3, 1.8), 2.2, 1.8, "Kafka Event Bus", "Partitioned Stream\nocsf.events\nfused.alerts", bg="#DCFCE7", border="#16A34A")
    
    draw_arrow(ax, (2.7, 2.7), (3.6, 2.7), "Heterogeneous JSON")
    draw_arrow(ax, (6.4, 2.7), (7.3, 2.7), "Strict OCSF JSON")
    
    plt.title("Figure 6.1: High-Throughput OCSF Normalization and ATT&CK Indexing Pipeline", fontsize=11, fontweight='bold', pad=15)
    p = os.path.join(FIG_DIR, "fig6_1_ocsf_pipeline.png")
    plt.savefig(p, bbox_inches='tight')
    plt.close()
    print("Generated:", p)

# -----------------------------------------------------------------------------
# Fig 6.2: Threat Intelligence Pipeline
# -----------------------------------------------------------------------------
def gen_fig6_2():
    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis('off')
    
    draw_box(ax, (0.5, 1.8), 2.2, 1.8, "External Threat Feeds", "TAXII 2.1 / MISP\nAlienVault OTX\nCISA KEV Catalog", bg="#F8FAFC", border="#64748B")
    draw_box(ax, (3.6, 1.8), 2.8, 1.8, "Redis Bloom Filter", "m=10M bits, k=7 hashes\np = 0.81% false-pos\nHigh-Speed Dedup", bg="#FEE2E2", border="#EF4444")
    draw_box(ax, (7.3, 1.8), 2.2, 1.8, "Persistence Sinks", "OpenSearch (iocs-*)\nQdrant (Vectors)\nNeo4j (:ThreatActor)", bg="#EEF2FF", border="#4F46E5")
    
    draw_arrow(ax, (2.7, 2.7), (3.6, 2.7), "Hourly Feeds")
    draw_arrow(ax, (6.4, 2.7), (7.3, 2.7), "Unique IOCs")
    
    plt.title("Figure 6.2: Threat Intelligence Ingestion, Bloom Filter Deduplication, and Sink Fan-out", fontsize=11, fontweight='bold', pad=15)
    p = os.path.join(FIG_DIR, "fig6_2_threatintel_bloom.png")
    plt.savefig(p, bbox_inches='tight')
    plt.close()
    print("Generated:", p)

# -----------------------------------------------------------------------------
# Fig 6.4: Neo4j Graph Schema
# -----------------------------------------------------------------------------
def gen_fig6_4():
    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')
    
    draw_box(ax, (0.8, 3.8), 2.0, 1.4, ":User", "id: String\nrisk_score: Float", bg="#EFF6FF", border="#3B82F6")
    draw_box(ax, (4.0, 3.8), 2.0, 1.4, ":Host", "id: String\nblast_radius: Int", bg="#EFF6FF", border="#3B82F6")
    draw_box(ax, (7.2, 3.8), 2.0, 1.4, ":Alert", "id: UUID\nseverity: Enum", bg="#FEF2F2", border="#EF4444")
    
    draw_box(ax, (4.0, 0.8), 2.0, 1.4, ":Technique", "id: 'T1078'\nname: Valid Accts", bg="#F5F3FF", border="#8B5CF6")
    draw_box(ax, (7.2, 0.8), 2.0, 1.4, ":Tactic", "id: 'TA0008'\nname: Lateral Mvt", bg="#F5F3FF", border="#8B5CF6")
    
    draw_arrow(ax, (2.8, 4.5), (4.0, 4.5), ":LOGGED_INTO")
    draw_arrow(ax, (6.0, 4.5), (7.2, 4.5), ":AFFECTS")
    draw_arrow(ax, (8.2, 3.8), (5.0, 2.2), ":USES")
    draw_arrow(ax, (6.0, 1.5), (7.2, 1.5), ":PART_OF")
    
    plt.title("Figure 6.4: Neo4j Knowledge Graph Schema with Kill-Chain Attack Traversals", fontsize=11, fontweight='bold', pad=15)
    p = os.path.join(FIG_DIR, "fig6_4_neo4j_graph_schema.png")
    plt.savefig(p, bbox_inches='tight')
    plt.close()
    print("Generated:", p)

# -----------------------------------------------------------------------------
# Fig 6.6: Blast-Radius Gating
# -----------------------------------------------------------------------------
def gen_fig6_6():
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')
    
    draw_box(ax, (0.5, 2.2), 2.2, 1.6, "RespondAgent\nProposed Action", "Isolate Host / Subnet\nRevoke Credentials", bg="#F8FAFC", border="#64748B")
    
    draw_box(ax, (3.8, 3.5), 2.8, 1.6, "L0–L2 Maturity Mode", "Always Request Approval\nPost Slack/Web Modal", bg="#FEF3C7", border="#D97706")
    draw_box(ax, (3.8, 0.8), 2.8, 1.8, "L3–L4 Maturity Mode\n(Blast Radius Gated)", "Query Neo4j (<= 3 hops)\nB_r(e) <= Policy Limit: Auto\nB_r(e) > Policy Limit: Gate", bg="#DCFCE7", border="#16A34A", fontsize=8.5)
    
    draw_box(ax, (7.6, 2.2), 2.0, 1.6, "Execution / Guard", "SOAR API Dispatch\nAudit Ledger Logged", bg="#EEF2FF", border="#4F46E5")
    
    draw_arrow(ax, (2.7, 3.3), (3.8, 4.2), "Policy L0-L2")
    draw_arrow(ax, (2.7, 2.7), (3.8, 1.7), "Policy L3-L4")
    draw_arrow(ax, (6.6, 4.2), (7.6, 3.3), "Human Approval")
    draw_arrow(ax, (6.6, 1.7), (7.6, 2.7), "Auto-Execute")
    
    plt.title("Figure 6.6: Blast-Radius Safety Gating Boundary and L0–L4 Approval Mechanism", fontsize=11, fontweight='bold', pad=15)
    p = os.path.join(FIG_DIR, "fig6_6_blast_radius_gating.png")
    plt.savefig(p, bbox_inches='tight')
    plt.close()
    print("Generated:", p)

# -----------------------------------------------------------------------------
# Fig 7.2: Case Study Trace
# -----------------------------------------------------------------------------
def gen_fig7_2():
    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis('off')
    
    timeline = [
        (1.0, "09:30:00 UTC", "DETECT", "Okta Auth (NY, USA)\nTechnique T1078\nSeverity: High", "#3B82F6"),
        (3.5, "09:38:00 UTC", "TRIAGE", "Okta Auth (Russia)\nVelocity > 55k km/h\nConf: 83/100 (HIGH)", "#D97706"),
        (6.0, "09:38:00.3 UTC", "HUNT", "ES|QL Query Sweep\nFound: Cloud Download\nfrom IP 203.0.113.50", "#9333EA"),
        (8.5, "09:38:00.8 UTC", "RESPOND", "Blast Radius: Safe (4)\nRevoked Okta Tokens\nPW Reset & Slack Post", "#16A34A")
    ]
    
    ax.axhline(2.5, color="#94A3B8", lw=3, zorder=1)
    
    for x, time_str, stage, desc, color in timeline:
        ax.plot(x, 2.5, 'o', color=color, markersize=12, zorder=2)
        ax.text(x, 2.9, f"{stage}\n{time_str}", ha='center', va='bottom', fontsize=8.5, fontweight='bold', color=color)
        draw_box(ax, (x - 1.1, 0.4), 2.2, 1.4, desc, "", bg="#F8FAFC", border=color, fontsize=7.5)
        ax.plot([x, x], [2.5, 1.8], color="#64748B", ls="--", lw=1)
        
    plt.title("Figure 7.2: Lateral Movement Investigation Trace in the Next.js Web Console", fontsize=11, fontweight='bold', pad=15)
    p = os.path.join(FIG_DIR, "fig7_2_case_study_trace.png")
    plt.savefig(p, bbox_inches='tight')
    plt.close()
    print("Generated:", p)

if __name__ == "__main__":
    gen_fig3_1()
    gen_fig4_5()
    gen_fig4_6()
    gen_fig6_1()
    gen_fig6_2()
    gen_fig6_4()
    gen_fig6_6()
    gen_fig7_2()
    print("All supplementary engineering figures generated successfully.")
