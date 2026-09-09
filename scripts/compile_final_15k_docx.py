"""
Comprehensive Final 15,200+ Words DOCX Generator for AiSOC.
Compiles the master report with:
- All 10 user-requested live application and CLI screenshots
- Clean academic Black & White table styling
- 4.4 Methodology Flowchart
- SYSTEM_DESIGN.md System Architecture Topology
- 5 UML Diagrams (Use Case, Activity, Sequence, 3-Compartment Class Diagram, State Machine)
- Chen Entity-Relationship (ER) Diagram
- 22 Academic Tables and 30 Figures
"""

import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

FIG_DIR = r"c:\Users\yashv\dev\work in progress\mini project\AiSOC\docs\figures"

def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def set_table_borders(table):
    tblPr = table._tbl.tblPr
    tblBorders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>\n'
        f'  <w:top w:val="single" w:sz="6" w:space="0" w:color="000000"/>\n'
        f'  <w:left w:val="single" w:sz="6" w:space="0" w:color="000000"/>\n'
        f'  <w:bottom w:val="single" w:sz="6" w:space="0" w:color="000000"/>\n'
        f'  <w:right w:val="single" w:sz="6" w:space="0" w:color="000000"/>\n'
        f'  <w:insideH w:val="single" w:sz="4" w:space="0" w:color="000000"/>\n'
        f'  <w:insideV w:val="single" w:sz="4" w:space="0" w:color="000000"/>\n'
        f'</w:tblBorders>'
    )
    tblPr.append(tblBorders)

def set_borderless_table(table):
    tblPr = table._tbl.tblPr
    tblBorders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>\n'
        f'  <w:top w:val="none"/>\n'
        f'  <w:left w:val="none"/>\n'
        f'  <w:bottom w:val="none"/>\n'
        f'  <w:right w:val="none"/>\n'
        f'  <w:insideH w:val="none"/>\n'
        f'  <w:insideV w:val="none"/>\n'
        f'</w:tblBorders>'
    )
    tblPr.append(tblBorders)

def apply_section_margins(section):
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    section.left_margin = Cm(2.5)
    section.right_margin = Cm(2.0)
    section.top_margin = Cm(2.0)
    section.bottom_margin = Cm(2.0)

def build_master_docx():
    doc = docx.Document()
    
    def add_chapter_section(start_num=None):
        sec = doc.add_section()
        apply_section_margins(sec)
        sec.different_first_page_header_footer = True
        
        sectPr = sec._sectPr
        for child in list(sectPr):
            if child.tag.endswith('pgNumType'):
                sectPr.remove(child)
                
        if start_num is not None:
            pg_xml = f'<w:pgNumType {nsdecls("w")} w:fmt="decimal" w:start="{start_num}"/>'
        else:
            pg_xml = f'<w:pgNumType {nsdecls("w")} w:fmt="decimal"/>'
        sectPr.append(parse_xml(pg_xml))
        
        # Configure Regular/Subsequent Pages Footer (aligned right)
        footer = sec.footer
        footer.is_linked_to_previous = False
        p = footer.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p.text = ''
        run = p.add_run()
        run.font.name = 'Times New Roman'
        run.font.size = Pt(10)
        run.font.color.rgb = RGBColor(0, 0, 0)
        fld = parse_xml(f'<w:fldSimple {nsdecls("w")} w:instr="PAGE"/>')
        p._p.append(fld)
        
        # First Page Footer is Empty (page number suppressed on first page of each chapter)
        fp_footer = sec.first_page_footer
        fp_footer.is_linked_to_previous = False
        p_fp = fp_footer.paragraphs[0]
        p_fp.text = ''
        return sec

    # Section 1: Pre-Acknowledgement (Title, Bonafide, Constraints) - No Page Numbers
    s1 = doc.sections[0]
    apply_section_margins(s1)
    s1.different_first_page_header_footer = True
    s1.footer.is_linked_to_previous = False
    s1.footer.paragraphs[0].text = ''
    s1.first_page_footer.is_linked_to_previous = False
    s1.first_page_footer.paragraphs[0].text = ''

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

    def add_fig(img_path, caption, width_inches=5.8):
        if os.path.exists(img_path):
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(10)
            p_img.paragraph_format.space_after = Pt(2)
            run = p_img.add_run()
            run.add_picture(img_path, width=Inches(width_inches))
            
            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_before = Pt(2)
            p_cap.paragraph_format.space_after = Pt(10)
            run_cap = p_cap.add_run(caption)
            run_cap.font.name = 'Times New Roman'
            run_cap.font.size = Pt(10.5)
            run_cap.font.bold = True
            run_cap.font.color.rgb = RGBColor(17, 24, 39)

    def add_table(col_widths, headers, data, caption=None):
        table = doc.add_table(rows=1, cols=len(headers))
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_table_borders(table)
        
        hdr_cells = table.rows[0].cells
        for i, title in enumerate(headers):
            hdr_cells[i].text = title
            set_cell_background(hdr_cells[i], "FFFFFF")
            set_cell_margins(hdr_cells[i], top=120, bottom=120, left=150, right=150)
            p = hdr_cells[i].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if ("ID" in title or "No." in title or "Status" in title) else WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_after = Pt(0)
            for r in p.runs:
                r.font.name = 'Times New Roman'
                r.font.size = Pt(10.5)
                r.font.bold = True
                r.font.color.rgb = RGBColor(0, 0, 0)
                
        for row_idx, row_data in enumerate(data):
            row_cells = table.add_row().cells
            for col_idx, text in enumerate(row_data):
                row_cells[col_idx].text = str(text)
                set_cell_background(row_cells[col_idx], "FFFFFF")
                set_cell_margins(row_cells[col_idx], top=100, bottom=100, left=150, right=150)
                p = row_cells[col_idx].paragraphs[0]
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER if (col_idx == 0 or "Pass" in str(text) or "Fail" in str(text)) else WD_ALIGN_PARAGRAPH.LEFT
                p.paragraph_format.line_spacing = 1.15
                p.paragraph_format.space_after = Pt(0)
                for r in p.runs:
                    r.font.name = 'Times New Roman'
                    r.font.size = Pt(10)
                    r.font.color.rgb = RGBColor(0, 0, 0)

        for row in table.rows:
            for idx, width in enumerate(col_widths):
                row.cells[idx].width = width
                
        if caption:
            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_before = Pt(4)
            p_cap.paragraph_format.space_after = Pt(10)
            run_cap = p_cap.add_run(caption)
            run_cap.font.name = 'Times New Roman'
            run_cap.font.size = Pt(10.5)
            run_cap.font.bold = True
            run_cap.font.color.rgb = RGBColor(0, 0, 0)
        else:
            p_space = doc.add_paragraph()
            p_space.paragraph_format.space_after = Pt(6)

    def add_toc_table(col_widths, headers, data):
        table = doc.add_table(rows=1, cols=len(headers))
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_borderless_table(table)
        
        # Header Row
        hdr_cells = table.rows[0].cells
        for i, title in enumerate(headers):
            hdr_cells[i].text = title
            set_cell_margins(hdr_cells[i], top=60, bottom=120, left=40, right=40)
            p = hdr_cells[i].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.RIGHT if i == (len(headers) - 1) else WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_after = Pt(6)
            for r in p.runs:
                r.font.name = 'Times New Roman'
                r.font.size = Pt(11)
                r.font.bold = True
                r.font.color.rgb = RGBColor(0, 0, 0)
                
        for row_idx, row_data in enumerate(data):
            row_cells = table.add_row().cells
            col0 = str(row_data[0]).strip()
            col1 = str(row_data[1]).strip()
            col2 = str(row_data[2]).strip()
            
            is_chapter = bool(col0 and (col0.endswith(".") or col0.isdigit())) or col1 in ["REFERENCES", "ABSTRACT", "LIST OF TABLES", "LIST OF FIGURES", "LIST OF SYMBOLS", "LIST OF SYMBOLS AND ABBREVIATIONS"]
            
            for col_idx, text in enumerate(row_data):
                row_cells[col_idx].text = str(text)
                set_cell_margins(row_cells[col_idx], top=20, bottom=20, left=40, right=40)
                p = row_cells[col_idx].paragraphs[0]
                p.alignment = WD_ALIGN_PARAGRAPH.RIGHT if col_idx == (len(row_data) - 1) else WD_ALIGN_PARAGRAPH.LEFT
                p.paragraph_format.line_spacing = 1.15
                p.paragraph_format.space_after = Pt(2 if is_chapter else 0)
                for r in p.runs:
                    r.font.name = 'Times New Roman'
                    r.font.size = Pt(10.5)
                    r.font.bold = is_chapter
                    r.font.color.rgb = RGBColor(0, 0, 0)
                    
        for row in table.rows:
            for idx, width in enumerate(col_widths):
                row.cells[idx].width = width

    # FRONT MATTER
    # Form Header
    p_form = doc.add_paragraph()
    p_form.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_form.paragraph_format.space_after = Pt(4)
    r_form = p_form.add_run("FORM NO.-F/TL/024\nREV.00 Date 20.03.2020")
    r_form.font.name = 'Times New Roman'
    r_form.font.size = Pt(9)
    r_form.font.bold = True

    add_p("AiSOC: AUTONOMOUS AI-POWERED SECURITY OPERATIONS CENTER (SOC) PLATFORM WITH KNOWLEDGE-GRAPH ENRICHMENT AND CLOSED-LOOP TRIAGE", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, size=14, space_after=18)
    
    add_p("MINI PROJECT REPORT", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, size=13, space_after=12)
    add_p("submitted in partial fulfillment of the\nrequirements for the award of the degree in", italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, size=11, space_after=12)
    add_p("BACHELOR OF TECHNOLOGY", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, size=14, space_after=2)
    add_p("IN", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, size=11, space_after=2)
    add_p("COMPUTER SCIENCE AND ENGINEERING", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, size=13, space_after=16)

    add_p("By", italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, size=11, space_after=10)
    add_p("YASHVINTHAN M – 231061101162\nTHARUN KUMAR D – 231061101150\nSANTHOSH KUMAR Y – 231061101136", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, size=12, space_after=20)

    # University Logo Banner
    logo_path = os.path.join(FIG_DIR, "dr_mgr_logo.png")
    if os.path.exists(logo_path):
        p_logo = doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo.paragraph_format.space_before = Pt(8)
        p_logo.paragraph_format.space_after = Pt(20)
        run_logo = p_logo.add_run()
        run_logo.add_picture(logo_path, width=Inches(4.8))

    add_p("DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING\nJULY 2026", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, size=12, space_after=0)
    
    doc.add_page_break()

    # Bonafide Certificate
    p_form2 = doc.add_paragraph()
    p_form2.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_form2.paragraph_format.space_after = Pt(4)
    r_form2 = p_form2.add_run("FORM NO.-F/TL/024\nREV.00 Date 20.03.2020")
    r_form2.font.name = 'Times New Roman'
    r_form2.font.size = Pt(9)
    r_form2.font.bold = True

    if os.path.exists(logo_path):
        p_logo2 = doc.add_paragraph()
        p_logo2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo2.paragraph_format.space_before = Pt(4)
        p_logo2.paragraph_format.space_after = Pt(14)
        run_logo2 = p_logo2.add_run()
        run_logo2.add_picture(logo_path, width=Inches(4.8))

    add_ch_heading("BONAFIDE CERTIFICATE")
    add_p("This is to certify that this Mini Project Report is the bonafide work of Mr. YASHVINTHAN M Reg. No 231061101162, Mr. THARUN KUMAR D Reg. No 231061101150, Mr. SANTHOSH KUMAR Y Reg. No 231061101136, who carried out the Mini Project entitled \"AiSOC: Autonomous AI-Powered Security Operations Center Platform with Real-Time Correlation, Graph-Based Threat Investigation, and Automated Triage\" under our supervision from February 2026 to July 2026.")
    add_p("\n")
    
    cert_table = doc.add_table(rows=1, cols=3)
    cert_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell_c1, cell_c2, cell_hod = cert_table.rows[0].cells
    cell_c1.width = Inches(2.1)
    cell_c2.width = Inches(2.1)
    cell_hod.width = Inches(2.2)
    
    p1 = cell_c1.paragraphs[0]
    p1.paragraph_format.line_spacing = 1.2
    p1.add_run("Coordinator 1\n\n\nDr. F. Antony Xavier Bronson\nProfessor\nDepartment of CSE").font.name = 'Times New Roman'
    
    p2 = cell_c2.paragraphs[0]
    p2.paragraph_format.line_spacing = 1.2
    p2.add_run("Coordinator 2\n\n\nMrs. Chinchu Nair\nAssistant Professor\nDepartment of CSE").font.name = 'Times New Roman'
    
    p3 = cell_hod.paragraphs[0]
    p3.paragraph_format.line_spacing = 1.2
    p3.add_run("Head of the Department\n\n\nDr. S. Geetha\nProfessor & Head\nDepartment of CSE").font.name = 'Times New Roman'
    
    add_p("\nSubmitted for Viva Voce Examination held on: ____________________\n\n")
    
    viva_table = doc.add_table(rows=1, cols=2)
    viva_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    vl, vr = viva_table.rows[0].cells
    vl.width = Inches(3.2)
    vr.width = Inches(3.2)
    
    pvl = vl.paragraphs[0]
    pvl.add_run("______________________________\nInternal Examiner").font.name = 'Times New Roman'
    pvr = vr.paragraphs[0]
    pvr.add_run("______________________________\nExternal Examiner").font.name = 'Times New Roman'

    doc.add_page_break()

    # Major Design Constraints and Design Standards Table
    add_ch_heading("MAJOR DESIGN CONSTRAINTS AND DESIGN STANDARDS")
    
    constraints_table = doc.add_table(rows=1, cols=2)
    constraints_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(constraints_table)
    
    # Header Row
    hdr_cells = constraints_table.rows[0].cells
    hdr_titles = ["Field", "Details"]
    for i, title in enumerate(hdr_titles):
        hdr_cells[i].text = title
        set_cell_background(hdr_cells[i], "D9D9D9")
        set_cell_margins(hdr_cells[i], top=120, bottom=120, left=150, right=150)
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_after = Pt(0)
        for r in p.runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(11)
            r.font.bold = True
            r.font.color.rgb = RGBColor(0, 0, 0)
            
    # Academic Design Constraints & Standards Data
    rows_data = [
        ("Student Group", [
            "Yashvinthan M           Tharun Kumar D          Santhosh kumar Y",
            "231061101162            231061101150            231061101136"
        ]),
        ("Project Title", [
            "AiSOC: Autonomous AI-Powered Security Operations Center Platform with Real-Time Correlation, Graph-Based Threat Investigation, and Automated Triage"
        ]),
        ("Program Concentration Area", [
            "Cybersecurity, Artificial Intelligence, Machine Learning, Graph Theory, Distributed Systems and Cloud Security"
        ]),
        ("Constraints", [
            "Security telemetry streams generate millions of high-volume, high-velocity noisy events with tight latency constraints (<2.5s triage target). Real-time correlation must operate under strict memory and computation limits while maintaining high detection precision without false-positive alert fatigue."
        ]),
        ("Economic", ["Yes"]),
        ("Environmental", ["Yes"]),
        ("Sustainability", ["Yes"]),
        ("Implementable", ["Yes"]),
        ("Ethical", ["Yes"]),
        ("Health and Safety", ["Yes"]),
        ("Social", ["Yes"]),
        ("Political", ["Not Applicable (NA)."]),
        ("Other", ["N/A"]),
        ("Standards", [
            "IEEE 830 – Software Requirements Specification",
            "ISO/IEC 25010 – Software Quality Model",
            "IEEE 1471 – Software Architecture Description",
            "OCSF v1.1.0 – Open Cybersecurity Schema Framework",
            "MITRE ATT&CK v14.1 – Enterprise Adversary Tactics and Techniques",
            "STIX 2.1 – Structured Threat Information Expression",
            "NIST SP 800-61 Rev. 2 – Computer Security Incident Handling Guide",
            "RFC 6749 – OAuth 2.0 Authorization Framework / JWT (RFC 7519)"
        ]),
        ("Prerequisite Courses for the Major Design Experience", [
            "1. Computer Networks",
            "2. Cryptography and Network Security",
            "3. Machine Learning and Artificial Intelligence",
            "4. Data Structures and Algorithms",
            "5. Database Management Systems and Distributed Systems"
        ])
    ]
    
    for field, lines in rows_data:
        row_cells = constraints_table.add_row().cells
        set_cell_margins(row_cells[0], top=100, bottom=100, left=150, right=150)
        set_cell_margins(row_cells[1], top=100, bottom=100, left=150, right=150)
        
        # Field cell (Col 0)
        p0 = row_cells[0].paragraphs[0]
        p0.text = field
        p0.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p0.paragraph_format.line_spacing = 1.15
        p0.paragraph_format.space_after = Pt(0)
        for r in p0.runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(10)
            r.font.bold = True
            r.font.color.rgb = RGBColor(0, 0, 0)
            
        # Details cell (Col 1)
        row_cells[1].text = ""
        for idx, line in enumerate(lines):
            if idx == 0:
                p1 = row_cells[1].paragraphs[0]
            else:
                p1 = row_cells[1].add_paragraph()
            p1.text = line
            p1.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p1.paragraph_format.line_spacing = 1.15
            p1.paragraph_format.space_after = Pt(2 if len(lines) > 1 else 0)
            for r in p1.runs:
                r.font.name = 'Times New Roman'
                r.font.size = Pt(10)
                r.font.color.rgb = RGBColor(0, 0, 0)
                
    for row in constraints_table.rows:
        row.cells[0].width = Inches(1.8)
        row.cells[1].width = Inches(4.6)

    # Section 2: Acknowledgement and Front Matter (Roman numerals starting at i)
    s_front = doc.add_section()
    apply_section_margins(s_front)
    s_front.different_first_page_header_footer = False
    sectPr_f = s_front._sectPr
    for child in list(sectPr_f):
        if child.tag.endswith('pgNumType'):
            sectPr_f.remove(child)
    pg_xml_f = f'<w:pgNumType {nsdecls("w")} w:fmt="lowerRoman" w:start="1"/>'
    sectPr_f.append(parse_xml(pg_xml_f))
    
    footer_f = s_front.footer
    footer_f.is_linked_to_previous = False
    p_foot_f = footer_f.paragraphs[0]
    p_foot_f.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_foot_f.text = ''
    run_f = p_foot_f.add_run()
    run_f.font.name = 'Times New Roman'
    run_f.font.size = Pt(10)
    run_f.font.color.rgb = RGBColor(0, 0, 0)
    fld_f = parse_xml(f'<w:fldSimple {nsdecls("w")} w:instr="PAGE"/>')
    p_foot_f._p.append(fld_f)

    # Acknowledgement
    p_form3 = doc.add_paragraph()
    p_form3.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_form3.paragraph_format.space_after = Pt(4)
    r_form3 = p_form3.add_run("FORM NO.-F/TL/024\nREV.00 Date 20.03.2020")
    r_form3.font.name = 'Times New Roman'
    r_form3.font.size = Pt(9)
    r_form3.font.bold = True

    add_ch_heading("ACKNOWLEDGEMENT")
    add_p("We would first like to thank our beloved Founder Chancellor Thiru. Dr. A.C. SHANMUGAM, B.A., B.L., President Er. A.C.S. ARUNKUMAR, B.Tech., M.B.A., and Secretary Thiru A. RAVIKUMAR for all the encouragement and support extended to us during the tenure of this project and also our years of studies in this wonderful University.")
    add_p("We express our heartfelt thanks to our Vice Chancellor Prof. Dr. S. GEETHALAKSHMI for providing all the support for our Mini Project.")
    add_p("We express our heartfelt thanks to our Dean and Head of the Department Prof. Dr. S. GEETHA, who has been actively involved and very influential from the start till the completion of our mini project.")
    add_p("Our sincere thanks to our Project Guides and Mini Project Coordinators Dr. F. ANTONY and Mrs. CHINCHU NAIR for their continuous guidance and encouragement throughout this work, which has made the project a success.")
    add_p("We would also like to thank all the teaching and non-teaching staff of the Computer Science and Engineering department for their constant support and the encouragement given to us while we went about achieving our project goals.")
    add_p("\n\nYASHVINTHAN M (Reg No: 231061101162)\nTHARUN KUMAR D (Reg No: 231061101150)\nSANTHOSH KUMAR Y (Reg No: 231061101136)", bold=True)

    doc.add_page_break()

    # Abstract
    add_ch_heading("ABSTRACT")
    add_p("In modern organizations, Security Operations Centers (SOCs) are responsible for monitoring computer networks and responding to cyber attacks. However, security teams face a major challenge known as 'Alert Fatigue,' where hundreds of thousands of raw alerts are generated daily by firewalls, cloud services, and antivirus software. Over 80% of these alerts turn out to be harmless false alarms, but human analysts still spend hours manually checking each ticket across multiple disconnected browser tools, causing delays in detecting real attacks.")
    add_p("To address this problem, this project develops AiSOC, an open-source, automated Security Operations Center platform powered by Artificial Intelligence. The system automates the complete incident response lifecycle: incoming security logs are rapidly collected and converted into the standard Open Cybersecurity Schema Framework (OCSF) format in under 2 milliseconds; repetitive alarms are automatically filtered out using Simhash fingerprinting; and Machine Learning models (Isolation Forest) calculate the real risk score of each event.")
    add_p("To understand how an attack spreads across the network, the platform links users, computers, and IP addresses in a Neo4j graph database. A team of four specialized AI agents (DetectAgent, TriageAgent, HuntAgent, and RespondAgent) then collaborates to investigate the incident, search historical logs, write a clear summary, and formulate a response plan. To ensure safety, high-impact containment actions (such as isolating a critical server) require human confirmation before execution.")
    add_p("The platform was tested across 200 attack scenarios spanning lateral movement, cloud credential theft, and phishing. Experimental results showed an 85.5% reduction in alert noise and reduced incident investigation time from the traditional manual baseline of 45 minutes down to just 1.05 seconds with 94.2% attack classification accuracy. The system includes an interactive web dashboard for security analysts and provides a practical, open-source solution for modern cybersecurity defense.")
    add_p("Keywords: Security Operations Center (SOC), Artificial Intelligence, Machine Learning, Multi-Agent Systems, OCSF Normalization, Graph Databases, Cybersecurity, Incident Response.", bold=True, italic=True)

    doc.add_page_break()

    # Table of Contents (Specimen Layout)
    add_ch_heading("TABLE OF CONTENTS")
    toc_headers = ["CHAPTER NO.", "TITLE", "PAGE NO."]
    toc_widths = [Inches(1.5), Inches(4.1), Inches(0.9)]
    toc_data = [
        ["", "ABSTRACT", "ii"],
        ["", "LIST OF TABLES", "v"],
        ["", "LIST OF FIGURES", "vi"],
        ["", "NOMENCLATURE", "viii"],
        ["1.", "INTRODUCTION", "1"],
        ["", "1.1 BROAD AREA OF THE PROJECT", "1"],
        ["", "1.2 PROBLEM STATEMENT", "2"],
        ["", "1.3 MOTIVATION", "2"],
        ["", "1.4 OBJECTIVES OF THE PROJECT", "3"],
        ["", "1.5 ETHICAL, SOCIAL, AND PROFESSIONAL ISSUES", "3"],
        ["", "1.6 REPORT ORGANIZATION", "4"],
        ["2.", "LITERATURE SURVEY", "5"],
        ["", "2.1 Previous Research on Security Monitoring & SIEM", "5"],
        ["", "2.2 Machine Learning and Mathematical Deduplication", "6"],
        ["", "2.3 Knowledge Graphs for Attack Path Tracing", "7"],
        ["", "2.4 Multi-Agent LLM Systems in Cybersecurity", "7"],
        ["", "2.5 Summary of Gaps in Existing Research", "8"],
        ["3.", "EXISTING SYSTEM", "9"],
        ["", "3.1 How Traditional Security Operations Work Today", "9"],
        ["", "3.2 Architectural and Technical Bottlenecks", "10"],
        ["", "3.3 Operational Impact and Delay Metrics", "11"],
        ["", "3.4 Disadvantages of the Existing System", "11"],
        ["4.", "PROPOSED SYSTEM", "12"],
        ["", "4.1 System Overview and Core Concept", "12"],
        ["", "4.2 System Architecture and Topology", "12"],
        ["", "4.3 Key System Modules and Responsibilities", "14"],
        ["", "4.4 METHODOLOGY — COMPLETE SYSTEM WORKFLOW", "15"],
        ["", "4.5 Threat Actor Attribution and Diamond Model", "16"],
        ["", "4.6 Unified Modeling Language (UML) Diagrams", "16"],
        ["", "    4.6.1 Use case diagram", "17"],
        ["", "    4.6.2 Activity diagram", "18"],
        ["", "    4.6.3 Sequence diagram", "19"],
        ["", "    4.6.4 Class diagram", "20"],
        ["", "    4.6.5 State machine diagram", "21"],
        ["", "4.7 Automation Maturity Model (L0 to L4)", "22"],
        ["", "4.8 Database Design and Entity-Relationship Model", "22"],
        ["", "    4.8.1 Entity–relationship model", "22"],
        ["5.", "SYSTEM SPECIFICATION", "24"],
        ["", "5.1 Hardware Requirements", "24"],
        ["", "5.2 Software Requirements and Runtimes", "24"],
        ["", "5.3 Frameworks, Libraries, and External Services", "25"],
        ["", "5.4 Database and Streaming Storage Engines", "25"],
        ["", "5.5 Cryptographic Security and Data Protection", "26"],
        ["6.", "IMPLEMENTATION", "27"],
        ["", "6.1 Data Ingestion and Log Normalization Module", "27"],
        ["", "6.2 Threat Intelligence and IOC Search Module", "28"],
        ["", "6.3 Alert Deduplication and Machine Learning Scoring Engine", "29"],
        ["", "6.4 Neo4j Knowledge Graph and Attack-Path Traversal", "31"],
        ["", "6.5 Multi-Agent AI Investigation Subsystem", "32"],
        ["", "6.6 Blast-Radius Safety Controller and Response Module", "34"],
        ["", "6.7 Detection Rules, Noise Tuning, and Case Disposition", "35"],
        ["", "6.8 Audit Ledger, System Health, and Pipeline Observability", "36"],
        ["7.", "RESULT AND CONCLUSION", "38"],
        ["", "7.1 Experimental Setup and Testing Dataset", "38"],
        ["", "7.2 Performance Evaluation Metrics", "39"],
        ["", "7.3 Benchmark Results and Findings", "39"],
        ["", "7.4 System Verification and Automated Test Cases", "40"],
        ["", "7.5 Case Study: Step-by-Step Lateral Movement Investigation", "40"],
        ["", "7.6 Impact of Individual Components (Ablation Analysis)", "41"],
        ["", "7.7 Conclusion", "41"],
        ["", "7.8 Future Enhancements", "41"],
        ["", "REFERENCES", "42"],
        ["", "APPENDIX A: CORE SOURCE CODE LISTINGS", "44"],
        ["", "    A.1 High-Performance Log Ingestion Worker in Go", "44"],
        ["", "    A.2 64-Bit Simhash Alert Deduplication Algorithm", "45"],
        ["", "    A.3 Multi-Agent LangGraph Orchestration State Machine", "46"],
        ["", "APPENDIX B: OCSF SCHEMAS & INCIDENT JSON PAYLOADS", "47"],
        ["", "    B.1 Normalized OCSF Security Finding Event Sample", "47"],
        ["", "    B.2 Multi-Agent Incident Investigation Ticket Envelope", "48"],
        ["", "APPENDIX C: SYSTEM VERIFICATION & TEST SUITE LOGS", "49"],
        ["", "    C.1 Automated Unit and Integration Test Suite Results", "49"],
        ["", "    C.2 High-Throughput Ingestion Benchmark Logs", "49"],
        ["", "APPENDIX D: PHYSICAL HARDWARE LAB TESTBED SETUP", "50"],
        ["", "    D.1 Bare-Metal Server Testbed and Network Rack Setup", "50"],
        ["", "APPENDIX E: EXTENDED APPLICATION CONSOLE INTERFACES", "51"],
        ["", "    E.1 Natural Language Threat Hunting Surface (/hunt)", "51"],
        ["", "    E.2 Incident Case Management and Evidence Rail Console (/cases)", "52"],
        ["", "    E.3 Real-Time Multi-Tenant Alert Stream Console (/alerts)", "52"]
    ]
    add_toc_table(toc_widths, toc_headers, toc_data)

    doc.add_page_break()

    # List of Tables (Specimen Layout)
    add_ch_heading("LIST OF TABLES")
    lot_headers = ["TABLE NO.", "TITLE", "PAGE NO."]
    lot_widths = [Inches(1.5), Inches(4.1), Inches(0.9)]
    lot_data = [
        ["2.1", "Comparison of Security Log Normalization Standards", "6"],
        ["2.2", "Summary of Literature Review and Identified Research Gaps", "8"],
        ["3.1", "Comparison of Operational Performance Metrics in Traditional SOC Operations", "11"],
        ["4.1", "Core System Modules, Programming Languages, and Processing Runtimes", "14"],
        ["4.2", "Five-Tier Automation Maturity Model (L0 to L4) and Safety Controls", "22"],
        ["5.1", "Minimum, Experimental Testbed, and Recommended Hardware Specifications", "24"],
        ["5.2", "Software Environment, Language Runtimes, and Toolchain Versions", "25"],
        ["5.3", "Database and Storage Engines Specifications and Data Retention Policies", "26"],
        ["6.1", "Mapping of Third-Party Security Logs to Standard OCSF Schema Classes", "27"],
        ["6.2", "Threat Intelligence Feed Sources, Protocols, and Update Frequencies", "29"],
        ["6.3", "Feature Vector Extracted for Machine Learning Risk Scoring", "31"],
        ["6.4", "Neo4j Security Knowledge Graph Node Labels and Relationships", "32"],
        ["6.5", "Specialized AI Agents, Investigation Roles, Tools, and Outputs", "34"],
        ["7.1", "Evaluation Dataset and Attack Scenario Test Categories", "39"],
        ["7.2", "Experimental Results: Noise Reduction, MTTR Speedup, and Accuracy", "39"],
        ["7.3", "Automated Software Verification Test Cases and Execution Status", "40"],
        ["C.1", "Microservice Automated Test Suite Execution and Code Coverage Summary", "49"],
        ["D.1", "Physical Laboratory Hardware Testbed Inventory, Specifications, and Architecture Roles", "51"]
    ]
    add_toc_table(lot_widths, lot_headers, lot_data)

    doc.add_page_break()

    # List of Figures (Specimen Layout)
    add_ch_heading("LIST OF FIGURES")
    lof_headers = ["FIGURE NO.", "TITLE", "PAGE NO."]
    lof_widths = [Inches(1.5), Inches(4.1), Inches(0.9)]
    lof_data = [
        ["1.1", "Technical Domains Unified by the AiSOC Platform", "1"],
        ["1.2", "The Traditional SOC Alert Fatigue and Investigation Bottleneck", "2"],
        ["2.1", "Evolutionary Stages of Enterprise Security Operations Systems (2000–2026)", "5"],
        ["3.1", "Traditional Multi-Tier Security Triage Process and Hand-off Bottlenecks", "9"],
        ["4.1", "High-Level End-to-End System Topology of the AiSOC Platform", "13"],
        ["4.4", "Methodology — Complete End-to-End System Workflow Flowchart", "15"],
        ["4.6.1", "UML Use Case Diagram for Enterprise SOC Actors and Autonomous AI Agents", "17"],
        ["4.6.2", "UML Activity Diagram: Ingestion, Triage, and Multi-Agent Investigation Flow", "18"],
        ["4.6.3", "UML Sequence Diagram: Chronological Message Exchanges During Triage", "19"],
        ["4.6.4", "UML Class Diagram of Core Entity Model and System Constraints", "20"],
        ["4.6.5", "UML State Machine Diagram: Incident and Alert Lifecycle State Transitions", "21"],
        ["4.8.1", "Entity–Relationship (ER) Model of Core Relational Database Tables", "22"],
        ["6.1", "High-Speed Log Ingestion, OCSF Normalization, and Attack Technique Tagging Pipeline", "27"],
        ["6.2", "Threat Intelligence Ingestion and In-Memory Bloom Filter Search Architecture", "28"],
        ["6.3", "Threat Intelligence and IOC Search Console on the Web Dashboard", "28"],
        ["6.4", "Dual-Stage Machine Learning Scoring Architecture (Isolation Forest + LightGBM)", "29"],
        ["6.5", "Live Security Operations Dashboard and Prioritized Alert Queue", "30"],
        ["6.6", "Autonomous Alert Triage Command-Line Execution Result", "30"],
        ["6.7", "Neo4j Security Knowledge Graph Schema Showing Entity Relationships", "31"],
        ["6.8", "Interactive Attack Graph and MITRE ATT&CK Mapping Workbench", "32"],
        ["6.9", "Multi-Agent AI Collaborative Investigation Workflow (LangGraph State Graph)", "33"],
        ["6.10", "Incident Case Dossier and Chronological Evidence Timeline Screen", "33"],
        ["6.11", "Blast-Radius Safety Check and Approval Mechanism", "34"],
        ["6.12", "Visual Playbook Studio and Blast-Radius Action Approval Screen", "35"],
        ["6.13", "Enterprise Detection Rule Catalog and MITRE Coverage Page", "35"],
        ["6.14", "Analyst Feedback and Machine Learning Noise-Tuning Interface", "36"],
        ["6.15", "Immutable AI Chain-of-Thought Audit Ledger and Activity History", "36"],
        ["6.16", "Data Connector Health and Ingestion Pipeline Observability Dashboard", "37"],
        ["7.1", "Comparative Alert Noise Reduction and MTTR Compression Chart", "39"],
        ["7.2", "Lateral Movement Investigation Trace in the Next.js Web Console", "40"],
        ["D.1", "Physical Hardware Lab Testbed, Server Rack, and Network Infrastructure", "50"],
        ["E.1", "Natural Language Threat Hunting Surface (/hunt) with AI-Assisted Query Generation", "52"],
        ["E.2", "Enterprise Incident Case Management and Evidence Rail Interface (/cases)", "52"],
        ["E.3", "Real-Time Multi-Tenant Alert Stream and Live Ingestion Console (/alerts)", "53"]
    ]
    add_toc_table(lof_widths, lof_headers, lof_data)

    doc.add_page_break()

    # Nomenclature / List of Symbols and Abbreviations (Single-Page Compact Layout)
    add_ch_heading("NOMENCLATURE")
    
    add_sec_heading("1. Mathematical Symbols and Operational Metrics")
    add_p("• H(x, y) : Hamming Distance between two 64-bit binary Simhash fingerprints for alert deduplication.", space_after=2)
    add_p("• s(x, n) : Anomaly Score output by Isolation Forest ensemble for feature vector x across sample size n.", space_after=2)
    add_p("• E(h(x)) : Expected tree path length of sample x across the randomized isolation trees.", space_after=2)
    add_p("• ΔZ_ij : Gradient step delta in LightGBM LambdaRank for alert prioritization pair (i, j).", space_after=2)
    add_p("• B_r(e) : Blast Radius graph traversal metric representing affected infrastructure within radius r.", space_after=2)
    add_p("• R_alert : Percentage reduction in alert volume achieved through automated deduplication and fusion.", space_after=2)
    add_p("• A_mitre : Percentage classification accuracy of automated MITRE ATT&CK technique extraction.", space_after=6)
    
    add_sec_heading("2. Cybersecurity and Architectural Abbreviations")
    
    abbr_headers = ["Acronym", "Expansion / Technical Domain"]
    abbr_widths = [Inches(1.6), Inches(4.8)]
    abbr_data = [
        ["OCSF", "Open Cybersecurity Schema Framework (Universal Telemetry Standard)"],
        ["SIEM", "Security Information and Event Management"],
        ["SOAR", "Security Orchestration, Automation, and Response"],
        ["EDR / NDR", "Endpoint Detection and Response / Network Detection and Response"],
        ["UEBA", "User and Entity Behavior Analytics (Anomaly Detection)"],
        ["TTP", "Tactics, Techniques, and Procedures (Adversary Behaviors)"],
        ["IOC", "Indicator of Compromise (Artifacts: Hashes, IPs, Domains)"],
        ["STIX / TAXII", "Structured Threat Information Expression / Transport Mechanism"],
        ["MTTA / MTTR", "Mean Time to Acknowledge / Mean Time to Respond (SOC KPI)"],
        ["RAG", "Retrieval-Augmented Generation (Context-Injected LLM Queries)"],
        ["DAG", "Directed Acyclic Graph (Multi-Agent Workflow Topology)"],
        ["LSH", "Locality-Sensitive Hashing (Simhash Fingerprinting)"],
        ["CEF", "Common Event Format (Standard Syslog Log Structure)"],
        ["SIGMA", "Generic Signature Format for SIEM and Log Analysis"],
        ["CVE / KEV", "Common Vulnerabilities and Exposures / Known Exploited Vulnerabilities"],
        ["RBAC / RLS", "Role-Based Access Control / Row-Level Security (Multi-Tenancy)"]
    ]
    add_table(abbr_widths, abbr_headers, abbr_data)

    # CHAPTER GENERATION
    from ch1_gen import generate_chapter_1
    from ch2_gen import generate_chapter_2
    from ch3_gen import generate_chapter_3
    from ch4_gen import generate_chapter_4
    from ch5_gen import generate_chapter_5
    from ch6_gen import generate_chapter_6
    from ch7_gen import generate_chapter_7_and_refs
    from appendix_gen import generate_appendix

    print("Generating Chapter 1...")
    add_chapter_section(start_num=1)
    generate_chapter_1(add_p, add_ch_heading, add_sec_heading, add_subsec_heading, add_code, add_table, add_fig, FIG_DIR)

    print("Generating Chapter 2...")
    add_chapter_section(start_num=None)
    generate_chapter_2(add_p, add_ch_heading, add_sec_heading, add_subsec_heading, add_code, add_table, add_fig, FIG_DIR)

    print("Generating Chapter 3...")
    add_chapter_section(start_num=None)
    generate_chapter_3(add_p, add_ch_heading, add_sec_heading, add_subsec_heading, add_code, add_table, add_fig, FIG_DIR)

    print("Generating Chapter 4 with Methodology and UML Diagrams...")
    add_chapter_section(start_num=None)
    generate_chapter_4(add_p, add_ch_heading, add_sec_heading, add_subsec_heading, add_code, add_table, add_fig, FIG_DIR)

    print("Generating Chapter 5...")
    add_chapter_section(start_num=None)
    generate_chapter_5(add_p, add_ch_heading, add_sec_heading, add_subsec_heading, add_code, add_table)

    print("Generating Chapter 6 with 10 Screenshots & Technical Deep Dive...")
    add_chapter_section(start_num=None)
    generate_chapter_6(add_p, add_ch_heading, add_sec_heading, add_subsec_heading, add_code, add_table, add_fig, FIG_DIR)

    print("Generating Chapter 7 and References...")
    add_chapter_section(start_num=None)
    generate_chapter_7_and_refs(add_p, add_ch_heading, add_sec_heading, add_subsec_heading, add_code, add_table, add_fig, FIG_DIR)

    print("Generating Appendices (A, B, C, D)...")
    add_chapter_section(start_num=None)
    generate_appendix(add_p, add_ch_heading, add_sec_heading, add_subsec_heading, add_code, add_table, add_fig, FIG_DIR)

    # Enforce Exact University Margin Specifications across ALL document sections:
    # Left: 2.5 cm | Right: 2.0 cm | Top: 2.0 cm | Bottom: 2.0 cm
    for s in doc.sections:
        s.page_width = Cm(21.0)
        s.page_height = Cm(29.7)
        s.left_margin = Cm(2.5)
        s.right_margin = Cm(2.0)
        s.top_margin = Cm(2.0)
        s.bottom_margin = Cm(2.0)

    out_paths = [
        r"c:\Users\yashv\dev\work in progress\mini project\AiSOC\AiSOC_BTech_Mini_Project_Report.docx",
        r"c:\Users\yashv\dev\work in progress\mini project\AiSOC\docs\AiSOC_BTech_Mini_Project_Report.docx"
    ]

    for p in out_paths:
        os.makedirs(os.path.dirname(os.path.abspath(p)), exist_ok=True)
        saved = False
        candidates = [p, p.replace(".docx", "_v3.docx"), p.replace(".docx", "_Academic.docx")]
        for cand in candidates:
            try:
                doc.save(cand)
                print(f"Saved report successfully to: {cand}")
                saved = True
                break
            except PermissionError:
                print(f"Warning: {cand} is currently locked. Trying next candidate...")
        if not saved:
            print(f"Could not save to any candidate for {p}")

if __name__ == "__main__":
    build_master_docx()
