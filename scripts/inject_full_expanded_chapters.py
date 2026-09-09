"""
Direct injector to expand all chapter generator scripts to achieve >= 15,200 words.
"""

ch3_full = '''"""
Chapter 3 generator with deep analytical comparison and comprehensive existing SOC failure mode analysis.
"""
import os
from docx.shared import Inches

def generate_chapter_3(add_p, add_ch_heading, add_sec_heading, add_subsec_heading, add_code, add_table, add_fig, fig_dir):
    add_ch_heading("CHAPTER 3\\nEXISTING SYSTEM")
    
    add_sec_heading("3.1 Overview of Current Enterprise SOC Workflows")
    add_p("The operational paradigm of contemporary enterprise Security Operations Centers (SOCs) relies on a rigid, multi-tiered human hierarchy structured around three primary escalation levels: Tier-1 Triage Analysts, Tier-2 Incident Responders, and Tier-3 Advanced Threat Hunters and SOC Leads.")
    add_p("Under this established operational model, raw security events generated across enterprise infrastructure—including endpoints, cloud environments, identity providers, and network boundaries—are collected and forwarded to a centralized SIEM or data lake repository. Detection engineering teams author static correlation rules, threshold queries, and regular expression patterns that continuously evaluate incoming log streams.")
    add_p("When a rule condition evaluates to true, an alert is generated and deposited into a shared triage queue. Tier-1 analysts manually review each alert sequentially, inspecting raw log fields, copying IOCs into external reputation databases, querying Active Directory to determine affected user identities, and manually deciding whether the alert represents a false positive or warrants escalation to Tier-2.")
    
    # Figure 3.1: Traditional SOC Funnel
    add_fig(os.path.join(fig_dir, "fig3_1_traditional_soc_funnel.png"), "Figure 3.1: Traditional Multi-Tier SOC Operational Funnel and Hand-off Delays", 5.8)

    add_p("If an alert is escalated, Tier-2 responders manually construct forensic queries in vendor-specific languages (e.g., Splunk SPL, Microsoft KQL) to determine the scope of compromise. If containment is deemed necessary, responders manually log into separate administrative portals (EDR consoles, firewall management consoles, identity provider admin dashboards) to execute manual containment actions.")
    add_p("This multi-tiered human workflow introduces severe operational friction. Because alerts must be manually reviewed, enriched, and escalated through successive human tiers, delays compound exponentially. A typical high-severity alert sits in unassigned queues for an average of 15 to 45 minutes before initial human inspection (Mean Time to Acknowledge - MTTA), and takes an additional 45 to 60 minutes to reach containment (Mean Time to Remediate - MTTR).")

    add_sec_heading("3.2 Architectural Bottlenecks and Deficiencies")
    add_p("The traditional multi-tiered SOC model suffers from four foundational architectural deficiencies that critically undermine modern enterprise cyber defense:")
    add_p("1. Semantic Context Fragmentation: Disparate security tools operate in complete isolation. An EDR alert concerning a suspicious process execution on a developer laptop is completely disconnected from an Okta login alert from an unfamiliar IP address and an AWS CloudTrail record indicating S3 bucket policy modification. Analysts must manually perform cognitive joins across disconnected vendor consoles.")
    add_p("2. Brittle Heuristic and Rule-Based Detection: Traditional SIEM platforms rely entirely on exact string matching, static threshold counts, and simple regex patterns. Attackers bypass these defenses trivially by altering command-line flags, encoding scripts in Base64, rotating IP addresses across cloud subnets, or utilizing legitimate system binaries (Living off the Land techniques - LotL).")
    add_p("3. High Latency Hand-off Funnels: The sequential hand-off between Tier-1, Tier-2, and Tier-3 introduces massive operational friction. Because alerts sit in queues awaiting analyst shift changes and manual reviews, the Mean Time to Acknowledge (MTTA) and Mean Time to Respond (MTTR) routinely stretch into hours or days, allowing adversaries ample time to complete lateral movement and data exfiltration.")
    add_p("4. Lack of Blast-Radius Safety and Closed-Loop Automation: First-generation SOAR platforms execute hardcoded scripts without contextual risk evaluation. If a playbook misidentifies an IP address or isolates a critical domain controller or database cluster, it causes catastrophic business disruption. As a result, enterprise risk officers frequently disable automated response actions, reverting the SOC to slow, manual response procedures.")
    add_p("5. High Ingestion Licensing Costs: Traditional SIEM architectures charge enterprises on a per-gigabyte or Events-Per-Second (EPS) licensing model. This economic penalty forces organizations to filter or truncate security telemetry prior to ingestion, creating critical blind spots that adversaries readily exploit.")

    add_sec_heading("3.3 Quantitative Deficiencies (MTTA, MTTR, False Positive Rates)")
    add_p("The quantitative operational failure of traditional SOC architectures is documented across enterprise benchmark studies. Table 3.1 synthesizes typical baseline performance metrics observed across enterprise organizations operating traditional SIEM and multi-tier SOC models.")

    table_ex_headers = ["Operational Metric", "Traditional SOC Baseline", "Impact on Cyber Defense", "Primary Root Cause"]
    table_ex_widths = [Inches(1.6), Inches(1.4), Inches(2.0), Inches(1.8)]
    table_ex_data = [
        ["Daily Alert Volume", "10,000 – 500,000", "Analyst triage capacity overwhelmed by alert volume.", "Lack of pre-triage locality-sensitive deduplication."],
        ["False Positive Ratio", "80% – 90%", "Widespread analyst cognitive fatigue and alert dismissal.", "Rigid regex heuristics lacking contextual risk scoring."],
        ["Mean Time to Acknowledge (MTTA)", "15 – 45 Minutes", "Critical alerts remain uninspected in backlogs.", "Linear human triage queue processing."],
        ["Mean Time to Remediate (MTTR)", "45 – 60+ Minutes", "Adversaries achieve complete data exfiltration.", "Manual swivel-chairing across 5-10 disconnected tools."],
        ["Adversary Dwell Time", "16 – 200+ Days", "Undetected lateral movement across enterprise networks.", "Lack of multi-hop graph correlation and timeline synthesis."],
        ["Analyst Annual Turnover", "35% – 50%", "Loss of institutional cybersecurity knowledge.", "Burnout driven by repetitive, low-level manual triage tasks."]
    ]
    add_table(table_ex_widths, table_ex_headers, table_ex_data)

    add_sec_heading("3.4 Disadvantages of the Existing System")
    add_p("In summary, the existing enterprise SOC paradigm presents several insurmountable operational disadvantages:")
    add_p("• Inability to Scale Horizontally: Adding human analysts scales linearly with cost and training time, whereas enterprise log volume grows exponentially with cloud expansion.")
    add_p("• Severe Vulnerability to Advanced Persistent Threats (APTs): Sophisticated adversaries deliberately generate high volumes of low-severity noise to mask targeted lateral movement activities.")
    add_p("• Exorbitant Total Cost of Ownership (TCO): Enterprise SIEM and SOAR platforms demand millions of dollars annually in proprietary ingestion volume licenses and dedicated professional services for playbook maintenance.")
    add_p("• High Risk of Human Error: Fatigued analysts operating under high stress routinely overlook subtle indicators of compromise or execute misconfigured containment commands.")
'''

with open(r'scripts\ch3_gen.py', 'w', encoding='utf-8') as f:
    f.write(ch3_full)

print("ch3_gen.py written.")
