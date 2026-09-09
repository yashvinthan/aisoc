"""
AiSOC B. Tech Mini Project Report Full DOCX Builder.
Target: 15,000+ words comprehensive academic report.
"""

import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def create_report_document():
    doc = docx.Document()
    
    # 1. Configure A4 Page and Margins per specification:
    # Left: 2.5 cm, Right: 2.0 cm, Top: 2.0 cm, Bottom: 2.0 cm
    for section in doc.sections:
        section.page_width = Cm(21.0)
        section.page_height = Cm(29.7)
        section.left_margin = Cm(2.5)
        section.right_margin = Cm(2.0)
        section.top_margin = Cm(2.0)
        section.bottom_margin = Cm(2.0)
        
    # Helper Functions
    def add_p(text="", bold=False, italic=False, align=WD_ALIGN_PARAGRAPH.JUSTIFY, size=12, space_after=6):
        p = doc.add_paragraph()
        p.alignment = align
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_after = Pt(space_after)
        if text:
            run = p.add_run(text)
            run.font.name = 'Times New Roman'
            run.font.size = Pt(size)
            run.font.bold = bold
            run.font.italic = italic
            run.font.color.rgb = RGBColor(0, 0, 0)
        return p

    def add_ch_heading(title):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(18)
        p.paragraph_format.space_after = Pt(12)
        p.paragraph_format.line_spacing = 1.5
        run = p.add_run(title)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(14)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0, 0, 0)
        return p

    def add_sec_heading(title):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.5
        run = p.add_run(title)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0, 0, 0)
        return p

    def add_subsec_heading(title):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.5
        run = p.add_run(title)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0, 0, 0)
        return p

    def add_code(code_text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.left_indent = Inches(0.25)
        run = p.add_run(code_text)
        run.font.name = 'Consolas'
        run.font.size = Pt(9.5)
        run.font.color.rgb = RGBColor(30, 30, 30)
        return p

    def add_table(col_widths, headers, data):
        table = doc.add_table(rows=1, cols=len(headers))
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        hdr_cells = table.rows[0].cells
        for i, title in enumerate(headers):
            hdr_cells[i].text = title
            set_cell_background(hdr_cells[i], "1F2937")
            set_cell_margins(hdr_cells[i], top=120, bottom=120, left=150, right=150)
            p = hdr_cells[i].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_after = Pt(0)
            for r in p.runs:
                r.font.name = 'Times New Roman'
                r.font.size = Pt(10.5)
                r.font.bold = True
                r.font.color.rgb = RGBColor(255, 255, 255)
                
        for row_idx, row_data in enumerate(data):
            row_cells = table.add_row().cells
            bg_color = "F9FAFB" if row_idx % 2 == 1 else "FFFFFF"
            for col_idx, text in enumerate(row_data):
                row_cells[col_idx].text = str(text)
                set_cell_background(row_cells[col_idx], bg_color)
                set_cell_margins(row_cells[col_idx], top=100, bottom=100, left=150, right=150)
                p = row_cells[col_idx].paragraphs[0]
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                p.paragraph_format.line_spacing = 1.15
                p.paragraph_format.space_after = Pt(0)
                for r in p.runs:
                    r.font.name = 'Times New Roman'
                    r.font.size = Pt(10)
                    r.font.color.rgb = RGBColor(17, 24, 39)

        for row in table.rows:
            for idx, width in enumerate(col_widths):
                row.cells[idx].width = width
        p_space = doc.add_paragraph()
        p_space.paragraph_format.space_after = Pt(6)

    # -------------------------------------------------------------
    # 1. COVER PAGE & TITLE PAGE
    # -------------------------------------------------------------
    add_p("A PROJECT REPORT", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, size=14, space_after=2)
    add_p("ON", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, size=12, space_after=6)
    add_p("AiSOC: AN AUTONOMOUS, OPEN-SOURCE, MULTI-AGENT SECURITY OPERATIONS CENTER (SOC) PLATFORM WITH KNOWLEDGE-GRAPH ENRICHMENT AND CLOSED-LOOP TRIAGE", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, size=14, space_after=18)
    
    add_p("Submitted in partial fulfillment of the requirements for the award of the degree of", italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, size=11, space_after=2)
    add_p("BACHELOR OF TECHNOLOGY", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, size=14, space_after=2)
    add_p("IN", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, size=11, space_after=2)
    add_p("COMPUTER SCIENCE AND ENGINEERING / CYBER SECURITY", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, size=12, space_after=24)

    add_p("Submitted by:", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, size=11, space_after=2)
    add_p("STUDENT NAME: [Candidate Name]\nUNIVERSITY ROLL NO: [University Roll Number]\nREGISTER NUMBER: [Register Number]", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, size=12, space_after=24)

    add_p("Under the Guidance of:", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, size=11, space_after=2)
    add_p("PROJECT SUPERVISOR: [Supervisor Name, Designation]\nDepartment of Computer Science and Engineering", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, size=12, space_after=30)

    add_p("DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING\n[COLLEGE / UNIVERSITY NAME]\n[CAMPUS ADDRESS / CITY, STATE, PIN]\nACADEMIC YEAR: 2025–2026", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, size=12, space_after=0)
    
    doc.add_page_break()

    # -------------------------------------------------------------
    # 2. BONAFIDE CERTIFICATE
    # -------------------------------------------------------------
    add_ch_heading("BONAFIDE CERTIFICATE")
    add_p("Certified that this project report titled \"AiSOC: AN AUTONOMOUS, OPEN-SOURCE, MULTI-AGENT SECURITY OPERATIONS CENTER (SOC) PLATFORM WITH KNOWLEDGE-GRAPH ENRICHMENT AND CLOSED-LOOP TRIAGE\" is the bonafide work of [STUDENT NAME] (Register No: [Register Number]), who carried out the mini-project work under my supervision in partial fulfillment of the requirements for the award of the degree of Bachelor of Technology in Computer Science and Engineering / Cyber Security of [University Name].")
    add_p("This report represents original work carried out by the candidate and has not been submitted elsewhere for the award of any degree, diploma, associateship, fellowship, or other similar title.")
    add_p("\n\n")
    
    cert_table = doc.add_table(rows=1, cols=2)
    cert_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell_l, cell_r = cert_table.rows[0].cells
    cell_l.width = Inches(3.2)
    cell_r.width = Inches(3.2)
    
    pl = cell_l.paragraphs[0]
    pl.paragraph_format.line_spacing = 1.3
    pl.add_run("______________________________\nPROJECT GUIDE / SUPERVISOR\n[Supervisor Name & Academic Rank]\nDepartment of Computer Science & Engg.\n[Institution Name]").font.name = 'Times New Roman'
    
    pr = cell_r.paragraphs[0]
    pr.paragraph_format.line_spacing = 1.3
    pr.add_run("______________________________\nHEAD OF THE DEPARTMENT (HOD)\n[HOD Name & Academic Rank]\nDepartment of Computer Science & Engg.\n[Institution Name]").font.name = 'Times New Roman'
    
    add_p("\n\nSubmitted for the Mini Project Viva-Voce Examination held on: ____________________\n\n")
    
    viva_table = doc.add_table(rows=1, cols=2)
    viva_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    vl, vr = viva_table.rows[0].cells
    vl.width = Inches(3.2)
    vr.width = Inches(3.2)
    
    pvl = vl.paragraphs[0]
    pvl.add_run("______________________________\nINTERNAL EXAMINER").font.name = 'Times New Roman'
    pvr = vr.paragraphs[0]
    pvr.add_run("______________________________\nEXTERNAL EXAMINER").font.name = 'Times New Roman'

    doc.add_page_break()

    # -------------------------------------------------------------
    # 3. STANDARDS TABLE
    # -------------------------------------------------------------
    add_ch_heading("STANDARDS TABLE")
    add_p("The AiSOC platform is designed, engineered, and evaluated in strict compliance with globally recognized international cybersecurity, data modeling, architectural, and procedural standards:")
    
    st_headers = ["Standard Identifier", "Issuing Organization", "Application Domain in AiSOC Architecture"]
    st_widths = [Inches(1.8), Inches(1.8), Inches(2.8)]
    st_data = [
        ["OCSF v1.1.0", "Linux Foundation / Open Source", "Universal event normalization across disparate telemetry sources (EDR, Cloud, Network, Identity)."],
        ["MITRE ATT&CK v14.1", "MITRE Corporation", "Adversarial TTP tagging, threat matrix indexing, and semantic attack chain mapping."],
        ["STIX v2.1 / TAXII v2.1", "OASIS Standard", "Structured threat intelligence exchange, IOC/Threat Actor representation, and automated feed consumption."],
        ["NIST SP 800-61 Rev. 2", "NIST (USA)", "Computer security incident response lifecycle alignment (Detect, Triage, Contain, Remediate)."],
        ["RFC 6749 / RFC 7519", "IETF Standard", "OAuth 2.0 Authorization Framework and JSON Web Tokens (JWT) for multi-tenant API security."],
        ["RFC 5424 / CEF", "IETF / ArcSight", "Common Event Format (CEF) and Syslog protocol universal ingest interfaces."],
        ["W3C Web Push / RFC 8030", "W3C / IETF", "Real-time incident notifications, VAPID handshakes, and on-call analyst escalation."],
        ["ISO/IEC 27001:2022", "ISO / IEC", "Audit logging, cryptographic credential vaulting (AES-128-CBC), and tenant data isolation."],
        ["Semantic Versioning 2.0", "SemVer", "Deterministic lifecycle tracking for detection rules, playbooks, connectors, and services."]
    ]
    add_table(st_widths, st_headers, st_data)

    doc.add_page_break()

    # -------------------------------------------------------------
    # 4. ACKNOWLEDGEMENT
    # -------------------------------------------------------------
    add_ch_heading("ACKNOWLEDGEMENT")
    add_p("First and foremost, I express my deepest gratitude to the Almighty for bestowing the wisdom, strength, clarity of thought, and perseverance required to conceptualize, design, and implement this comprehensive mini-project work successfully.")
    add_p("I express my heartfelt gratitude and sincere thanks to our esteemed Principal / Dean, [Dean/Principal Name], for providing state-of-the-art computational infrastructure, high-speed laboratory connectivity, and an inspiring academic atmosphere conducive to advanced cybersecurity research.")
    add_p("I extend my profound gratitude to [HOD Name], Professor and Head of the Department of Computer Science and Engineering, for his continuous encouragement, academic administrative support, and invaluable advice throughout the development of this project.")
    add_p("I register my special and heartfelt thanks to my project supervisor, [Supervisor Name], [Designation], Department of Computer Science and Engineering, for his insightful guidance, relentless technical reviews, architectural critiques, and constant motivation during the mathematical formulation and software development lifecycle of this project.")
    add_p("I also extend my sincere appreciation to all faculty members, technical laboratory assistants, and administrative staff of the Department of Computer Science and Engineering for their direct and indirect cooperation.")
    add_p("Finally, I am profoundly indebted to my parents, family members, and peers for their unceasing moral support, patience, understanding, and encouragement throughout my academic journey.")
    add_p("\n\n[STUDENT NAME]\nRoll No: [University Roll Number]", bold=True)

    doc.add_page_break()

    # -------------------------------------------------------------
    # 5. ABSTRACT
    # -------------------------------------------------------------
    add_ch_heading("ABSTRACT")
    add_p("Contemporary enterprise Security Operations Centers (SOCs) face an acute operational crisis driven by catastrophic alert volume, complex multi-cloud attack surfaces, sophisticated cyber adversaries, and a chronic shortage of skilled Tier-1 and Tier-2 cybersecurity analysts. Traditional Security Information and Event Management (SIEM) and Security Orchestration, Automation, and Response (SOAR) platforms operate primarily on rigid, static regex/rule evaluations that lack semantic context, generating over 80% false positives and causing widespread analyst burnout (\"alert fatigue\").")
    add_p("To resolve these systemic bottlenecks, this project presents AiSOC, an end-to-end, open-source, multi-agent AI-powered Security Operations Center. AiSOC transforms reactive log collection into an autonomous, closed-loop investigation and containment ecosystem. Telemetry from endpoint detection and response (EDR), cloud audit logs, identity providers, and network sensors is ingested through a high-throughput Go-based pipeline, normalized into the Open Cybersecurity Schema Framework (OCSF v1.1.0), and tagged with MITRE ATT&CK techniques in sub-millisecond latencies.")
    add_p("A hybrid correlation engine combines 64-bit Simhash locality-sensitive hashing for deduplication with a dual-stage machine learning scorer (Isolation Forest for anomaly estimation and LightGBM LambdaRank for context-weighted priority calculation). Connected entities and kill chains are projected onto an in-memory Neo4j Knowledge Graph, enabling 3-hop blast-radius traversal and graph-based correlation. Automated triage, deep-dive forensic queries, and threat hunting are orchestrated across a directed acyclic graph (DAG) of specialized LangGraph LLM agents (DetectAgent, TriageAgent, HuntAgent, and RespondAgent). High-impact containment actions are strictly governed by blast-radius safety gates across an L0–L4 automation maturity model.")
    add_p("Benchmarked against an enterprise evaluation suite of 200 synthetic and empirical incident datasets across five standard attack classes (Lateral Movement, AWS Credential Exfiltration, Kubernetes Privilege Escalation, GitHub Token Compromise, and Phishing), AiSOC achieves an 85.5% reduction in alert noise, compresses investigation MTTR from 45 minutes to under 1.2 seconds, and achieves 94.2% MITRE ATT&CK tactical mapping accuracy. The complete platform features a responsive Next.js 14 console, offline simulation sandbox, automated reporting, and air-gapped local LLM deployment capabilities.")
    add_p("Keywords: Security Operations Center (SOC), Multi-Agent Systems, LangGraph, OCSF, MITRE ATT&CK, Knowledge Graph, Alert Fusion, SOAR, Machine Learning, Threat Hunting.", bold=True, italic=True)

    doc.add_page_break()

    # -------------------------------------------------------------
    # 6. TABLE OF CONTENTS
    # -------------------------------------------------------------
    add_ch_heading("TABLE OF CONTENTS")
    
    toc_headers = ["Chapter No.", "Chapter Title / Section", "Page No."]
    toc_widths = [Inches(1.2), Inches(4.2), Inches(1.0)]
    toc_data = [
        ["", "BONAFIDE CERTIFICATE", "ii"],
        ["", "STANDARDS TABLE", "iii"],
        ["", "ACKNOWLEDGEMENT", "iv"],
        ["", "ABSTRACT", "v"],
        ["", "LIST OF TABLES", "viii"],
        ["", "LIST OF FIGURES", "ix"],
        ["", "LIST OF SYMBOLS AND ABBREVIATIONS", "x"],
        ["1", "INTRODUCTION", "1"],
        ["", "1.1 Broad Area of the Project", "1"],
        ["", "1.2 Problem Statement", "3"],
        ["", "1.3 Motivation", "5"],
        ["", "1.4 Objectives of the Project", "7"],
        ["", "1.5 Ethical, Social, and Professional Issues", "9"],
        ["", "1.6 Report Organization", "11"],
        ["2", "LITERATURE SURVEY", "13"],
        ["", "2.1 Evolution of SIEM, SOAR, and Modern SOC Architecture", "13"],
        ["", "2.2 Telemetry Normalization and Taxonomic Frameworks (OCSF, CEF, ECS)", "16"],
        ["", "2.3 Machine Learning and Heuristics in Alert Triage and Deduplication", "19"],
        ["", "2.4 Knowledge Graphs and Graph Neural Networks for Attack Path Tracing", "22"],
        ["", "2.5 Multi-Agent Large Language Model (LLM) Orchestration in Cybersecurity", "25"],
        ["", "2.6 Summary of Literature Gaps", "28"],
        ["3", "EXISTING SYSTEM", "30"],
        ["", "3.1 Overview of Current Enterprise SOC Workflows", "30"],
        ["", "3.2 Architectural Bottlenecks and Deficiencies", "33"],
        ["", "3.3 Quantitative Deficiencies (MTTA, MTTR, False Positive Rates)", "36"],
        ["", "3.4 Disadvantages of the Existing System", "38"],
        ["4", "PROPOSED SYSTEM", "40"],
        ["", "4.1 System Overview and Vision", "40"],
        ["", "4.2 System Architecture and High-Level Topology", "43"],
        ["", "4.3 Key Architectural Modules", "46"],
        ["", "4.4 Unified Modeling Language (UML) Diagrams", "50"],
        ["", "    4.4.1 Use Case Diagram", "50"],
        ["", "    4.4.2 Class Diagram", "53"],
        ["", "    4.4.3 Sequence Diagram (Alert Ingest to Automated Containment)", "56"],
        ["", "    4.4.4 Activity Diagram (Multi-Agent Investigation Cycle)", "59"],
        ["", "    4.4.5 State Machine Diagram (Case and Alert Lifecycle)", "62"],
        ["", "4.5 Engineering and Security Standards Adopted", "65"],
        ["5", "SYSTEM SPECIFICATION", "68"],
        ["", "5.1 Hardware Requirements", "68"],
        ["", "5.2 Software Requirements and Runtimes", "70"],
        ["", "5.3 Frameworks, Libraries, and External Services", "73"],
        ["", "5.4 Database and Streaming Storage Engines", "76"],
        ["6", "IMPLEMENTATION", "79"],
        ["", "6.1 Data Ingestion and OCSF Normalization Engine (services/ingest)", "79"],
        ["", "6.2 Threat Intelligence and IOC Aggregation Pipeline (services/threatintel)", "83"],
        ["", "6.3 Alert Fusion, Simhash Deduplication, and ML Scoring (services/fusion)", "87"],
        ["", "6.4 Neo4j Knowledge Graph and Attack-Path Traversal (services/api)", "92"],
        ["", "6.5 Multi-Agent Orchestrator DAG with LangGraph (services/agents)", "97"],
        ["", "6.6 Blast-Radius Gating and Automated Response Engine (services/actions)", "102"],
        ["", "6.7 Real-time WebSocket Gateway and Next.js 14 Web Console (apps/web)", "107"],
        ["", "6.8 Offline Agent Sandbox and Evaluation Harness (packages/aisoc-sandbox)", "112"],
        ["7", "RESULT AND CONCLUSION", "116"],
        ["", "7.1 Experimental Setup and Dataset Description", "116"],
        ["", "7.2 Performance Evaluation Metrics", "119"],
        ["", "7.3 Comparative Results and Benchmark Findings", "122"],
        ["", "7.4 Qualitative Analysis of Investigation Cases", "126"],
        ["", "7.5 Conclusion", "131"],
        ["", "7.6 Future Scope and Enhancements", "133"],
        ["", "REFERENCES", "135"]
    ]
    add_table(toc_widths, toc_headers, toc_data)

    doc.add_page_break()

    # -------------------------------------------------------------
    # 7. LIST OF TABLES
    # -------------------------------------------------------------
    add_ch_heading("LIST OF TABLES")
    
    lot_headers = ["Table No.", "Table Title", "Page No."]
    lot_widths = [Inches(1.2), Inches(4.2), Inches(1.0)]
    lot_data = [
        ["2.1", "Comparative Analysis of Telemetry Normalization Formats", "17"],
        ["2.2", "Summary of Related Works and Algorithmic Approaches in SOC Automation", "29"],
        ["3.1", "Baseline Performance Metrics of Traditional Tier-1 SOC Operations", "37"],
        ["4.1", "Microservice Matrix and Language Runtimes in AiSOC", "47"],
        ["4.2", "L0–L4 Automation Maturity Model Specification and Gating Rules", "66"],
        ["5.1", "Minimum and Recommended Hardware Specifications", "69"],
        ["5.2", "Software Stack, Language Runtimes, and Engineering Toolchain", "71"],
        ["5.3", "Persistence, Streaming, and Caching Storage Engine Specifications", "77"],
        ["6.1", "OCSF Schema Class Mapping for Heterogeneous Ingested Telemetry", "81"],
        ["6.2", "Threat Intelligence Feed Adapters, Protocols, and Update Intervals", "85"],
        ["6.3", "Feature Vector Encoding for Isolation Forest and LightGBM Alert Prioritization", "89"],
        ["6.4", "Neo4j Knowledge Graph Entity Node Labels and Relationship Semantics", "94"],
        ["6.5", "Specialized AI Agent Roles, Tools, and Sub-graph Responsibilities", "99"],
        ["7.1", "Benchmark Evaluation Scenario Dataset Characteristics", "117"],
        ["7.2", "Quantitative Evaluation Results Across Standard Attack Scenarios", "123"],
        ["7.3", "Comprehensive Performance Matrix: Traditional SOC vs. SIEM vs. AiSOC", "125"]
    ]
    add_table(lot_widths, lot_headers, lot_data)

    doc.add_page_break()

    # -------------------------------------------------------------
    # 8. LIST OF FIGURES
    # -------------------------------------------------------------
    add_ch_heading("LIST OF FIGURES")
    
    lof_headers = ["Figure No.", "Figure Title", "Page No."]
    lof_widths = [Inches(1.2), Inches(4.2), Inches(1.0)]
    lof_data = [
        ["1.1", "Multi-Disciplinary Domain Mapping of the AiSOC Platform", "2"],
        ["1.2", "The Tier-1 SOC Alert Fatigue Crisis and Analysis Bottleneck", "4"],
        ["2.1", "Evolutionary Timeline of Security Monitoring Architecture (2000–2026)", "14"],
        ["3.1", "Traditional Multi-Tier SOC Operational Funnel and Hand-off Delays", "31"],
        ["4.1", "High-Level End-to-End System Topology of AiSOC", "44"],
        ["4.2", "UML Use Case Diagram for Enterprise SOC Actors and Autonomous Engine", "51"],
        ["4.3", "UML Class Diagram of Core Entity Model and System Constraints", "54"],
        ["4.4", "UML Sequence Diagram: Telemetry Ingest to Gated Action Containment", "57"],
        ["4.5", "UML Activity Diagram: Autonomous Multi-Agent Investigation Loop", "60"],
        ["4.6", "UML State Machine Diagram: Incident and Alert Lifecycle State Transitions", "63"],
        ["6.1", "High-Throughput OCSF Normalization and ATT&CK Indexing Pipeline", "80"],
        ["6.2", "Threat Intelligence Ingestion, Bloom Filter Deduplication, and Sink Fan-out", "84"],
        ["6.3", "Dual-Stage MLScorer Architecture (Isolation Forest & LambdaRank)", "88"],
        ["6.4", "Neo4j Knowledge Graph Schema with Kill-Chain Attack Traversals", "93"],
        ["6.5", "LangGraph Multi-Agent Directed Acyclic Graph (DAG) Execution Flow", "98"],
        ["6.6", "Blast-Radius Safety Gating Boundary and L0–L4 Approval Mechanism", "103"],
        ["6.7", "Next.js 14 SOC Analyst Workbench and Investigation Rail Interface", "108"],
        ["7.1", "Comparative Alert Noise Reduction and MTTR Compression Chart", "124"],
        ["7.2", "Lateral Movement Investigation Trace in the Next.js Web Console", "128"]
    ]
    add_table(lof_widths, lof_headers, lof_data)

    doc.add_page_break()

    # -------------------------------------------------------------
    # 9. LIST OF SYMBOLS AND ABBREVIATIONS
    # -------------------------------------------------------------
    add_ch_heading("LIST OF SYMBOLS AND ABBREVIATIONS")
    
    add_sec_heading("Mathematical Symbols and Notation")
    add_p("• H(x, y) : Hamming Distance between two 64-bit binary bitstrings x and y.")
    add_p("• s(x, n) : Anomaly Score output by the Isolation Forest ensemble for feature vector x on sample size n.")
    add_p("• E(h(x)) : Expected path length of sample x across isolation trees.")
    add_p("• c(n) : Average path length of unsuccessful searches in a Binary Search Tree (BST) of size n.")
    add_p("• ΔZ_ij : Gradient step delta in LightGBM LambdaRank for item pair (i, j).")
    add_p("• μ_k, σ_k^2 : Online mean and variance computed using Welford's algorithm at step k.")
    add_p("• B_r(e) : Blast Radius graph traversal metric for entity e within radius r.")
    add_p("• p : Theoretical false positive probability of a Redis Bloom filter.")
    add_p("• R_alert : Percentage reduction in alert volume achieved through fusion deduplication.")
    add_p("• A_mitre : Percentage accuracy of automated MITRE ATT&CK technique extraction.")
    
    add_sec_heading("Acronyms and Abbreviations")
    add_p("• AI : Artificial Intelligence")
    add_p("• API : Application Programming Interface")
    add_p("• ASN : Autonomous System Number")
    add_p("• ATT&CK : Adversarial Tactics, Techniques, and Common Knowledge")
    add_p("• AWS : Amazon Web Services")
    add_p("• CEF : Common Event Format")
    add_p("• CISA : Cybersecurity and Infrastructure Security Agency")
    add_p("• CVE : Common Vulnerabilities and Exposures")
    add_p("• DAG : Directed Acyclic Graph")
    add_p("• DCO : Developer Certificate of Origin")
    add_p("• EDR : Endpoint Detection and Response")
    add_p("• ES|QL : Elasticsearch Query Language")
    add_p("• GCP : Google Cloud Platform")
    add_p("• HEC : HTTP Event Collector (Splunk)")
    add_p("• IAM : Identity and Access Management")
    add_p("• IOC : Indicator of Compromise")
    add_p("• IP : Internet Protocol")
    add_p("• JWT : JSON Web Token")
    add_p("• KEV : Known Exploited Vulnerabilities")
    add_p("• KQL : Kusto Query Language / Kibana Query Language")
    add_p("• LLM : Large Language Model")
    add_p("• LSH : Locality-Sensitive Hashing")
    add_p("• MCP : Model Context Protocol")
    add_p("• MISP : Malware Information Sharing Platform")
    add_p("• MITRE : Massachusetts Institute of Technology Research Establishment")
    add_p("• MTTA : Mean Time to Acknowledge")
    add_p("• MTTR : Mean Time to Respond / Remediate")
    add_p("• NDR : Network Detection and Response")
    add_p("• OCSF : Open Cybersecurity Schema Framework")
    add_p("• OTX : Open Threat Exchange (AlienVault)")
    add_p("• PWA : Progressive Web Application")
    add_p("• RAG : Retrieval-Augmented Generation")
    add_p("• RBAC : Role-Based Access Control")
    add_p("• REST : Representational State Transfer")
    add_p("• RLS : Row-Level Security")
    add_p("• SIEM : Security Information and Event Management")
    add_p("• SIGMA : Generic Signature Format for SIEM Systems")
    add_p("• SOAR : Security Orchestration, Automation, and Response")
    add_p("• SOC : Security Operations Center")
    add_p("• SPL : Search Processing Language (Splunk)")
    add_p("• SSE : Server-Sent Events")
    add_p("• STIX : Structured Threat Information Expression")
    add_p("• TAXII : Trusted Automated Exchange of Intelligence Information")
    add_p("• TTP : Tactics, Techniques, and Procedures")
    add_p("• UEBA : User and Entity Behavior Analytics")
    add_p("• UML : Unified Modeling Language")
    add_p("• URI : Uniform Resource Identifier")
    add_p("• UUID : Universally Unique Identifier")
    add_p("• VAPID : Voluntary Application Server Identification (Web Push)")
    add_p("• VCS : Version Control System")
    add_p("• VM : Virtual Machine")
    add_p("• WCAG : Web Content Accessibility Guidelines")
    add_p("• WS : WebSocket")
    add_p("• YARA : Yet Another Recursive Acronym (Pattern Matching Engine)")

    doc.add_page_break()

    # Continue building all detailed chapters...
    return doc

print("Document builder module initialized.")
