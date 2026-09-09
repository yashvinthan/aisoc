"""
Chapter 2: Literature Survey
Written in clear, accessible, human-understandable academic language.
Explains the evolution of security monitoring, data normalization standards, machine learning methods, graph databases, and AI multi-agent systems.
"""
import os
from docx.shared import Inches

def generate_chapter_2(add_p, add_ch_heading, add_sec_heading, add_subsec_heading, add_code, add_table, add_fig, fig_dir):
    add_ch_heading("CHAPTER 2\nLITERATURE SURVEY")
    
    add_sec_heading("2.1 Evolution of Security Monitoring Technologies")
    add_p("Over the past two decades, security monitoring technology has evolved through four major generations:")
    add_p("1. First Generation (2000–2010): Early Security Information and Event Management (SIEM) systems used standard relational databases (such as Oracle or SQL Server) to store text log files. These systems were slow, could not handle large volumes of data, and required manual searching.")
    add_p("2. Second Generation (2010–2018): Modern big-data search engines (such as Elasticsearch and Splunk) and message streaming tools (like Apache Kafka) enabled companies to store millions of logs per day. However, detection still relied on simple keyword matching and threshold rules, causing an overwhelming number of false alarms.")
    add_p("3. Third Generation (2018–2023): Security Orchestration, Automation, and Response (SOAR) tools introduced automated scripts (playbooks) to execute repetitive tasks like blocking an IP address. While helpful, these playbooks are rigid and break easily when log formats change or when dealing with complex, multi-step cyber attacks.")
    add_p("4. Fourth Generation (2024–Present): Modern AI-powered SOC platforms, such as AiSOC, combine high-speed data streaming, interconnected Knowledge Graphs, and Multi-Agent AI systems. This allows the system to not only collect logs, but also understand the context of an attack, trace how it spreads, and propose intelligent response plans.")
    
    # Figure 2.1: Evolution Timeline
    add_fig(os.path.join(fig_dir, "fig2_1_evolution_timeline.png"), "Figure 2.1: Evolutionary Stages of Enterprise Security Operations Systems (2000–2026)", 5.8)

    add_sec_heading("2.2 Log Normalization Standards (OCSF, CEF, ECS)")
    add_p("A major obstacle in cybersecurity monitoring is that every software tool writes log files differently. For example, a firewall might name a source IP address 'src_ip', while a cloud provider calls it 'sourceAddress', and an antivirus program calls it 'client_ip'. If security tools cannot understand each other's data formats, correlation becomes impossible.")
    add_p("To solve this, industry standards have been developed over time:")
    add_p("• Common Event Format (CEF): A legacy format created for traditional network firewalls, but limited in cloud and identity features.")
    add_p("• Elastic Common Schema (ECS): A widely used JSON schema designed primarily for Elasticsearch environments.")
    add_p("• Open Cybersecurity Schema Framework (OCSF v1.1.0): An open-source, vendor-neutral standard launched by the Linux Foundation. OCSF provides structured categories (System, Network, Identity, Application, Cloud) and standard numerical IDs for every security activity.")
    table_norm_headers = ["Standard", "Organization", "Data Format", "Cloud & Identity Support", "Industry Adoption"]
    table_norm_widths = [Inches(1.5), Inches(1.5), Inches(1.5), Inches(1.8), Inches(1.2)]
    table_norm_data = [
        ["CEF (Common Event Format)", "Micro Focus / ArcSight", "Text with Pipe Delimiters", "Limited to Traditional Networks", "High in Legacy Systems"],
        ["ECS (Elastic Common)", "Elastic NV", "JSON Namespace Hierarchy", "Good Cloud & Server Support", "Widespread in SIEM"],
        ["LEEF (Log Event Format)", "IBM QRadar", "Header + Key-Value Pairs", "Proprietary QRadar Format", "Moderate"],
        ["OCSF v1.1.0", "Linux Foundation / Open", "Strongly Typed Standard Schema", "Complete (Cloud, EDR, IAM, Network)", "Rapidly Growing Industry Standard"]
    ]
    add_table(table_norm_widths, table_norm_headers, table_norm_data, "Table 2.1: Comparison of Security Log Normalization Standards")
    add_p("As compared in Table 2.1, OCSF provides the most comprehensive, vendor-neutral data format for modern cloud and endpoint security telemetry.")

    add_sec_heading("2.3 Machine Learning for Alert Deduplication and Risk Scoring")
    add_p("Machine learning helps security systems distinguish between harmless background noise and genuine threats:")
    add_p("1. Eliminating Duplicate Alerts with Simhash: When a system experiences an issue (like a misconfigured server), it may generate thousands of near-identical error messages. Charikar's 64-bit Simhash algorithm calculates a mathematical fingerprint for each alert. If two alerts share almost identical fingerprints (measured by Hamming distance), the system recognizes them as duplicates and groups them together automatically.")
    add_p("2. Unsupervised Anomaly Detection with Isolation Forests: In cybersecurity, genuine attacks represent less than 0.1% of all logs, making supervised training difficult. The Isolation Forest algorithm isolates rare anomalies by building random decision trees. Normal events require many splits to isolate, while anomalous attacks stand out quickly with very short tree path lengths:")
    add_p("s(x, n) = 2^(- E(h(x)) / c(n))  ...Equ. (2.1)")
    add_p("where E(h(x)) is the average path length for observation x across the trees, and c(n) is the average path length of an unsuccessful search in a binary tree.")
    add_p("3. Smart Alert Prioritization (LambdaRank): Instead of sorting alerts by static vendor labels (like 'Low' or 'High'), AiSOC uses the LightGBM LambdaRank algorithm to dynamically rank incidents based on real contextual risk, ensuring that critical multi-stage attacks appear at the top of the analyst queue.")

    add_sec_heading("2.4 Knowledge Graphs for Attack Path Tracing")
    add_p("Traditional relational databases store logs as isolated rows in flat tables. This makes it difficult to see how an attacker moved from one computer to another over several days.")
    add_p("Graph databases (such as Neo4j) solve this by storing data as nodes (Users, Computers, IP Addresses, Files) and edges (Relationships such as LOGGED_INTO, ACCESSED, EXECUTED).")
    add_p("When an alert occurs, the system performs a multi-hop graph search to instantly identify all connected devices and compute the 'Blast Radius' (the potential impact of the incident):")
    add_p("B_r(e) = sum_{v in N_r(e)} w(v) * Criticality(v)  ...Equ. (2.2)")
    add_p("where N_r(e) represents the group of all connected entities within r hops of the alert, and Criticality(v) measures the business importance of each affected device or user account.")

    add_sec_heading("2.5 Multi-Agent Artificial Intelligence in Security Operations")
    add_p("Recent advancements in Large Language Models (LLMs) allow AI to assist with complex reasoning tasks. Rather than relying on a single AI model to do everything, modern systems use a Multi-Agent architecture where specialized agents work together like a team of human analysts:")
    add_p("• DetectAgent: Checks which attack techniques (MITRE ATT&CK) match the incoming alert.")
    add_p("• TriageAgent: Checks user login history, geographic travel speed, and system baselines to verify if the alert is a true threat or a false alarm.")
    add_p("• HuntAgent: Writes database queries in search languages (such as ES|QL or KQL) to search historical logs for related suspicious activities.")
    add_p("• RespondAgent: Plans safe containment actions (such as isolating an infected laptop or resetting a compromised password) based on safety policies.")

    add_sec_heading("2.6 Summary of Literature Gaps")
    table_lit_headers = ["Authors & Year", "Technique Used", "Application", "Limitation Addressed by AiSOC"]
    table_lit_widths = [Inches(1.5), Inches(1.5), Inches(1.8), Inches(2.2)]
    table_lit_data = [
        ["Liu et al. (2008)", "Isolation Forest", "Unsupervised anomaly detection.", "Lacks security context; produces high false alarms without graph relationships."],
        ["Charikar (2002)", "Simhash (Locality-Sensitive Hashing)", "Finding duplicate text documents.", "Previously not applied to real-time security log streams in OCSF format."],
        ["Milajerdi et al. (2019)", "Attack Provenance Graphs", "Tracing advanced attacks across system logs.", "Slow relational storage; lacked automated AI reasoning and plain-English summaries."],
        ["Islam et al. (2019)", "SOAR Playbook Automation", "Automating repetitive incident response steps.", "Rigid scripts that break easily; lacked blast-radius safety checks before execution."],
        ["Wu et al. (2023)", "Multi-Agent AI Collaboration", "Team-based problem solving with LLMs.", "General-purpose; lacked specialized cybersecurity schemas, MITRE tools, and safety controls."]
    ]
    add_table(table_lit_widths, table_lit_headers, table_lit_data, "Table 2.2: Summary of Literature Review and Identified Research Gaps")
    add_p("As synthesized in Table 2.2, existing methods lack the end-to-end integration of graph traversal and multi-agent AI reasoning provided by AiSOC.")

print("Chapter 2 rewritten in clear, understandable academic style.")
