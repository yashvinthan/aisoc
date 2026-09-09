"""
Chapter 1: Introduction
Written in clear, simple, human-understandable academic language.
Strictly follows Section 3.9 of the University Project Guidelines:
(Broad area of the project, Problem statement, motivation, ethical, social, professional issues)
"""
import os
from docx.shared import Inches

def generate_chapter_1(add_p, add_ch_heading, add_sec_heading, add_subsec_heading, add_code, add_table, add_fig, fig_dir):
    add_ch_heading("CHAPTER 1\nINTRODUCTION")
    
    add_sec_heading("1.1 BROAD AREA OF THE PROJECT")
    add_p("The broad area of this project is Computer Network Security and Applied Artificial Intelligence (Cybersecurity and Machine Learning), specifically focusing on Security Operations Center (SOC) automation and intelligent incident response.")
    add_p("In any modern organization, such as an IT enterprise, university campus, hospital, or financial institution, hundreds of servers, routers, firewalls, and employee workstations operate continuously. Every time a user logs in, enters an incorrect password, downloads a file, or connects to an external server, the underlying system generates a timestamped security log.")
    add_p("A Security Operations Center (SOC) is a dedicated department responsible for monitoring these log streams 24 hours a day to prevent data theft, ransomware infections, and unauthorized access. However, because modern computer networks produce millions of log records every day, human security teams face an overwhelming volume of alerts. Most of these alerts represent harmless routine events, but inspecting each alert manually causes severe operational delays.")
    
    # Figure 1.1: Domain Mapping
    add_fig(os.path.join(fig_dir, "fig1_1_domain_mapping.png"), "Figure 1.1: Technical Domains Unified by the AiSOC Platform", 5.8)
    
    add_p("This project brings together Network Security, Graph Databases, and Machine Learning. The primary goal is to build an automated software platform called AiSOC that collects logs from diverse devices, automatically filters out repetitive alarms using mathematical fingerprinting, connects related entities in a visual knowledge graph, and uses intelligent agents to assist human analysts in rapidly detecting and stopping real cyber attacks.")

    add_sec_heading("1.2 PROBLEM STATEMENT")
    add_p("Security teams in companies today face a severe operational challenge known as 'Alert Fatigue.' A typical medium-to-large enterprise receives between 10,000 and 500,000 security alerts every single day from firewalls, antivirus software, cloud accounts, and identity servers.")
    add_p("Industry studies indicate that more than 80% of these alerts are false alarms or harmless routine events. However, because legacy monitoring tools cannot understand the context of an event, human security analysts must manually inspect each alert one by one.")
    
    # Figure 1.2: Alert Fatigue
    add_fig(os.path.join(fig_dir, "fig1_2_alert_fatigue.png"), "Figure 1.2: The Traditional SOC Alert Fatigue and Investigation Bottleneck", 5.8)
    
    add_p("For every single alert, an analyst has to open multiple different browser tabs (such as the firewall console, antivirus portal, Active Directory, and threat intelligence databases), copy-paste IP addresses, and manually piece together what happened. This manual process takes 15 to 45 minutes per alert.")
    add_p("Because humans cannot keep up with this massive volume, critical attacks often get buried in the queue for days or weeks. Real-world data indicates that cyber attackers frequently remain undetected inside corporate networks for over 200 days before being discovered. At the same time, security analysts suffer from high stress and burnout, leading to high job turnover rates.")

    add_sec_heading("1.3 MOTIVATION")
    add_p("The main motivation of this project is to build an intelligent, automated assistant for security analysts that can instantly analyze security events 24/7 without getting tired or missing critical clues.")
    add_p("Traditional automated tools rely on rigid, pre-written 'if-then' scripts. If an attacker changes even a single letter in a command or uses a new IP address, traditional rules fail to catch them. In contrast, modern Machine Learning models and collaborative AI agents have strong reasoning capabilities and can understand the intent behind complex computer commands and logs.")
    add_p("Furthermore, existing commercial AI security software is proprietary and extremely expensive, making it unaffordable for universities, small businesses, non-profit organizations, and hospitals. By building an open-source, transparent platform, this project aims to make advanced AI security defense accessible to everyone.")

    add_sec_heading("1.4 OBJECTIVES OF THE PROJECT")
    add_p("The specific engineering goals of this project are:")
    add_p("1. Build a Fast Log Ingestion Engine: Develop a high-speed data intake worker in the Go programming language that converts diverse log formats into the Open Cybersecurity Schema Framework (OCSF) standard in under 2 milliseconds.")
    add_p("2. Implement Smart Deduplication and Risk Scoring: Use mathematical fingerprinting (Simhash) and Machine Learning (Isolation Forest and LightGBM) to eliminate duplicate alarms and prioritize truly dangerous threats.")
    add_p("3. Construct a Live Security Knowledge Graph: Use a Neo4j graph database to map relationships between users, devices, files, and alerts so analysts can visually see the attack path.")
    add_p("4. Create a Multi-Agent AI Investigation System: Build four specialized AI agents (DetectAgent, TriageAgent, HuntAgent, and RespondAgent) that collaborate to research alerts, query historical logs, and write clear incident summaries.")
    add_p("5. Implement Blast-Radius Safety Gating: Ensure that automated actions (like isolating a computer or resetting a password) are checked for safety so that critical production servers are never accidentally taken offline.")
    add_p("6. Provide an Easy-to-Use Web Dashboard: Deliver a clean, responsive web interface where human analysts can review live alerts, view evidence timelines, and approve response actions with one click.")

    add_sec_heading("1.5 ETHICAL, SOCIAL, AND PROFESSIONAL ISSUES")
    add_p("When giving artificial intelligence the ability to analyze logs and recommend response actions on computer systems, ethical, social, and professional safety standards must be strictly upheld:")
    add_p("1. Ethical Issues and Safe AI Execution: If an AI mistakenly locks an essential server (such as a hospital patient database or a banking transaction gateway), it could cause serious real-world harm. AiSOC solves this by enforcing a 'Human-in-the-Loop' safety boundary: every high-impact action is calculated against a blast-radius risk metric and paused until a human supervisor clicks 'Approve.'")
    add_p("2. Social Responsibility: Protecting digital infrastructure directly benefits society by preventing ransomware disruptions in public schools, municipal utilities, and healthcare institutions. By publishing AiSOC as open source under the MIT License, the platform provides equal access to advanced cyber defense for organizations that cannot afford commercial proprietary tools.")
    add_p("3. Professional and Legal Data Privacy: Security logs frequently contain employee names, email addresses, and IP addresses. The system adheres to professional data protection standards by masking personal identifiers, providing strict multi-tenant data isolation, and recording all automated queries in an immutable audit ledger.")

    add_sec_heading("1.6 REPORT ORGANIZATION")
    add_p("The remainder of this project report is structured as follows:")
    add_p("• Chapter 2 (Literature Survey): Reviews previous academic research and existing commercial tools in log management, machine learning for security, and AI agents.")
    add_p("• Chapter 3 (Existing System): Explains how traditional SOCs work today and details the shortcomings that cause alert fatigue and delays.")
    add_p("• Chapter 4 (Proposed System): Presents the complete design of AiSOC, including the step-by-step methodology flowchart, system architecture, and standard UML diagrams.")
    add_p("• Chapter 5 (System Specification): Lists the exact hardware, software runtimes, database engines, and security protocols used in the project.")
    add_p("• Chapter 6 (Implementation): Describes how each software module was built, accompanied by 10 live application screenshots showing the system in action.")
    add_p("• Chapter 7 (Result and Conclusion): Presents the experimental testing results on 200 attack scenarios, compares performance before and after automation, discusses future improvements, and lists references.")

print("Chapter 1 rewritten strictly adhering to Section 3.9.")


