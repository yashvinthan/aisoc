"""
Enrich chapters 2, 3, 4, 5, 6, 7 with exhaustive academic and mathematical depth to guarantee >= 15,200 words.
"""

ch2_code = '''"""
Expanded Chapter 2 Literature Survey with detailed academic rigor, mathematical formulations, and comparison tables.
"""
import os
from docx.shared import Inches

def generate_chapter_2(add_p, add_ch_heading, add_sec_heading, add_subsec_heading, add_code, add_table, add_fig, fig_dir):
    add_ch_heading("CHAPTER 2\\nLITERATURE SURVEY")
    
    add_sec_heading("2.1 Evolution of SIEM, SOAR, and Modern SOC Architecture")
    add_p("The discipline of centralized security event monitoring has undergone four distinct evolutionary epochs over the past two decades. In the first generation (2000–2010), Security Information and Event Management (SIEM) systems relied on centralized relational database management systems (RDBMS) such as Oracle and Microsoft SQL Server to ingest text-based Syslog records (Chuvakin & Schmidt 2014; Kent & Souppaya 2006).")
    add_p("These early systems suffered from severe disk I/O bottlenecks and lacked the capability to correlate events across multi-source enterprise networks in real time.")
    add_p("The second generation (2010–2018) introduced distributed search engines and horizontally scalable streaming message brokers (Bose et al. 2017), notably Apache Kafka, Elasticsearch, and Splunk HEC. While these architectures resolved raw data ingestion scale, they introduced acute operational challenges: detection logic remained constrained to static, handcrafted regular expressions and threshold queries, resulting in exponential alert volume without contextual fidelity.")
    add_p("The third generation (2018–2023) saw the emergence of Security Orchestration, Automation, and Response (SOAR) platforms (Islam et al. 2019). SOAR systems introduced automated playbooks designed to execute linear remediation steps via vendor REST APIs.")
    add_p("However, contemporary literature highlights that first-generation SOAR implementations are brittle: they lack adaptive decision-making capabilities, require constant manual maintenance as third-party API schemas drift, and fail to synthesize holistic investigation hypotheses across distributed attack surfaces.")
    add_p("The fourth generation (2024–present), embodied by autonomous AI platforms like AiSOC, bridges the divide between big-data telemetry pipelines, topological graph databases, and Large Language Model (LLM) cognitive reasoning. By modeling cyber telemetry as an active property graph and deploying stateful multi-agent DAGs, fourth-generation SOCs achieve closed-loop automated detection, triage, and response.")
    
    # Figure 2.1: Evolution Timeline
    add_fig(os.path.join(fig_dir, "fig2_1_evolution_timeline.png"), "Figure 2.1: Evolutionary Timeline of Security Monitoring Architecture (2000–2026)", 5.8)

    add_sec_heading("2.2 Telemetry Normalization and Taxonomic Frameworks (OCSF, CEF, ECS)")
    add_p("A primary barrier to autonomous security operations is the extreme semantic heterogeneity of security telemetry. Disparate endpoint, cloud, network, and identity vendors emit logs with proprietary field naming conventions (e.g., `src_ip`, `sourceAddress`, `client_ip`, `originIpAddress`).")
    add_p("Historically, ArcSight Common Event Format (CEF) and Elastic Common Schema (ECS) provided partial standardization. However, both CEF and ECS lack vendor-agnostic governance and comprehensive cloud-native identity taxonomy.")
    add_p("In 2023, the Linux Foundation and industry consortia published the Open Cybersecurity Schema Framework (OCSF v1.1.0). OCSF provides a strongly typed, hierarchical schema defining standardized categories (System, Network, Identity, Application, Cloud), classes, and attributes (Linux Foundation 2023).")
    add_p("Table 2.1 presents a comparative analysis of contemporary telemetry normalization standards.")

    table_norm_headers = ["Taxonomy Standard", "Governing Body", "Extensibility Model", "Multi-Cloud & Identity Support", "Industry Adoption"]
    table_norm_widths = [Inches(1.5), Inches(1.5), Inches(1.5), Inches(1.8), Inches(1.2)]
    table_norm_data = [
        ["CEF (Common Event Format)", "Micro Focus / ArcSight", "Rigid Pipe-Delimited Keys", "Limited Legacy Network Focus", "High Legacy Base"],
        ["ECS (Elastic Common)", "Elastic NV", "JSON Namespace Hierarchy", "Strong Elasticsearch Focus", "Widespread SIEM"],
        ["LEEF (Log Event Ext.)", "IBM QRadar", "Header + Key-Value", "Proprietary QRadar Format", "Moderate"],
        ["OCSF v1.1.0", "Linux Foundation / Open", "Strongly Typed Open Schema", "Native Cloud, EDR, Identity, App", "Accelerating Rapidly"]
    ]
    add_table(table_norm_widths, table_norm_headers, table_norm_data)

    add_p("OCSF introduces a deterministic dictionary of integer identifiers for activity types, class UIDs, and category UIDs. For instance, Category 3 represents Identity & Access Management, Class 3001 denotes Authentication Activity, and Type UID 300101 specifies a Logon Event. This numeric indexing enables compiled stream processors (such as Go workers) to execute zero-allocation schema validation and binary routing.")

    add_sec_heading("2.3 Machine Learning and Heuristics in Alert Triage and Deduplication")
    add_p("The application of machine learning for alert reduction has been widely researched. Landauer et al. (2020) demonstrated that system log clustering using tree-based parsing can group syntactically identical messages. However, naive clustering fails when timestamps, process IDs, and UUIDs vary dynamically across related events.")
    add_p("To overcome this, Locality-Sensitive Hashing (LSH), specifically Charikar\'s 64-bit Simhash algorithm (Charikar 2002), maps high-dimensional text observables into compact binary hashes where the Hamming distance between hashes directly reflects semantic and lexical similarity.")
    add_p("For risk prioritization, supervised classifiers frequently suffer from severe class imbalance, as true security incidents constitute less than 0.1% of raw event logs (Sommer & Paxson 2010). Unsupervised anomaly detection methods, specifically Isolation Forests (Liu et al. 2008), construct ensembles of random decision trees to isolate anomalies based on path length:")
    add_p("s(x, n) = 2^(- E(h(x)) / c(n))  ...Equ. (2.1)")
    add_p("where E(h(x)) is the average path length across trees and c(n) is the average path length of an unsuccessful search in a Binary Search Tree (BST) of size n. Hassan et al. (2019) demonstrated that combining unsupervised anomaly scoring with learning-to-rank algorithms (such as LightGBM LambdaRank; Burges 2010) optimizes analyst triage queues significantly better than static severity tags.")
    add_p("In the LambdaRank formulation, the gradient step Delta Z_ij for a pair of alerts (i, j) where alert i is more critical than alert j is scaled directly by the change in Normalized Discounted Cumulative Gain (NDCG):")
    add_p("Delta Z_ij = ( -sigma / (1 + e^(sigma * (s_i - s_j))) ) * |Delta NDCG_ij|  ...Equ. (2.2)")
    add_p("This guarantees that high-confidence zero-day anomalies and multi-stage lateral movements are dynamically elevated to the top of the analyst triage queue regardless of static vendor severity tags.")

    add_sec_heading("2.4 Knowledge Graphs and Graph Neural Networks for Attack Path Tracing")
    add_p("Representing security events as independent relational database rows obscures multi-stage attack progression (King & Chen 2003; Milajerdi et al. 2019). An adversary conducting lateral movement traverses multiple identity accounts, endpoint hosts, and cloud storage buckets over hours or days.")
    add_p("Noel & Jajodia (2004) and Al-Mohannadi et al. (2020) established that topological attack graphs provide superior situational awareness by modeling adversarial transition probabilities.")
    add_p("Modern property graph databases (e.g., Neo4j) enable real-time Cypher traversal queries to reconstruct 3-hop entity neighborhoods and calculate blast radius metrics B_r(e):")
    add_p("B_r(e) = sum_{v in N_r(e)} w(v) * Criticality(v)  ...Equ. (2.3)")
    add_p("Recent literature has also explored Graph Neural Networks (GNNs; Kipf & Welling 2017) to predict missing attack edges and identify lateral movement paths in enterprise Active Directory graphs.")

    add_sec_heading("2.5 Multi-Agent Large Language Model (LLM) Orchestration in Cybersecurity")
    add_p("The advent of frontier Large Language Models (LLMs) and multi-agent framework architectures (e.g., LangGraph, AutoGen; Wu et al. 2023; Chase 2023) has introduced cognitive reasoning into defensive security operations.")
    add_p("Multi-agent architectures decompose complex cybersecurity workflows into specialized, role-oriented sub-agents: DetectAgent evaluates MITRE ATT&CK techniques; TriageAgent verifies false-positive hypotheses; HuntAgent synthesizes domain-specific queries (ES|QL, SPL, KQL); and RespondAgent evaluates blast-radius policies to formulate containment actions.")
    add_p("Crucially, chaining agents in a stateful Directed Acyclic Graph (DAG) with structured Chain-of-Thought (CoT) ledgers guarantees verifiable provenance, auditability, and deterministic error recovery.")

    add_sec_heading("2.6 Summary of Literature Gaps")
    add_p("Table 2.2 synthesizes the foundational related works, algorithmic methods, and key structural limitations addressed by the AiSOC architecture.")

    table_lit_headers = ["Authors & Year", "Core Algorithmic Technique", "Primary Application", "Identified Structural Literature Gap"]
    table_lit_widths = [Inches(1.5), Inches(1.5), Inches(1.8), Inches(2.2)]
    table_lit_data = [
        ["Liu et al. (2008)", "Isolation Forest Ensemble", "Unsupervised anomaly detection in high-dimensional data.", "Lacks temporal cyber context; high false positive rate without knowledge graph context."],
        ["Charikar (2002)", "Locality-Sensitive Hashing (Simhash)", "Near-duplicate document detection in web search.", "Not applied to real-time OCSF normalized security event deduplication streams."],
        ["Milajerdi et al. (2019)", "Provenance Graph Anomaly State", "APT attack reconstruction via system audit logs (HOLMES).", "Relies on heavy relational storage; lacks LLM natural language query synthesis."],
        ["Islam et al. (2019)", "SOAR Workflow Orchestration", "Automated linear response playbooks for enterprise SOC.", "Brittle static execution paths; lacks graph blast-radius safety gating."],
        ["Wu et al. (2023)", "Multi-Agent Conversation DAG", "Collaborative problem solving via LLM sub-agents.", "General purpose; lacks domain-specific OCSF schemas, MITRE indexing, and SOAR tools."]
    ]
    add_table(table_lit_widths, table_lit_headers, table_lit_data)
'''

with open(r'scripts\ch2_gen.py', 'w', encoding='utf-8') as f:
    f.write(ch2_code)

print("ch2_gen.py enriched.")
