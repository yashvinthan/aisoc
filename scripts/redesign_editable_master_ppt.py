import os
import sys
import shutil
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

# =============================================================================
# COLOR PALETTE (Dark Cybersecurity Theme)
# =============================================================================
BG_DARK = RGBColor(15, 23, 42)        # Slate 900 (#0f172a)
BG_CARD = RGBColor(30, 41, 59)        # Slate 800 (#1e293b)
BG_CARD_LIGHT = RGBColor(51, 65, 85)  # Slate 700 (#334155)
BG_CARD_INNER = RGBColor(24, 32, 47)  # Slate 850
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
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.32), Inches(11.7), Inches(0.32))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        tf_cat.margin_left = tf_cat.margin_top = tf_cat.margin_right = tf_cat.margin_bottom = 0
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = f"SECTION {slide_num} | {category.upper()}"
        p_cat.font.name = 'Calibri'
        p_cat.font.size = Pt(11.5)
        p_cat.font.bold = True
        p_cat.font.color.rgb = ACCENT_CYAN

        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.62), Inches(11.7), Inches(0.55))
        tf_t = title_box.text_frame
        tf_t.word_wrap = True
        tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
        p_t = tf_t.paragraphs[0]
        p_t.text = title
        p_t.font.name = 'Calibri'
        p_t.font.size = Pt(21)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_MAIN

        if subtitle:
            sub_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.15), Inches(11.7), Inches(0.32))
            tf_s = sub_box.text_frame
            tf_s.word_wrap = True
            tf_s.margin_left = tf_s.margin_top = tf_s.margin_right = tf_s.margin_bottom = 0
            p_s = tf_s.paragraphs[0]
            p_s.text = subtitle
            p_s.font.name = 'Calibri'
            p_s.font.size = Pt(12)
            p_s.font.color.rgb = TEXT_MUTED

    def add_card(slide, left, top, width, height, title=None, title_color=ACCENT_BLUE, bg_color=BG_CARD, border_color=BORDER_COLOR, corner_radius=0.03):
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = bg_color
        shape.line.color.rgb = border_color
        shape.line.width = Pt(1.5)
        try:
            shape.adjustments[0] = corner_radius
        except Exception:
            pass
        
        if title:
            tb = slide.shapes.add_textbox(left + Inches(0.22), top + Inches(0.18), width - Inches(0.44), Inches(0.42))
            tf = tb.text_frame
            tf.word_wrap = True
            tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
            p = tf.paragraphs[0]
            p.text = title
            p.font.name = 'Calibri'
            p.font.size = Pt(13.5)
            p.font.bold = True
            p.font.color.rgb = title_color
        return shape

    def add_bullet_list(slide, left, top, width, height, items, font_size=12, space_after=10, text_color=TEXT_MAIN, prefix_color=ACCENT_CYAN):
        tb = slide.shapes.add_textbox(left, top, width, height)
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        
        for i, item in enumerate(items):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.space_after = Pt(space_after)
            p.font.name = 'Calibri'
            p.font.size = Pt(font_size)
            
            if isinstance(item, tuple):
                prefix, text = item
                r1 = p.add_run()
                r1.text = prefix + ": "
                r1.font.bold = True
                r1.font.color.rgb = prefix_color
                
                r2 = p.add_run()
                r2.text = text
                r2.font.bold = False
                r2.font.color.rgb = text_color
            else:
                r = p.add_run()
                r.text = item
                r.font.color.rgb = text_color

    def add_spec_box(slide, left, top, width, height, line1, line2=None, col=ACCENT_CYAN, bg_col=BG_CARD_LIGHT):
        box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        box.fill.solid()
        box.fill.fore_color.rgb = bg_col
        box.line.color.rgb = col
        box.line.width = Pt(1.2)
        try:
            box.adjustments[0] = 0.06
        except Exception:
            pass
        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.12)
        tf.margin_right = Inches(0.12)
        tf.margin_top = Inches(0.08)
        tf.margin_bottom = Inches(0.08)
        
        p1 = tf.paragraphs[0]
        p1.text = line1
        p1.font.name = 'Calibri'
        p1.font.size = Pt(10.5)
        p1.font.bold = True
        p1.font.color.rgb = col
        p1.alignment = PP_ALIGN.CENTER
        
        if line2:
            p2 = tf.add_paragraph()
            p2.text = line2
            p2.font.name = 'Calibri'
            p2.font.size = Pt(9.5)
            p2.font.bold = False
            p2.font.color.rgb = TEXT_MAIN
            p2.alignment = PP_ALIGN.CENTER
            p2.space_before = Pt(2)
        return box

    def add_arrow(slide, left, top, width, height, col=ACCENT_CYAN):
        arr = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, left, top, width, height)
        arr.fill.solid()
        arr.fill.fore_color.rgb = col
        arr.line.fill.background()
        return arr

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
    # SLIDE 1: TITLE & COVER
    # =========================================================================
    s1 = add_blank_slide()
    
    logo_path = "docs/figures/dr_mgr_logo.png"
    if os.path.exists(logo_path):
        logo_bg = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.5), Inches(0.45), Inches(3.0), Inches(0.85))
        logo_bg.fill.solid()
        logo_bg.fill.fore_color.rgb = WHITE
        logo_bg.line.color.rgb = ACCENT_CYAN
        logo_bg.line.width = Pt(1.5)
        try:
            logo_bg.adjustments[0] = 0.08
        except Exception:
            pass
        s1.shapes.add_picture(logo_path, Inches(9.65), Inches(0.52), width=Inches(2.7), height=Inches(0.71))

    tb_badge = s1.shapes.add_textbox(Inches(0.8), Inches(0.55), Inches(8.5), Inches(0.4))
    tf_b = tb_badge.text_frame
    p_b = tf_b.paragraphs[0]
    p_b.text = "BACHELOR OF TECHNOLOGY | MINI PROJECT PRESENTATION & VIVA VOCE"
    p_b.font.name = 'Calibri'
    p_b.font.size = Pt(12)
    p_b.font.bold = True
    p_b.font.color.rgb = ACCENT_CYAN

    tb_title = s1.shapes.add_textbox(Inches(0.8), Inches(1.25), Inches(11.7), Inches(1.4))
    tf_t = tb_title.text_frame
    tf_t.word_wrap = True
    p_t = tf_t.paragraphs[0]
    p_t.text = "AiSOC: Autonomous AI-Powered Security Operations Center"
    p_t.font.name = 'Calibri'
    p_t.font.size = Pt(30)
    p_t.font.bold = True
    p_t.font.color.rgb = TEXT_MAIN

    p_sub = tf_t.add_paragraph()
    p_sub.text = "Automated Threat Detection, Intelligent Machine Learning Triage, and Instant Incident Response"
    p_sub.font.name = 'Calibri'
    p_sub.font.size = Pt(13.5)
    p_sub.font.color.rgb = ACCENT_BLUE
    p_sub.space_before = Pt(6)

    add_card(s1, Inches(0.8), Inches(3.0), Inches(5.7), Inches(3.9), "PROJECT TEAM MEMBERS", title_color=ACCENT_BLUE, corner_radius=0.03)
    team_members = [
        ("Yashvinthan M", "231061101162  (Lead AI Architecture & Backend)"),
        ("Tharun Kumar D", "231061101150  (Machine Learning Triage & Detection)"),
        ("Sanjeev V", "231061101140  (Log Ingestion & Cloud Connectors)"),
        ("Srinithi J S", "231061101149  (Analyst Dashboard & Response Studio)")
    ]
    add_bullet_list(s1, Inches(1.02), Inches(3.6), Inches(5.25), Inches(2.3), team_members, font_size=12.5, space_after=10)
    add_spec_box(s1, Inches(1.02), Inches(5.85), Inches(5.25), Inches(0.85), "Team: 4-Member Collaborative Engineering Group", "Tech Stack: Python FastAPI | Next.js 14 | Neo4j | Kafka | ML Models", col=ACCENT_BLUE, bg_col=BG_CARD_LIGHT)

    add_card(s1, Inches(6.8), Inches(3.0), Inches(5.7), Inches(3.9), "DEPARTMENT & ACADEMIC DETAILS", title_color=ACCENT_CYAN, corner_radius=0.03)
    dept_info = [
        ("Department", "Department of Computer Science and Engineering"),
        ("Institution", "Faculty of Engineering & Technology"),
        ("Academic Year", "2025-2026 (July 2026 Examination)"),
        ("Project Domain", "Artificial Intelligence & Cybersecurity Operations"),
        ("Hardware Testbed", "Cisco Catalyst Switch & Proxmox Server Cluster")
    ]
    add_bullet_list(s1, Inches(7.02), Inches(3.6), Inches(5.25), Inches(2.3), dept_info, font_size=12.5, space_after=8)
    add_spec_box(s1, Inches(7.02), Inches(5.85), Inches(5.25), Inches(0.85), "Degree Evaluation: B.Tech Mini Project Viva Defense", "Dr. M.G.R. Educational and Research Institute (Deemed to be University)", col=ACCENT_CYAN, bg_col=BG_CARD_LIGHT)

    # =========================================================================
    # SLIDE 2: ABSTRACT (EXECUTIVE VISUAL SUMMARY)
    # =========================================================================
    s2 = add_blank_slide()
    add_header(s2, "2", "Executive Summary", "Abstract: Autonomous Security Operations Platform", "High-level overview of the problem, AI methodology, and validated results")

    pills = [
        (Inches(0.8), "89.4% Noise Filtered", ACCENT_GREEN),
        (Inches(3.8), "3.8 min Response Time", ACCENT_CYAN),
        (Inches(6.8), "16+ Data Connectors", ACCENT_BLUE),
        (Inches(9.8), "100% Safe Gated Actions", ACCENT_AMBER)
    ]
    for left, txt, col in pills:
        pill = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, Inches(1.5), Inches(2.7), Inches(0.45))
        pill.fill.solid()
        pill.fill.fore_color.rgb = BG_CARD_LIGHT
        pill.line.color.rgb = col
        pill.line.width = Pt(1.5)
        try:
            pill.adjustments[0] = 0.08
        except Exception:
            pass
        p = pill.text_frame.paragraphs[0]
        p.text = txt
        p.font.name = 'Calibri'
        p.font.size = Pt(11.5)
        p.font.bold = True
        p.font.color.rgb = col
        p.alignment = PP_ALIGN.CENTER

    add_card(s2, Inches(0.8), Inches(2.1), Inches(11.7), Inches(5.0), "Project Summary in Simple Terms", title_color=ACCENT_CYAN, border_color=ACCENT_CYAN, corner_radius=0.02)
    abs_bullets = [
        ("The Challenge", "Modern companies receive millions of security logs every day. Human analysts face alert fatigue because over 83% of alerts are harmless false alarms, leading to dangerous delays in catching real attacks."),
        ("Our Solution", "We built AiSOC, an open-source autonomous security platform that replaces slow manual triage with four smart AI agents working together (Detect, Triage, Hunt, Respond)."),
        ("How It Works", "AiSOC standardizes logs from 16+ tools, uses machine learning to instantly filter noise, and maps connected attack steps inside a real-time visual knowledge graph."),
        ("Safety Built-In", "To prevent accidental outages, all high-impact response actions (like isolating a server) are checked with safety rules and require human confirmation."),
        ("Proven Results", "Tested on 200 real attack scenarios, AiSOC filters 89.4% of false alarms, reduces incident response time from 103 hours down to 3.8 minutes, and achieves 96.4% accuracy.")
    ]
    add_bullet_list(s2, Inches(1.02), Inches(2.65), Inches(11.25), Inches(3.6), abs_bullets, font_size=12, space_after=10)
    add_spec_box(s2, Inches(1.02), Inches(6.3), Inches(11.25), Inches(0.6), "Key Takeaway: An intelligent, safe, and open-source platform that cuts incident response time by 99%", col=ACCENT_CYAN, bg_col=BG_CARD_LIGHT)

    # =========================================================================
    # SLIDE 3: PROBLEM STATEMENT (4-BOX VISUAL BOTTLENECK DIAGRAM)
    # =========================================================================
    s3 = add_blank_slide()
    add_header(s3, "3", "Root Cause Analysis", "Problem Statement: Key Failures in Traditional Security Operations", "Four critical problems that make traditional security teams slow and overwhelmed")

    prob_cards = [
        (Inches(0.8), Inches(1.6), Inches(5.7), Inches(2.6), "1. Alert Fatigue & False Alarms", ACCENT_ROSE, [
            ("Too Many Alerts", "Security teams get 500+ alerts daily; over 83% are harmless noise."),
            ("Burnout & Missed Threats", "Analysts get exhausted doing repetitive checks, causing real attacks to be missed."),
            ("Slow Manual Checks", "Looking up every IP address and file hash manually takes 10-15 minutes per alert.")
        ]),
        (Inches(6.8), Inches(1.6), Inches(5.7), Inches(2.6), "2. Disconnected Tools & Log Silos", ACCENT_AMBER, [
            ("Incompatible Formats", "AWS, Firewalls, and Windows logs all use completely different formats."),
            ("No Big Picture", "Traditional tools look at alerts individually and cannot connect multi-step attacks."),
            ("Blind Spots", "Attackers move quietly between cloud and office computers without being linked.")
        ]),
        (Inches(0.8), Inches(4.35), Inches(5.7), Inches(2.6), "3. Slow Escalations & Long Delays", ACCENT_BLUE, [
            ("Passing the Ticket", "Passing alerts between Tier-1, Tier-2, and Tier-3 teams causes 4 to 24 hours of delay."),
            ("Attacker Dwell Time", "Hackers stay hidden in corporate networks for an average of 4.3 days (103 hours)."),
            ("Inconsistent Steps", "Different analysts handle the same security incident in completely different ways.")
        ]),
        (Inches(6.8), Inches(4.35), Inches(5.7), Inches(2.6), "4. Dangerous Actions & High Costs", ACCENT_ROSE, [
            ("Accidental Outages", "Rushing to block a computer can accidentally shut down critical business servers."),
            ("Expensive Software", "Commercial security software costs millions of dollars in annual licensing fees."),
            ("No Privacy Control", "Cloud-only AI tools cannot run in secure banks, defense, or offline networks.")
        ])
    ]
    for left, top, w, h, title, col, items in prob_cards:
        add_card(s3, left, top, w, h, title, title_color=col, border_color=BORDER_COLOR, corner_radius=0.03)
        add_bullet_list(s3, left + Inches(0.22), top + Inches(0.62), w - Inches(0.44), h - Inches(0.7), items, font_size=11.5, space_after=8)

    # =========================================================================
    # SLIDE 4: OBJECTIVES (4 TARGET MATRIX)
    # =========================================================================
    s4 = add_blank_slide()
    add_header(s4, "4", "Project Scope", "Primary Objectives of the AiSOC Project", "Four clear, measurable technical goals achieved in this project")

    obj_cards = [
        (Inches(0.8), Inches(1.6), Inches(5.7), Inches(2.6), "Objective 1: Universal Log Ingestion", ACCENT_BLUE, [
            ("Connect 16+ Data Sources", "Ingest security logs from AWS, Okta, CrowdStrike, and firewalls seamlessly."),
            ("High Speed Pipeline", "Process over 10,000 logs every second with zero data loss using Apache Kafka."),
            ("Standard Data Format", "Convert all vendor logs into one universal cybersecurity standard (OCSF).")
        ]),
        (Inches(6.8), Inches(1.6), Inches(5.7), Inches(2.6), "Objective 2: Smart ML Noise Filtering", ACCENT_CYAN, [
            ("Filter 85%+ False Alarms", "Use AI anomaly detection to automatically discard routine background noise."),
            ("Instant Threat Lookup", "Match known hacker IPs and malicious files in less than 1 millisecond."),
            ("Priority Ranking", "Rank remaining alerts from 0 to 100 so analysts focus on the most dangerous threats first.")
        ]),
        (Inches(0.8), Inches(4.35), Inches(5.7), Inches(2.6), "Objective 3: Real-Time Attack Graph", ACCENT_AMBER, [
            ("Visual Attack Map", "Build a live connected graph showing users, computers, files, and network traffic."),
            ("Trace Lateral Movement", "Automatically trace how an attacker moved from patient-zero to the domain admin."),
            ("Plain English Search", "Let analysts search for threats by typing questions in plain English.")
        ]),
        (Inches(6.8), Inches(4.35), Inches(5.7), Inches(2.6), "Objective 4: Safe & Instant Response", ACCENT_ROSE, [
            ("Sub-5-Minute Response", "Reduce total incident containment time from days to under 4 minutes."),
            ("Safety Guardrails", "Enforce approval checks so critical servers are never shut down by accident."),
            ("Tamper-Proof Audit", "Record every action taken in a secure cryptographic ledger for forensic review.")
        ])
    ]
    for left, top, w, h, title, col, items in obj_cards:
        add_card(s4, left, top, w, h, title, title_color=col, border_color=col, corner_radius=0.03)
        add_bullet_list(s4, left + Inches(0.22), top + Inches(0.62), w - Inches(0.44), h - Inches(0.7), items, font_size=11.5, space_after=8)

    # =========================================================================
    # SLIDE 5: INTRODUCTION (MULTI-AGENT PARADIGM & SDG)
    # =========================================================================
    s5 = add_blank_slide()
    add_header(s5, "5", "Background & Context", "Introduction: The Need for Autonomous AI in Cybersecurity", "Why traditional methods fail against modern cyber attacks and how AI changes the game")

    add_card(s5, Inches(0.8), Inches(1.6), Inches(3.7), Inches(5.4), "Modern Cyber Attacks Move Fast", title_color=ACCENT_ROSE, corner_radius=0.03)
    int_c1 = [
        ("Automated Attackers", "Hackers use automated scripts to scan and exploit systems in seconds."),
        ("Fast Ransomware", "Modern ransomware begins locking files within 45 minutes of entering a network."),
        ("Multi-Stage Breaches", "Attackers steal user logins, jump across computers, and target central servers."),
        ("Humans Cannot Keep Up", "Human analysts cannot manually read millions of logs fast enough to stop active breaches.")
    ]
    add_bullet_list(s5, Inches(1.02), Inches(2.2), Inches(3.25), Inches(3.5), int_c1, font_size=11.5, space_after=10)
    add_spec_box(s5, Inches(1.02), Inches(5.85), Inches(3.25), Inches(0.95), "Speed Reality: <45min Ransomware", "Requires Sub-Second Automated Defense", col=ACCENT_ROSE, bg_col=BG_CARD_LIGHT)

    add_card(s5, Inches(4.8), Inches(1.6), Inches(3.7), Inches(5.4), "Why Multi-Agent AI?", title_color=ACCENT_BLUE, corner_radius=0.03)
    int_c2 = [
        ("Specialized Roles", "Instead of one generic chatbot, AiSOC uses 4 specialized AI agents working as a team."),
        ("Step-by-Step Logic", "Each agent has a clear job: Ingest logs, filter noise, trace attack paths, and respond."),
        ("No Guesswork", "Every decision is checked against strict rules and verified threat intelligence."),
        ("Human Control", "AI handles repetitive tasks, while human experts approve high-risk actions.")
    ]
    add_bullet_list(s5, Inches(5.02), Inches(2.2), Inches(3.25), Inches(3.5), int_c2, font_size=11.5, space_after=10)
    add_spec_box(s5, Inches(5.02), Inches(5.85), Inches(3.25), Inches(0.95), "AI Design: 4 Coordinated Agents", "Reliable Execution with Full Human Oversight", col=ACCENT_BLUE, bg_col=BG_CARD_LIGHT)

    add_card(s5, Inches(8.8), Inches(1.6), Inches(3.7), Inches(5.4), "UN SDG Global Alignment", title_color=ACCENT_CYAN, corner_radius=0.03)
    int_c3 = [
        ("SDG 9: Resilient Infrastructure", "Protects digital enterprise systems from cyber attacks using open-source tools."),
        ("SDG 16: Peace & Justice", "Provides clear, tamper-proof audit trails to hold cybercriminals accountable."),
        ("SDG 8: Decent Work", "Eliminates boring, repetitive night shifts and alert burnout for security workers."),
        ("SDG 4: Quality Education", "Provides a free, lightweight training tool (aisoc-sandbox) for students to learn cybersecurity.")
    ]
    add_bullet_list(s5, Inches(9.02), Inches(2.2), Inches(3.25), Inches(3.5), int_c3, font_size=11.5, space_after=10)
    add_spec_box(s5, Inches(9.02), Inches(5.85), Inches(3.25), Inches(0.95), "Global Goals: UN SDGs 4, 8, 9, 16", "Open-Source Democratization of AI Defense", col=ACCENT_CYAN, bg_col=BG_CARD_LIGHT)

    # =========================================================================
    # SLIDE 6: LITERATURE SURVEY (COMPARATIVE ARCHITECTURE MATRIX)
    # =========================================================================
    s6 = add_blank_slide()
    add_header(s6, "6", "Academic & Industrial Background", "Literature Survey: How Existing Technologies Compare", "Review of traditional SIEM, automation tools, machine learning, and knowledge graphs")

    lit_cards = [
        (Inches(0.8), Inches(1.6), Inches(5.7), Inches(2.6), "1. Traditional SIEM Log Systems", ACCENT_BLUE, [
            ("Technologies", "Splunk, Microsoft Sentinel, IBM QRadar, Elastic SIEM."),
            ("How They Work", "Collect all company logs into one database and trigger alerts using basic keyword rules."),
            ("Key Limitation", "Generates over 80% false alarms and cannot connect attack steps across multiple servers.")
        ]),
        (Inches(6.8), Inches(1.6), Inches(5.7), Inches(2.6), "2. Standard Automation (SOAR) Tools", ACCENT_CYAN, [
            ("Technologies", "Palo Alto Cortex XSOAR, Splunk Phantom, Tines."),
            ("How They Work", "Run predefined scripts when an alert fires (e.g. send an email, block an IP)."),
            ("Key Limitation", "Very brittle; if log formats change or a new attack appears, the automated scripts fail.")
        ]),
        (Inches(0.8), Inches(4.35), Inches(5.7), Inches(2.6), "3. Machine Learning Anomaly Detection", ACCENT_AMBER, [
            ("Technologies", "Isolation Forests, Neural Networks, Supervised Ranking Models."),
            ("How They Work", "Learn normal employee activity and flag unusual behavior automatically."),
            ("Key Limitation", "Single ML models either let real attacks slip by or still produce too many false alarms.")
        ]),
        (Inches(6.8), Inches(4.35), Inches(5.7), Inches(2.6), "4. Knowledge Graphs & AI LLMs", ACCENT_ROSE, [
            ("Technologies", "Neo4j Graph Database, LangChain Multi-Agent, MITRE ATT&CK Matrix."),
            ("How They Work", "Map relationships between devices and use AI to understand incident context."),
            ("Key Limitation", "AI must have strict safety guardrails so it doesn't run dangerous commands by mistake.")
        ])
    ]
    for left, top, w, h, title, col, items in lit_cards:
        add_card(s6, left, top, w, h, title, title_color=col, corner_radius=0.03)
        add_bullet_list(s6, left + Inches(0.22), top + Inches(0.62), w - Inches(0.44), h - Inches(0.7), items, font_size=11.5, space_after=8)

    # =========================================================================
    # SLIDE 7: FINDINGS IN LITERATURE SURVEY (PROBLEM -> AISOC SOLUTION FLOW)
    # =========================================================================
    s7 = add_blank_slide()
    add_header(s7, "7", "Research Gap Analysis", "Findings in Literature Survey: The 4 Critical Gaps We Solved", "Visual problem-to-solution bridge showing how AiSOC overcomes each industry bottleneck")

    gaps_flows = [
        (Inches(1.6), "Gap 1: Fragile Vendor Regex Parsers", "Every vendor uses different log schemas, breaking automated SIEM rules.",
         "AiSOC Solution: Universal OCSF Ingest Engine", "Standardizes 16+ data connectors into clean OCSF JSON at 10,000+ logs/sec.", ACCENT_ROSE, ACCENT_BLUE),
        
        (Inches(2.95), "Gap 2: Slow Overnight Batch Graph Processing", "Legacy systems build graph relationships in slow offline batch jobs.",
         "AiSOC Solution: Real-Time Streaming Neo4j Graph", "Batched UNWIND transactions update 17 node types in real-time as logs arrive.", ACCENT_AMBER, ACCENT_CYAN),
        
        (Inches(4.3), "Gap 3: Single-Model Triage Blindspots", "Standalone Isolation Forest or Neural Nets over-filter or under-filter.",
         "AiSOC Solution: Dual-Stage ML Triage Pipeline", "Stage 1 removes 89.4% false alarms + Stage 2 ranks true incident urgency 0-100.", ACCENT_ROSE, ACCENT_AMBER),
        
        (Inches(5.65), "Gap 4: Dangerous LLM Bot Automation Risks", "Uncontrolled bots risk shutting down domain controllers and web stores.",
         "AiSOC Solution: Blast-Radius L0-L4 Safety Gating", "Evaluates asset criticality with mandatory human approval on high-risk actions.", ACCENT_AMBER, ACCENT_GREEN)
    ]

    for top, p_title, p_desc, s_title, s_desc, p_col, s_col in gaps_flows:
        # Problem Card (Left)
        p_card = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), top, Inches(5.4), Inches(1.15))
        p_card.fill.solid()
        p_card.fill.fore_color.rgb = BG_CARD
        p_card.line.color.rgb = p_col
        p_card.line.width = Pt(1.5)
        try:
            p_card.adjustments[0] = 0.06
        except Exception:
            pass
        tf_p = p_card.text_frame
        tf_p.word_wrap = True
        tf_p.margin_left = tf_p.margin_right = Inches(0.15)
        tf_p.margin_top = Inches(0.1)
        p1 = tf_p.paragraphs[0]
        p1.text = p_title
        p1.font.name = 'Calibri'
        p1.font.size = Pt(11.5)
        p1.font.bold = True
        p1.font.color.rgb = p_col
        p2 = tf_p.add_paragraph()
        p2.text = p_desc
        p2.font.name = 'Calibri'
        p2.font.size = Pt(10)
        p2.font.color.rgb = TEXT_MUTED
        p2.space_before = Pt(2)

        # Arrow in center
        add_arrow(s7, Inches(6.35), top + Inches(0.4), Inches(0.6), Inches(0.35), col=ACCENT_CYAN)

        # Solution Card (Right)
        s_card = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.1), top, Inches(5.4), Inches(1.15))
        s_card.fill.solid()
        s_card.fill.fore_color.rgb = BG_CARD
        s_card.line.color.rgb = s_col
        s_card.line.width = Pt(1.5)
        try:
            s_card.adjustments[0] = 0.06
        except Exception:
            pass
        tf_s = s_card.text_frame
        tf_s.word_wrap = True
        tf_s.margin_left = tf_s.margin_right = Inches(0.15)
        tf_s.margin_top = Inches(0.1)
        s1 = tf_s.paragraphs[0]
        s1.text = s_title
        s1.font.name = 'Calibri'
        s1.font.size = Pt(11.5)
        s1.font.bold = True
        s1.font.color.rgb = s_col
        s2 = tf_s.add_paragraph()
        s2.text = s_desc
        s2.font.name = 'Calibri'
        s2.font.size = Pt(10)
        s2.font.color.rgb = TEXT_MAIN
        s2.space_before = Pt(2)

    # =========================================================================
    # SLIDE 8: EXISTING METHODOLOGY (FLOWCHART DIAGRAM)
    # =========================================================================
    s8 = add_blank_slide()
    add_header(s8, "8", "Baseline Process", "Existing Methodology: The Traditional Manual SOC Workflow", "Visual flowchart showing how legacy 3-tier security teams process security alerts")

    flow_steps = [
        (Inches(0.8), "1. Unsorted Logs\n(Firewalls, AWS, EDR)\n10M+ Daily Events", ACCENT_ROSE, "Messy Formats"),
        (Inches(3.8), "2. Basic SIEM Rules\n(Keyword Matches)\n83% False Alarms", ACCENT_AMBER, "High Noise"),
        (Inches(6.8), "3. Manual Triage\n(Copy-Paste Checks)\n4 - 8 Hours Delay", ACCENT_BLUE, "Analyst Fatigue"),
        (Inches(9.8), "4. Delayed Response\n(Manual Isolation)\n103 Hours Total MTTR", ACCENT_ROSE, "Slow & Risky")
    ]
    for left, txt, col, badge in flow_steps:
        card = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, Inches(1.6), Inches(2.7), Inches(2.2))
        card.fill.solid()
        card.fill.fore_color.rgb = BG_CARD
        card.line.color.rgb = col
        card.line.width = Pt(1.5)
        try:
            card.adjustments[0] = 0.05
        except Exception:
            pass
        p = card.text_frame.paragraphs[0]
        p.text = txt
        p.font.name = 'Calibri'
        p.font.size = Pt(11.5)
        p.font.bold = True
        p.font.color.rgb = TEXT_MAIN
        p.alignment = PP_ALIGN.CENTER
        
        b_pill = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left + Inches(0.25), Inches(3.35), Inches(2.2), Inches(0.35))
        b_pill.fill.solid()
        b_pill.fill.fore_color.rgb = BG_CARD_LIGHT
        b_pill.line.color.rgb = col
        b_pill.line.width = Pt(1)
        try:
            b_pill.adjustments[0] = 0.08
        except Exception:
            pass
        pb = b_pill.text_frame.paragraphs[0]
        pb.text = badge
        pb.font.name = 'Calibri'
        pb.font.size = Pt(9.5)
        pb.font.bold = True
        pb.font.color.rgb = col
        pb.alignment = PP_ALIGN.CENTER

    for arr_left in [Inches(3.55), Inches(6.55), Inches(9.55)]:
        add_arrow(s8, arr_left - Inches(0.05), Inches(2.4), Inches(0.3), Inches(0.3), col=ACCENT_CYAN)

    add_card(s8, Inches(0.8), Inches(4.0), Inches(5.7), Inches(3.0), "Why the Traditional Process Fails", title_color=ACCENT_ROSE, border_color=ACCENT_ROSE, corner_radius=0.03)
    ex_left = [
        ("Long Waiting Queues", "Over 70% of total investigation time is spent waiting in unread ticket queues between teams."),
        ("Repetitive Manual Work", "Analysts spend hours copying and pasting IP addresses into different lookup websites."),
        ("Disconnected Clues", "Single alerts don't show the full story, making it easy to miss sophisticated attacks.")
    ]
    add_bullet_list(s8, Inches(1.02), Inches(4.6), Inches(5.25), Inches(2.2), ex_left, font_size=11.5, space_after=8)

    add_card(s8, Inches(6.8), Inches(4.0), Inches(5.7), Inches(3.0), "The Cost to Businesses", title_color=ACCENT_AMBER, border_color=ACCENT_AMBER, corner_radius=0.03)
    ex_right = [
        ("Hackers Stay Inside for Days", "Attackers remain hidden for 4.3 days (103 hours) on average before being discovered."),
        ("Risk of Accidental Outages", "Manual panic containment often cuts off critical company web servers by mistake."),
        ("High Staff Turnover", "Burnout from non-stop false alarms causes security analysts to quit within 18 months.")
    ]
    add_bullet_list(s8, Inches(7.02), Inches(4.6), Inches(5.25), Inches(2.2), ex_right, font_size=11.5, space_after=8)

    # =========================================================================
    # SLIDE 9: DEMERITS IN EXISTING METHODOLOGY (4-CARD IMPACT BREAKDOWN)
    # =========================================================================
    s9 = add_blank_slide()
    add_header(s9, "9", "Systemic Failures", "Demerits in Existing Methodology: Quantifying the Inefficiency", "Numerical and practical impact of traditional security bottlenecks")

    demerits = [
        (Inches(0.8), Inches(1.6), Inches(5.7), Inches(2.6), "1. 83% False Alarm Overload", ACCENT_ROSE, [
            ("Massive False Positives", "83% of daily alerts are harmless system updates or normal employee logins."),
            ("Desensitized Analysts", "When everything is an alarm, real ransomware warnings get ignored as noise."),
            ("Severe Staff Burnout", "Over 60% of analysts report severe burnout from constant repetitive triage.")
        ]),
        (Inches(6.8), Inches(1.6), Inches(5.7), Inches(2.6), "2. 103 Hours Response Delay (4.3 Days)", ACCENT_AMBER, [
            ("Dangerous Window", "Ransomware locks files in 45 minutes, but legacy teams take 103 hours to respond."),
            ("Data Exfiltration", "Attackers have days to steal confidential customer data and company records."),
            ("Ticket Escalation Delay", "Most time is lost waiting for senior analysts to open transferred tickets.")
        ]),
        (Inches(0.8), Inches(4.35), Inches(5.7), Inches(2.6), "3. Missing Attack Connections", ACCENT_CYAN, [
            ("Isolated Detections", "Traditional tools cannot connect a phishing email to a later password change."),
            ("No Memory", "Once a ticket is closed, context about the attacker's infrastructure is forgotten."),
            ("Hard to Find Patient-Zero", "Tracing the original infected machine requires days of manual log digging.")
        ]),
        (Inches(6.8), Inches(4.35), Inches(5.7), Inches(2.6), "4. High Cost & Outage Risks", ACCENT_BLUE, [
            ("Accidental Outages", "Mistaken containment commands can knock down critical payroll or email servers."),
            ("Millions in Software Costs", "Commercial tools charge expensive fees per gigabyte, forcing companies to drop logs."),
            ("No Audit Trail", "Manual notes fail to provide tamper-proof evidence needed for legal compliance.")
        ])
    ]
    for left, top, w, h, title, col, items in demerits:
        add_card(s9, left, top, w, h, title, title_color=col, border_color=col, corner_radius=0.03)
        add_bullet_list(s9, left + Inches(0.22), top + Inches(0.62), w - Inches(0.44), h - Inches(0.7), items, font_size=11.5, space_after=8)

    # =========================================================================
    # SLIDE 10: PROPOSED METHODOLOGY (4-AGENT CONNECTED PIPELINE DIAGRAM)
    # =========================================================================
    s10 = add_blank_slide()
    add_header(s10, "10", "Proposed Architecture", "Proposed Methodology: The 4-Agent Autonomous AI Pipeline", "Connected multi-agent defense workflow replacing manual multi-tier triage")

    prop_agents = [
        (Inches(0.8), "1. DetectAgent", ACCENT_BLUE, [
            ("Role", "Log Ingestion & Normalization"),
            ("Inputs", "AWS, Okta, CrowdStrike, Firewalls"),
            ("Speed", "10,000+ logs processed per second"),
            ("Standard", "Universal OCSF JSON format"),
            ("Security", "Encrypted credential vault"),
            ("Output", "Sends normalized events to Kafka stream and updates live graph nodes.")
        ], "Speed: 10,000+ Logs/Sec", "Format: Universal OCSF Standard"),
        
        (Inches(3.75), "2. TriageAgent", ACCENT_CYAN, [
            ("Role", "AI Noise Filtering & Prioritization"),
            ("AI Engines", "Bloom Filter + Isolation Forest + Ranker"),
            ("Threat Matching", "Checks known threats in <1 millisecond"),
            ("Noise Filter", "Removes 89.4% of false alarms"),
            ("Scoring", "Calculates 0-100 severity score"),
            ("Output", "Passes validated true incidents with confidence scores to HuntAgent.")
        ], "Noise Filter: 89.4% Suppressed", "Threat Lookup: <1ms Match"),
        
        (Inches(6.7), "3. HuntAgent", ACCENT_AMBER, [
            ("Role", "Attack Path Tracing & Root Cause"),
            ("Graph Engine", "Neo4j Real-Time Knowledge Graph"),
            ("Connections", "17 Entity Types (Users, Hosts, IPs)"),
            ("Attack Mapping", "MITRE ATT&CK Framework"),
            ("Search Surface", "Natural Language Search (/hunt)"),
            ("Output", "Reconstructs complete multi-hop attack trace from patient-zero.")
        ], "Graph Map: 17 Entity Types", "Interface: Plain English Search"),
        
        (Inches(9.65), "4. RespondAgent", ACCENT_ROSE, [
            ("Role", "Safe Automated Containment"),
            ("Playbooks", "25 Pre-Built Response Actions"),
            ("Safety Guard", "Scores risk to avoid server crashes"),
            ("Human Approval", "Requires sign-off for critical servers"),
            ("Audit Trail", "Tamper-proof digital ledger"),
            ("Output", "Executes verified containment and records full audit provenance.")
        ], "Response: 25 Safe Playbooks", "Safety: 0.0% Accidental Outages")
    ]
    
    for left, title, col, items, spec1, spec2 in prop_agents:
        add_card(s10, left, Inches(1.6), Inches(2.8), Inches(5.4), title, title_color=col, border_color=col, corner_radius=0.03)
        add_bullet_list(s10, left + Inches(0.18), Inches(2.15), Inches(2.44), Inches(3.6), items, font_size=11.5, space_after=7)
        add_spec_box(s10, left + Inches(0.18), Inches(5.85), Inches(2.44), Inches(0.95), spec1, spec2, col=col, bg_col=BG_CARD_LIGHT)

    # Connecting Flow Arrows between Agents
    for arr_left in [Inches(3.45), Inches(6.4), Inches(9.35)]:
        add_arrow(s10, arr_left, Inches(1.75), Inches(0.25), Inches(0.25), col=ACCENT_CYAN)

    # =========================================================================
    # SLIDE 11: SYSTEM ARCHITECTURE (4-TIER ARCHITECTURE DIAGRAM)
    # =========================================================================
    s11 = add_blank_slide()
    add_header(s11, "11", "System Blueprint", "System Architecture of the AiSOC Platform", "The four interconnected technical layers powering the autonomous platform")

    arch_layers = [
        (Inches(0.8), Inches(1.6), Inches(5.7), Inches(2.6), "Layer 1: Ingestion & Data Normalization", ACCENT_BLUE, [
            ("16+ Connectors", "Connects to AWS GuardDuty, CrowdStrike, Okta, Zeek, and Linux/Windows syslogs."),
            ("Apache Kafka Streaming", "High-speed streaming queue handling 10,000+ logs per second with zero loss."),
            ("OCSF Standardizer", "Converts messy vendor logs into clean, standardized cybersecurity events.")
        ]),
        (Inches(6.8), Inches(1.6), Inches(5.7), Inches(2.6), "Layer 2: ML Triage & Knowledge Graph", ACCENT_CYAN, [
            ("Fast Threat Intel Lookup", "Instant sub-millisecond matching against 50,000+ known malicious IPs and files."),
            ("2-Stage ML Triage", "Stage 1 removes routine noise; Stage 2 scores urgency from 0 to 100."),
            ("Streaming Neo4j Graph", "Builds a visual map connecting users, computers, and processes in real-time.")
        ]),
        (Inches(0.8), Inches(4.35), Inches(5.7), Inches(2.6), "Layer 3: Multi-Agent AI Orchestration", ACCENT_AMBER, [
            ("LangGraph State Machine", "Coordinates the 4 AI agents with step-by-step reasoning and zero infinite loops."),
            ("Encrypted Credential Vault", "Keeps all passwords and cloud API keys securely encrypted with AES-128."),
            ("PostgreSQL & Redis", "Fast database storage for incident cases and live real-time notification streams.")
        ]),
        (Inches(6.8), Inches(4.35), Inches(5.7), Inches(2.6), "Layer 4: Analyst Web Console & Safe Response", ACCENT_ROSE, [
            ("Modern Web Interface", "Next.js 14 dashboard with live alert feeds, investigation sidebars, and attack graphs."),
            ("Safety Guardrails", "Evaluates risk so automated actions never shut down business-critical servers."),
            ("Tamper-Proof Audit Log", "Records every AI step and human approval in a permanent cryptographic ledger.")
        ])
    ]
    for left, top, w, h, title, col, items in arch_layers:
        add_card(s11, left, top, w, h, title, title_color=col, border_color=col, corner_radius=0.03)
        add_bullet_list(s11, left + Inches(0.22), top + Inches(0.62), w - Inches(0.44), h - Inches(0.7), items, font_size=11.5, space_after=8)

    # Vertical Connecting Indicators
    add_arrow(s11, Inches(3.5), Inches(4.1), Inches(0.3), Inches(0.22), col=ACCENT_CYAN)
    add_arrow(s11, Inches(9.5), Inches(4.1), Inches(0.3), Inches(0.22), col=ACCENT_CYAN)

    # =========================================================================
    # SLIDE 12: LIST OF MODULES (4-QUADRANT SYSTEM MAP)
    # =========================================================================
    s12 = add_blank_slide()
    add_header(s12, "12", "Module Breakdown", "List of Modules in the Proposed AiSOC Platform", "Overview of the four core engineering modules comprising the platform")

    modules_list = [
        (Inches(0.8), Inches(1.6), Inches(5.7), Inches(2.6), "Module 1: Telemetry Ingestion & OCSF Engine", ACCENT_BLUE, [
            ("Core Focus", "High-speed log collection and universal data formatting."),
            ("Technologies Used", "Python FastAPI, Apache Kafka, OCSF Standard v1.1.0."),
            ("Main Function", "Collects raw logs from 16+ tools, decrypts credentials, and creates standard OCSF records.")
        ]),
        (Inches(6.8), Inches(1.6), Inches(5.7), Inches(2.6), "Module 2: ML Triage & Threat Intelligence", ACCENT_CYAN, [
            ("Core Focus", "Removing false alarms and scoring incident urgency."),
            ("Technologies Used", "Bloom Filters, Isolation Forest ML, LambdaRank Priority Model."),
            ("Main Function", "Filters 89.4% of false alarms and assigns a clear 0-100 severity score to true incidents.")
        ]),
        (Inches(0.8), Inches(4.35), Inches(5.7), Inches(2.6), "Module 3: Knowledge Graph Threat Hunting", ACCENT_AMBER, [
            ("Core Focus", "Tracing attack paths and natural language threat search."),
            ("Technologies Used", "Neo4j Graph Database, Cypher Queries, MITRE ATT&CK Matrix."),
            ("Main Function", "Connects multi-step attacks in a visual graph and lets analysts search using plain English.")
        ]),
        (Inches(6.8), Inches(4.35), Inches(5.7), Inches(2.6), "Module 4: Safe Autonomous Response & SOAR", ACCENT_ROSE, [
            ("Core Focus", "Automated incident containment with safety controls."),
            ("Technologies Used", "LangGraph Workflow, Automated Playbooks, Tamper-Proof Audit Log."),
            ("Main Function", "Safely contains threats (isolate host, revoke tokens) with human approval for critical assets.")
        ])
    ]
    for left, top, w, h, title, col, items in modules_list:
        add_card(s12, left, top, w, h, title, title_color=col, border_color=col, corner_radius=0.03)
        add_bullet_list(s12, left + Inches(0.22), top + Inches(0.62), w - Inches(0.44), h - Inches(0.7), items, font_size=11.5, space_after=8)

    # =========================================================================
    # SLIDE 13: MODULE 1 (DESCRIPTION) WITH SCREENSHOT & FLOW
    # =========================================================================
    s13 = add_blank_slide()
    add_header(s13, "13", "Module Specification", "Module 1: Telemetry Ingestion & OCSF Normalization", "Collecting and standardizing logs from all enterprise security tools")

    add_card(s13, Inches(0.8), Inches(1.6), Inches(4.8), Inches(5.4), "Module 1 Architecture & Features", title_color=ACCENT_BLUE, corner_radius=0.03)
    m1_bullets = [
        ("16+ Pre-Built Connectors", "Direct integration with AWS GuardDuty, CrowdStrike, Okta, Sysdig, Zeek, and Linux syslogs."),
        ("10,000+ Logs Per Second", "High-throughput Kafka streaming queue handles peak enterprise log volume with zero dropped events."),
        ("Universal OCSF Standard", "Converts all different log formats into a single standard schema for easy analysis."),
        ("Encrypted Credential Vault", "Protects sensitive cloud access tokens using strong AES-128 encryption."),
        ("5-Tier Severity Scale", "Accurately maps vendor alert levels (Info, Low, Medium, High, Critical) without loss."),
        ("Reliable Replay Queue", "Automatically retries and recovers logs if any network disconnect occurs.")
    ]
    add_bullet_list(s13, Inches(1.02), Inches(2.15), Inches(4.35), Inches(3.6), m1_bullets, font_size=11.5, space_after=7)
    add_spec_box(s13, Inches(1.02), Inches(5.85), Inches(4.35), Inches(0.95), "Speed: 10,000+ Logs/Sec | 16+ Connectors", "Standard: Universal OCSF v1.1.0 | AES-128 Vault", col=ACCENT_BLUE, bg_col=BG_CARD_LIGHT)

    add_card(s13, Inches(5.8), Inches(1.6), Inches(6.7), Inches(5.4), "Live Observability Dashboard & Ingestion View", title_color=ACCENT_BLUE, border_color=ACCENT_BLUE, corner_radius=0.02)
    img_m1_ss = "docs/figures/screen10_system_observability.png"
    add_image_safe(s13, img_m1_ss, Inches(6.0), Inches(2.25), width=Inches(6.3), height=Inches(4.55))

    # =========================================================================
    # SLIDE 14: MODULE 2 (DESCRIPTION) WITH SCREENSHOT & FLOW
    # =========================================================================
    s14 = add_blank_slide()
    add_header(s14, "14", "Module Specification", "Module 2: ML Triage & Threat Intelligence Filtering", "Using machine learning to eliminate false alarms and prioritize real threats")

    add_card(s14, Inches(0.8), Inches(1.6), Inches(4.8), Inches(5.4), "Module 2 Architecture & Features", title_color=ACCENT_CYAN, corner_radius=0.03)
    m2_bullets = [
        ("Instant Threat Lookup", "Checks 50,000+ known attacker IPs and malicious file hashes in under 1 millisecond."),
        ("Stage-1: Noise Filter", "Machine learning model spots routine administrative activity and automatically discards it."),
        ("Stage-2: Priority Ranking", "Ranks the remaining real security events so analysts handle urgent threats first."),
        ("89.4% Noise Reduction", "Proven reduction in daily alert volume, cutting 500+ alerts down to actionable cases."),
        ("0-100 Confidence Score", "Gives every alert an easy-to-understand confidence percentage and severity tag."),
        ("Self-Learning Baselines", "Continuously learns regular company patterns to keep improving triage accuracy.")
    ]
    add_bullet_list(s14, Inches(1.02), Inches(2.15), Inches(4.35), Inches(3.6), m2_bullets, font_size=11.5, space_after=7)
    add_spec_box(s14, Inches(1.02), Inches(5.85), Inches(4.35), Inches(0.95), "Accuracy: 89.4% False Alarms Filtered", "Speed: <1ms Known Threat Lookup | 2-Stage ML", col=ACCENT_CYAN, bg_col=BG_CARD_LIGHT)

    add_card(s14, Inches(5.8), Inches(1.6), Inches(6.7), Inches(5.4), "Autonomous AI Triage Result (CLI Execution)", title_color=ACCENT_CYAN, border_color=ACCENT_CYAN, corner_radius=0.02)
    img_m2_ss = "docs/figures/screen2_cli_triage_result.png"
    add_image_safe(s14, img_m2_ss, Inches(6.0), Inches(2.25), width=Inches(6.3), height=Inches(4.55))

    # =========================================================================
    # SLIDE 15: MODULE 3 (DESCRIPTION) WITH SCREENSHOT & FLOW
    # =========================================================================
    s15 = add_blank_slide()
    add_header(s15, "15", "Module Specification", "Module 3: Real-Time Attack Graph & Threat Hunting", "Visualizing attack connections and enabling simple plain-English threat searches")

    add_card(s15, Inches(0.8), Inches(1.6), Inches(4.8), Inches(5.4), "Module 3 Architecture & Features", title_color=ACCENT_AMBER, corner_radius=0.03)
    m3_bullets = [
        ("Live Visual Graph", "Builds an interconnected map of users, devices, files, and logins in real-time."),
        ("17 Entity Types Connected", "Connects Users -> Passwords -> Processes -> Servers -> External Network IPs."),
        ("Traces Attack Paths", "Automatically uncovers how an attacker hopped from a phishing email to the server room."),
        ("MITRE ATT&CK Mapping", "Tags recognized attacker tactics (e.g. Password Theft, Lateral Movement)."),
        ("Plain English /hunt Search", "Analysts can type questions in normal English (e.g. 'Show logins from Russia')."),
        ("Strict Data Privacy", "Ensures sensitive department data is strictly isolated within the graph.")
    ]
    add_bullet_list(s15, Inches(1.02), Inches(2.15), Inches(4.35), Inches(3.6), m3_bullets, font_size=11.5, space_after=7)
    add_spec_box(s15, Inches(1.02), Inches(5.85), Inches(4.35), Inches(0.95), "Graph Map: 17 Entity Types | 14 Relationships", "Search: Plain English /hunt -> Auto Graph Query", col=ACCENT_AMBER, bg_col=BG_CARD_LIGHT)

    add_card(s15, Inches(5.8), Inches(1.6), Inches(6.7), Inches(5.4), "Threat Hunting (/hunt) Plain English Workbench", title_color=ACCENT_AMBER, border_color=ACCENT_AMBER, corner_radius=0.02)
    img_m3_ss = "docs/figures/app_screenshot_hunt.png"
    add_image_safe(s15, img_m3_ss, Inches(6.0), Inches(2.25), width=Inches(6.3), height=Inches(4.55))

    # =========================================================================
    # SLIDE 16: MODULE 4 (DESCRIPTION) WITH SCREENSHOT & FLOW
    # =========================================================================
    s16 = add_blank_slide()
    add_header(s16, "16", "Module Specification", "Module 4: Safe Autonomous Response & Playbook Studio", "Executing fast incident containment with strict safety guardrails and audit logs")

    add_card(s16, Inches(0.8), Inches(1.6), Inches(4.8), Inches(5.4), "Module 4 Architecture & Features", title_color=ACCENT_ROSE, corner_radius=0.03)
    m4_bullets = [
        ("Safety Risk Scoring", "Calculates asset importance before acting so critical servers are never taken down."),
        ("4-Level Safety Model", "Low-risk actions run automatically; high-risk actions (isolate server) require human sign-off."),
        ("25 Pre-Built Playbooks", "Instant automated workflows for isolating infected hosts, resetting passwords, and blocking IPs."),
        ("Network Safety Guard", "Blocks automated actions from accidentally targeting private company IP ranges."),
        ("Tamper-Proof Audit Log", "Records every step, decision reason, and human approval in an immutable digital log."),
        ("ChatOps Notifications", "Sends instant alerts to Slack & Teams with one-click approval buttons for analysts.")
    ]
    add_bullet_list(s16, Inches(1.02), Inches(2.15), Inches(4.35), Inches(3.6), m4_bullets, font_size=11.5, space_after=7)
    add_spec_box(s16, Inches(1.02), Inches(5.85), Inches(4.35), Inches(0.95), "Safety Control: 4-Level Maturity Ladder", "Response: 25 Playbooks | 0.0% Accidental Outages", col=ACCENT_ROSE, bg_col=BG_CARD_LIGHT)

    add_card(s16, Inches(5.8), Inches(1.6), Inches(6.7), Inches(5.4), "Visual Playbook Studio & Action Approval Interface", title_color=ACCENT_ROSE, border_color=ACCENT_ROSE, corner_radius=0.02)
    img_m4_ss = "docs/figures/screen8_action_approval.png"
    add_image_safe(s16, img_m4_ss, Inches(6.0), Inches(2.25), width=Inches(6.3), height=Inches(4.55))

    # =========================================================================
    # SLIDE 17: EXPERIMENTAL RESULTS (METRICS & BENCHMARK CHARTS)
    # =========================================================================
    s17 = add_blank_slide()
    add_header(s17, "17", "Empirical Evaluation", "Experimental Results: Performance Benchmarks & Comparison", "Validated against a benchmark dataset of 200 attack incidents and 50,000 security events")

    metric_cards = [
        (Inches(0.8), "89.4%", "False Alarms Filtered", ACCENT_GREEN),
        (Inches(3.8), "3.8 min", "Average Response Time", ACCENT_CYAN),
        (Inches(6.8), "96.4%", "MITRE Attack Accuracy", ACCENT_BLUE),
        (Inches(9.8), "100%", "Zero-Outage Safety Rate", ACCENT_AMBER)
    ]
    for left, val, lbl, col in metric_cards:
        c_box = s17.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, Inches(1.5), Inches(2.7), Inches(1.15))
        c_box.fill.solid()
        c_box.fill.fore_color.rgb = BG_CARD
        c_box.line.color.rgb = col
        c_box.line.width = Pt(1.5)
        try:
            c_box.adjustments[0] = 0.08
        except Exception:
            pass
        
        tb = s17.shapes.add_textbox(left, Inches(1.58), Inches(2.7), Inches(0.55))
        tf = tb.text_frame
        p = tf.paragraphs[0]
        p.text = val
        p.font.name = 'Calibri'
        p.font.size = Pt(25)
        p.font.bold = True
        p.font.color.rgb = col
        p.alignment = PP_ALIGN.CENTER
        
        tb2 = s17.shapes.add_textbox(left, Inches(2.15), Inches(2.7), Inches(0.4))
        tf2 = tb2.text_frame
        p2 = tf2.paragraphs[0]
        p2.text = lbl
        p2.font.name = 'Calibri'
        p2.font.size = Pt(11)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_MAIN
        p2.alignment = PP_ALIGN.CENTER

    table_shape = s17.shapes.add_table(5, 4, Inches(0.8), Inches(2.85), Inches(5.8), Inches(4.3))
    tbl = table_shape.table
    tbl.columns[0].width = Inches(2.0)
    tbl.columns[1].width = Inches(1.25)
    tbl.columns[2].width = Inches(1.25)
    tbl.columns[3].width = Inches(1.3)

    t_headers = ["Performance Metric", "Traditional SIEM", "Legacy SOAR", "AiSOC (Ours)"]
    for c_i, th in enumerate(t_headers):
        cell = tbl.cell(0, c_i)
        cell.fill.solid()
        cell.fill.fore_color.rgb = BG_CARD_LIGHT if c_i < 3 else ACCENT_CYAN
        p = cell.text_frame.paragraphs[0]
        p.text = th
        p.font.name = 'Calibri'
        p.font.size = Pt(10.5)
        p.font.bold = True
        p.font.color.rgb = TEXT_MAIN if c_i < 3 else BG_DARK
        p.alignment = PP_ALIGN.CENTER

    t_rows = [
        ("Response Time (MTTR)", "103.2 hours", "14.5 hours", "3.8 minutes (1600x faster)"),
        ("False Alarm Noise Rate", "83.4% noise", "62.1% noise", "10.6% (89.4% filtered)"),
        ("Attack Path Accuracy", "42.0%", "58.5%", "96.4% Accuracy"),
        ("Accidental Outage Rate", "12.5% outages", "8.0% outages", "0.0% (100% Safe Gated)")
    ]
    for r_i, r_data in enumerate(t_rows):
        for c_i, val in enumerate(r_data):
            cell = tbl.cell(r_i + 1, c_i)
            cell.fill.solid()
            cell.fill.fore_color.rgb = BG_CARD if c_i < 3 else RGBColor(24, 48, 70)
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.name = 'Calibri'
            p.font.size = Pt(9.5)
            p.font.bold = (c_i == 0 or c_i == 3)
            p.font.color.rgb = ACCENT_CYAN if c_i == 3 else (TEXT_MAIN if c_i == 0 else TEXT_MUTED)

    add_card(s17, Inches(6.8), Inches(2.85), Inches(5.7), Inches(4.3), "Empirical Performance Benchmark Charts", title_color=ACCENT_CYAN, border_color=ACCENT_CYAN, corner_radius=0.02)
    img_res = "docs/ppt_figures/ppt_fig_experimental_results.png"
    add_image_safe(s17, img_res, Inches(6.95), Inches(3.4), width=Inches(5.4), height=Inches(3.6))

    # =========================================================================
    # SLIDE 18: CONCLUSION & FUTURE ROADMAP (4-PHASE ROADMAP DIAGRAM)
    # =========================================================================
    s18 = add_blank_slide()
    add_header(s18, "18", "Project Summary", "Conclusion & Future Work: Advancing Autonomous Cybersecurity", "Key achievements accomplished and visual 4-phase roadmap for future enhancements")

    add_card(s18, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.4), "Project Milestones & Conclusion", title_color=ACCENT_CYAN, border_color=ACCENT_CYAN, corner_radius=0.03)
    conc_bullets = [
        ("Full Autonomous SOC Delivered", "Built a complete open-source platform uniting 16+ data sources and four collaborative AI agents."),
        ("Proven 89.4% Noise Reduction", "Empirically verified that AI triage removes 89.4% of false alarms while cutting response time to 3.8 minutes."),
        ("100% Safe Containment", "Designed safety guardrails that prevent accidental server shutdowns while recording full audit logs."),
        ("Verified on Real Hardware", "Successfully tested on a physical enterprise Cisco Catalyst switch and Proxmox server cluster."),
        ("Production Open-Source Code", "Delivered a complete Next.js web console, Python microservices, and 939 executable detection rules.")
    ]
    add_bullet_list(s18, Inches(1.02), Inches(2.15), Inches(5.25), Inches(3.6), conc_bullets, font_size=11.5, space_after=9)
    add_spec_box(s18, Inches(1.02), Inches(5.85), Inches(5.25), Inches(0.95), "Hardware Status: 100% Verified on Cisco 3850 & Proxmox", "Codebase: 939 Executable Detection Rules | Full CI/CD Pass", col=ACCENT_CYAN, bg_col=BG_CARD_LIGHT)

    add_card(s18, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.4), "Future Research & Development Roadmap", title_color=ACCENT_BLUE, border_color=ACCENT_BLUE, corner_radius=0.03)
    
    # 4-Phase Visual Roadmap Steps
    roadmap_phases = [
        (Inches(2.15), "Phase 1: Deep Kernel eBPF Probes", "Sub-millisecond rootkit detection bypassing user-space log tampering.", ACCENT_BLUE),
        (Inches(3.05), "Phase 2: Federated Threat Sharing", "Zero-knowledge proof threat intelligence sharing between organizations.", ACCENT_CYAN),
        (Inches(3.95), "Phase 3: Self-Tuning Detection AI", "Generative adversary agents that automatically write and test Sigma rules.", ACCENT_AMBER),
        (Inches(4.85), "Phase 4: Autonomous Self-Healing SOC", "Closed-loop autonomous remediation for routine cloud and endpoint events.", ACCENT_GREEN)
    ]
    for top, p_title, p_desc, col in roadmap_phases:
        r_box = s18.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.02), top, Inches(5.25), Inches(0.78))
        r_box.fill.solid()
        r_box.fill.fore_color.rgb = BG_CARD_LIGHT
        r_box.line.color.rgb = col
        r_box.line.width = Pt(1.2)
        try:
            r_box.adjustments[0] = 0.08
        except Exception:
            pass
        tf_r = r_box.text_frame
        tf_r.word_wrap = True
        tf_r.margin_left = tf_r.margin_right = Inches(0.12)
        tf_r.margin_top = Inches(0.06)
        pr1 = tf_r.paragraphs[0]
        pr1.text = p_title
        pr1.font.name = 'Calibri'
        pr1.font.size = Pt(11)
        pr1.font.bold = True
        pr1.font.color.rgb = col
        pr2 = tf_r.add_paragraph()
        pr2.text = p_desc
        pr2.font.name = 'Calibri'
        pr2.font.size = Pt(9.5)
        pr2.font.color.rgb = TEXT_MAIN
        pr2.space_before = Pt(1)

    add_spec_box(s18, Inches(7.02), Inches(5.85), Inches(5.25), Inches(0.95), "Target Strategic Milestone: AiSOC v8.0 Architecture Deployment", "Next Horizons: eBPF Kernel Probes | GPU Graph AI | Threat Sharing", col=ACCENT_BLUE, bg_col=BG_CARD_LIGHT)

    # =========================================================================
    # SLIDE 19: REFERENCES (15 FORMAL REFERENCES)
    # =========================================================================
    s19 = add_blank_slide()
    add_header(s19, "19", "Academic & Industrial Standards", "References: Foundational Literature & Industry Standards", "Complete bibliography of 15 peer-reviewed papers and international standards")

    add_card(s19, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.4), "Academic & Research References (1-8)", title_color=ACCENT_BLUE, border_color=BORDER_COLOR, corner_radius=0.03)
    refs_col1 = [
        ("[1] OCSF Standard", "Open Cybersecurity Schema Framework v1.1.0, Linux Foundation, 2023."),
        ("[2] Isolation Forest", "F. T. Liu, K. M. Ting, Z.-H. Zhou, in IEEE 8th ICDM, pp. 413-422, 2008."),
        ("[3] LambdaRank Algorithm", "C. J. Burges, 'From RankNet to LambdaRank to LambdaMART,' Microsoft Research, 2010."),
        ("[4] Bloom Filter Matching", "B. H. Bloom, 'Space/Time Trade-offs in Hash Coding,' Comm. ACM, 13(7), 1970."),
        ("[5] MITRE ATT&CK Matrix", "B. E. Strom et al., 'MITRE ATT&CK: Design and Philosophy,' MITRE Tech Report, 2020."),
        ("[6] Neo4j Graph Database", "Neo4j Graph Database Architecture & Cypher Optimization Manual, Neo4j, 2024."),
        ("[7] LangGraph Multi-Agent", "H. Chase et al., 'Multi-Agent Cyclic Graphs for LLMs,' LangChain Research, 2024."),
        ("[8] NIST Incident Guide", "NIST Computer Security Incident Handling Guide, Special Publication 800-61, 2012.")
    ]
    add_bullet_list(s19, Inches(1.02), Inches(2.15), Inches(5.25), Inches(3.6), refs_col1, font_size=11, space_after=6.5, prefix_color=ACCENT_BLUE)
    add_spec_box(s19, Inches(1.02), Inches(5.85), Inches(5.25), Inches(0.95), "Foundational Research: Machine Learning & Graph Theory", "OCSF Normalization | Isolation Forest Anomaly Detection | LangGraph State Machine", col=ACCENT_BLUE, bg_col=BG_CARD_LIGHT)

    add_card(s19, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.4), "Industry Standards & Frameworks (9-15)", title_color=ACCENT_CYAN, border_color=BORDER_COLOR, corner_radius=0.03)
    refs_col2 = [
        ("[9] ISO/IEC 27035 Standard", "Information Technology — Security Incident Management, ISO/IEC, 2023."),
        ("[10] CISA Response Playbooks", "Cybersecurity Incident & Vulnerability Response Playbooks, CISA, 2021."),
        ("[11] SIEM Best Practices", "Security Information and Event Management Architecture, Splunk Docs, 2023."),
        ("[12] Apache Kafka Streaming", "J. Kreps, N. Narkhede, J. Rao, 'Kafka: Distributed Log Processing,' 2011."),
        ("[13] Sigma Detection Rules", "F. Roth, T. Patzke, 'Sigma: Generic Signature Format for SIEM Systems,' 2024."),
        ("[14] Zeek Network Monitor", "Zeek Project, 'Zeek Network Security Monitor: Architecture & Scripting,' 2024."),
        ("[15] UN SDG Framework", "United Nations, 'Sustainable Development Goals Report 2023,' UN DESA, 2023.")
    ]
    add_bullet_list(s19, Inches(7.02), Inches(2.15), Inches(5.25), Inches(3.6), refs_col2, font_size=11, space_after=9.5, prefix_color=ACCENT_CYAN)
    add_spec_box(s19, Inches(7.02), Inches(5.85), Inches(5.25), Inches(0.95), "Enterprise Compliance & International Standards", "ISO/IEC 27035-1 | CISA Response Playbooks | UN Sustainable Development Goals", col=ACCENT_CYAN, bg_col=BG_CARD_LIGHT)

    # =========================================================================
    # SLIDE 20: CLOSING / THANK YOU & LIVE DEMO
    # =========================================================================
    s20 = add_blank_slide()
    
    tb_thank = s20.shapes.add_textbox(Inches(0.8), Inches(1.3), Inches(11.7), Inches(1.5))
    tf_th = tb_thank.text_frame
    p_th = tf_th.paragraphs[0]
    p_th.text = "THANK YOU!"
    p_th.font.name = 'Calibri'
    p_th.font.size = Pt(44)
    p_th.font.bold = True
    p_th.font.color.rgb = ACCENT_CYAN
    p_th.alignment = PP_ALIGN.CENTER

    p_th_sub = tf_th.add_paragraph()
    p_th_sub.text = "Questions, Feedback & Live Project Demonstration"
    p_th_sub.font.name = 'Calibri'
    p_th_sub.font.size = Pt(22)
    p_th_sub.font.color.rgb = TEXT_MAIN
    p_th_sub.alignment = PP_ALIGN.CENTER
    p_th_sub.space_before = Pt(8)

    add_card(s20, Inches(1.5), Inches(3.1), Inches(10.333), Inches(3.8), "AiSOC PROJECT REPOSITORY & LIVE DEMONSTRATION ACCESS", title_color=ACCENT_BLUE, corner_radius=0.03)
    demo_details = [
        ("Project Architecture", "AiSOC: Autonomous AI-Powered Security Operations Center (Open Source MIT License)"),
        ("Live Interactive Web Console", "http://localhost:3000/dashboard  (Local Next.js + FastAPI Console)"),
        ("Instant Offline Sandbox Demo", "pip install aisoc-sandbox && aisoc-sandbox demo  (<30s local execution)"),
        ("Complete Project Documentation", "Local Architecture Docs, Graph Schema & Connector Guides (docs/)"),
        ("Team Members & Register Nos", "Yashvinthan M (231061101162) | Tharun Kumar D (231061101150) | Sanjeev V (231061101140) | Srinithi J S (231061101149)"),
        ("Department & College", "Department of Computer Science and Engineering, Dr. M.G.R. Educational and Research Institute")
    ]
    add_bullet_list(s20, Inches(1.8), Inches(3.7), Inches(9.7), Inches(2.2), demo_details, font_size=12.5, space_after=8)
    add_spec_box(s20, Inches(1.8), Inches(6.0), Inches(9.7), Inches(0.65), "Live Demo Ready: Running locally on Proxmox VE Cluster & Cisco 3850 Testbed", "Instant Cold-Start: pip install aisoc-sandbox && aisoc-sandbox demo", col=ACCENT_CYAN, bg_col=BG_CARD_LIGHT)

    # Save to Master presentation
    out_file = "AiSOC_Mini_Project_Presentation_Master.pptx"
    prs.save(out_file)
    print(f"SUCCESS: Generated '{out_file}' with diagrammatic visual workflows!")

    # Also sync to AiSOC_Mini_Project_Presentation.pptx if possible
    sync_file = "AiSOC_Mini_Project_Presentation.pptx"
    try:
        shutil.copyfile(out_file, sync_file)
        print(f"SUCCESS: Synced '{sync_file}'!")
    except Exception as e:
        print(f"Notice: Could not copy to '{sync_file}' directly: {e}")

if __name__ == '__main__':
    build_presentation()
