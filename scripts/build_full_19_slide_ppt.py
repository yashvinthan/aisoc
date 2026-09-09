import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

# --- Professional Dark Theme Palette ---
BG_DARK = RGBColor(15, 23, 42)        # Deep Navy / Slate 900 (#0f172a)
BG_CARD = RGBColor(30, 41, 59)        # Slate 800 (#1e293b)
BG_CARD_LIGHT = RGBColor(51, 65, 85)  # Slate 700 (#334155)
ACCENT_BLUE = RGBColor(56, 189, 248)  # Sky 400 (#38bdf8)
ACCENT_CYAN = RGBColor(45, 212, 191)  # Teal 400 (#2dd4bf)
ACCENT_AMBER = RGBColor(251, 191, 36) # Amber 400 (#fbbf24)
ACCENT_ROSE = RGBColor(244, 63, 94)   # Rose 500 (#f43f5e)
ACCENT_GREEN = RGBColor(74, 222, 128) # Green 400 (#4ade80)
TEXT_MAIN = RGBColor(248, 250, 252)   # Slate 50 (#f8fafc)
TEXT_MUTED = RGBColor(148, 163, 184)  # Slate 400 (#94a3b8)
BORDER_COLOR = RGBColor(71, 85, 105)  # Slate 600 (#475569)
WHITE = RGBColor(255, 255, 255)

def build_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    def add_blank_slide():
        slide = prs.slides.add_slide(blank_layout)
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_DARK
        bg.line.fill.background()
        return slide

    def add_header(slide, slide_num, category, title, subtitle=None):
        # Section Number & Category Pill
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.35), Inches(11.7), Inches(0.32))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        tf_cat.margin_left = tf_cat.margin_top = tf_cat.margin_right = tf_cat.margin_bottom = 0
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = f"SECTION {slide_num} | {category.upper()}"
        p_cat.font.name = 'Calibri'
        p_cat.font.size = Pt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = ACCENT_CYAN

        # Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.65), Inches(11.7), Inches(0.55))
        tf_t = title_box.text_frame
        tf_t.word_wrap = True
        tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
        p_t = tf_t.paragraphs[0]
        p_t.text = title
        p_t.font.name = 'Calibri'
        p_t.font.size = Pt(21)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_MAIN

        # Subtitle
        if subtitle:
            sub_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.18), Inches(11.7), Inches(0.32))
            tf_s = sub_box.text_frame
            tf_s.word_wrap = True
            tf_s.margin_left = tf_s.margin_top = tf_s.margin_right = tf_s.margin_bottom = 0
            p_s = tf_s.paragraphs[0]
            p_s.text = subtitle
            p_s.font.name = 'Calibri'
            p_s.font.size = Pt(11.5)
            p_s.font.color.rgb = TEXT_MUTED

    def add_card(slide, left, top, width, height, title=None, bg_color=BG_CARD, border_color=BORDER_COLOR):
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = bg_color
        shape.line.color.rgb = border_color
        shape.line.width = Pt(1.5)
        
        if title:
            tb = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.14), width - Inches(0.4), Inches(0.38))
            tf = tb.text_frame
            tf.word_wrap = True
            tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
            p = tf.paragraphs[0]
            p.text = title
            p.font.name = 'Calibri'
            p.font.size = Pt(13)
            p.font.bold = True
            p.font.color.rgb = ACCENT_BLUE
        return shape

    def add_bullet_list(slide, left, top, width, height, items, font_size=11, text_color=TEXT_MAIN):
        tb = slide.shapes.add_textbox(left, top, width, height)
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        
        for i, item in enumerate(items):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.space_after = Pt(4.5)
            p.font.name = 'Calibri'
            p.font.size = Pt(font_size)
            
            if isinstance(item, tuple):
                prefix, text = item
                r1 = p.add_run()
                r1.text = prefix + ": "
                r1.font.bold = True
                r1.font.color.rgb = ACCENT_CYAN
                
                r2 = p.add_run()
                r2.text = text
                r2.font.bold = False
                r2.font.color.rgb = text_color
            else:
                r = p.add_run()
                r.text = item
                r.font.color.rgb = text_color

    def add_image_safe(slide, img_path, left, top, width=None, height=None):
        if os.path.exists(img_path):
            try:
                img = slide.shapes.add_picture(img_path, left, top, width=width, height=height)
                return img
            except Exception as e:
                print(f"Error loading {img_path}: {e}")
        else:
            print(f"Image not found: {img_path}")
        return None

    # =========================================================================
    # SLIDE 1: TITLE
    # =========================================================================
    s1 = add_blank_slide()
    
    # College Logo Container at Top Right
    logo_path = "docs/figures/dr_mgr_logo.png"
    if os.path.exists(logo_path):
        logo_bg = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.5), Inches(0.45), Inches(3.0), Inches(0.85))
        logo_bg.fill.solid()
        logo_bg.fill.fore_color.rgb = WHITE
        logo_bg.line.color.rgb = ACCENT_CYAN
        logo_bg.line.width = Pt(1.5)
        s1.shapes.add_picture(logo_path, Inches(9.65), Inches(0.52), width=Inches(2.7), height=Inches(0.71))

    # Top Program Badge
    tb_badge = s1.shapes.add_textbox(Inches(0.8), Inches(0.6), Inches(8.5), Inches(0.4))
    tf_b = tb_badge.text_frame
    p_b = tf_b.paragraphs[0]
    p_b.text = "BACHELOR OF TECHNOLOGY | MINI PROJECT PRESENTATION & VIVA VOCE"
    p_b.font.name = 'Calibri'
    p_b.font.size = Pt(12)
    p_b.font.bold = True
    p_b.font.color.rgb = ACCENT_CYAN

    # Main Project Title
    tb_title = s1.shapes.add_textbox(Inches(0.8), Inches(1.3), Inches(11.7), Inches(1.4))
    tf_t = tb_title.text_frame
    tf_t.word_wrap = True
    p_t = tf_t.paragraphs[0]
    p_t.text = "AiSOC: Autonomous AI-Powered Security Operations Center"
    p_t.font.name = 'Calibri'
    p_t.font.size = Pt(30)
    p_t.font.bold = True
    p_t.font.color.rgb = TEXT_MAIN

    p_sub = tf_t.add_paragraph()
    p_sub.text = "Multi-Agent Security Orchestration, OCSF Telemetry Normalization, Dual-Stage ML Triage, and Graph-Driven Incident Response"
    p_sub.font.name = 'Calibri'
    p_sub.font.size = Pt(13.5)
    p_sub.font.color.rgb = ACCENT_BLUE
    p_sub.space_before = Pt(6)

    # Team Members Card
    add_card(s1, Inches(0.8), Inches(3.1), Inches(5.7), Inches(3.7), "PROJECT TEAM MEMBERS")
    team_members = [
        ("Yashvinthan M", "231061101162  (Lead AI & Backend Architecture)"),
        ("Tharun Kumar D", "231061101150  (ML Triage & Detection Engineering)"),
        ("Sanjeev V", "231061101140  (OCSF Ingestion & Cloud Connectors)"),
        ("Srinithi J S", "231061101149  (Analyst Workbench & Playbook Studio)")
    ]
    add_bullet_list(s1, Inches(1.0), Inches(3.7), Inches(5.3), Inches(2.9), team_members, font_size=12)

    # Department & Supervisor Card
    add_card(s1, Inches(6.8), Inches(3.1), Inches(5.7), Inches(3.7), "DEPARTMENT & ACADEMIC DETAILS")
    dept_info = [
        ("Department", "Department of Computer Science and Engineering"),
        ("Institution", "Faculty of Engineering & Technology"),
        ("Academic Year", "2025-2026 (July 2026 Examination)"),
        ("Project Domain", "Autonomous AI, Cybersecurity & Multi-Agent Systems"),
        ("Verification Testbed", "Enterprise Cisco Catalyst 3850 & Proxmox VE Cluster")
    ]
    add_bullet_list(s1, Inches(7.0), Inches(3.7), Inches(5.3), Inches(2.9), dept_info, font_size=12)

    # =========================================================================
    # SLIDE 2: ABSTRACT
    # =========================================================================
    s2 = add_blank_slide()
    add_header(s2, "2", "Executive Summary", "Abstract: Autonomous Security Operations Platform", "High-level overview of methodology, architectural breakthroughs, and empirical validation")

    add_card(s2, Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.3), "Project Abstract & Scope", border_color=ACCENT_CYAN)
    abs_bullets = [
        ("Context & Motivation", "Enterprise Security Operations Centers (SOCs) face an existential scalability crisis, ingesting tens of millions of daily security logs while grappling with 83% false-positive noise and a severe global workforce shortage exceeding 4.0 million professionals."),
        ("Proposed Innovation", "This project designs, implements, and evaluates AiSOC, an open-source, full-lifecycle autonomous platform that replaces fragmented manual tier-1/tier-2 triage with a collaborative four-agent funnel (DetectAgent, TriageAgent, HuntAgent, RespondAgent)."),
        ("Standardization & ML", "Raw telemetry across 16+ vendor sources is normalized in real-time into the Open Cybersecurity Schema Framework (OCSF) and processed via an in-memory Bloom filter and dual-stage machine learning engine (Isolation Forest anomaly filtering + LambdaRank priority ranking)."),
        ("Graph Correlation & Safety", "Attacks are correlated in real-time within a streaming Neo4j knowledge graph (17 node types, 14 edge relationships) and mitigated via parameterised SOAR playbooks governed by a strict Blast-Radius L0-L4 safety gating model."),
        ("Empirical Results", "Benchmarked across 200 enterprise incidents and 50,000 telemetry events, AiSOC achieves 89.4% noise reduction, reduces MTTR from 103 hours to 3.8 minutes (1,600x acceleration), maintains 96.4% MITRE ATT&CK accuracy, and ensures 100% zero-outage safety execution.")
    ]
    add_bullet_list(s2, Inches(1.0), Inches(2.2), Inches(11.3), Inches(4.5), abs_bullets, font_size=11.5)

    # =========================================================================
    # SLIDE 3: PROBLEM STATEMENT
    # =========================================================================
    s3 = add_blank_slide()
    add_header(s3, "3", "Root Cause Analysis", "Problem Statement: Key Structural Failures in Modern SOCs", "Analyzing critical bottlenecks across data volume, cognitive saturation, and remediation latency")

    prob_cards = [
        (Inches(0.8), Inches(1.6), Inches(5.7), Inches(2.55), "1. Alert Fatigue & Noise Explosion", [
            ("Overwhelming Volume", "Tier-1 analysts receive 500+ alerts daily; 83% are benign noise or misconfigurations."),
            ("High Miss Rate", "Up to 62% of security alerts are closed without thorough investigation due to burnout."),
            ("Analyst Desensitization", "Repetitive IOC lookups lead to cognitive exhaustion and catastrophic security blindspots.")
        ]),
        (Inches(6.8), Inches(1.6), Inches(5.7), Inches(2.55), "2. Context Fragmentation & Data Silos", [
            ("Incompatible Schemas", "Disparate log formats across AWS GuardDuty, CrowdStrike, Okta, and Zeek network logs."),
            ("Missing Graph Context", "Relational SIEM logs fail to connect multi-hop lateral movement across hosts and cloud roles."),
            ("Manual Enrichment Delay", "Querying external threat intelligence feeds takes 5-15 minutes per single alert.")
        ]),
        (Inches(0.8), Inches(4.35), Inches(5.7), Inches(2.55), "3. Escalation Latency & High MTTR", [
            ("Idle Handoff Latency", "Tier-1 to Tier-3 escalation queues introduce 4 to 24 hours of investigation delay."),
            ("Critical Dwell Time", "Average industry dwell time exceeds 4.3 days (103 hours), enabling massive data exfiltration."),
            ("Unrepeatable Playbooks", "Human manual execution varies wildly across shifts and analyst experience levels.")
        ]),
        (Inches(6.8), Inches(4.35), Inches(5.7), Inches(2.55), "4. Remediation Hazards & Vendor Lock-In", [
            ("Blast-Radius Risks", "Manual host isolation risks knocking down business-critical production domain controllers."),
            ("Exorbitant Ingest Costs", "Commercial SIEMs charge thousands per GB/day, forcing enterprises to discard logs."),
            ("Air-Gap Incompatibility", "SaaS-only commercial AI tools cannot operate in sovereign, defense, or banking enclaves.")
        ])
    ]
    for left, top, w, h, title, items in prob_cards:
        add_card(s3, left, top, w, h, title)
        add_bullet_list(s3, left + Inches(0.2), top + Inches(0.55), w - Inches(0.4), h - Inches(0.65), items, font_size=10.5)

    # =========================================================================
    # SLIDE 4: OBJECTIVES
    # =========================================================================
    s4 = add_blank_slide()
    add_header(s4, "4", "Project Scope", "Primary Objectives of the AiSOC Platform", "Concrete, measurable engineering and research goals established for the project")

    obj_cards = [
        (Inches(0.8), Inches(1.6), Inches(5.7), Inches(2.55), "Objective 1: Universal OCSF Ingestion", ACCENT_BLUE, [
            ("Standardized Normalization", "Develop 16+ first-party data connectors mapping vendor telemetry into OCSF schema."),
            ("High-Throughput Streaming", "Build a Kafka streaming ingest pipeline handling 10,000+ events/sec with zero loss."),
            ("Encrypted Vault", "Implement Fernet AES-128-CBC + HMAC-SHA256 application-level credential encryption.")
        ]),
        (Inches(6.8), Inches(1.6), Inches(5.7), Inches(2.55), "Objective 2: Dual-Stage ML Triage", ACCENT_CYAN, [
            ("85%+ Noise Suppression", "Deploy Stage-1 Isolation Forest to filter out routine background administrative anomalies."),
            ("Priority Ranking", "Implement Stage-2 LambdaRank Learning-to-Rank to compute 0-100 incident urgency scores."),
            ("O(1) Threat Intel", "Integrate in-memory Bloom filter for constant-time sub-millisecond IOC lookup.")
        ]),
        (Inches(0.8), Inches(4.35), Inches(5.7), Inches(2.55), "Objective 3: Real-Time Graph Threat Hunting", ACCENT_AMBER, [
            ("Streaming Neo4j Ingest", "Construct an entity graph with 17 node labels and 14 edge types in real-time."),
            ("Multi-Hop Attack Pathing", "Automatically reconstruct lateral movement traces from initial ingress to domain escalation."),
            ("Natural Language /hunt", "Translate analyst plain English hunting queries into validated KQL/Cypher templates.")
        ]),
        (Inches(6.8), Inches(4.35), Inches(5.7), Inches(2.55), "Objective 4: Gated Response & Sovereignty", ACCENT_ROSE, [
            ("Blast-Radius Safety Gating", "Enforce L0-L4 automation maturity model with human approval gates on high-risk assets."),
            ("Sub-5-Minute MTTR", "Accelerate end-to-end incident response from days to under 4 minutes."),
            ("Air-Gapped Sovereign Readiness", "Enable fully offline execution with local Ollama LLMs and zero cloud dependencies.")
        ])
    ]
    for left, top, w, h, title, col, items in obj_cards:
        add_card(s4, left, top, w, h, title, border_color=col)
        add_bullet_list(s4, left + Inches(0.2), top + Inches(0.55), w - Inches(0.4), h - Inches(0.65), items, font_size=10.5)

    # =========================================================================
    # SLIDE 5: INTRODUCTION
    # =========================================================================
    s5 = add_blank_slide()
    add_header(s5, "5", "Background & Context", "Introduction: The Asymmetric Warfare in Enterprise Cybersecurity", "Evolution from legacy manual SOC operations to autonomous multi-agent cyber defense")

    add_card(s5, Inches(0.8), Inches(1.6), Inches(3.7), Inches(5.3), "The Modern Threat Landscape")
    int_c1 = [
        ("Asymmetric Warfare", "Attackers leverage AI-driven automation to scan and exploit vulnerabilities in milliseconds."),
        ("Multi-Stage Campaigns", "Modern attacks involve sophisticated multi-hop lateral movement across hybrid cloud identity fabrics."),
        ("Ransomware Speed", "Active ransomware encryption begins within 45 minutes of initial perimeter breach."),
        ("Human Capacity Limit", "Human analysts cannot manually keep pace with millions of telemetry events per second.")
    ]
    add_bullet_list(s5, Inches(1.0), Inches(2.2), Inches(3.3), Inches(4.5), int_c1, font_size=11)

    add_card(s5, Inches(4.8), Inches(1.6), Inches(3.7), Inches(5.3), "The Multi-Agent Paradigm Shift")
    int_c2 = [
        ("Beyond Single Chatbots", "Single-prompt LLMs fail in SOCs due to lack of tool integration, hallucination, and state loss."),
        ("Collaborative Multi-Agent DAG", "AiSOC uses specialized agents that reason, plan, and verify actions across discrete stages."),
        ("LangGraph State Machine", "Cyclic graph routing with checkpointing ensures deterministic execution and zero loops."),
        ("Transparent Reasoning", "Every decision is accompanied by a full chain-of-thought provenance and confidence score.")
    ]
    add_bullet_list(s5, Inches(5.0), Inches(2.2), Inches(3.3), Inches(4.5), int_c2, font_size=11)

    add_card(s5, Inches(8.8), Inches(1.6), Inches(3.7), Inches(5.3), "UN SDG Global Alignment")
    int_c3 = [
        ("SDG 9 (Resilient Infra)", "Protects vital digital enterprise infrastructure and democratizes cyber defense via open-source."),
        ("SDG 16 (Peace & Justice)", "Provides tamper-evident cryptographic audit ledgers to combat cybercrime and ensure accountability."),
        ("SDG 8 (Decent Work)", "Eliminates soul-crushing 24/7 alert fatigue, allowing analysts to perform strategic engineering."),
        ("SDG 4 (Quality Education)", "Provides a lightweight 30-second sandbox (aisoc-sandbox demo) for student training.")
    ]
    add_bullet_list(s5, Inches(9.0), Inches(2.2), Inches(3.3), Inches(4.5), int_c3, font_size=11)

    # =========================================================================
    # SLIDE 6: LITERATURE SURVEY
    # =========================================================================
    s6 = add_blank_slide()
    add_header(s6, "6", "Academic & Industrial Background", "Literature Survey: Review of State-of-the-Art Approaches", "Critical review of SIEM evolution, SOAR orchestration, and machine learning triage in cybersecurity")

    lit_cards = [
        (Inches(0.8), Inches(1.6), Inches(5.7), Inches(2.55), "1. SIEM & Rule-Based Correlation Engines", [
            ("Foundational Works", "Splunk, Elastic SIEM, Microsoft Sentinel, IBM QRadar architectures."),
            ("Methodology", "Centralized log aggregation with regex-based alert rules and statistical threshold counting."),
            ("Academic Consensus", "High sensitivity but catastrophic false-positive rate (>80%), with zero intrinsic semantic understanding of attacker intent.")
        ]),
        (Inches(6.8), Inches(1.6), Inches(5.7), Inches(2.55), "2. SOAR Orchestration & Playbook Automation", [
            ("Foundational Works", "Palo Alto Cortex XSOAR, Splunk Phantom, Tines automated workflows."),
            ("Methodology", "Imperative, hardcoded directed acyclic graphs (DAGs) executing scripted API calls on alerts."),
            ("Academic Consensus", "Extremely brittle; minor upstream API or schema changes break workflows, and systems cannot adapt dynamically to novel attack patterns.")
        ]),
        (Inches(0.8), Inches(4.35), Inches(5.7), Inches(2.55), "3. Machine Learning in Anomaly Detection", [
            ("Foundational Works", "Isolation Forests (Liu et al., 2008), LambdaRank (Burges, 2010), Autoencoders."),
            ("Methodology", "Unsupervised outlier detection and supervised Learning-to-Rank for alert scoring."),
            ("Academic Consensus", "Highly effective at noise reduction but requires robust feature engineering and ground-truth contextual enrichment to avoid blind spots.")
        ]),
        (Inches(6.8), Inches(4.35), Inches(5.7), Inches(2.55), "4. Graph Databases & LLM Reasoning in SOCs", [
            ("Foundational Works", "Knowledge Graphs in Cyber (Neo4j), LangChain/LangGraph, MITRE ATT&CK."),
            ("Methodology", "Entity relationship mapping combined with generative AI for natural language triage."),
            ("Academic Consensus", "Graph correlation provides critical multi-hop context; however, LLM action generation MUST be bounded by deterministic safety guardrails.")
        ])
    ]
    for left, top, w, h, title, items in lit_cards:
        add_card(s6, left, top, w, h, title)
        add_bullet_list(s6, left + Inches(0.2), top + Inches(0.55), w - Inches(0.4), h - Inches(0.65), items, font_size=10.5)

    # =========================================================================
    # SLIDE 7: FINDINGS IN LITERATURE SURVEY
    # =========================================================================
    s7 = add_blank_slide()
    add_header(s7, "7", "Research Gap Analysis", "Findings in Literature Survey: The 4 Critical Gaps in Existing Systems", "Key technological deficiencies identified across literature that form the motivation for AiSOC")

    findings = [
        (Inches(0.8), Inches(1.6), Inches(5.7), Inches(2.55), "Gap 1: Absence of Universal Normalization", ACCENT_ROSE, [
            ("Problem", "Every security vendor (AWS, Okta, CrowdStrike, Zeek) emits completely proprietary JSON/syslog schemas."),
            ("Literature Deficiency", "Existing systems rely on dozens of fragile regex parsers that break continuously."),
            ("AiSOC Solution", "Native Open Cybersecurity Schema Framework (OCSF v1.1.0) standardization at the ingest layer.")
        ]),
        (Inches(6.8), Inches(1.6), Inches(5.7), Inches(2.55), "Gap 2: Ingestion-Time Graph Construction Gap", ACCENT_AMBER, [
            ("Problem", "Traditional graph intrusion detection systems process graphs in slow offline batch jobs."),
            ("Literature Deficiency", "Fails to provide active analysts with real-time entity pivoting during live lateral movement."),
            ("AiSOC Solution", "Batched streaming UNWIND queries update Neo4j entity graph (17 nodes, 14 edges) inline with Kafka ingest.")
        ]),
        (Inches(0.8), Inches(4.35), Inches(5.7), Inches(2.55), "Gap 3: Single-Model Triage Inadequacy", ACCENT_CYAN, [
            ("Problem", "Standalone Isolation Forest or standalone neural networks either over-filter or under-filter alerts."),
            ("Literature Deficiency", "Lack of a dual-stage architecture combining unsupervised outlier filtering with supervised ranking."),
            ("AiSOC Solution", "Dual-Stage Pipeline: Isolation Forest (Anomaly Filter) + LambdaRank (Priority Ranking).")
        ]),
        (Inches(6.8), Inches(4.35), Inches(5.7), Inches(2.55), "Gap 4: Dangerous LLM Blast-Radius Hazards", ACCENT_BLUE, [
            ("Problem", "Early LLM security agents directly execute unverified CLI commands, risking accidental infrastructure destruction."),
            ("Literature Deficiency", "Zero mathematical modeling of asset criticality, user tier, or blast-radius impact."),
            ("AiSOC Solution", "Blast-Radius Safety Gating (L0-L4 maturity ladder) with immutable cryptographic audit ledger.")
        ])
    ]
    for left, top, w, h, title, col, items in findings:
        add_card(s7, left, top, w, h, title, border_color=col)
        add_bullet_list(s7, left + Inches(0.2), top + Inches(0.55), w - Inches(0.4), h - Inches(0.65), items, font_size=10.5)

    # =========================================================================
    # SLIDE 8: EXISTING METHODOLOGY
    # =========================================================================
    s8 = add_blank_slide()
    add_header(s8, "8", "Baseline Process", "Existing Methodology: Traditional Multi-Tier SOC Workflow", "Detailed examination of the legacy manual 3-tier escalation and triage funnel")

    # Left: Bullet Description
    add_card(s8, Inches(0.8), Inches(1.6), Inches(4.2), Inches(5.3), "Traditional SOC Workflow Stages")
    ex_bullets = [
        ("Step 1: Unstructured Ingestion", "Raw syslog/JSON collected across siloed SIEM appliances without universal schema mapping."),
        ("Step 2: Static Threshold Rules", "Static regex rules match single events, generating 10,000+ daily alerts (83% benign noise)."),
        ("Step 3: Tier-1 Manual Triage", "Analyst manually copies IPs, hashes, and usernames to check external portals (4-8 hours delay)."),
        ("Step 4: Tier-2 / Tier-3 Escalation", "Escalated to senior engineers via ticketing queues; MTTR reaches 103 hours (4.3 days)."),
        ("Step 5: Manual Containment", "Operator manually logs into firewalls/EDR to isolate hosts with high risk of operational error.")
    ]
    add_bullet_list(s8, Inches(1.0), Inches(2.2), Inches(3.8), Inches(4.5), ex_bullets, font_size=10.5)

    # Right: Custom Diagram
    img_exist = "docs/ppt_figures/ppt_fig_existing_methodology.png"
    add_card(s8, Inches(5.2), Inches(1.6), Inches(7.3), Inches(5.3), None, bg_color=BG_CARD)
    add_image_safe(s8, img_exist, Inches(5.3), Inches(1.7), width=Inches(7.1), height=Inches(5.1))

    # =========================================================================
    # SLIDE 9: DEMERITS IN EXISTING METHODOLOGY
    # =========================================================================
    s9 = add_blank_slide()
    add_header(s9, "9", "Systemic Failures", "Demerits in Existing Methodology: Quantifying the Cost of Inefficiency", "Numerical and operational impact of legacy SOC bottlenecks on enterprise defense")

    demerits = [
        (Inches(0.8), Inches(1.6), Inches(5.7), Inches(2.55), "1. Crippling Alert Fatigue & False Alarms", ACCENT_ROSE, [
            ("83% False Positive Rate", "Massive volume of benign operational alerts masks true advanced persistent threats (APTs)."),
            ("Analyst Desensitization", "High cognitive saturation causes analysts to overlook legitimate credential dumping indicators."),
            ("High Industry Churn", "Average SOC analyst tenure is under 18 months due to chronic exhaustion from manual triage.")
        ]),
        (Inches(6.8), Inches(1.6), Inches(5.7), Inches(2.55), "2. Dangerous Attacker Dwell Time (103 Hours)", ACCENT_AMBER, [
            ("4.3 Days Mean Time to Respond", "Attackers maintain unhindered network persistence, escalating from patient-zero to Domain Admin."),
            ("Rapid Exfiltration Window", "Ransomware operators encrypt files in under 45 minutes; 103 hours of delay is fatal."),
            ("Idle Queue Latency", "70% of total MTTR is spent waiting in unread ticket queues between SOC tiers.")
        ]),
        (Inches(0.8), Inches(4.35), Inches(5.7), Inches(2.55), "3. Missing Multi-Hop Graph Visibility", ACCENT_CYAN, [
            ("Isolated Point Detections", "SIEMs view alerts in isolation; cannot correlate a phishing email with a subsequent PsExec execution."),
            ("Lack of Entity Memory", "Historical attacker infrastructure is forgotten once an alert ticket is marked closed."),
            ("Zero Attack Path Modeling", "Analysts must manually reconstruct network paths without automated graph traversal.")
        ]),
        (Inches(6.8), Inches(4.35), Inches(5.7), Inches(2.55), "4. Remediation Hazards & Prohibitive Costs", ACCENT_BLUE, [
            ("Accidental Outage Risk", "Manual containment commands frequently isolate core DNS/Active Directory servers."),
            ("Commercial Monopolies", "Enterprise SIEM licenses cost millions annually while locking users into closed ecosystems."),
            ("Compliance Blindspots", "Manual ticket logs lack tamper-proof cryptographic audit trails required for legal forensics.")
        ])
    ]
    for left, top, w, h, title, col, items in demerits:
        add_card(s9, left, top, w, h, title, border_color=col)
        add_bullet_list(s9, left + Inches(0.2), top + Inches(0.55), w - Inches(0.4), h - Inches(0.65), items, font_size=10.5)

    # =========================================================================
    # SLIDE 10: PROPOSED METHODOLOGY
    # =========================================================================
    s10 = add_blank_slide()
    add_header(s10, "10", "Proposed Architecture", "Proposed Methodology: The 4-Agent Autonomous Defense Funnel", "Replacing manual triage with an intelligent, collaborative, schema-governed multi-agent pipeline")

    prop_agents = [
        (Inches(0.8), Inches(1.6), Inches(2.8), Inches(5.3), "1. DetectAgent", ACCENT_BLUE, [
            ("Stage", "Ingest & Schema Normalization"),
            ("Input", "Syslog, GuardDuty, Okta, Zeek, EDR"),
            ("Standard", "OCSF JSON Mapping"),
            ("Throughput", "10,000+ EPS via Kafka"),
            ("Role", "Transforms heterogeneous raw logs into standardized OCSF classes and triggers real-time graph node upserts.")
        ]),
        (Inches(3.75), Inches(1.6), Inches(2.8), Inches(5.3), "2. TriageAgent", ACCENT_CYAN, [
            ("Stage", "Dual-Stage Machine Learning"),
            ("Engines", "Bloom Filter + Isolation Forest + LambdaRank"),
            ("Noise Filter", "Suppresses 89.4% Benign Alarms"),
            ("Scoring", "0-100 Confidence & Severity Band"),
            ("Role", "Evaluates behavioral anomalies against baselines, checks C2 IOCs in O(1) time, and filters benign noise.")
        ]),
        (Inches(6.7), Inches(1.6), Inches(2.8), Inches(5.3), "3. HuntAgent", ACCENT_AMBER, [
            ("Stage", "Graph Traversal & Root Cause"),
            ("Engine", "Neo4j Knowledge Graph & Cypher"),
            ("Topology", "17 Node Labels, 14 Edge Types"),
            ("Correlation", "MITRE ATT&CK Matrix Mapping"),
            ("Role", "Executes multi-hop graph queries to uncover lateral movement paths, compromised identities, and patient-zero.")
        ]),
        (Inches(9.65), Inches(1.6), Inches(2.8), Inches(5.3), "4. RespondAgent", ACCENT_ROSE, [
            ("Stage", "Blast-Radius Gated Response"),
            ("Safety Model", "Blast-Radius L0-L4 Maturity Gating"),
            ("Playbooks", "25 Parameterised Actions"),
            ("Auditability", "Cryptographic Audit Ledger"),
            ("Role", "Executes verified containment playbooks with automated asset impact calculation and human-in-the-loop approval.")
        ])
    ]
    for left, top, w, h, title, col, items in prop_agents:
        add_card(s10, left, top, w, h, title, border_color=col)
        add_bullet_list(s10, left + Inches(0.15), top + Inches(0.55), w - Inches(0.3), h - Inches(0.65), items, font_size=10.5)

    # =========================================================================
    # SLIDE 11: SYSTEM ARCHITECTURE OF PROPOSED METHODOLOGY
    # =========================================================================
    s11 = add_blank_slide()
    add_header(s11, "11", "System Blueprint", "System Architecture of Proposed Methodology", "End-to-end multi-layer architecture integrating streaming ingest, ML scoring, graph correlation, and web rail")

    add_card(s11, Inches(0.8), Inches(1.6), Inches(4.2), Inches(5.3), "Architecture Subsystems")
    arch_bullets = [
        ("1. Ingest Fabric", "16+ first-party connectors feed raw logs to distributed Kafka topics with OCSF schema mapping."),
        ("2. ML & Graph Engine", "In-memory Bloom filters, Isolation Forest, LambdaRank ML, and Neo4j real-time entity graph."),
        ("3. LangGraph Orchestrator", "Cyclic state machine coordinating DetectAgent, TriageAgent, HuntAgent, and RespondAgent."),
        ("4. Analyst Workbench", "Next.js 14 Web Portal with real-time WebSocket Alert Queue and Investigation Rail."),
        ("5. Security Fabric", "Fernet AES-128 Credential Vault and immutable SHA-256 audit ledger.")
    ]
    add_bullet_list(s11, Inches(1.0), Inches(2.2), Inches(3.8), Inches(4.5), arch_bullets, font_size=10.5)

    img_arch = "docs/ppt_figures/ppt_fig_system_architecture.png"
    add_card(s11, Inches(5.2), Inches(1.6), Inches(7.3), Inches(5.3), None, bg_color=BG_CARD)
    add_image_safe(s11, img_arch, Inches(5.3), Inches(1.7), width=Inches(7.1), height=Inches(5.1))

    # =========================================================================
    # SLIDE 12: LIST OF MODULES IN PROPOSED METHODOLOGY
    # =========================================================================
    s12 = add_blank_slide()
    add_header(s12, "12", "Module Breakdown", "List of Modules in Proposed Methodology", "The four interconnected technical modules comprising the AiSOC autonomous platform")

    modules_list = [
        (Inches(0.8), Inches(1.6), Inches(5.7), Inches(2.55), "Module 1: Telemetry Ingestion & OCSF Engine", ACCENT_BLUE, [
            ("Core Focus", "High-Throughput Streaming Log Normalization & Schema Standard"),
            ("Key Technologies", "FastAPI, Apache Kafka, Pydantic v2, OCSF Schema v1.1.0"),
            ("Primary Function", "Ingests raw telemetry across 16+ connectors, decrypts vault secrets, and validates standard OCSF JSON records.")
        ]),
        (Inches(6.8), Inches(1.6), Inches(5.7), Inches(2.55), "Module 2: Dual-Stage ML Triage & Threat Intel", ACCENT_CYAN, [
            ("Core Focus", "Intelligent False-Positive Suppression & Priority Ranking"),
            ("Key Technologies", "Scalable Bloom Filter, Scikit-learn (Isolation Forest), LightGBM (LambdaRank)"),
            ("Primary Function", "Filters 89.4% benign noise, performs sub-millisecond C2 IOC matching, and generates 0-100 severity scores.")
        ]),
        (Inches(0.8), Inches(4.35), Inches(5.7), Inches(2.55), "Module 3: Knowledge Graph Threat Hunting", ACCENT_AMBER, [
            ("Core Focus", "Streaming Entity Graph, Multi-Hop Correlation & MITRE Mapping"),
            ("Key Technologies", "Neo4j Graph Database, Cypher Query Language, LangChain RAG"),
            ("Primary Function", "Reconstructs attack paths (17 nodes / 14 edges), maps MITRE techniques, and provides natural-language /hunt surface.")
        ]),
        (Inches(6.8), Inches(4.35), Inches(5.7), Inches(2.55), "Module 4: Blast-Radius Gated Response & SOAR", ACCENT_ROSE, [
            ("Core Focus", "Deterministic Safety Gating, Playbook Automation & Audit Ledger"),
            ("Key Technologies", "LangGraph State Machine, Celery Workers, SSRF Guard, Fernet Vault"),
            ("Primary Function", "Enforces L0-L4 maturity model, executes parameterised playbooks, and records immutable tamper-evident logs.")
        ])
    ]
    for left, top, w, h, title, col, items in modules_list:
        add_card(s12, left, top, w, h, title, border_color=col)
        add_bullet_list(s12, left + Inches(0.2), top + Inches(0.55), w - Inches(0.4), h - Inches(0.65), items, font_size=10.5)

    # =========================================================================
    # SLIDE 13: MODULE 1 (DESCRIPTION)
    # =========================================================================
    s13 = add_blank_slide()
    add_header(s13, "13", "Module Specification", "Module 1: Telemetry Ingestion & OCSF Normalization Engine", "Standardizing heterogeneous enterprise telemetry into unified Open Cybersecurity Schema Framework")

    add_card(s13, Inches(0.8), Inches(1.6), Inches(4.2), Inches(5.3), "Module 1 Technical Details")
    m1_bullets = [
        ("16+ First-Party Connectors", "Pre-built connectors for AWS GuardDuty, CrowdStrike, Okta, Sysdig, Zeek, Tines, Cloudflare ZT, Vault, etc."),
        ("Kafka Distributed Ingest", "Partitioned message broker sustaining 10,000+ EPS with guaranteed delivery."),
        ("OCSF JSON Normalization", "Maps raw logs into standard classes (Authentication, Process Activity, Network Traffic)."),
        ("Encrypted Credential Vault", "Sensitive auth tokens stored as vault:v1:<base64> encrypted with Fernet AES-128-CBC + HMAC-SHA256."),
        ("5-Tier Severity Ladder", "Preserves exact vendor severity (info, low, medium, high, critical) without collapsing.")
    ]
    add_bullet_list(s13, Inches(1.0), Inches(2.2), Inches(3.8), Inches(4.5), m1_bullets, font_size=10.5)

    img_m1 = "docs/ppt_figures/ppt_fig_module1_ingest.png"
    add_card(s13, Inches(5.2), Inches(1.6), Inches(7.3), Inches(5.3), None, bg_color=BG_CARD)
    add_image_safe(s13, img_m1, Inches(5.3), Inches(1.7), width=Inches(7.1), height=Inches(5.1))

    # =========================================================================
    # SLIDE 14: MODULE 2 (DESCRIPTION)
    # =========================================================================
    s14 = add_blank_slide()
    add_header(s14, "14", "Module Specification", "Module 2: Dual-Stage ML Triage & Threat Intelligence Filtering", "In-memory Bloom filter threat intel matching and dual-stage machine learning noise reduction")

    add_card(s14, Inches(0.8), Inches(1.6), Inches(4.2), Inches(5.3), "Module 2 Technical Details")
    m2_bullets = [
        ("In-Memory Bloom Filter", "Evaluates 50,000+ IOCs/sec in constant O(1) time with mathematical zero false negatives."),
        ("Stage-1: Isolation Forest", "Unsupervised anomaly detection scoring s(x, n) = 2^(-E(h(x))/c(n)) across 100 decision trees to filter benign administrative noise."),
        ("Stage-2: LambdaRank", "Supervised Learning-to-Rank optimizing pairwise loss λ_ij to prioritize true security incidents."),
        ("89.4% Noise Suppression", "Proven suppression of false positives, reducing 500+ daily alerts to actionable cases."),
        ("Dynamic Scoring Output", "Emits calibrated 0-100 Confidence score and assigned severity band.")
    ]
    add_bullet_list(s14, Inches(1.0), Inches(2.2), Inches(3.8), Inches(4.5), m2_bullets, font_size=10.5)

    img_m2 = "docs/ppt_figures/ppt_fig_module2_ml_triage.png"
    add_card(s14, Inches(5.2), Inches(1.6), Inches(7.3), Inches(5.3), None, bg_color=BG_CARD)
    add_image_safe(s14, img_m2, Inches(5.3), Inches(1.7), width=Inches(7.1), height=Inches(5.1))

    # =========================================================================
    # SLIDE 15: MODULE 3 (DESCRIPTION)
    # =========================================================================
    s15 = add_blank_slide()
    add_header(s15, "15", "Module Specification", "Module 3: Real-Time Knowledge Graph & Multi-Hop Threat Hunting", "Streaming Neo4j graph entity correlation, attack path pivoting, and natural language threat hunting")

    add_card(s15, Inches(0.8), Inches(1.6), Inches(4.2), Inches(5.3), "Module 3 Technical Details")
    m3_bullets = [
        ("Graph at Ingest", "Neo4j graph populated in real-time via batched UNWIND transactions without blocking ingest."),
        ("Comprehensive Topology", "Models 17 node types (User, Process, Host, IP, Alert) and 14 edge types (SPAWNED_ON, AUTHENTICATED_TO)."),
        ("Multi-Hop Attack Correlation", "Uncovers complex lateral movement chains (e.g. User -> PowerShell -> DCSync -> DC-01)."),
        ("MITRE ATT&CK Matrix", "Tags MITRE tactics (Initial Access, Credential Dumping T1003, Lateral Movement T1021)."),
        ("Natural Language /hunt", "Translates analyst plain-language prompts into syntax-validated KQL, SPL, and Cypher templates.")
    ]
    add_bullet_list(s15, Inches(1.0), Inches(2.2), Inches(3.8), Inches(4.5), m3_bullets, font_size=10.5)

    img_m3 = "docs/ppt_figures/ppt_fig_module3_graph_hunt.png"
    add_card(s15, Inches(5.2), Inches(1.6), Inches(7.3), Inches(5.3), None, bg_color=BG_CARD)
    add_image_safe(s15, img_m3, Inches(5.3), Inches(1.7), width=Inches(7.1), height=Inches(5.1))

    # =========================================================================
    # SLIDE 16: MODULE 4 (DESCRIPTION)
    # =========================================================================
    s16 = add_blank_slide()
    add_header(s16, "16", "Module Specification", "Module 4: Blast-Radius Gated Autonomous Response & SOAR Studio", "Automated incident containment governed by strict L0-L4 maturity gating and immutable audit ledger")

    add_card(s16, Inches(0.8), Inches(1.6), Inches(4.2), Inches(5.3), "Module 4 Technical Details")
    m4_bullets = [
        ("Blast-Radius Function", "B(Action) = Σ [w_k * Impact(Asset_k, Action)] evaluates asset criticality and operational risk."),
        ("L0-L4 Maturity Ladder", "L0: Read-only; L1: Low impact (flush cache); L2: Moderate (temp IP block); L3/L4: High impact (requires human sign-off)."),
        ("25 Parameterised Playbooks", "Automated workflows for host quarantine, session revocation, firewall blocking, and token rotation."),
        ("SSRF & Safety Guard", "All outbound HTTP actions verified against private IP and cloud metadata blocklists."),
        ("Cryptographic Audit Ledger", "Immutable chain-of-thought ledger capturing analyst overrides, token signatures, and justification.")
    ]
    add_bullet_list(s16, Inches(1.0), Inches(2.2), Inches(3.8), Inches(4.5), m4_bullets, font_size=10.5)

    img_m4 = "docs/ppt_figures/ppt_fig_module4_blast_radius.png"
    add_card(s16, Inches(5.2), Inches(1.6), Inches(7.3), Inches(5.3), None, bg_color=BG_CARD)
    add_image_safe(s16, img_m4, Inches(5.3), Inches(1.7), width=Inches(7.1), height=Inches(5.1))

    # =========================================================================
    # SLIDE 17: EXPERIMENTAL RESULTS
    # =========================================================================
    s17 = add_blank_slide()
    add_header(s17, "17", "Empirical Evaluation", "Experimental Results: Benchmarks, Graphs & Performance Metrics", "Validation against a standardized dataset of 200 incidents and 50,000 security telemetry events")

    # 4 Metric Cards across Top
    metric_cards = [
        (Inches(0.8), Inches(1.5), Inches(2.7), Inches(1.4), "89.4%", "Alert Noise Reduction", ACCENT_GREEN),
        (Inches(3.8), Inches(1.5), Inches(2.7), Inches(1.4), "3.8 min", "Mean Time to Respond", ACCENT_CYAN),
        (Inches(6.8), Inches(1.5), Inches(2.7), Inches(1.4), "96.4%", "MITRE ATT&CK Accuracy", ACCENT_BLUE),
        (Inches(9.8), Inches(1.5), Inches(2.7), Inches(1.4), "100%", "Zero-Outage Safety Rate", ACCENT_AMBER)
    ]
    for left, top, w, h, val, lbl, col in metric_cards:
        add_card(s17, left, top, w, h, None, border_color=col)
        tb = s17.shapes.add_textbox(left, top + Inches(0.1), w, Inches(0.65))
        tf = tb.text_frame
        p = tf.paragraphs[0]
        p.text = val
        p.font.name = 'Calibri'
        p.font.size = Pt(26)
        p.font.bold = True
        p.font.color.rgb = col
        p.alignment = PP_ALIGN.CENTER
        
        tb2 = s17.shapes.add_textbox(left, top + Inches(0.75), w, Inches(0.45))
        tf2 = tb2.text_frame
        p2 = tf2.paragraphs[0]
        p2.text = lbl
        p2.font.name = 'Calibri'
        p2.font.size = Pt(10.5)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_MAIN
        p2.alignment = PP_ALIGN.CENTER

    # Left: Custom Experimental Results Diagram
    img_res = "docs/ppt_figures/ppt_fig_experimental_results.png"
    add_card(s17, Inches(0.8), Inches(3.05), Inches(7.0), Inches(3.9), None, bg_color=BG_CARD)
    add_image_safe(s17, img_res, Inches(0.9), Inches(3.15), width=Inches(6.8), height=Inches(3.7))

    # Right: Experimental Findings Card
    add_card(s17, Inches(8.0), Inches(3.05), Inches(4.5), Inches(3.9), "Key Empirical Findings")
    res_findings = [
        ("1,600x MTTR Acceleration", "Reduced mean response time from 103.2 hours (4.3 days) to 3.8 minutes on validated attacks."),
        ("Precision & Recall", "Achieved 94.8% investigation completeness and 96.4% MITRE technique classification accuracy."),
        ("Zero Destructive Failures", "Blast-radius safety checks prevented 100% of unintended containment actions on critical servers."),
        ("Substrate Honesty", "All synthetic and real evaluation splits explicitly separated and verified against committed CI test gates.")
    ]
    add_bullet_list(s17, Inches(8.2), Inches(3.55), Inches(4.1), Inches(3.2), res_findings, font_size=10)

    # =========================================================================
    # SLIDE 18: CONCLUSION & FUTURE WORK
    # =========================================================================
    s18 = add_blank_slide()
    add_header(s18, "18", "Project Summary", "Conclusion & Future Work: Advancing Autonomous Cybersecurity", "Key research milestones achieved and strategic roadmap for future enhancements")

    add_card(s18, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.3), "Project Milestones & Conclusion", border_color=ACCENT_CYAN)
    conc_bullets = [
        ("Full-Lifecycle Implementation", "Delivered complete open-source 4-agent autonomous SOC platform unifying 16+ enterprise connectors under OCSF standards."),
        ("Validated 89.4% Noise Reduction", "Empirically proved dual-stage ML triage filters 89.4% of false alarms while reducing MTTR from 103 hours to 3.8 minutes."),
        ("Deterministic Safety & Audit", "Engineered Blast-Radius L0-L4 maturity model, eliminating accidental outages and ensuring cryptographic forensic auditability."),
        ("Physical Testbed Verification", "Validated across enterprise Cisco Catalyst 3850, Sophos XG210 firewall, and Proxmox VE server cluster."),
        ("Production Open-Source Milestone", "Delivered deployable Next.js 14 web console, FastAPI microservices, and 939 executable detection rules.")
    ]
    add_bullet_list(s18, Inches(1.0), Inches(2.2), Inches(5.3), Inches(4.5), conc_bullets, font_size=11)

    add_card(s18, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.3), "Future Research & Development", border_color=ACCENT_BLUE)
    fut_bullets = [
        ("Kernel eBPF Telemetry Ingestion", "Implement in-kernel eBPF probes for sub-millisecond rootkit detection bypassing user-space log tampering."),
        ("Federated Multi-Tenant Threat Intel", "Develop zero-knowledge proof federated learning allowing sovereign organizations to share C2 IOCs securely."),
        ("Self-Evolving Detection Engineering", "Build generative adversary emulation agents that automatically write, test, and tune Sigma/YARA rules."),
        ("Hardware-Accelerated Graph Inference", "Deploy GPU-accelerated Graph Neural Networks (GNNs) for predictive lateral movement path blocking.")
    ]
    add_bullet_list(s18, Inches(7.0), Inches(2.2), Inches(5.3), Inches(4.5), fut_bullets, font_size=11)

    # =========================================================================
    # SLIDE 19: REFERENCES (MINIMUM 15 REFERENCES)
    # =========================================================================
    s19 = add_blank_slide()
    add_header(s19, "19", "Academic & Industrial Standards", "References: Key Foundational Literature & Enterprise Standards", "Comprehensive bibliography of 15 peer-reviewed papers, international standards, and specifications")

    # 2 Columns of References
    add_card(s19, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.3), "Academic & Architectural References (1-8)")
    refs_col1 = [
        "[1] Open Cybersecurity Schema Framework (OCSF) v1.1.0 Specification. Linux Foundation, 2023.",
        "[2] F. T. Liu, K. M. Ting, and Z.-H. Zhou, 'Isolation Forest,' in IEEE 8th International Conference on Data Mining (ICDM), 2008, pp. 413-422.",
        "[3] C. J. Burges, 'From RankNet to LambdaRank to LambdaMART: An Overview,' Microsoft Research Technical Report, MSR-TR-2010-82, 2010.",
        "[4] B. H. Bloom, 'Space/Time Trade-offs in Hash Coding with Allowable Errors,' Communications of the ACM, vol. 13, no. 7, pp. 422-426, 1970.",
        "[5] B. E. Strom et al., 'MITRE ATT&CK: Design and Philosophy,' The MITRE Corporation, Technical Report, 2020.",
        "[6] Neo4j Graph Database Architecture & Cypher Query Optimization Manual, Neo4j Inc., 2024.",
        "[7] H. Chase et al., 'LangChain & LangGraph: Multi-Agent Cyclic Graphs for LLMs,' LangChain Research, 2024.",
        "[8] NIST Special Publication 800-61 Rev. 2, 'Computer Security Incident Handling Guide,' NIST, 2012."
    ]
    add_bullet_list(s19, Inches(1.0), Inches(2.15), Inches(5.3), Inches(4.6), refs_col1, font_size=9.2)

    add_card(s19, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.3), "Standards & Framework References (9-15)")
    refs_col2 = [
        "[9] ISO/IEC 27035-1:2023, 'Information technology — Information security incident management,' ISO/IEC, 2023.",
        "[10] CISA, 'Cybersecurity Incident and Vulnerability Response Playbooks,' Cybersecurity and Infrastructure Security Agency, 2021.",
        "[11] Splunk Inc., 'Security Information and Event Management (SIEM) Architecture & Best Practices,' Splunk Core Docs, 2023.",
        "[12] J. Kreps, N. Narkhede, and J. Rao, 'Kafka: A Distributed Messaging System for Log Processing,' NetDB, 2011.",
        "[13] F. Roth and T. Patzke, 'Sigma: Generic Signature Format for SIEM Systems,' Sigma-HQ, 2024.",
        "[14] Zeek Project, 'Zeek Network Security Monitor: Architecture and Scripting,' The Zeek Project, 2024.",
        "[15] United Nations, 'The Sustainable Development Goals Report 2023,' United Nations Department of Economic and Social Affairs, 2023."
    ]
    add_bullet_list(s19, Inches(7.0), Inches(2.15), Inches(5.3), Inches(4.6), refs_col2, font_size=9.2)

    # =========================================================================
    # SLIDE 20: CLOSING / THANK YOU & LIVE DEMO
    # =========================================================================
    s20 = add_blank_slide()
    
    tb_thank = s20.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(11.7), Inches(1.5))
    tf_th = tb_thank.text_frame
    p_th = tf_th.paragraphs[0]
    p_th.text = "THANK YOU!"
    p_th.font.name = 'Calibri'
    p_th.font.size = Pt(42)
    p_th.font.bold = True
    p_th.font.color.rgb = ACCENT_CYAN
    p_th.alignment = PP_ALIGN.CENTER

    p_th_sub = tf_th.add_paragraph()
    p_th_sub.text = "Questions, Feedback & Live Project Demonstration"
    p_th_sub.font.name = 'Calibri'
    p_th_sub.font.size = Pt(20)
    p_th_sub.font.color.rgb = TEXT_MAIN
    p_th_sub.alignment = PP_ALIGN.CENTER
    p_th_sub.space_before = Pt(10)

    add_card(s20, Inches(2.0), Inches(3.6), Inches(9.333), Inches(3.2), "AiSOC PROJECT REPOSITORY & DEMONSTRATION ACCESS")
    demo_details = [
        ("Project Core", "Autonomous Multi-Agent SOC Architecture (Open Source MIT License)"),
        ("Live Interactive Demo", "tryaisoc.com/dashboard  (Active Multi-Tenant Web Console)"),
        ("Instant Cold-Start Demo", "pip install aisoc-sandbox && aisoc-sandbox demo  (<30 seconds offline)"),
        ("Team Contact", "Yashvinthan M (231061101162) | Tharun Kumar D (231061101150)"),
        ("Team Contact", "Sanjeev V (231061101140) | Srinithi J S (231061101149)"),
        ("Department", "Department of Computer Science and Engineering, Faculty of Engineering & Tech")
    ]
    add_bullet_list(s20, Inches(2.3), Inches(4.2), Inches(8.7), Inches(2.4), demo_details, font_size=11)

    # Save Presentation
    out_file = "AiSOC_Mini_Project_Presentation.pptx"
    prs.save(out_file)
    print(f"SUCCESS: Generated {len(prs.slides)} slides in '{out_file}' conforming exactly to 19-section syllabus!")

if __name__ == '__main__':
    build_presentation()
