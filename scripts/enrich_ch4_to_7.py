"""
Enrich chapters 4, 5, 6, and 7 with deep academic, architectural, and mathematical rigor.
"""

ch4_expanded = '''"""
Chapter 4 generator with extensive architectural depth, 4.4 Methodology, UML models, and ER design.
"""
import os
from docx.shared import Inches

def generate_chapter_4(add_p, add_ch_heading, add_sec_heading, add_subsec_heading, add_code, add_table, add_fig, fig_dir):
    add_ch_heading("CHAPTER 4\\nPROPOSED SYSTEM")
    
    add_sec_heading("4.1 System Overview and Vision")
    add_p("The proposed AiSOC platform introduces a paradigm shift in defensive cybersecurity operations. Instead of treating security events as disconnected, isolated text records inside relational databases, AiSOC models the entire enterprise ecosystem as an interconnected, dynamic Knowledge Graph and deploys an autonomous Multi-Agent Directed Acyclic Graph (DAG) powered by specialized LLM agents.")
    add_p("AiSOC replaces the fragile, multi-tier human escalation funnel with a high-throughput, closed-loop pipeline that standardizes telemetry at ingest, deduplicates noise via locality-sensitive hashing, scores risk using dual-stage machine learning, projects relational dependencies into Neo4j, executes multi-agent forensic investigations, and enforces mathematically safe containment through graph blast-radius gating.")
    add_p("By unifying high-throughput telemetry normalization, locality-sensitive deduplication, graph-based context traversal, cognitive LLM reasoning, and blast-radius safety verification, AiSOC transforms security operations from a reactive, human-constrained queue to a proactive, self-healing, autonomous defense fabric.")
    add_p("The central philosophy of AiSOC rests on four engineering pillars: (1) Schema Universality through OCSF v1.1.0, (2) Sub-second Ingest-to-Triage Latency, (3) Mathematical Containment Safety via Graph Blast-Radius Verification, and (4) Full Open-Source Transparency without Vendor Lock-in.")

    add_sec_heading("4.2 System Architecture and High-Level Topology")
    add_p("The AiSOC platform is architectured as a cloud-native, microservices-based distributed system designed for horizontal scalability, sub-millisecond ingest latency, and multi-tenant operational resilience.")
    
    # Figure 4.1: System Topology matching SYSTEM_DESIGN.md
    add_fig(os.path.join(fig_dir, "fig4_1_system_topology.png"), "Figure 4.1: High-Level End-to-End System Topology of AiSOC (SYSTEM_DESIGN.md Architecture)", 5.8)
    
    add_p("The architecture comprises seven foundational architectural tiers:")
    add_p("1. Universal Intake and Connectors Layer: Interfaces with over 83 third-party data sources (EDR, CloudTrail, Okta, Splunk, Zeek, Kubernetes) via asynchronous polling workers (APScheduler) and high-speed webhook receivers.")
    add_p("2. High-Throughput Normalization Engine (services/ingest): A compiled Go 1.21 microservice that normalizes raw JSON/Syslog payloads into OCSF v1.1.0 schemas and performs in-memory MITRE ATT&CK technique extraction using an Aho-Corasick trie.")
    add_p("3. Distributed Streaming Event Bus (Apache Kafka): Decouples ingestion from downstream compute via partitioned event streams (ocsf.events, fused.alerts, vulnerability.matches).")
    add_p("4. Alert Fusion and Machine Learning Engine (services/fusion): Applies 64-bit Simhash locality-sensitive hashing for sliding-window deduplication, an Isolation Forest for unsupervised anomaly scoring, and a LightGBM LambdaRank model for context-aware priority ranking.")
    add_p("5. Core API and Enterprise Knowledge Graph (services/api & Neo4j): Manages relational entity graphs (Hosts, Users, IOCs, Alerts, Cases, TTPs), multi-tenant Row-Level Security (RLS), and RESTful/GraphQL interfaces.")
    add_p("6. Cognitive Multi-Agent DAG Orchestrator (services/agents): A stateful LangGraph execution engine deploying DetectAgent, TriageAgent, HuntAgent, and RespondAgent to autonomously investigate alerts and synthesize queries.")
    add_p("7. Blast-Radius Safety Controller and SOAR Engine (services/actions): Enforces L0–L4 maturity policies, validates graph blast-radius caps, and coordinates automated containment with Slack/Teams ChatOps approval.")
    add_p("8. Real-time SOC Workbench and Responder Console (apps/web & services/realtime): A responsive Next.js 14 / React 19 web application featuring live WebSocket alert feeds, interactive Cytoscape graph visualizers, and two-pane Investigation Rails.")

    add_sec_heading("4.3 Key Architectural Modules and Microservices Matrix")
    add_p("Table 4.1 details the functional breakdown, language runtimes, and core responsibilities of each microservice in the AiSOC ecosystem.")

    table_svc_headers = ["Microservice Directory", "Runtime / Language", "Hot-Path Latency", "Primary Architectural Responsibilities"]
    table_svc_widths = [Inches(1.8), Inches(1.4), Inches(1.2), Inches(2.0)]
    table_svc_data = [
        ["services/ingest", "Go 1.21", "< 2 ms", "Sub-millisecond OCSF normalization, in-memory ATT&CK trie matching, CISA KEV correlation."],
        ["services/fusion", "Python 3.11", "< 15 ms", "Simhash 64-bit deduplication, Isolation Forest anomaly scoring, LightGBM LambdaRank priority."],
        ["services/api", "Python 3.11 / FastAPI", "< 30 ms", "Case management, multi-tenancy RLS, Neo4j graph driver, REST/GraphQL API, audit logging."],
        ["services/threatintel", "Python 3.11", "Background", "TAXII 2.1, MISP, AlienVault OTX feed ingestion, Redis Bloom filter deduplication."],
        ["services/agents", "Python 3.11 / LangGraph", "0.5 – 1.5 s", "Multi-agent cognitive DAG execution, semantic RAG query over MITRE ATT&CK STIX bundles."],
        ["services/actions", "Python 3.11", "< 50 ms", "SOAR execution, 3-hop graph blast-radius validation, Slack/Teams ChatOps approval hooks."],
        ["services/realtime", "Node 20 / TypeScript", "< 5 ms", "WebSocket client fan-out, Server-Sent Events (SSE), Web Push notifications."],
        ["apps/web", "Next.js 14 / React 19", "Client-Side", "Analyst console, Cytoscape graph visualizer, Investigation Rail, PDF export."],
        ["packages/aisoc-sandbox", "Python 3.10+", "< 10 ms", "Standalone, zero-dependency offline CLI simulator for local demonstrations and evals."]
    ]
    add_table(table_svc_widths, table_svc_headers, table_svc_data)

    # -------------------------------------------------------------
    # 4.4 METHODOLOGY — COMPLETE SYSTEM WORKFLOW
    # -------------------------------------------------------------
    add_sec_heading("4.4 METHODOLOGY — COMPLETE SYSTEM WORKFLOW")
    add_p("The operational lifecycle of the AiSOC platform is structured around an autonomous, closed-loop methodology spanning five sequential execution phases: Intake, Normalization, Deduplication & Risk Scoring, Multi-Agent Cognitive Investigation, and Blast-Radius Gated Containment.")
    
    # Figure 4.0 / 4.4 Methodology
    add_fig(os.path.join(fig_dir, "fig4_0_complete_methodology.png"), "Figure 4.4: Methodology — Complete System Workflow Flowchart", 5.8)
    
    add_p("1. Phase I (Intake & Continuous Capture): Telemetry from over 83 enterprise data sources is received via active polling workers (`services/connectors`) and push webhooks (`/v1/inbox`).")
    add_p("2. Phase II (Sub-millisecond Normalization): The Go ingest engine translates vendor-specific fields into the canonical OCSF v1.1.0 schema and tags MITRE ATT&CK techniques using an in-memory Aho-Corasick trie.")
    add_p("3. Phase III (Deduplication & Anomaly Scoring): The fusion engine computes a 64-bit Simhash fingerprint to discard redundant noise in Redis. Deduplicated events are scored by an Isolation Forest and ranked by LightGBM LambdaRank.")
    add_p("4. Phase IV (Multi-Agent Cognitive DAG Investigation): If risk score >= 30, the LangGraph DAG triggers. DetectAgent validates signatures; TriageAgent verifies context; HuntAgent sweeps warm logs; RespondAgent formulates a containment plan.")
    add_p("5. Phase V (Blast-Radius Gating & Containment): The actions engine computes the 3-hop graph blast radius. Safe actions execute autonomously; high-impact actions prompt human approval via Slack/Web modals before containment.")

    add_sec_heading("4.5 Threat Actor Attribution & Diamond Model Mapping")
    add_p("Beyond tactical triage, AiSOC incorporates an advanced Threat Actor Attribution Engine within `services/threatintel` implementing Sergio et al.\'s Cyber Diamond Model (Adversary, Capability, Infrastructure, Victim). An attribution vector D(C) is matched against STIX 2.1 threat group profiles using Jaccard and Cosine similarity metrics:")
    add_p("Sim(C, G_k) = 0.7 * Cosine(TTP_C, TTP_G_k) + 0.3 * Jaccard(IOC_C, IOC_G_k)  ...Equ. (4.1)")
    add_p("This quantitative similarity score enables the platform to attribute incoming multi-stage attack campaigns to known threat actor groups (e.g., APT28, APT29, FIN7, Lazarus Group) with mathematically verifiable confidence scores.")

    add_sec_heading("4.6 Unified Modeling Language (UML) Diagrams")
    add_p("To formally specify the architectural structure, interactions, and behavioral dynamics of the AiSOC platform, five standard Unified Modeling Language (UML) models are documented below:")

    add_subsec_heading("4.6.1 Use case diagram")
    add_p("The Use Case diagram specifies the functional interactions between human actors (SOC Tier-1 Analyst, SOC Lead / Administrator) and the automated AiSOC engine:")
    
    # Figure 4.2: Use Case Diagram
    add_fig(os.path.join(fig_dir, "fig4_2_use_case_diagram.png"), "Figure 4.6.1: UML Use Case Diagram for Enterprise SOC Actors and Autonomous Engine", 5.6)
    
    add_p("• Use Case 1 (Authenticate / MFA Login): Analysts and administrators securely authenticate via JWT/OAuth2 and MFA.")
    add_p("• Use Case 2 (Monitor Real-Time Alert Queue): The Analyst views live, fused security alerts streamed via WebSockets.")
    add_p("• Use Case 3 (Inspect AI Investigation Dossier): The Analyst inspects the automated narrative timeline and entity pivot paths.")
    add_p("• Use Case 4 (Execute Natural Language Hunt): Analysts query warm-tier data lakes in natural language translated into ES|QL/SPL/KQL.")
    add_p("• Use Case 5 (Approve Gated Containment Action): The SOC Lead approves high-blast-radius containment actions (e.g., host isolation).")
    add_p("• Use Case 6 (Generate Compliance PDF Report): Administrators export signed PDF incident dossiers for audit compliance.")

    add_subsec_heading("4.6.2 Activity diagram")
    add_p("The Activity diagram models the internal decision logic, loopbacks, and asynchronous multi-agent investigation cycles:")
    
    # Figure 4.5: Activity Diagram
    add_fig(os.path.join(fig_dir, "fig4_5_activity_diagram.png"), "Figure 4.6.2: UML Activity Diagram: Ingestion, Triage, and Multi-Agent Investigation Flow", 5.6)
    
    add_p("• Telemetry is ingested and checked against Redis Simhash cache for duplicates (looping back if duplicate).")
    add_p("• Fused alerts are scored by the ML engine. Alerts with risk < 30 are auto-suppressed; alerts with risk >= 30 open an incident case.")
    add_p("• The Multi-Agent AI Subprocess triggers: TriageAgent verifies hypotheses, HuntAgent executes lake sweeps, Neo4j expands graph entities, and RespondAgent executes safe SOAR containment before reaching the final end state.")

    add_subsec_heading("4.6.3 Sequence diagram")
    add_p("The Sequence diagram specifies the chronological message exchanges from alert intake to automated containment:")
    
    # Figure 4.4: Sequence Diagram
    add_fig(os.path.join(fig_dir, "fig4_4_sequence_diagram.png"), "Figure 4.6.3: UML Sequence Diagram: Telemetry Ingest to Gated Action Containment", 5.8)
    
    add_p("1. Analyst opens web console to view incoming alert.")
    add_p("2. Web console invokes `GET /api/v1/alerts/{id}`.")
    add_p("3. Core API triggers LangGraph multi-agent investigation.")
    add_p("4. Agents query Neo4j graph for attack path and blast-radius context.")
    add_p("5. Neo4j returns graph neighborhood; agents propose containment plan.")
    add_p("6. Core API pushes live dossier updates over WebSockets.")
    add_p("7. Analyst clicks \'Approve Containment\'.")
    add_p("8. Actions service dispatches SOAR API containment (host isolation) and confirms execution.")

    add_subsec_heading("4.6.4 Class diagram")
    add_p("The Class Diagram models the core entity structures, attributes, methods, and associative constraints governing the platform:")
    
    # Figure 4.3: Class Diagram
    add_fig(os.path.join(fig_dir, "fig4_3_class_diagram.png"), "Figure 4.6.4: UML Class Diagram of Core Entity Model and System Constraints", 5.8)
    
    add_p("1. OcsfEvent: Represents normalized events with attributes {id, class_uid, category_uid, time, observables}. Implements normalize() and tagMitre().")
    add_p("2. Alert: Represents deduplicated threat alerts with attributes {id, title, severity, confidence, simhash}. Implements fuse() and scoreRisk().")
    add_p("3. Case: Container grouping related alerts with attributes {id, title, status, priority, analyst}. Implements closeCase() and exportPdf().")
    add_p("4. EntityNode: Represents graph nodes in Neo4j with attributes {id, type, risk_score, blast_radius}. Implements getBlastRadius() and getAttackPath().")
    add_p("5. AgentLedgerStep: Immutable CoT trace step with attributes {step_idx, agent_name, action, rationale}. Implements serialize().")
    add_p("6. ActionExecution: Represents gated containment actions with attributes {id, action_type, target, blast_tier}. Implements validateGating() and execute().")

    add_subsec_heading("4.6.5 State machine diagram")
    add_p("The State Machine Diagram documents the finite lifecycle states of alerts and cases:")
    
    # Figure 4.6: State Machine Diagram
    add_fig(os.path.join(fig_dir, "fig4_6_state_machine.png"), "Figure 4.6.5: UML State Machine Diagram: Incident and Alert Lifecycle State Transitions", 5.6)
    
    add_p("• States: Ingested -> Fused -> Triaged -> Investigating -> PendingApproval -> AutoRemediating -> Resolved -> Closed.")
    add_p("• Transition Ingested -> Fused occurs upon passing Simhash deduplication.")
    add_p("• Transition Investigating -> PendingApproval occurs when RespondAgent requests an action exceeding the blast-radius cap.")

    add_sec_heading("4.7 Engineering and Security Standards Adopted")
    add_subsec_heading("4.7.1 The L0–L4 Automation Maturity Model")
    add_p("To provide enterprise risk officers with granular governance over autonomous agent execution, AiSOC establishes a five-tier Automation Maturity Model:")

    table_mat_headers = ["Maturity Level", "Operational Name", "Autonomous Agent Permissions", "Human Operator Role"]
    table_mat_widths = [Inches(1.2), Inches(1.5), Inches(2.3), Inches(1.4)]
    table_mat_data = [
        ["L0", "Manual Monitoring", "Zero automated action; agents only format and display raw logs.", "Analyst performs all triage, hunting, and execution manually."],
        ["L1", "Assisted Investigation", "Agents synthesize timelines, extract IOCs, and recommend containment steps.", "Analyst reviews recommendations and clicks to execute each action."],
        ["L2", "Supervised Autonomous", "Non-invasive actions (IP enrichment, domain lookup, ticket updates) execute automatically.", "Analyst approves all active containment actions (host isolation, lockout)."],
        ["L3", "Conditional Autonomous", "Containment actions execute automatically if graph blast-radius <= configured policy threshold.", "Analyst is notified post-action; alerted immediately if blast-radius is breached."],
        ["L4", "Fully Autonomous", "Closed-loop autonomous detection, triage, hunting, containment, and report generation.", "Analyst acts as high-level auditor reviewing daily executive summaries."]
    ]
    add_table(table_mat_widths, table_mat_headers, table_mat_data)

    add_sec_heading("4.8 DATABASE DESIGN")
    add_p("The storage architecture of AiSOC utilizes a polyglot persistence design, combining PostgreSQL for relational ACID state management, Neo4j for property graph modeling, OpenSearch for log indexing, and Redis for in-memory caching.")
    
    add_subsec_heading("4.8.1 Entity–relationship model")
    add_p("The Entity-Relationship (ER) model specifies the core relational schema governing tenants, users, incident cases, alerts, and action execution records:")
    
    # Figure 4.8.1: ER Model
    add_fig(os.path.join(fig_dir, "fig4_8_er_model.png"), "Figure 4.8.1: Entity–Relationship (ER) Model of Core Relational Database Tables", 5.8)
    
    add_p("• Entity USER / TENANT: Stores user accounts with attributes {user_id (PK), username, tenant_id, role}. Has a 1-to-Many (1:M) relationship with INCIDENT_CASE.")
    add_p("• Entity INCIDENT_CASE: Stores security cases with attributes {case_id (PK), severity, status, created_at}. Has a 1-to-N (1:N) relationship with ACTION_EXEC.")
    add_p("• Entity ACTION_EXEC: Stores executed and pending containment actions with attributes {action_id (PK), action_type, blast_radius, status, approved_by}.")
'''

with open(r'scripts\ch4_gen.py', 'w', encoding='utf-8') as f:
    f.write(ch4_expanded)

print("ch4_gen.py updated.")
