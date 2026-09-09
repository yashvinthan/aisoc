"""
Chapter 4: Proposed System
Written in clear, simple, human-understandable academic language.
Explains the system vision, architecture, 5-phase methodology, threat attribution, UML models (Use Case, Activity, Sequence, Class, State Machine), and ER database design.
No raw code directory paths (e.g. services/ingest) are present in the prose.
"""
import os
from docx.shared import Inches

def generate_chapter_4(add_p, add_ch_heading, add_sec_heading, add_subsec_heading, add_code, add_table, add_fig, fig_dir):
    add_ch_heading("CHAPTER 4\nPROPOSED SYSTEM")
    
    add_sec_heading("4.1 System Overview and Vision")
    add_p("The proposed AiSOC platform is designed to transform how cybersecurity teams detect and respond to threats. Instead of treating security logs as isolated rows of text in disconnected tables, AiSOC connects all users, computers, IP addresses, and alerts into an interconnected Security Knowledge Graph. It then uses a team of specialized Artificial Intelligence (AI) agents to investigate incidents, explain them clearly in plain English, and recommend safe response actions.")
    add_p("AiSOC automates the entire security workflow from the moment a log is received until the threat is safely contained:")
    add_p("1. Universal Log Ingestion: Ingests logs from firewalls, servers, cloud accounts, and employee laptops, converting them into a standardized format.")
    add_p("2. Smart Noise Reduction: Automatically filters out repetitive alarms using mathematical fingerprinting and Machine Learning.")
    add_p("3. Interactive Graph Modeling: Visually maps how an attack moves from one computer to another.")
    add_p("4. Multi-Agent AI Investigation: Deploys four specialized AI agents that verify the alert, search historical logs, and write an investigation report.")
    add_p("5. Safe, Gated Threat Containment: Calculates the potential impact before taking response actions, ensuring that critical business servers are never accidentally locked.")

    add_sec_heading("4.2 System Architecture and High-Level Topology")
    add_p("AiSOC is built as a modular, cloud-native system composed of specialized services designed for high speed, reliability, and security.")
    
    # Figure 4.1: System Topology
    add_fig(os.path.join(fig_dir, "fig4_1_system_topology.png"), "Figure 4.1: High-Level End-to-End System Topology of the AiSOC Platform", 5.8)
    
    add_p("The platform consists of seven core architectural layers:")
    add_p("1. Log Intake and Connectors Layer: Collects raw security logs from over 80 standard enterprise data sources (such as CrowdStrike, Microsoft Defender, AWS CloudTrail, Okta, and Zeek network monitors).")
    add_p("2. Log Ingestion and Normalization Module: A high-speed worker written in the Go programming language that parses raw logs and converts them into the standard Open Cybersecurity Schema Framework (OCSF) format in under 2 milliseconds.")
    add_p("3. Distributed Message Streaming Bus (Apache Kafka): A high-capacity message pipeline that reliably buffers and streams millions of events per day to processing modules without data loss.")
    add_p("4. Alert Deduplication and ML Scoring Engine: Uses mathematical hashing (Simhash) to drop duplicate alerts and applies Machine Learning models (Isolation Forest and LightGBM) to calculate risk scores.")
    add_p("5. Central Management Backend and Knowledge Graph: The core API server (built with FastAPI) and graph database (Neo4j) that manage user accounts, incident cases, and relationship maps.")
    add_p("6. Multi-Agent AI Investigation Subsystem: Uses the LangGraph AI framework to coordinate four specialized AI agents (DetectAgent, TriageAgent, HuntAgent, RespondAgent) that investigate alerts collaboratively.")
    add_p("7. Automated Response and Containment Controller: Executes containment actions (like isolating an infected device) and requests human manager approval whenever an action affects critical systems.")
    add_p("8. Security Analyst Web Dashboard: A modern web interface (built with Next.js and React) where analysts can view live alert queues, examine evidence timelines, and approve response actions.")

    add_sec_heading("4.3 Core System Modules and Components Matrix")
    table_svc_headers = ["System Module Name", "Programming Language", "Processing Speed", "Primary Role & Responsibility"]
    table_svc_widths = [Inches(1.8), Inches(1.4), Inches(1.2), Inches(2.0)]
    table_svc_data = [
        ["Log Ingestion & Normalization Module", "Go 1.21", "< 2 ms", "Converts raw log streams into standardized OCSF format and tags MITRE ATT&CK techniques."],
        ["Alert Deduplication & ML Scoring Engine", "Python 3.11", "< 15 ms", "Removes duplicate alarms with Simhash and calculates risk scores using Isolation Forest."],
        ["Central Management Backend (Core API)", "Python 3.11 / FastAPI", "< 30 ms", "Manages incident cases, user authentication, graph queries, and system audit logs."],
        ["Threat Intelligence Engine", "Python 3.11", "Background", "Pulls known malicious IP and domain lists from public threat feeds (TAXII/MISP)."],
        ["Multi-Agent AI Investigation Subsystem", "Python / LangGraph", "0.5 to 1.5 s", "Coordinates the four AI agents to analyze evidence, search logs, and draft summaries."],
        ["Automated Response & Containment Controller", "Python 3.11", "< 50 ms", "Executes containment commands and verifies safety limits before isolating devices."],
        ["Real-Time Notification Service", "Node.js / TypeScript", "< 5 ms", "Pushes live alerts to the web dashboard instantly using WebSocket connections."],
        ["Security Analyst Web Dashboard", "Next.js 14 / React 19", "Client-Side", "Interactive user interface for monitoring alerts, viewing graphs, and taking action."],
        ["Offline Simulation & Testing Sandbox", "Python 3.10+", "< 10 ms", "Self-contained local testing tool for running instant attack simulations without dependencies."]
    ]
    add_table(table_svc_widths, table_svc_headers, table_svc_data, "Table 4.1: Core System Modules, Programming Languages, and Processing Responsibilities")
    add_p("As outlined in Table 4.1, each module in AiSOC is specialized for its role, ensuring modularity, high performance, and fault tolerance.")

    # -------------------------------------------------------------
    # 4.4 METHODOLOGY — COMPLETE SYSTEM WORKFLOW
    # -------------------------------------------------------------
    add_sec_heading("4.4 METHODOLOGY — COMPLETE SYSTEM WORKFLOW")
    add_p("The end-to-end operation of the AiSOC platform follows an automated five-phase methodology from initial log intake to incident resolution:")
    
    # Figure 4.4 Methodology Flowchart
    add_fig(os.path.join(fig_dir, "fig4_0_complete_methodology.png"), "Figure 4.4: Methodology — Complete End-to-End System Workflow Flowchart", 5.8)
    
    add_p("• Phase 1 (Data Ingestion & Continuous Capture): Raw security logs from firewalls, servers, and identity providers are received continuously by the platform's data connectors.")
    add_p("• Phase 2 (High-Speed Normalization): The Go ingestion worker translates incoming logs into standard OCSF format and matches known attack signatures.")
    add_p("• Phase 3 (Deduplication & Risk Scoring): The system generates a 64-bit mathematical fingerprint for each alert. Duplicate alerts are grouped together in Redis, while unique alerts are scored by the Machine Learning engine. If the risk score is below 30, the alert is marked as background noise; if 30 or higher, an incident case is opened.")
    add_p("• Phase 4 (Multi-Agent AI Investigation): The four AI agents collaborate step-by-step: DetectAgent identifies the attack technique; TriageAgent checks user history and travel speeds; HuntAgent searches historical logs for related activity; and RespondAgent creates a response plan.")
    add_p("• Phase 5 (Safety Check & Containment): The system checks the blast radius (potential business impact). Low-risk actions execute automatically; high-impact actions send an approval prompt to a human manager before execution.")

    add_sec_heading("4.5 Threat Actor Attribution and Campaign Matching")
    add_p("In addition to investigating single alerts, the platform includes a Threat Intelligence Engine that identifies which known hacking group might be responsible for an attack. The system compares the observed techniques and IP addresses against international threat profiles using Cosine and Jaccard similarity formulas:")
    add_p("Similarity = 0.7 * Cosine_Similarity(Observed_Techniques, Known_Group_Techniques) + 0.3 * Jaccard_Similarity(Observed_IPs, Known_Group_IPs)  ...Equ. (4.1)")
    add_p("This calculation allows the system to tell the analyst if an ongoing attack matches the signature of known cybercrime groups (such as ransomware gangs or state-sponsored groups).")

    add_sec_heading("4.6 Unified Modeling Language (UML) Diagrams")
    add_p("To formally specify how the AiSOC software was designed and how its components interact, five standard Unified Modeling Language (UML) diagrams are presented below:")

    add_subsec_heading("4.6.1 Use Case Diagram")
    add_p("The Use Case diagram models the interactions between human security roles and the automated platform across five distinct actors:")
    
    # Figure 4.6.1: Use Case Diagram
    add_fig(os.path.join(fig_dir, "fig4_2_use_case_diagram.png"), "Figure 4.6.1: UML Use Case Diagram for Enterprise SOC Actors and Autonomous AI Engine", 5.8)
    
    add_p("1. SOC Analyst (Tier-1 / Tier-2): Logs into the platform with Multi-Factor Authentication (MFA), monitors the real-time alert queue, reviews AI-generated investigation summaries, runs natural-language search queries, and submits feedback to help train the ML models.")
    add_p("2. Detection Engineer: Creates and tests new detection rules (Sigma/YARA), manages threat intelligence feeds, and configures noise-filtering thresholds.")
    add_p("3. SOC Lead / Incident Commander: Reviews overall security metrics and approves high-impact containment actions (such as isolating critical servers).")
    add_p("4. Compliance Auditor / CISO: Inspects the tamper-evident audit ledger and exports signed compliance PDF reports for regulatory audits.")
    add_p("5. Autonomous AI Engine (System Actor): Automatically receives logs, removes duplicates, runs multi-agent AI investigations, and safely executes low-risk response actions in the background.")

    add_subsec_heading("4.6.2 Activity Diagram")
    add_p("The Activity diagram illustrates the step-by-step decision flow and internal logic of the system as an alert moves from intake to resolution:")
    
    # Figure 4.6.2: Activity Diagram
    add_fig(os.path.join(fig_dir, "fig4_5_activity_diagram.png"), "Figure 4.6.2: UML Activity Diagram: Ingestion, Triage, and Multi-Agent Investigation Flow", 5.6)
    
    add_p("• The system receives a log and checks if it is a duplicate using Simhash fingerprinting.")
    add_p("• The Machine Learning model calculates a risk score. Low-risk events (<30) are suppressed; high-risk events (>=30) trigger an investigation.")
    add_p("• The Multi-Agent AI system investigates the event, searches the database, and creates a containment plan.")
    add_p("• If the containment action is safe, it runs automatically; if it has a high impact, it waits for human approval before closing the ticket.")

    add_subsec_heading("4.6.3 Sequence Diagram")
    add_p("The Sequence diagram shows the chronological order of messages exchanged between the user interface, backend API, graph database, AI agents, and response controller:")
    
    # Figure 4.6.3: Sequence Diagram
    add_fig(os.path.join(fig_dir, "fig4_4_sequence_diagram.png"), "Figure 4.6.3: UML Sequence Diagram: Chronological Message Exchanges During Incident Triage", 5.8)
    
    add_p("1. The analyst opens the web console to view an incoming alert.")
    add_p("2. The web console requests alert details from the Central Management Backend.")
    add_p("3. The backend starts the Multi-Agent AI investigation.")
    add_p("4. The AI agents query the Neo4j graph database to see which other devices are connected to the infected computer.")
    add_p("5. The AI agents generate an investigation report and suggest a containment plan.")
    add_p("6. The report is pushed live to the analyst's screen.")
    add_p("7. The analyst reviews the summary and clicks 'Approve Containment.'")
    add_p("8. The Response Controller sends an instruction to the network firewall to isolate the device and confirms success.")

    add_subsec_heading("4.6.4 Class Diagram")
    add_p("The Class diagram outlines the core object-oriented structures, properties, and methods used in the system's software code:")
    
    # Figure 4.6.4: Class Diagram
    add_fig(os.path.join(fig_dir, "fig4_3_class_diagram.png"), "Figure 4.6.4: UML Class Diagram of Core Entity Model and System Constraints", 5.8)
    
    add_p("• OcsfEvent: Represents a standardized log event with properties such as ID, timestamp, category, and observables (IPs, hashes). Contains methods to normalize logs and tag attack techniques.")
    add_p("• Alert: Represents a grouped threat alarm with properties such as severity, risk score, and fingerprint. Contains methods to score risk and calculate deduplication.")
    add_p("• Case: Represents an active incident ticket containing multiple related alerts, investigation notes, and assigned analyst details.")
    add_p("• EntityNode: Represents a device, user, or IP address in the Neo4j graph database, with methods to calculate the blast radius and attack path.")
    add_p("• ActionExecution: Represents a containment command (such as isolating a host or locking an account) with safety verification methods.")

    add_subsec_heading("4.6.5 State Machine Diagram")
    add_p("The State Machine diagram models the different lifecycle states that an alert and incident case pass through from start to finish:")
    
    # Figure 4.6.5: State Machine Diagram
    add_fig(os.path.join(fig_dir, "fig4_6_state_machine.png"), "Figure 4.6.5: UML State Machine Diagram: Incident and Alert Lifecycle State Transitions", 5.6)
    
    add_p("• States: Ingested -> Fused -> Triaged -> Investigating -> PendingApproval -> AutoRemediating -> Resolved -> Closed.")
    add_p("• An event moves from Ingested to Fused after passing duplicate checks.")
    add_p("• An event moves from Investigating to PendingApproval whenever a high-impact containment action requires human confirmation.")

    add_sec_heading("4.7 Automation Maturity Model (L0 to L4)")
    table_mat_headers = ["Maturity Level", "Level Name", "What the AI Does Automatically", "Role of the Human Analyst"]
    table_mat_widths = [Inches(1.2), Inches(1.5), Inches(2.3), Inches(1.4)]
    table_mat_data = [
        ["L0", "Manual Monitoring", "No automated actions. AI only formats and displays raw logs.", "Analyst does all investigation and response manually."],
        ["L1", "Assisted Triage", "AI writes investigation summaries and suggests response steps.", "Analyst reviews suggestions and manually clicks to run each action."],
        ["L2", "Supervised Autonomy", "AI automatically performs harmless lookups (IP checks, ticket updates).", "Analyst must approve active containment steps (host isolation)."],
        ["L3", "Conditional Autonomy", "AI automatically contains threats if the impact score is below a safe limit.", "Analyst is notified immediately and only steps in if safety limits are exceeded."],
        ["L4", "Full Autonomy", "AI handles the full cycle: detection, triage, containment, and report generation.", "Analyst acts as an auditor reviewing daily executive summaries."]
    ]
    add_table(table_mat_widths, table_mat_headers, table_mat_data, "Table 4.2: Five-Tier Automation Maturity Model (L0 to L4) and Safety Controls")
    add_p("As detailed in Table 4.2, organizations can choose their preferred level of automation based on their operational risk policies.")

    add_sec_heading("4.8 Database Design and Entity-Relationship (ER) Model")
    add_p("The platform uses a combination of modern database technologies: PostgreSQL for storing users, cases, and audit logs; Neo4j for storing relationships between devices and users; and Redis for fast in-memory caching.")
    
    add_subsec_heading("4.8.1 Entity–Relationship (ER) Model")
    add_p("The Entity-Relationship (ER) diagram models the primary database tables, attributes, and foreign-key relationships:")
    
    # Figure 4.8.1: ER Model
    add_fig(os.path.join(fig_dir, "fig4_8_er_model.png"), "Figure 4.8.1: Entity–Relationship (ER) Model of Core Relational Database Tables", 5.8)
    
    add_p("• USER Table: Stores user accounts with attributes {user_id (Primary Key), username, role, organization_id}. Connected to INCIDENT_CASE with a 1-to-Many relationship.")
    add_p("• INCIDENT_CASE Table: Stores security incident tickets with attributes {case_id (Primary Key), title, severity, status, created_at}. Connected to ALERTS and ACTION_EXEC.")
    add_p("• ACTION_EXEC Table: Records all containment commands with attributes {action_id (Primary Key), action_type, target_device, impact_score, status, approved_by}.")

print("Chapter 4 rewritten in clear, understandable academic style.")
