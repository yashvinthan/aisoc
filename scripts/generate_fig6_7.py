"""
Generate authentic Next.js SOC Workbench UI visualization for Figure 6.7.
"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

FIG_DIR = r"c:\Users\yashv\dev\work in progress\mini project\AiSOC\docs\figures"
os.makedirs(FIG_DIR, exist_ok=True)

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10
plt.rcParams['figure.dpi'] = 300

def gen_fig6_7():
    fig, ax = plt.subplots(figsize=(11, 6.2))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8.5)
    ax.axis('off')

    # Background Window
    rect_main = patches.FancyBboxPatch((0.2, 0.2), 13.6, 8.0, boxstyle="round,pad=0.02,rounding_size=0.08", facecolor="#0B0F19", edgecolor="#334155", lw=1.5)
    ax.add_patch(rect_main)

    # Top Header Bar
    rect_hdr = patches.Rectangle((0.2, 7.6), 13.6, 0.6, facecolor="#111827", edgecolor="none")
    ax.add_patch(rect_hdr)
    ax.text(0.6, 7.9, "AiSOC | Autonomous Security Operations Console", fontsize=10, fontweight='bold', color="#F8FAFC", va='center')
    ax.text(12.8, 7.9, "● Live Stream (WS: 4ms)", fontsize=8.5, fontweight='bold', color="#10B981", va='center')

    # Left Pane: Real-Time Alert Stream (Width: 6.2)
    rect_left = patches.Rectangle((0.4, 0.4), 6.0, 7.0, facecolor="#111827", edgecolor="#1F2937", lw=1)
    ax.add_patch(rect_left)
    ax.text(0.6, 7.1, "ACTIVE INCIDENT QUEUE (FUSED)", fontsize=9, fontweight='bold', color="#94A3B8")

    alerts = [
        ("INC-8492", "Lateral Movement / Impossible Travel", "CRITICAL", "Conf: 83%", "#EF4444", 6.2, True),
        ("INC-8491", "AWS IAM Long-Lived Key Exfiltration", "HIGH", "Conf: 94%", "#F59E0B", 4.9, False),
        ("INC-8490", "Kubernetes Container Escape (cluster-admin)", "CRITICAL", "Conf: 98%", "#EF4444", 3.6, False),
        ("INC-8489", "GitHub PAT Token Mass Repository Clone", "HIGH", "Conf: 100%", "#F59E0B", 2.3, False),
        ("INC-8488", "Spear-Phishing Encoded PowerShell One-Liner", "HIGH", "Conf: 92%", "#F59E0B", 1.0, False),
    ]

    for inc_id, title, sev, conf, color, y, selected in alerts:
        bg_col = "#1E293B" if selected else "#0F172A"
        border_col = "#6366F1" if selected else "#334155"
        card = patches.FancyBboxPatch((0.6, y), 5.6, 1.1, boxstyle="round,pad=0.02,rounding_size=0.04", facecolor=bg_col, edgecolor=border_col, lw=1.2)
        ax.add_patch(card)
        ax.text(0.8, y + 0.75, f"{inc_id} • {title}", fontsize=8, fontweight='bold', color="#F8FAFC")
        
        # Badges
        badge_sev = patches.Rectangle((0.8, y + 0.2), 1.2, 0.35, facecolor=color, edgecolor="none")
        ax.add_patch(badge_sev)
        ax.text(1.4, y + 0.37, sev, fontsize=6.5, fontweight='bold', color="white", ha='center', va='center')
        
        badge_conf = patches.Rectangle((2.2, y + 0.2), 1.2, 0.35, facecolor="#312E81", edgecolor="#4F46E5", lw=0.8)
        ax.add_patch(badge_conf)
        ax.text(2.8, y + 0.37, conf, fontsize=6.5, fontweight='bold', color="#C7D2FE", ha='center', va='center')

    # Right Pane: Two-Pane Investigation Rail (Width: 7.0)
    rect_right = patches.Rectangle((6.6, 0.4), 7.0, 7.0, facecolor="#0F172A", edgecolor="#1F2937", lw=1)
    ax.add_patch(rect_right)
    ax.text(6.8, 7.1, "INVESTIGATION RAIL: INC-8492 (LATERAL MOVEMENT)", fontsize=9, fontweight='bold', color="#818CF8")

    # CoT Agent Ledger Box
    box_ledger = patches.FancyBboxPatch((6.8, 4.3), 6.6, 2.6, boxstyle="round,pad=0.02,rounding_size=0.04", facecolor="#1E293B", edgecolor="#334155", lw=1)
    ax.add_patch(box_ledger)
    ax.text(7.0, 6.6, "AI AGENT INVESTIGATION LEDGER (CHAIN-OF-THOUGHT)", fontsize=7.5, fontweight='bold', color="#38BDF8")
    
    steps = [
        "1. DetectAgent: Ingested Okta Class 3001 | Extracted MITRE T1078 (Valid Accounts)",
        "2. TriageAgent: NY -> St. Petersburg (7,500km / 8min > 55,000 km/h) | Conf: 83%",
        "3. HuntAgent: Executed ES|QL warm-lake sweep | Found IP 203.0.113.50 AWS S3 sync",
        "4. RespondAgent: Formulated 4-step containment plan | Evaluated Blast Radius: 4"
    ]
    for idx, s in enumerate(steps):
        ax.text(7.0, 6.1 - idx * 0.45, s, fontsize=7, color="#E2E8F0")

    # Action Proposal / Blast-Radius Safety Gate
    box_action = patches.FancyBboxPatch((6.8, 0.6), 6.6, 3.5, boxstyle="round,pad=0.02,rounding_size=0.04", facecolor="#1E293B", edgecolor="#10B981", lw=1.2)
    ax.add_patch(box_action)
    ax.text(7.0, 3.8, "PROPOSED CONTAINMENT PLAYBOOK (L3 CONDITIONAL AUTONOMOUS)", fontsize=7.5, fontweight='bold', color="#34D399")
    
    ax.text(7.0, 3.2, "• Action 1: Revoke Active Okta Session Tokens (`POST /api/v1/users/{id}/sessions`)", fontsize=7, color="#F8FAFC")
    ax.text(7.0, 2.6, "• Action 2: Trigger Temporary Active Directory Password Reset", fontsize=7, color="#F8FAFC")
    ax.text(7.0, 2.0, "• Action 3: Isolate Workstation `HOST-FIN-09` via CrowdStrike Falcon API", fontsize=7, color="#F8FAFC")
    ax.text(7.0, 1.4, "• Action 4: Post Executive Dossier to `#soc-incident-response` on Slack", fontsize=7, color="#F8FAFC")

    # Approval Status Pill
    pill = patches.FancyBboxPatch((7.0, 0.75), 6.2, 0.45, boxstyle="round,pad=0.02,rounding_size=0.03", facecolor="#064E3B", edgecolor="#059669")
    ax.add_patch(pill)
    ax.text(10.1, 0.97, "BLAST RADIUS VALIDATED (B_r = 4 <= 5) • AUTONOMOUS EXECUTION CONFIRMED", fontsize=7, fontweight='bold', color="#6EE7B7", ha='center', va='center')

    p = os.path.join(FIG_DIR, "fig6_7_workbench_interface.png")
    plt.savefig(p, bbox_inches='tight', facecolor='#0B0F19')
    plt.close()
    print("Generated authentic Fig 6.7:", p)

if __name__ == "__main__":
    gen_fig6_7()
