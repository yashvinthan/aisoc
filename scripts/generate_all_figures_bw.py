"""
Master script to generate ALL figures in strict academic BLACK AND WHITE / GREYSCALE:
- Generous box padding with no text overflowing borders
- Generous arrow label spacing
- No internal plt.title (docx handles captions)
- Pure black lines and white backgrounds
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

def draw_bw_box(ax, xy, width, height, title, subtitle="", fontsize=9.0, bold=True, linestyle='-'):
    rect = patches.FancyBboxPatch(xy, width, height, boxstyle="round,pad=0.04,rounding_size=0.06", linewidth=1.5, linestyle=linestyle, edgecolor="black", facecolor="white")
    ax.add_patch(rect)
    cx = xy[0] + width / 2.0
    if subtitle:
        cy_title = xy[1] + height * 0.70
        cy_sub = xy[1] + height * 0.35
        ax.text(cx, cy_title, title, ha='center', va='center', fontsize=fontsize, fontweight='bold' if bold else 'normal', color='black')
        ax.text(cx, cy_sub, subtitle, ha='center', va='center', fontsize=fontsize*0.82, color='black')
    else:
        cy = xy[1] + height / 2.0
        ax.text(cx, cy, title, ha='center', va='center', fontsize=fontsize, fontweight='bold' if bold else 'normal', color='black')

def draw_bw_arrow(ax, start, end, label="", linestyle='-', lw=1.3):
    ax.annotate('', xy=end, xytext=start, arrowprops=dict(arrowstyle="->", color="black", lw=lw, ls=linestyle))
    if label:
        mx = (start[0] + end[0]) / 2.0
        my = (start[1] + end[1]) / 2.0 + 0.16
        ax.text(mx, my, label, ha='center', va='center', fontsize=7.5, fontweight='bold', color='black', bbox=dict(boxstyle="square,pad=0.15", fc="white", ec="none"))

# Fig 1.1: Domain Mapping (B&W)
def gen_fig1_1():
    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis('off')
    
    draw_bw_box(ax, (3.3, 2.3), 3.4, 2.2, "AiSOC Platform", "Central Autonomous SOC Engine\n(Multi-Agent AI + Graph)", fontsize=9.5)
    
    # Top-Left: Cybersecurity Operations
    draw_bw_box(ax, (0.4, 4.8), 2.8, 1.4, "Cybersecurity Operations", "Detection, Triage, Containment", fontsize=8.5)
    draw_bw_arrow(ax, (3.2, 4.8), (3.3, 4.3))

    # Top-Right: Distributed Systems
    draw_bw_box(ax, (6.8, 4.8), 2.8, 1.4, "Distributed Systems", "Go Ingest, Kafka, Microservices", fontsize=8.5)
    draw_bw_arrow(ax, (6.8, 4.8), (6.7, 4.3))

    # Bottom-Left: Machine Learning
    draw_bw_box(ax, (0.4, 0.6), 2.8, 1.4, "Machine Learning", "Simhash, Isolation Forest, Ranker", fontsize=8.5)
    draw_bw_arrow(ax, (3.2, 2.0), (3.3, 2.5))

    # Bottom-Right: Knowledge Graphs
    draw_bw_box(ax, (6.8, 0.6), 2.8, 1.4, "Knowledge Graphs", "Neo4j Property Graphs, Cypher", fontsize=8.5)
    draw_bw_arrow(ax, (6.8, 2.0), (6.7, 2.5))
        
    plt.savefig(os.path.join(FIG_DIR, "fig1_1_domain_mapping.png"), bbox_inches='tight')
    plt.close()

# Fig 1.2: Alert Fatigue (B&W)
def gen_fig1_2():
    fig, ax = plt.subplots(figsize=(9.5, 4.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')
    
    draw_bw_box(ax, (0.4, 3.8), 2.7, 1.6, "High-Volume Logs", "10k - 500k logs/day\n85%+ False Positives", fontsize=8.5)
    draw_bw_box(ax, (3.65, 3.8), 2.7, 1.6, "Tier-1 Bottleneck", "3-5 mins/alert manual\nSevere Alert Fatigue", fontsize=8.5)
    draw_bw_box(ax, (6.9, 3.8), 2.7, 1.6, "Delayed Response", "Dwell Time > 200d\nMTTR > 45 mins", fontsize=8.5)
    
    draw_bw_arrow(ax, (3.1, 4.6), (3.65, 4.6), "Overwhelms")
    draw_bw_arrow(ax, (6.35, 4.6), (6.9, 4.6), "Causes")
    
    draw_bw_box(ax, (1.8, 0.8), 6.4, 1.8, "AiSOC Autonomous Solution", "Go Ingest -> Simhash LSH -> MLScorer -> LangGraph DAG\n85.5% Noise Filtered | MTTR < 1.2 Seconds", fontsize=9.0)
    draw_bw_arrow(ax, (5.0, 3.8), (5.0, 2.6), "Autonomous Remediation")
    
    plt.savefig(os.path.join(FIG_DIR, "fig1_2_alert_fatigue.png"), bbox_inches='tight')
    plt.close()

# Fig 2.1: Evolution Timeline (B&W)
def gen_fig2_1():
    fig, ax = plt.subplots(figsize=(10, 4.0))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis('off')
    
    ax.axhline(2.5, color="black", lw=2, zorder=1)
    
    eras = [
        (1.0, "2000–2010", "1st Gen SIEM\n(Relational SQL)", "Text Syslog / RDBMS\nSevere I/O Bottlenecks"),
        (3.7, "2010–2018", "2nd Gen SIEM\n(Big Data / Search)", "Elasticsearch, Kafka\nStatic Alert Regexes"),
        (6.3, "2018–2023", "1st Gen SOAR\n(Linear Scripts)", "Python Playbooks\nBrittle API Scripts"),
        (9.0, "2024–2026", "Autonomous SOC\n(AiSOC Platform)", "OCSF + Neo4j + LLMs\nMulti-Agent DAG Triage")
    ]
    
    for x, era, title, desc in eras:
        ax.plot(x, 2.5, 'o', color="black", markersize=10, zorder=2)
        ax.plot(x, 2.5, 'o', color="white", markersize=6, zorder=3)
        ax.text(x, 2.9, f"{era}\n{title}", ha='center', va='bottom', fontsize=8.0, fontweight='bold', color='black')
        draw_bw_box(ax, (x - 1.0, 0.4), 2.0, 1.3, desc, "", fontsize=7.2)
        ax.plot([x, x], [2.5, 1.7], color="black", ls="--", lw=1)
        
    plt.savefig(os.path.join(FIG_DIR, "fig2_1_evolution_timeline.png"), bbox_inches='tight')
    plt.close()

# Fig 3.1: Traditional SOC Funnel (B&W)
def gen_fig3_1():
    fig, ax = plt.subplots(figsize=(9, 5.0))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis('off')
    
    draw_bw_box(ax, (0.8, 5.2), 8.4, 1.3, "SIEM Detection Rule Evaluation", "10,000 – 50,000 raw daily alerts | 85%+ False Positives", fontsize=8.5)
    draw_bw_box(ax, (1.8, 3.5), 6.4, 1.3, "Tier-1 Human Monitoring & Triage", "Swivel-chair across 5-10 tabs | 3-5 mins/alert | Backlog Latency: 15-45m", fontsize=8.0)
    draw_bw_box(ax, (2.8, 1.8), 4.4, 1.3, "Tier-2 Incident Response", "Manual SPL queries | Scope forensics | MTTR: 45-60 mins", fontsize=7.8)
    draw_bw_box(ax, (3.8, 0.3), 2.4, 0.9, "Tier-3 Escalation", "Lead Hunters / Admins", fontsize=7.5)
    
    draw_bw_arrow(ax, (5.0, 5.2), (5.0, 4.8), "Escalate (10%)")
    draw_bw_arrow(ax, (5.0, 3.5), (5.0, 3.1), "Escalate (2%)")
    draw_bw_arrow(ax, (5.0, 1.8), (5.0, 1.2), "Escalate (0.2%)")
    
    plt.savefig(os.path.join(FIG_DIR, "fig3_1_traditional_soc_funnel.png"), bbox_inches='tight')
    plt.close()

# Fig 4.1: System Topology (B&W)
def gen_fig4_1():
    fig, ax = plt.subplots(figsize=(12, 7.5))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.axis('off')

    draw_bw_box(ax, (0.4, 6.6), 3.2, 1.8, "Universal Telemetry Ingest", "83 Connectors (EDR, Cloud, IAM)\nWebhooks & CEF / HEC Listeners", fontsize=8.5)
    draw_bw_box(ax, (4.1, 6.6), 3.3, 1.8, "services/ingest (Go 1.21)", "OCSF v1.1.0 Normalization\nIn-Memory ATT&CK Trie Indexing", fontsize=8.5)
    draw_bw_box(ax, (7.9, 6.6), 2.7, 1.8, "Apache Kafka", "Partitioned Event Bus\nocsf.events | fused.alerts", fontsize=8.5)
    draw_bw_box(ax, (11.0, 6.6), 2.6, 1.8, "services/fusion", "Simhash LSH Dedup\nIsolation Forest MLScorer", fontsize=8.5)

    draw_bw_box(ax, (0.4, 2.4), 3.6, 2.6, "Cognitive Multi-Agent DAG", "services/agents (LangGraph)\n- DetectAgent (Signatures)\n- TriageAgent (Risk Scoring)\n- HuntAgent (ES|QL Query)\n- RespondAgent (Containment)", fontsize=8.5)
    draw_bw_box(ax, (4.6, 2.4), 4.4, 2.6, "Knowledge Graph & Storage", "services/api (FastAPI)\n- Neo4j (Entity & Attack Graph)\n- PostgreSQL (State & CoT Ledger)\n- OpenSearch + Qdrant (RAG)", fontsize=8.5)
    draw_bw_box(ax, (9.6, 2.4), 4.0, 2.6, "Action & Presentation Tier", "- services/actions (Blast-Radius)\n- apps/web (Next.js 14 Console)\n- services/realtime (WebSockets)\n- Slack/Teams ChatOps Approval", fontsize=8.5)

    draw_bw_arrow(ax, (3.6, 7.5), (4.1, 7.5))
    draw_bw_arrow(ax, (7.4, 7.5), (7.9, 7.5))
    draw_bw_arrow(ax, (10.6, 7.5), (11.0, 7.5))
    
    draw_bw_arrow(ax, (12.3, 6.6), (12.3, 5.0))
    draw_bw_arrow(ax, (12.3, 5.0), (7.0, 5.0))
    draw_bw_arrow(ax, (4.6, 3.7), (4.0, 3.7))
    draw_bw_arrow(ax, (9.0, 3.7), (9.6, 3.7))

    plt.savefig(os.path.join(FIG_DIR, "fig4_1_system_topology.png"), bbox_inches='tight')
    plt.close()

# Fig 4.6: State Machine (B&W)
def gen_fig4_6():
    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')
    
    ax.plot(0.8, 4.8, 'o', color="black", markersize=10)
    
    draw_bw_box(ax, (1.6, 4.2), 1.8, 1.2, "Ingested", "Raw OCSF Event", fontsize=8.0)
    draw_bw_box(ax, (4.2, 4.2), 1.8, 1.2, "Fused", "Simhash & Scored", fontsize=8.0)
    draw_bw_box(ax, (6.8, 4.2), 2.2, 1.2, "Investigating", "LangGraph DAG Active", fontsize=8.0)
    
    draw_bw_box(ax, (6.8, 1.4), 2.2, 1.2, "PendingApproval", "Blast Radius > Limit", fontsize=8.0)
    draw_bw_box(ax, (4.2, 1.4), 1.8, 1.2, "AutoRemediating", "SOAR API Executing", fontsize=8.0)
    draw_bw_box(ax, (1.6, 1.4), 1.8, 1.2, "Resolved / Closed", "Ledger Finalized", fontsize=8.0)
    
    draw_bw_arrow(ax, (1.0, 4.8), (1.6, 4.8))
    draw_bw_arrow(ax, (3.4, 4.8), (4.2, 4.8), "Deduped")
    draw_bw_arrow(ax, (6.0, 4.8), (6.8, 4.8), "Risk >= 30")
    draw_bw_arrow(ax, (7.9, 4.2), (7.9, 2.6), "High Blast")
    draw_bw_arrow(ax, (6.8, 2.0), (6.0, 2.0), "Approved")
    draw_bw_arrow(ax, (7.4, 4.2), (5.5, 2.6), "Low Blast")
    draw_bw_arrow(ax, (4.2, 2.0), (3.4, 2.0), "Executed")
    
    plt.savefig(os.path.join(FIG_DIR, "fig4_6_state_machine.png"), bbox_inches='tight')
    plt.close()

# Fig 6.1: OCSF Normalization Pipeline (B&W)
def gen_fig6_1():
    fig, ax = plt.subplots(figsize=(9, 4.0))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis('off')
    
    draw_bw_box(ax, (0.4, 1.5), 2.5, 2.0, "Raw Telemetry Ingest", "Syslog / CEF / HEC\nWebhooks / CloudTrail", fontsize=8.5)
    draw_bw_box(ax, (3.6, 1.5), 3.0, 2.0, "Go Normalizer Engine", "OCSF v1.1.0 Taxonomy\nAho-Corasick ATT&CK Trie\nLatency: < 2 ms", fontsize=8.5)
    draw_bw_box(ax, (7.3, 1.5), 2.3, 2.0, "Kafka Event Bus", "Partitioned Stream\nocsf.events\nfused.alerts", fontsize=8.5)
    
    draw_bw_arrow(ax, (2.9, 2.5), (3.6, 2.5), "Raw Payloads")
    draw_bw_arrow(ax, (6.6, 2.5), (7.3, 2.5), "OCSF Schema")
    
    plt.savefig(os.path.join(FIG_DIR, "fig6_1_ocsf_pipeline.png"), bbox_inches='tight')
    plt.close()

# Fig 6.2: Threat Intelligence (B&W) - FIXED PADDING & TEXT OVERFLOW
def gen_fig6_2():
    fig, ax = plt.subplots(figsize=(10, 4.5))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 5)
    ax.axis('off')
    
    draw_bw_box(ax, (0.5, 1.2), 3.0, 2.6, "External Threat Feeds", "TAXII 2.1 / MISP Feeds\nAlienVault OTX Subscriptions\nCISA KEV Vulnerability Catalog", fontsize=8.5)
    draw_bw_box(ax, (4.4, 1.2), 3.2, 2.6, "Redis Bloom Filter", "m = 10,000,000 bits\nk = 7 hashing functions\np = 0.81% false positive rate\nSub-millisecond deduplication", fontsize=8.5)
    draw_bw_box(ax, (8.5, 1.2), 3.0, 2.6, "Persistence Sinks", "OpenSearch (iocs-*)\nQdrant (Threat Embeddings)\nNeo4j (:ThreatActor Nodes)", fontsize=8.5)
    
    draw_bw_arrow(ax, (3.5, 2.5), (4.4, 2.5), "Hourly Feeds")
    draw_bw_arrow(ax, (7.6, 2.5), (8.5, 2.5), "Unique IOCs")
    
    plt.savefig(os.path.join(FIG_DIR, "fig6_2_threatintel_bloom.png"), bbox_inches='tight')
    plt.close()

# Fig 6.3: Dual Stage ML (B&W) - FIXED PADDING & OVERFLOW
def gen_fig6_3():
    fig, ax = plt.subplots(figsize=(11, 5.5))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 6)
    ax.axis('off')

    draw_bw_box(ax, (0.5, 1.8), 3.0, 2.4, "Deduplicated Alert", "Extracted Feature Vector x\n(Severity, Entity Risk, Velocity,\nTime Delta, Port Anomaly)", fontsize=8.5)
    draw_bw_box(ax, (4.4, 3.4), 3.8, 2.2, "Isolation Forest (Unsupervised)", "100 Isolation Trees Anomaly Estimator\ns(x, n) normalized in [0.0, 1.0]", fontsize=8.5)
    draw_bw_box(ax, (4.4, 0.4), 3.8, 2.2, "LightGBM LambdaRank (Supervised)", "Listwise NDCG Ranking Optimization\nPriority Rank in [1, 100]", fontsize=8.5)
    draw_bw_box(ax, (9.2, 1.8), 3.2, 2.4, "Fused Scored Alert", "Calculated Risk Score (0-100)\nConfidence Band: Low/Med/High\nRouted to LangGraph DAG", fontsize=8.5)

    draw_bw_arrow(ax, (3.5, 3.2), (4.4, 4.3))
    draw_bw_arrow(ax, (3.5, 2.8), (4.4, 1.5))
    draw_bw_arrow(ax, (8.2, 4.3), (9.2, 3.2))
    draw_bw_arrow(ax, (8.2, 1.5), (9.2, 2.8))

    plt.savefig(os.path.join(FIG_DIR, "fig6_3_dual_stage_ml.png"), bbox_inches='tight')
    plt.close()

# Fig 6.4: Neo4j Graph Schema (B&W)
def gen_fig6_4():
    fig, ax = plt.subplots(figsize=(9.5, 5.0))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')
    
    draw_bw_box(ax, (0.6, 3.8), 2.2, 1.5, ":User", "id: String\nrisk_score: Float", fontsize=8.5)
    draw_bw_box(ax, (3.9, 3.8), 2.2, 1.5, ":Host", "id: String\nblast_radius: Int", fontsize=8.5)
    draw_bw_box(ax, (7.2, 3.8), 2.2, 1.5, ":Alert", "id: UUID\nseverity: Enum", fontsize=8.5)
    
    draw_bw_box(ax, (3.9, 0.7), 2.2, 1.5, ":Technique", "id: 'T1078'\nname: Valid Accts", fontsize=8.5)
    draw_bw_box(ax, (7.2, 0.7), 2.2, 1.5, ":Tactic", "id: 'TA0008'\nname: Lateral Mvt", fontsize=8.5)
    
    draw_bw_arrow(ax, (2.8, 4.5), (3.9, 4.5), ":LOGGED_INTO")
    draw_bw_arrow(ax, (6.1, 4.5), (7.2, 4.5), ":AFFECTS")
    draw_bw_arrow(ax, (8.3, 3.8), (5.0, 2.2), ":USES")
    draw_bw_arrow(ax, (6.1, 1.4), (7.2, 1.4), ":PART_OF")
    
    plt.savefig(os.path.join(FIG_DIR, "fig6_4_neo4j_graph_schema.png"), bbox_inches='tight')
    plt.close()

# Fig 6.5: LangGraph Multi-Agent DAG (B&W)
def gen_fig6_5():
    fig, ax = plt.subplots(figsize=(11, 4.5))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 5)
    ax.axis('off')

    agents = [
        ((0.4, 1.4), 2.4, 2.2, "DetectAgent", "Evaluates Signatures\n& MITRE TTP Rules\nOpens Incident Case"),
        ((3.3, 1.4), 2.4, 2.2, "TriageAgent", "Verifies Context\nCalculates Anomaly\nConfidence: 0-100"),
        ((6.2, 1.4), 2.4, 2.2, "HuntAgent", "Warm-Lake Query\nES|QL / SPL Sweep\nDiscovers Lateral Nodes"),
        ((9.1, 1.4), 2.5, 2.2, "RespondAgent", "Formulates Gated Plan\nEvaluates Blast Radius\nDispatches Containment")
    ]

    for xy, w, h, t, s in agents:
        draw_bw_box(ax, xy, w, h, t, s, fontsize=8.5)

    draw_bw_arrow(ax, (2.8, 2.5), (3.3, 2.5), "Verified")
    draw_bw_arrow(ax, (5.7, 2.5), (6.2, 2.5), "Conf >= 30")
    draw_bw_arrow(ax, (8.6, 2.5), (9.1, 2.5), "Correlated")

    plt.savefig(os.path.join(FIG_DIR, "fig6_5_langgraph_dag.png"), bbox_inches='tight')
    plt.close()

# Fig 6.6: Blast-Radius Gating (B&W)
def gen_fig6_6():
    fig, ax = plt.subplots(figsize=(10, 4.5))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 5)
    ax.axis('off')
    
    draw_bw_box(ax, (0.4, 1.4), 2.5, 2.2, "Proposed Action\n(RespondAgent)", "Isolate Host / Subnet\nRevoke API Credentials\nEnforce Password Reset", fontsize=8.0)
    draw_bw_box(ax, (3.8, 2.7), 3.2, 1.8, "L0–L2 Mode", "Always Request Approval\nPost Slack/Web Modal\nWait for SOC Lead Sign-off", fontsize=8.0)
    draw_bw_box(ax, (3.8, 0.4), 3.2, 2.0, "L3–L4 Mode\n(Blast Radius Gated)", "B_r(e) <= Threshold: Auto-Exec\nB_r(e) > Threshold: Gated Modal", fontsize=8.0)
    draw_bw_box(ax, (7.9, 1.4), 2.6, 2.2, "Execution / Guard", "SOAR API Dispatch\nImmutable Ledger Trace\nTenant Isolation Guard", fontsize=8.0)
    
    draw_bw_arrow(ax, (2.9, 2.9), (3.8, 3.6), "L0-L2")
    draw_bw_arrow(ax, (2.9, 2.1), (3.8, 1.4), "L3-L4")
    draw_bw_arrow(ax, (7.0, 3.6), (7.9, 2.9), "Human Approval")
    draw_bw_arrow(ax, (7.0, 1.4), (7.9, 2.1), "Auto-Execute")
    
    plt.savefig(os.path.join(FIG_DIR, "fig6_6_blast_radius_gating.png"), bbox_inches='tight')
    plt.close()

# Fig 7.1: Benchmark Charts (B&W)
def gen_fig7_1():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.0))
    
    scenarios = ['Lateral Mvt', 'AWS Exfil', 'K8s Privesc', 'GitHub Token', 'Phishing', '200-Inc Corpus']
    noise_reduction = [95.8, 95.8, 96.8, 94.4, 96.3, 85.5]
    mttr_seconds = [0.82, 1.15, 0.96, 0.74, 1.30, 1.08]
    
    # Left Bar Chart: Noise Reduction (%)
    bars = ax1.bar(scenarios, noise_reduction, color="white", edgecolor="black", linewidth=1.5, hatch="//")
    ax1.set_ylabel('Alert Noise Reduction (%)', fontsize=8.5, fontweight='bold')
    ax1.set_ylim(0, 105)
    ax1.set_xticks(range(len(scenarios)))
    ax1.set_xticklabels(scenarios, rotation=35, ha='right', fontsize=7.5)
    for bar in bars:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2.0, yval + 1.5, f"{yval:.1f}%", ha='center', va='bottom', fontsize=7.2, fontweight='bold')
    ax1.set_title("Alert Noise Reduction (%)", fontsize=9.0, fontweight='bold')
    
    # Right Bar Chart: MTTR (Seconds)
    bars2 = ax2.bar(scenarios, mttr_seconds, color="white", edgecolor="black", linewidth=1.5, hatch="\\\\")
    ax2.set_ylabel('Mean Time to Remediate (s)', fontsize=8.5, fontweight='bold')
    ax2.set_ylim(0, 1.6)
    ax2.set_xticks(range(len(scenarios)))
    ax2.set_xticklabels(scenarios, rotation=35, ha='right', fontsize=7.5)
    for bar in bars2:
        yval = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2.0, yval + 0.03, f"{yval:.2f}s", ha='center', va='bottom', fontsize=7.2, fontweight='bold')
    ax2.set_title("Mean Time to Remediate (s)", fontsize=9.0, fontweight='bold')

    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, "fig7_1_benchmark_charts.png"), bbox_inches='tight')
    plt.close()

# Fig 7.2: Case Study Trace (B&W)
def gen_fig7_2():
    fig, ax = plt.subplots(figsize=(10, 4.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis('off')
    
    timeline = [
        (1.0, "09:30:00 UTC", "DETECT", "Okta Auth (NY, USA)\nTechnique T1078\nSeverity: High"),
        (3.5, "09:38:00 UTC", "TRIAGE", "Okta Auth (Russia)\nVelocity > 55k km/h\nConf: 83/100 (HIGH)"),
        (6.0, "09:38:00.3 UTC", "HUNT", "ES|QL Query Sweep\nFound: Cloud Download\nfrom IP 203.0.113.50"),
        (8.5, "09:38:00.8 UTC", "RESPOND", "Blast Radius: Safe (4)\nRevoked Okta Tokens\nPW Reset & Slack Post")
    ]
    
    ax.axhline(2.5, color="black", lw=2, zorder=1)
    
    for x, time_str, stage, desc in timeline:
        ax.plot(x, 2.5, 'o', color="black", markersize=10, zorder=2)
        ax.plot(x, 2.5, 'o', color="white", markersize=6, zorder=3)
        ax.text(x, 2.9, f"{stage}\n{time_str}", ha='center', va='bottom', fontsize=7.8, fontweight='bold', color='black')
        draw_bw_box(ax, (x - 1.1, 0.4), 2.2, 1.4, desc, "", fontsize=7.2)
        ax.plot([x, x], [2.5, 1.8], color="black", ls="--", lw=1)
        
    plt.savefig(os.path.join(FIG_DIR, "fig7_2_case_study_trace.png"), bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    gen_fig1_1()
    gen_fig1_2()
    gen_fig2_1()
    gen_fig3_1()
    gen_fig4_1()
    gen_fig4_6()
    gen_fig6_1()
    gen_fig6_2()
    gen_fig6_3()
    gen_fig6_4()
    gen_fig6_5()
    gen_fig6_6()
    gen_fig7_1()
    gen_fig7_2()
    print("All figures successfully re-generated with clean padding, zero overlap, and no redundant titles.")
