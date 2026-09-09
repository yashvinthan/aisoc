import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

os.makedirs('docs/ppt_figures', exist_ok=True)

# Color Palette Matching PPT Dark Theme
BG_DARK = '#0f172a'       # Slate 900
BG_CARD = '#1e293b'       # Slate 800
BG_CARD_LIGHT = '#334155' # Slate 700
ACCENT_CYAN = '#2dd4bf'   # Teal 400
ACCENT_BLUE = '#38bdf8'   # Sky 400
ACCENT_AMBER = '#fbbf24'  # Amber 400
ACCENT_ROSE = '#f43f5e'   # Rose 500
ACCENT_GREEN = '#4ade80'  # Green 400
TEXT_MAIN = '#f8fafc'     # Slate 50
TEXT_MUTED = '#94a3b8'    # Slate 400
BORDER_COL = '#475569'    # Slate 600

def set_dark_style(fig, ax):
    fig.patch.set_facecolor(BG_DARK)
    ax.set_facecolor(BG_DARK)
    ax.axis('off')

# =============================================================================
# 1. Existing Methodology Flowchart (ppt_fig_existing_methodology.png)
# =============================================================================
def draw_existing_methodology():
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    set_dark_style(fig, ax)
    
    # Title Banner
    ax.text(5, 5.2, "TRADITIONAL 3-TIER SOC WORKFLOW & LATENCY BOTTLENECKS", 
            ha='center', va='center', color=ACCENT_CYAN, fontsize=13, fontweight='bold')
    
    stages = [
        ("Raw Telemetry Silos\n(EDR, Syslog, Firewalls)\n10,000+ Alerts / Day", 1.2, 3.2, ACCENT_ROSE, "Unnormalized Ingest"),
        ("Static Rule SIEM\n(Threshold & Regex)\n83% Benign Noise", 3.7, 3.2, ACCENT_AMBER, "High False Positives"),
        ("Tier-1 Analyst Triage\n(Manual Copy-Paste)\n4 - 8 Hours Delay", 6.2, 3.2, ACCENT_BLUE, "Analyst Fatigue"),
        ("Tier-3 Incident Response\n(Manual Host Isolation)\n4.3 Days Avg MTTR", 8.7, 3.2, ACCENT_ROSE, "Outage Risk")
    ]
    
    for title, x, y, col, sub in stages:
        # Card Box
        rect = patches.FancyBboxPatch((x-1.0, y-1.0), 2.0, 2.0, boxstyle="round,pad=0.1",
                                      facecolor=BG_CARD, edgecolor=col, linewidth=2)
        ax.add_patch(rect)
        # Text
        ax.text(x, y+0.2, title, ha='center', va='center', color=TEXT_MAIN, fontsize=9.5, fontweight='bold', linespacing=1.2)
        # Subtitle pill
        sub_rect = patches.FancyBboxPatch((x-0.85, y-0.8), 1.7, 0.35, boxstyle="round,pad=0.05",
                                          facecolor=BG_CARD_LIGHT, edgecolor=col, linewidth=1)
        ax.add_patch(sub_rect)
        ax.text(x, y-0.62, sub, ha='center', va='center', color=col, fontsize=8, fontweight='bold')
        
    # Arrows
    for x in [2.3, 4.8, 7.3]:
        ax.annotate('', xy=(x+0.35, 3.2), xytext=(x-0.05, 3.2),
                    arrowprops=dict(arrowstyle="->", color=ACCENT_CYAN, lw=2.5))
        
    # Bottom Callout Banner
    bot_rect = patches.FancyBboxPatch((0.5, 0.4), 9.0, 1.1, boxstyle="round,pad=0.1",
                                     facecolor='#3b1820', edgecolor=ACCENT_ROSE, linewidth=1.5)
    ax.add_patch(bot_rect)
    ax.text(5, 1.15, "Critical Flaws: 83% Noise Ratio | 103 Hours Dwell Time | No Graph Context | Human Error",
            ha='center', va='center', color='#fca5a5', fontsize=10.5, fontweight='bold')
    ax.text(5, 0.7, "Manual correlation across disconnected portals introduces severe investigation delays and missed zero-day attacks.",
            ha='center', va='center', color=TEXT_MUTED, fontsize=9)

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5.7)
    plt.tight_layout()
    plt.savefig('docs/ppt_figures/ppt_fig_existing_methodology.png', facecolor=BG_DARK, bbox_inches='tight')
    plt.close()

# =============================================================================
# 2. System Architecture of Proposed Methodology (ppt_fig_system_architecture.png)
# =============================================================================
def draw_system_architecture():
    fig, ax = plt.subplots(figsize=(11, 6.2), dpi=300)
    set_dark_style(fig, ax)
    
    ax.text(5.5, 5.8, "AiSOC END-TO-END AUTONOMOUS MULTI-AGENT ARCHITECTURE", 
            ha='center', va='center', color=ACCENT_CYAN, fontsize=14, fontweight='bold')
    
    # Layer 1: Connectors & Ingest
    l1_box = patches.FancyBboxPatch((0.5, 3.8), 2.2, 1.6, boxstyle="round,pad=0.08",
                                    facecolor=BG_CARD, edgecolor=ACCENT_BLUE, linewidth=2)
    ax.add_patch(l1_box)
    ax.text(1.6, 5.1, "1. INGESTION LAYER", ha='center', color=ACCENT_BLUE, fontsize=10, fontweight='bold')
    ax.text(1.6, 4.4, "• 16+ Connectors\n• Kafka Streaming\n• OCSF Normalization\n• DetectAgent", 
            ha='center', va='center', color=TEXT_MAIN, fontsize=8.5, linespacing=1.2)
    
    # Layer 2: ML Triage & Enrichment
    l2_box = patches.FancyBboxPatch((3.1, 3.8), 2.2, 1.6, boxstyle="round,pad=0.08",
                                    facecolor=BG_CARD, edgecolor=ACCENT_CYAN, linewidth=2)
    ax.add_patch(l2_box)
    ax.text(4.2, 5.1, "2. ML TRIAGE LAYER", ha='center', color=ACCENT_CYAN, fontsize=10, fontweight='bold')
    ax.text(4.2, 4.4, "• Bloom Filter IOCs\n• Isolation Forest\n• LambdaRank ML\n• TriageAgent (89% Filter)", 
            ha='center', va='center', color=TEXT_MAIN, fontsize=8.5, linespacing=1.2)

    # Layer 3: Knowledge Graph & Hunting
    l3_box = patches.FancyBboxPatch((5.7, 3.8), 2.2, 1.6, boxstyle="round,pad=0.08",
                                    facecolor=BG_CARD, edgecolor=ACCENT_AMBER, linewidth=2)
    ax.add_patch(l3_box)
    ax.text(6.8, 5.1, "3. KNOWLEDGE GRAPH", ha='center', color=ACCENT_AMBER, fontsize=10, fontweight='bold')
    ax.text(6.8, 4.4, "• Neo4j Real-Time Graph\n• 17 Nodes / 14 Edges\n• Attack Path Pivoting\n• HuntAgent (/hunt)", 
            ha='center', va='center', color=TEXT_MAIN, fontsize=8.5, linespacing=1.2)

    # Layer 4: Blast Radius & Containment
    l4_box = patches.FancyBboxPatch((8.3, 3.8), 2.2, 1.6, boxstyle="round,pad=0.08",
                                    facecolor=BG_CARD, edgecolor=ACCENT_ROSE, linewidth=2)
    ax.add_patch(l4_box)
    ax.text(9.4, 5.1, "4. RESPONSE & GATING", ha='center', color=ACCENT_ROSE, fontsize=10, fontweight='bold')
    ax.text(9.4, 4.4, "• Blast-Radius Gating\n• L0–L4 Maturity Model\n• SOAR Playbooks\n• RespondAgent", 
            ha='center', va='center', color=TEXT_MAIN, fontsize=8.5, linespacing=1.2)

    # Connecting Arrows across top layers
    for x in [2.75, 5.35, 7.95]:
        ax.annotate('', xy=(x+0.3, 4.6), xytext=(x-0.05, 4.6),
                    arrowprops=dict(arrowstyle="->", color=ACCENT_CYAN, lw=2.5))

    # Bottom Subsystems: Data Stores & Interface
    # Left Store: Neo4j + PostgreSQL + Redis
    store_box = patches.FancyBboxPatch((0.5, 1.0), 4.8, 2.3, boxstyle="round,pad=0.08",
                                       facecolor=BG_CARD, edgecolor=BORDER_COL, linewidth=1.5)
    ax.add_patch(store_box)
    ax.text(2.9, 3.0, "CORE PERSISTENCE & SECURITY FABRIC", ha='center', color=ACCENT_BLUE, fontsize=10, fontweight='bold')
    ax.text(2.9, 2.0, "• PostgreSQL 16 (Async SQLAlchemy) - Cases, Alerts, Telemetry\n• Redis Pub/Sub & Memory Cache - Real-Time Events & IOCs\n• Neo4j Graph DB - Entity Relationships & Graph Traversal\n• Fernet AES-128 Encrypted Credential Vault (BYOK)", 
            ha='center', va='center', color=TEXT_MAIN, fontsize=8.5, linespacing=1.3)

    # Right Interface: Web Console & LangGraph Agent Engine
    ui_box = patches.FancyBboxPatch((5.7, 1.0), 4.8, 2.3, boxstyle="round,pad=0.08",
                                    facecolor=BG_CARD, edgecolor=ACCENT_GREEN, linewidth=1.5)
    ax.add_patch(ui_box)
    ax.text(8.1, 3.0, "ANALYST CONSOLE & AGENT DAG ENGINE", ha='center', color=ACCENT_GREEN, fontsize=10, fontweight='bold')
    ax.text(8.1, 2.0, "• Next.js 14 Web Workbench & Investigation Rail (SSR)\n• LangGraph Multi-Agent Cyclic State Machine\n• Local Sovereign LLMs (Ollama) & Enterprise APIs (LiteLLM)\n• Immutable Chain-of-Thought Audit Ledger & Human Sign-off", 
            ha='center', va='center', color=TEXT_MAIN, fontsize=8.5, linespacing=1.3)

    # Vertical Connecting Arrows
    ax.annotate('', xy=(2.9, 3.35), xytext=(2.9, 3.75), arrowprops=dict(arrowstyle="<->", color=ACCENT_BLUE, lw=2))
    ax.annotate('', xy=(8.1, 3.35), xytext=(8.1, 3.75), arrowprops=dict(arrowstyle="<->", color=ACCENT_GREEN, lw=2))

    # Bottom Footer Pill
    foot_rect = patches.FancyBboxPatch((0.5, 0.2), 10.0, 0.55, boxstyle="round,pad=0.05",
                                      facecolor='#0b3b32', edgecolor=ACCENT_CYAN, linewidth=1.2)
    ax.add_patch(foot_rect)
    ax.text(5.5, 0.47, "Outcome: Sub-4 Minute MTTR | 89.4% False Positive Suppression | 100% Deterministic Safety Gating",
            ha='center', va='center', color='#5eead4', fontsize=9.5, fontweight='bold')

    ax.set_xlim(0, 11)
    ax.set_ylim(0, 6.2)
    plt.tight_layout()
    plt.savefig('docs/ppt_figures/ppt_fig_system_architecture.png', facecolor=BG_DARK, bbox_inches='tight')
    plt.close()

# =============================================================================
# 3. Module 1: Ingestion & OCSF Normalization (ppt_fig_module1_ingest.png)
# =============================================================================
def draw_module1_ingest():
    fig, ax = plt.subplots(figsize=(10, 5.2), dpi=300)
    set_dark_style(fig, ax)
    
    ax.text(5, 4.9, "MODULE 1: TELEMETRY INGESTION & OCSF NORMALIZATION", 
            ha='center', va='center', color=ACCENT_BLUE, fontsize=13, fontweight='bold')
    
    boxes = [
        ("Raw Vendor Logs\n(Syslog, AWS GuardDuty,\nOkta, Zeek, CrowdStrike)", 1.5, 2.7, ACCENT_ROSE),
        ("Kafka Broker & Ingest\n(Partitioned Topics,\n10,000+ Events/Sec)", 4.0, 2.7, ACCENT_AMBER),
        ("OCSF Schema Normalizer\n(Unified Security Classes,\nJSON Schema Validation)", 6.5, 2.7, ACCENT_CYAN),
        ("Standardized Stream\n(To Dual-Stage ML &\nNeo4j Knowledge Graph)", 9.0, 2.7, ACCENT_GREEN)
    ]
    
    for txt, x, y, col in boxes:
        rect = patches.FancyBboxPatch((x-1.0, y-1.0), 2.0, 2.0, boxstyle="round,pad=0.08",
                                      facecolor=BG_CARD, edgecolor=col, linewidth=2)
        ax.add_patch(rect)
        ax.text(x, y, txt, ha='center', va='center', color=TEXT_MAIN, fontsize=9, fontweight='bold', linespacing=1.2)
        
    for x in [2.55, 5.05, 7.55]:
        ax.annotate('', xy=(x+0.4, 2.7), xytext=(x-0.05, 2.7),
                    arrowprops=dict(arrowstyle="->", color=ACCENT_BLUE, lw=2.5))
        
    # Summary info box
    bot_box = patches.FancyBboxPatch((0.5, 0.3), 9.0, 0.9, boxstyle="round,pad=0.08",
                                    facecolor=BG_CARD, edgecolor=BORDER_COL, linewidth=1.5)
    ax.add_patch(bot_box)
    ax.text(5, 0.75, "Key Metric: 16+ First-Party Connectors | Zero Data Loss | Vendor-Agnostic Schema Interoperability",
            ha='center', va='center', color=ACCENT_CYAN, fontsize=10, fontweight='bold')

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5.3)
    plt.tight_layout()
    plt.savefig('docs/ppt_figures/ppt_fig_module1_ingest.png', facecolor=BG_DARK, bbox_inches='tight')
    plt.close()

# =============================================================================
# 4. Module 2: Dual-Stage ML & Threat Intel (ppt_fig_module2_ml_triage.png)
# =============================================================================
def draw_module2_ml_triage():
    fig, ax = plt.subplots(figsize=(10, 5.2), dpi=300)
    set_dark_style(fig, ax)
    
    ax.text(5, 4.9, "MODULE 2: DUAL-STAGE ML TRIAGE & THREAT INTEL ENGINE", 
            ha='center', va='center', color=ACCENT_CYAN, fontsize=13, fontweight='bold')

    boxes = [
        ("Normalized Events\n(10,000+ EPS)", 1.2, 2.7, ACCENT_BLUE),
        ("In-Memory Bloom Filter\n(O(1) Threat Intel\n50k IOC Lookup/s)", 3.7, 2.7, ACCENT_CYAN),
        ("Stage-1: Isolation Forest\n(Anomaly Filtering\nSuppresses 89.4% Noise)", 6.2, 2.7, ACCENT_AMBER),
        ("Stage-2: LambdaRank\n(Learning-to-Rank\nPriority 0-100 Score)", 8.7, 2.7, ACCENT_GREEN)
    ]
    
    for txt, x, y, col in boxes:
        rect = patches.FancyBboxPatch((x-1.0, y-1.0), 2.0, 2.0, boxstyle="round,pad=0.08",
                                      facecolor=BG_CARD, edgecolor=col, linewidth=2)
        ax.add_patch(rect)
        ax.text(x, y, txt, ha='center', va='center', color=TEXT_MAIN, fontsize=9, fontweight='bold', linespacing=1.2)
        
    for x in [2.25, 4.75, 7.25]:
        ax.annotate('', xy=(x+0.4, 2.7), xytext=(x-0.05, 2.7),
                    arrowprops=dict(arrowstyle="->", color=ACCENT_CYAN, lw=2.5))
        
    bot_box = patches.FancyBboxPatch((0.5, 0.3), 9.0, 0.9, boxstyle="round,pad=0.08",
                                    facecolor=BG_CARD, edgecolor=BORDER_COL, linewidth=1.5)
    ax.add_patch(bot_box)
    ax.text(5, 0.75, "Mathematical Foundation: s(x, n) = 2^(-E(h(x))/c(n)) | λ_ij Optimization | Zero False Negatives",
            ha='center', va='center', color=ACCENT_GREEN, fontsize=10, fontweight='bold')

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5.3)
    plt.tight_layout()
    plt.savefig('docs/ppt_figures/ppt_fig_module2_ml_triage.png', facecolor=BG_DARK, bbox_inches='tight')
    plt.close()

# =============================================================================
# 5. Module 3: Knowledge Graph & Threat Hunting (ppt_fig_module3_graph_hunt.png)
# =============================================================================
def draw_module3_graph_hunt():
    fig, ax = plt.subplots(figsize=(10, 5.2), dpi=300)
    set_dark_style(fig, ax)
    
    ax.text(5, 4.9, "MODULE 3: REAL-TIME KNOWLEDGE GRAPH & THREAT HUNTING", 
            ha='center', va='center', color=ACCENT_AMBER, fontsize=13, fontweight='bold')

    # Graph Entities Visualization
    nodes = [
        ("User\n(Identity)", 1.5, 3.2, ACCENT_BLUE),
        ("Process\n(PID: 4120)", 4.0, 3.2, ACCENT_AMBER),
        ("Host / Asset\n(DC-01)", 6.5, 3.2, ACCENT_ROSE),
        ("Ext IP / C2\n(198.51.100.4)", 9.0, 3.2, ACCENT_CYAN)
    ]
    
    for txt, x, y, col in nodes:
        circle = patches.Circle((x, y), 0.75, facecolor=BG_CARD, edgecolor=col, linewidth=2.5)
        ax.add_patch(circle)
        ax.text(x, y, txt, ha='center', va='center', color=TEXT_MAIN, fontsize=8.5, fontweight='bold', linespacing=1.2)
        
    # Edge labels
    edges = [
        (1.5+0.75, 4.0-0.75, "AUTHENTICATED_TO", ACCENT_BLUE),
        (4.0+0.75, 6.5-0.75, "SPAWNED_ON", ACCENT_AMBER),
        (6.5+0.75, 9.0-0.75, "NETWORK_EGRESS", ACCENT_CYAN)
    ]
    for x1, x2, lbl, col in edges:
        ax.annotate('', xy=(x2, 3.2), xytext=(x1, 3.2),
                    arrowprops=dict(arrowstyle="->", color=col, lw=2.5))
        ax.text((x1+x2)/2, 3.45, lbl, ha='center', va='center', color=col, fontsize=7.5, fontweight='bold')

    bot_box = patches.FancyBboxPatch((0.5, 0.4), 9.0, 1.2, boxstyle="round,pad=0.08",
                                    facecolor=BG_CARD, edgecolor=BORDER_COL, linewidth=1.5)
    ax.add_patch(bot_box)
    ax.text(5, 1.15, "Neo4j Streaming Graph: 17 Node Types | 14 Edge Relationships | MITRE ATT&CK Mapping",
            ha='center', va='center', color=ACCENT_AMBER, fontsize=10, fontweight='bold')
    ax.text(5, 0.7, "Enables HuntAgent to execute natural-language queries (/hunt) translating to multi-hop Cypher patterns.",
            ha='center', va='center', color=TEXT_MUTED, fontsize=9)

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5.3)
    plt.tight_layout()
    plt.savefig('docs/ppt_figures/ppt_fig_module3_graph_hunt.png', facecolor=BG_DARK, bbox_inches='tight')
    plt.close()

# =============================================================================
# 6. Module 4: Blast-Radius Gated Response (ppt_fig_module4_blast_radius.png)
# =============================================================================
def draw_module4_blast_radius():
    fig, ax = plt.subplots(figsize=(10, 5.2), dpi=300)
    set_dark_style(fig, ax)
    
    ax.text(5, 4.9, "MODULE 4: BLAST-RADIUS GATED RESPONSE & SOAR STUDIO", 
            ha='center', va='center', color=ACCENT_ROSE, fontsize=13, fontweight='bold')

    tiers = [
        ("L0: Read-Only\n(Telemetry Query,\nZero Risk)", 1.2, 2.7, ACCENT_BLUE, "Auto-Exec"),
        ("L1: Low Impact\n(Enrichment,\nFlush Cache)", 3.7, 2.7, ACCENT_GREEN, "Auto-Exec"),
        ("L2: Moderate\n(Temp IP Block,\nRevoke Session)", 6.2, 2.7, ACCENT_AMBER, "Policy Gate"),
        ("L3/L4: High Risk\n(Host Isolation,\nRevoke DC Key)", 8.7, 2.7, ACCENT_ROSE, "Human Sign-off")
    ]
    
    for txt, x, y, col, tag in tiers:
        rect = patches.FancyBboxPatch((x-1.0, y-1.0), 2.0, 2.0, boxstyle="round,pad=0.08",
                                      facecolor=BG_CARD, edgecolor=col, linewidth=2)
        ax.add_patch(rect)
        ax.text(x, y+0.2, txt, ha='center', va='center', color=TEXT_MAIN, fontsize=9, fontweight='bold', linespacing=1.2)
        
        tag_rect = patches.FancyBboxPatch((x-0.8, y-0.8), 1.6, 0.35, boxstyle="round,pad=0.05",
                                          facecolor=BG_CARD_LIGHT, edgecolor=col, linewidth=1)
        ax.add_patch(tag_rect)
        ax.text(x, y-0.62, tag, ha='center', va='center', color=col, fontsize=8, fontweight='bold')

    for x in [2.25, 4.75, 7.25]:
        ax.annotate('', xy=(x+0.4, 2.7), xytext=(x-0.05, 2.7),
                    arrowprops=dict(arrowstyle="->", color=ACCENT_ROSE, lw=2.5))

    bot_box = patches.FancyBboxPatch((0.5, 0.3), 9.0, 0.9, boxstyle="round,pad=0.08",
                                    facecolor=BG_CARD, edgecolor=BORDER_COL, linewidth=1.5)
    ax.add_patch(bot_box)
    ax.text(5, 0.75, "Safety Formula: B(Action) = Σ [w_k * Impact(Asset_k)] | Cryptographic Tamper-Proof Audit Ledger",
            ha='center', va='center', color=ACCENT_ROSE, fontsize=10, fontweight='bold')

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5.3)
    plt.tight_layout()
    plt.savefig('docs/ppt_figures/ppt_fig_module4_blast_radius.png', facecolor=BG_DARK, bbox_inches='tight')
    plt.close()

# =============================================================================
# 7. Experimental Results Charts (ppt_fig_experimental_results.png)
# =============================================================================
def draw_experimental_results():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5.0), dpi=300)
    fig.patch.set_facecolor(BG_DARK)
    
    # Chart 1: MTTR Comparison
    ax1.set_facecolor(BG_CARD)
    categories = ['Traditional SIEM', 'Legacy SOAR', 'AiSOC (Proposed)']
    mttr_values = [103.2, 14.5, 0.063] # in hours (0.063 hrs = 3.8 mins)
    colors = [ACCENT_ROSE, ACCENT_AMBER, ACCENT_CYAN]
    
    bars = ax1.bar(categories, mttr_values, color=colors, width=0.55, edgecolor=BORDER_COL, linewidth=1.5)
    ax1.set_yscale('log')
    ax1.set_ylabel('Mean Time to Respond (Hours - Log Scale)', color=TEXT_MAIN, fontsize=9.5, fontweight='bold')
    ax1.set_title('Mean Time to Respond (MTTR) Comparison', color=ACCENT_CYAN, fontsize=11, fontweight='bold', pad=12)
    ax1.tick_params(colors=TEXT_MUTED, labelsize=8.5)
    for spine in ax1.spines.values():
        spine.set_color(BORDER_COL)
    
    # Direct Value Annotations
    ax1.text(0, 120, '103.2 hrs\n(4.3 days)', ha='center', color=ACCENT_ROSE, fontweight='bold', fontsize=8.5)
    ax1.text(1, 18, '14.5 hrs', ha='center', color=ACCENT_AMBER, fontweight='bold', fontsize=8.5)
    ax1.text(2, 0.08, '3.8 mins\n(1,600x Faster)', ha='center', color=ACCENT_CYAN, fontweight='bold', fontsize=8.5)

    # Chart 2: Alert Reduction & Accuracy Metrics
    ax2.set_facecolor(BG_CARD)
    metrics = ['Alert Noise\nReduction', 'MITRE ATT&CK\nAccuracy', 'Investigation\nCompleteness', 'Zero-Outage\nSafety Rate']
    scores = [89.4, 96.4, 94.8, 100.0]
    m_colors = [ACCENT_GREEN, ACCENT_BLUE, ACCENT_AMBER, ACCENT_CYAN]
    
    bars2 = ax2.bar(metrics, scores, color=m_colors, width=0.55, edgecolor=BORDER_COL, linewidth=1.5)
    ax2.set_ylim(0, 115)
    ax2.set_ylabel('Benchmark Score (%)', color=TEXT_MAIN, fontsize=9.5, fontweight='bold')
    ax2.set_title('Empirical System Performance Metrics (200 Incidents)', color=ACCENT_GREEN, fontsize=11, fontweight='bold', pad=12)
    ax2.tick_params(colors=TEXT_MUTED, labelsize=8.5)
    for spine in ax2.spines.values():
        spine.set_color(BORDER_COL)

    for bar, score in zip(bars2, scores):
        yval = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2.0, yval + 2.5, f'{score:.1f}%', ha='center', va='bottom', color=TEXT_MAIN, fontweight='bold', fontsize=9)

    plt.tight_layout()
    plt.savefig('docs/ppt_figures/ppt_fig_experimental_results.png', facecolor=BG_DARK, bbox_inches='tight')
    plt.close()

if __name__ == '__main__':
    draw_existing_methodology()
    draw_system_architecture()
    draw_module1_ingest()
    draw_module2_ml_triage()
    draw_module3_graph_hunt()
    draw_module4_blast_radius()
    draw_experimental_results()
    print("SUCCESS: All 7 PPT-matched diagrams generated in 'docs/ppt_figures/'")
