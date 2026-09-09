"""
Full B. Tech Project Report Generator for AiSOC.
Produces an extensive >= 15,000 words docx report.
"""

import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def build_docx_report(output_path):
    doc = docx.Document()
    
    # Page setup: A4, Margins: Left=2.5cm, Right=2.0cm, Top=2.0cm, Bottom=2.0cm
    for section in doc.sections:
        section.page_width = Cm(21.0)
        section.page_height = Cm(29.7)
        section.left_margin = Cm(2.5)
        section.right_margin = Cm(2.0)
        section.top_margin = Cm(2.0)
        section.bottom_margin = Cm(2.0)
        
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
        p.paragraph_format.space_before = Pt(20)
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
    # 1. FRONT MATTER (Cover, Bonafide, Standards, Ack, Abstract, TOC)
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

    # Bonafide Certificate
    add_ch_heading("BONAFIDE CERTIFICATE")
    add_p("Certified that this project report titled \"AiSOC: AN AUTONOMOUS, OPEN-SOURCE, MULTI-AGENT SECURITY OPERATIONS CENTER (SOC) PLATFORM WITH KNOWLEDGE-GRAPH ENRICHMENT AND CLOSED-LOOP TRIAGE\" is the bonafide work of [STUDENT NAME] (Register No: [Register Number]), who carried out the mini-project work under my supervision in partial fulfillment of the requirements for the award of the degree of Bachelor of Technology in Computer Science and Engineering / Cyber Security of [University Name].")
    add_p("This report represents original work carried out by the candidate and has not been submitted elsewhere for the award of any degree, diploma, associateship, fellowship, or other similar title. All sources, standards, and academic literature consulted during this project have been thoroughly cited and referenced in accordance with ethical standards.")
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

    # Standards Table
    add_ch_heading("STANDARDS TABLE")
    add_p("The AiSOC platform is designed, engineered, and evaluated in strict compliance with globally recognized international cybersecurity, data modeling, architectural, and procedural standards:")
    
    st_headers = ["Standard Identifier", "Issuing Organization", "Application Domain in AiSOC Architecture"]
    st_widths = [Inches(1.8), Inches(1.8), Inches(2.8)]
    st_data = [
        ["OCSF v1.1.0", "Linux Foundation / Open Source", "Universal event normalization across disparate telemetry sources (EDR, Cloud, Network, Identity)."],
        ["MITRE ATT&CK® v14.1", "MITRE Corporation", "Adversarial TTP tagging, threat matrix indexing, and semantic attack chain mapping."],
        ["STIX™ v2.1 / TAXII™ v2.1", "OASIS Standard", "Structured threat intelligence exchange, IOC/Threat Actor representation, and automated feed consumption."],
        ["NIST SP 800-61 Rev. 2", "NIST (USA)", "Computer security incident response lifecycle alignment (Detect, Triage, Contain, Remediate)."],
        ["RFC 6749 / RFC 7519", "IETF Standard", "OAuth 2.0 Authorization Framework and JSON Web Tokens (JWT) for multi-tenant API security."],
        ["RFC 5424 / CEF", "IETF / ArcSight", "Common Event Format (CEF) and Syslog protocol universal ingest interfaces."],
        ["W3C Web Push / RFC 8030", "W3C / IETF", "Real-time incident notifications, VAPID handshakes, and on-call analyst escalation."],
        ["ISO/IEC 27001:2022", "ISO / IEC", "Audit logging, cryptographic credential vaulting (AES-128-CBC), and tenant data isolation."],
        ["Semantic Versioning 2.0", "SemVer", "Deterministic lifecycle tracking for detection rules, playbooks, connectors, and services."]
    ]
    add_table(st_widths, st_headers, st_data)

    doc.add_page_break()

    # Acknowledgement
    add_ch_heading("ACKNOWLEDGEMENT")
    add_p("First and foremost, I express my deepest gratitude to the Almighty for bestowing the wisdom, strength, clarity of thought, and perseverance required to conceptualize, design, and implement this comprehensive mini-project work successfully.")
    add_p("I express my heartfelt gratitude and sincere thanks to our esteemed Principal / Dean, [Dean/Principal Name], for providing state-of-the-art computational infrastructure, high-speed laboratory connectivity, and an inspiring academic atmosphere conducive to advanced cybersecurity research.")
    add_p("I extend my profound gratitude to [HOD Name], Professor and Head of the Department of Computer Science and Engineering, for his continuous encouragement, academic administrative support, and invaluable advice throughout the development of this project.")
    add_p("I register my special and heartfelt thanks to my project supervisor, [Supervisor Name], [Designation], Department of Computer Science and Engineering, for his insightful guidance, relentless technical reviews, architectural critiques, and constant motivation during the mathematical formulation and software development lifecycle of this project.")
    add_p("I also extend my sincere appreciation to all faculty members, technical laboratory assistants, and administrative staff of the Department of Computer Science and Engineering for their direct and indirect cooperation.")
    add_p("Finally, I am profoundly indebted to my parents, family members, and peers for their unceasing moral support, patience, understanding, and encouragement throughout my academic journey.")
    add_p("\n\n[STUDENT NAME]\nRoll No: [University Roll Number]", bold=True)

    doc.add_page_break()

    # Abstract
    add_ch_heading("ABSTRACT")
    add_p("Contemporary enterprise Security Operations Centers (SOCs) face an acute operational crisis driven by catastrophic alert volume, complex multi-cloud attack surfaces, sophisticated cyber adversaries, and a chronic shortage of skilled Tier-1 and Tier-2 cybersecurity analysts. Traditional Security Information and Event Management (SIEM) and Security Orchestration, Automation, and Response (SOAR) platforms operate primarily on rigid, static regex/rule evaluations that lack semantic context, generating over 80% false positives and causing widespread analyst burnout (\"alert fatigue\").")
    add_p("To resolve these systemic bottlenecks, this project presents AiSOC, an end-to-end, open-source, multi-agent AI-powered Security Operations Center. AiSOC transforms reactive log collection into an autonomous, closed-loop investigation and containment ecosystem. Telemetry from endpoint detection and response (EDR), cloud audit logs, identity providers, and network sensors is ingested through a high-throughput Go-based pipeline, normalized into the Open Cybersecurity Schema Framework (OCSF v1.1.0), and tagged with MITRE ATT&CK techniques in sub-millisecond latencies.")
    add_p("A hybrid correlation engine combines 64-bit Simhash locality-sensitive hashing for deduplication with a dual-stage machine learning scorer (Isolation Forest for anomaly estimation and LightGBM LambdaRank for context-weighted priority calculation). Connected entities and kill chains are projected onto an in-memory Neo4j Knowledge Graph, enabling 3-hop blast-radius traversal and graph-based correlation. Automated triage, deep-dive forensic queries, and threat hunting are orchestrated across a directed acyclic graph (DAG) of specialized LangGraph LLM agents (DetectAgent, TriageAgent, HuntAgent, and RespondAgent). High-impact containment actions are strictly governed by blast-radius safety gates across an L0–L4 automation maturity model.")
    add_p("Benchmarked against an enterprise evaluation suite of 200 synthetic and empirical incident datasets across five standard attack classes (Lateral Movement, AWS Credential Exfiltration, Kubernetes Privilege Escalation, GitHub Token Compromise, and Phishing), AiSOC achieves an 85.5% reduction in alert noise, compresses investigation MTTR from 45 minutes to under 1.2 seconds, and achieves 94.2% MITRE ATT&CK tactical mapping accuracy. The complete platform features a responsive Next.js 14 console, offline simulation sandbox, automated reporting, and air-gapped local LLM deployment capabilities.")
    add_p("Keywords: Security Operations Center (SOC), Multi-Agent Systems, LangGraph, OCSF, MITRE ATT&CK, Knowledge Graph, Alert Fusion, SOAR, Machine Learning, Threat Hunting.", bold=True, italic=True)

    doc.add_page_break()

    # -------------------------------------------------------------
    # Now let's import the full content loader that injects Chapters 1 through 7
    # -------------------------------------------------------------
    return doc

print("Main generator skeleton ready.")
