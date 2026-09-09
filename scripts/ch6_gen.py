"""
Chapter 6: Implementation
Written in clear, simple, human-understandable academic language.
Explains the software implementation of each module, accompanied by the 10 live application screenshots.
No raw code directory paths (e.g. services/ingest) are present in the prose.
"""
import os
from docx.shared import Inches

def generate_chapter_6(add_p, add_ch_heading, add_sec_heading, add_subsec_heading, add_code, add_table, add_fig, fig_dir):
    add_ch_heading("CHAPTER 6\nIMPLEMENTATION")
    
    add_sec_heading("6.1 Data Ingestion and Log Normalization Module")
    add_p("The data ingestion module is implemented in the Go programming language to achieve maximum processing speed and low memory usage. It continuously receives security logs from over 80 enterprise software sources (such as CrowdStrike, Microsoft Defender, AWS CloudTrail, and Okta) and converts them into the standardized Open Cybersecurity Schema Framework (OCSF) format.")
    add_p("By using Go's lightweight concurrency (goroutines) and reusable memory buffers, the ingestion module normalizes each log event in under 1.4 milliseconds, easily processing over 25,000 to 50,000 events per second.")
    
    # Figure 6.1: OCSF Pipeline
    add_fig(os.path.join(fig_dir, "fig6_1_ocsf_pipeline.png"), "Figure 6.1: High-Speed Log Ingestion, OCSF Normalization, and Attack Technique Tagging Pipeline", 5.8)
    
    table_ocsf_headers = ["Log Origin / Tool", "Input Format", "Standard OCSF Category", "Standard Class ID", "Standard Class Name"]
    table_ocsf_widths = [Inches(1.5), Inches(1.2), Inches(1.5), Inches(1.2), Inches(1.8)]
    table_ocsf_data = [
        ["CrowdStrike EDR", "JSON Webhook", "System Activity", "1001", "Process Activity"],
        ["Okta Identity Provider", "Syslog Message", "Identity & Access", "3001", "Authentication / Logon"],
        ["AWS CloudTrail", "Cloud Event Stream", "Cloud & Audit", "6003", "API / Audit Activity"],
        ["Zeek Network Monitor", "Tab-Separated Log", "Network Activity", "4001", "Network Connection"],
        ["Kubernetes Audit", "JSON AuditLog", "Application Activity", "6001", "Container / Pod Activity"]
    ]
    add_table(table_ocsf_widths, table_ocsf_headers, table_ocsf_data, "Table 6.1: Mapping of Third-Party Security Logs to Standard OCSF Schema Classes")
    add_p("As shown in Table 6.1, incoming logs are standardized into numeric OCSF classes, enabling fast processing across all downstream components.")

    add_sec_heading("6.2 Threat Intelligence and IOC Search Module")
    add_p("To help analysts quickly identify known malicious files, IP addresses, and domain names, the platform includes a Threat Intelligence module. This module regularly downloads updated lists of known cyber threats from public feeds (such as the CISA Known Exploited Vulnerabilities catalog, AlienVault OTX, and MISP).")
    
    # Figure 6.2: Threat Intel Pipeline
    add_fig(os.path.join(fig_dir, "fig6_2_threatintel_bloom.png"), "Figure 6.2: Threat Intelligence Ingestion and In-Memory Bloom Filter Search Architecture", 5.8)
    
    # Screenshot 6: Threat Intel / IOC Search Page
    add_fig(os.path.join(fig_dir, "screen6_threat_intel_iocs.png"), "Figure 6.3: Threat Intelligence and IOC Search Console on the Web Dashboard", 5.8)

    add_p("As shown in Figure 6.3, the Threat Intelligence search console allows security analysts to type in any suspicious IP address, domain, or file hash and immediately see if it has been linked to known malware or phishing campaigns.")
    add_p("To make lookups instantaneous, all known threat indicators are stored in an in-memory Redis Bloom filter. This allows the system to check millions of indicators in less than a millisecond without overloading the main database.")

    table_ti_headers = ["Threat Feed Source", "Communication Protocol", "Update Frequency", "Types of Data Collected", "Threat Reliability"]
    table_ti_widths = [Inches(1.5), Inches(1.5), Inches(1.2), Inches(1.8), Inches(1.2)]
    table_ti_data = [
        ["CISA KEV Catalog", "HTTPS JSON", "Every 6 Hours", "Actively Exploited Software Vulnerabilities", "100% (Critical)"],
        ["AlienVault OTX", "REST API", "Hourly", "Malicious IP Addresses, File Hashes", "85% (High)"],
        ["MISP Threat Sharing", "STIX 2.1 / REST", "Real-Time Push", "Adversary TTPs, Attack Signatures", "95% (High)"],
        ["AbuseIPDB", "REST API v2", "Every 30 Minutes", "Reported Hacker & Botnet IP Addresses", "80% (Medium)"],
        ["URLhaus (Abuse.ch)", "CSV Feed", "Hourly", "Malicious URLs and Malware Dropper Sites", "90% (High)"]
    ]
    add_table(table_ti_widths, table_ti_headers, table_ti_data, "Table 6.2: Threat Intelligence Feed Sources, Protocols, and Update Frequencies")
    add_p("As summarized in Table 6.2, multiple public and commercial threat feeds are aggregated to ensure comprehensive detection coverage.")

    add_sec_heading("6.3 Alert Deduplication and Machine Learning Scoring Engine")
    add_p("The Alert Deduplication and Scoring Engine is responsible for reducing alert fatigue by filtering out repetitive alarms and highlighting true attacks.")
    
    # Figure 6.4: Dual Stage ML
    add_fig(os.path.join(fig_dir, "fig6_3_dual_stage_ml.png"), "Figure 6.4: Dual-Stage Machine Learning Scoring Architecture (Isolation Forest & LambdaRank)", 5.8)
    
    # Screenshot 1: Dashboard / Alert Queue
    add_fig(os.path.join(fig_dir, "screen1_dashboard_queue.png"), "Figure 6.5: Live Security Operations Dashboard and Prioritized Alert Queue", 5.8)

    # Screenshot 2: CLI Demo Triage Result
    add_fig(os.path.join(fig_dir, "screen2_cli_triage_result.png"), "Figure 6.6: Autonomous Alert Triage Command-Line Execution Result", 5.8)

    add_p("As shown in Figure 6.5, the main Web Dashboard displays live security alerts ranked by their real risk score. Figure 6.6 shows the command-line tool executing an automated triage cycle in less than a second, outputting the attack explanation and recommended actions directly to the console.")

    table_ft_headers = ["Feature", "Feature Name", "Value Range", "Security Meaning"]
    table_ft_widths = [Inches(1.0), Inches(1.8), Inches(1.4), Inches(2.8)]
    table_ft_data = [
        ["f_0", "Vendor Severity", "1 to 5", "The initial severity tag provided by the originating firewall or antivirus."],
        ["f_1", "Entity Risk Score", "0 to 100", "The historical risk level of the affected computer or user account."],
        ["f_2", "Travel Velocity", "km/h", "Calculates how fast a user traveled between two login locations to detect impossible travel."],
        ["f_3", "Network Anomaly", "0.0 to 1.0", "Measures how unusual the login network is compared to the user's normal routine."],
        ["f_4", "Off-Hours Delta", "Hours", "Measures how far outside normal working hours the activity occurred."],
        ["f_5", "Asset Criticality", "1 to 4", "The importance of the target computer (e.g., Domain Controller vs. temporary laptop)."],
        ["f_6", "Kill-Chain Step", "Count", "The number of suspicious steps observed in this attack sequence so far."]
    ]
    add_table(table_ft_widths, table_ft_headers, table_ft_data, "Table 6.3: Feature Vector Extracted for Machine Learning Risk Scoring")
    add_p("As detailed in Table 6.3, these seven extracted features provide the Machine Learning model with the contextual signals needed to score risk accurately.")

    add_sec_heading("6.4 Neo4j Knowledge Graph and Attack-Path Traversal")
    add_p("The platform stores connections between computers, user accounts, and alerts inside a Neo4j graph database. This allows the system to trace how an attacker moved across the network.")
    
    # Figure 6.7: Graph Schema
    add_fig(os.path.join(fig_dir, "fig6_4_neo4j_graph_schema.png"), "Figure 6.7: Neo4j Security Knowledge Graph Schema Showing Entity Relationships", 5.8)
    
    # Screenshot 4: MITRE ATT&CK & Graph Correlation View
    add_fig(os.path.join(fig_dir, "screen4_mitre_attack_correlation.png"), "Figure 6.8: Interactive Attack Graph and MITRE ATT&CK Mapping Workbench", 5.8)

    add_p("As seen in Figure 6.8, the interactive graph interface visually displays the infected host, the compromised user account, and the external hacker IP address, along with mapped MITRE ATT&CK techniques.")

    table_graph_headers = ["Graph Node / Relationship", "Node Category", "Key Properties Stored", "Purpose in Investigation"]
    table_graph_widths = [Inches(1.8), Inches(1.4), Inches(2.2), Inches(1.8)]
    table_graph_data = [
        [":User", "User Account", "username, email, department, risk_score", "Identifies who was targeted."],
        [":Host", "Computer / Server", "hostname, ip_address, operating_system", "Identifies which device is compromised."],
        [":Alert", "Security Alarm", "alert_id, severity, confidence, timestamp", "Records the specific threat event."],
        [":Technique", "Attack Tactic", "technique_id, technique_name, description", "Maps the attack to MITRE ATT&CK."],
        [":LOGGED_INTO", "Relationship", "timestamp, authentication_status", "Connects users to computers."],
        [":AFFECTS", "Relationship", "impact_score, severity", "Connects alerts to affected computers."]
    ]
    add_table(table_graph_widths, table_graph_headers, table_graph_data, "Table 6.4: Neo4j Security Knowledge Graph Node Labels and Relationships")
    add_p("As outlined in Table 6.4, the graph model maps the core entities required for multi-hop attack reconstruction.")

    add_sec_heading("6.5 Multi-Agent AI Investigation Subsystem")
    add_p("The reasoning brain of AiSOC is the Multi-Agent AI system built with LangGraph. Instead of a single AI model, four specialized agents work together like a collaborative team:")
    add_p("1. DetectAgent: Matches the incoming alert against known attack rules (Sigma/YARA).")
    add_p("2. TriageAgent: Checks if the user was traveling or working late to verify if the alert is real.")
    add_p("3. HuntAgent: Searches historical database logs to see if other computers were touched by the same attacker.")
    add_p("4. RespondAgent: Formulates a safe containment plan and calculates the blast radius.")
    
    # Figure 6.9: LangGraph Multi-Agent DAG
    add_fig(os.path.join(fig_dir, "fig6_5_langgraph_dag.png"), "Figure 6.9: Multi-Agent AI Collaborative Investigation Workflow (LangGraph DAG)", 5.8)
    
    # Screenshot 3: Case Evidence Timeline
    add_fig(os.path.join(fig_dir, "screen3_case_evidence_timeline.png"), "Figure 6.10: Incident Case Dossier and Chronological Evidence Timeline Screen", 5.8)

    add_p("As shown in Figure 6.10, the Incident Case screen presents an easy-to-read chronological timeline of evidence, along with the AI-written incident summary, related IP addresses, and recommended next steps.")

    table_agent_headers = ["AI Agent Name", "Specialized Role", "Tools & Databases Used", "Output Produced"]
    table_agent_widths = [Inches(1.4), Inches(1.4), Inches(2.2), Inches(1.8)]
    table_agent_data = [
        ["DetectAgent", "Rule & Technique Matching", "Sigma Rule Engine, MITRE Attack Trie", "List of matched attack techniques and severity."],
        ["TriageAgent", "False Positive Verification", "Neo4j Graph, Travel Velocity Calculator", "Confidence Score (0-100) and context explanation."],
        ["HuntAgent", "Historical Log Search", "Database Search Engine (OpenSearch/ClickHouse)", "List of other connected computers and IP addresses."],
        ["RespondAgent", "Safety Check & Containment", "Blast-Radius Calculator, Firewall API", "Recommended containment plan and safety score."]
    ]
    add_table(table_agent_widths, table_agent_headers, table_agent_data, "Table 6.5: Specialized AI Agents, Investigation Roles, Tools, and Outputs")
    add_p("As detailed in Table 6.5, dividing the investigation across four focused agents ensures structured, reliable reasoning.")

    add_sec_heading("6.6 Blast-Radius Safety Controller and Response Module")
    add_p("To prevent automated actions from accidentally taking important business servers offline, the Response Controller verifies the potential impact (blast radius) before taking action.")
    
    # Figure 6.11: Blast Radius Gating
    add_fig(os.path.join(fig_dir, "fig6_6_blast_radius_gating.png"), "Figure 6.11: Blast-Radius Safety Check and Approval Mechanism", 5.8)
    
    # Screenshot 8: Approval Screen for Actions / Playbooks
    add_fig(os.path.join(fig_dir, "screen8_action_approval.png"), "Figure 6.12: Visual Playbook Studio and Blast-Radius Action Approval Screen", 5.8)

    add_p("As illustrated in Figure 6.12, if an action involves isolating an important server, the system automatically pauses and displays a clear approval prompt on the web dashboard (or sends a message to Slack/Teams), allowing a human manager to review and confirm the action with one click.")

    add_sec_heading("6.7 Detection Rules, Noise Tuning, and Case Disposition")
    add_p("Security engineers can manage detection rules and tune noise filters directly from the web interface.")
    
    # Screenshot 5: Detection Rules Page
    add_fig(os.path.join(fig_dir, "screen5_detection_rules.png"), "Figure 6.13: Enterprise Detection Rule Catalog and MITRE Coverage Page", 5.8)

    # Screenshot 7: Analyst Feedback & Case Disposition
    add_fig(os.path.join(fig_dir, "screen7_case_disposition.png"), "Figure 6.14: Analyst Feedback and Machine Learning Noise-Tuning Interface", 5.8)

    add_p("Figure 6.13 shows the detection rule catalog containing active Sigma and YARA rules. Figure 6.14 shows the feedback screen where analysts can mark an alert as 'Benign Noise.' When feedback is submitted, the system learns from the analyst and automatically suppresses similar harmless alerts in the future.")

    add_sec_heading("6.8 Audit Ledger, System Health, and Pipeline Observability")
    add_p("To ensure complete transparency and compliance with cybersecurity standards (such as SOC-2 and ISO 27001), every step taken by the AI agents is recorded into an unchangeable audit ledger.")
    
    # Screenshot 9: Audit Ledger
    add_fig(os.path.join(fig_dir, "screen9_audit_ledger.png"), "Figure 6.15: Immutable AI Chain-of-Thought Audit Ledger and Activity History", 5.8)

    # Screenshot 10: System Health & Observability
    add_fig(os.path.join(fig_dir, "screen10_system_observability.png"), "Figure 6.16: Data Connector Health and Ingestion Pipeline Observability Dashboard", 5.8)

    add_p("Figure 6.15 shows the complete audit ledger, showing exactly why each decision was made. Figure 6.16 displays the system health dashboard, showing the real-time status, event processing speeds, and latency of all active data connectors.")

print("Chapter 6 rewritten in clear, understandable academic style.")
