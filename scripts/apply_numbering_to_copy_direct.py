import docx
from docx.shared import Cm, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
import os
import shutil

def apply_section_margins(section):
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    section.left_margin = Cm(2.5)
    section.right_margin = Cm(2.0)
    section.top_margin = Cm(2.0)
    section.bottom_margin = Cm(2.0)

def clear_footer(footer):
    footer.is_linked_to_previous = False
    for p in footer.paragraphs:
        p.text = ''
        p._p.remove(p._p.get_or_add_pPr()) if hasattr(p._p, 'get_or_add_pPr') else None

def set_footer_page_number(footer):
    footer.is_linked_to_previous = False
    p = footer.paragraphs[0]
    p.text = ''
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = p.add_run()
    run.font.name = 'Times New Roman'
    run.font.size = Pt(10)
    run.font.color.rgb = RGBColor(0, 0, 0)
    fld = parse_xml(f'<w:fldSimple {nsdecls("w")} w:instr="PAGE"/>')
    p._p.append(fld)

def configure_section_numbering(section, is_roman=False, start_num=None, suppress_first_page=True):
    apply_section_margins(section)
    section.different_first_page_header_footer = suppress_first_page
    
    sectPr = section._sectPr
    for child in list(sectPr):
        if child.tag.endswith('pgNumType'):
            sectPr.remove(child)
            
    fmt = 'lowerRoman' if is_roman else 'decimal'
    if start_num is not None:
        pg_xml = f'<w:pgNumType {nsdecls("w")} w:fmt="{fmt}" w:start="{start_num}"/>'
    else:
        pg_xml = f'<w:pgNumType {nsdecls("w")} w:fmt="{fmt}"/>'
    sectPr.append(parse_xml(pg_xml))
    
    # Configure regular footer (page 2 onwards)
    set_footer_page_number(section.footer)
    
    # Configure first page footer
    if suppress_first_page:
        section.first_page_footer.is_linked_to_previous = False
        p_fp = section.first_page_footer.paragraphs[0]
        p_fp.text = ''
    else:
        # If not suppressed (like Section 2 Front Matter), show page number on first page too
        set_footer_page_number(section.first_page_footer)

def main():
    doc_path = 'AiSOC_BTech_Mini_Project_Report - Copy.docx'
    doc = docx.Document(doc_path)
    
    targets = [
        ('ACKNOWLEDGEMENT', 'Acknowledgement'),
        ('CHAPTER 1', 'Chapter 1'),
        ('CHAPTER 2', 'Chapter 2'),
        ('CHAPTER 3', 'Chapter 3'),
        ('CHAPTER 4', 'Chapter 4'),
        ('CHAPTER 5', 'Chapter 5'),
        ('CHAPTER 6', 'Chapter 6'),
        ('CHAPTER 7', 'Chapter 7'),
        ('APPENDIX A', 'Appendix A')
    ]
    
    # Find matching paragraph indices
    target_indices = []
    for tgt_prefix, name in targets:
        found = False
        for idx, p in enumerate(doc.paragraphs):
            t = p.text.strip().replace('\n', ' ')
            if t.upper().startswith(tgt_prefix):
                target_indices.append((idx, tgt_prefix, name))
                found = True
                break
        if not found:
            print(f"WARNING: Target not found: {tgt_prefix}")

    print(f"Found {len(target_indices)} section boundary points:")
    for idx, prefix, name in target_indices:
        print(f"  P{idx}: {name} ({prefix})")
        
    # Insert sectPr before each target paragraph
    # Note: To avoid index shifting issues, we access by element or work from end to start or on existing paragraph objects
    for idx, prefix, name in target_indices:
        target_p = doc.paragraphs[idx]
        prev_p = doc.paragraphs[idx - 1]
        
        # Remove any page break elements in target_p or prev_p
        for br in target_p._p.xpath('.//w:br[@w:type="page"]'):
            br.getparent().remove(br)
        for br in prev_p._p.xpath('.//w:br[@w:type="page"]'):
            br.getparent().remove(br)
            
        # Add sectPr to prev_p
        pPr = prev_p._p.get_or_add_pPr()
        # Remove any existing sectPr
        for child in list(pPr):
            if child.tag.endswith('sectPr'):
                pPr.remove(child)
        sectPr = parse_xml(f'<w:sectPr {nsdecls("w")}><w:type w:val="nextPage"/></w:sectPr>')
        pPr.append(sectPr)

    # Re-open or inspect doc.sections
    print(f"Total sections created: {len(doc.sections)}")
    
    # Section 0: Title & Bonafide Certificate & Prelims
    s0 = doc.sections[0]
    apply_section_margins(s0)
    s0.different_first_page_header_footer = True
    s0.footer.is_linked_to_previous = False
    s0.footer.paragraphs[0].text = ''
    s0.first_page_footer.is_linked_to_previous = False
    s0.first_page_footer.paragraphs[0].text = ''
    print("Section 0 (Title & Certificate): Unprinted (No page numbers)")
    
    # Section 1: Front Matter (Acknowledgement to List of Figures) -> Roman i, ii, iii...
    s1 = doc.sections[1]
    configure_section_numbering(s1, is_roman=True, start_num=1, suppress_first_page=False)
    print("Section 1 (Acknowledgements & Prelims): Roman i, ii, iii...")
    
    # Section 2: Chapter 1 -> Arabic starting at 1, First page suppressed
    s2 = doc.sections[2]
    configure_section_numbering(s2, is_roman=False, start_num=1, suppress_first_page=True)
    print("Section 2 (Chapter 1): Arabic 1..N, First page suppressed")
    
    # Sections 3 to 9: Chapters 2-7 and Appendices -> Arabic continuous, First page suppressed
    section_names = [
        "Chapter 2", "Chapter 3", "Chapter 4", "Chapter 5",
        "Chapter 6", "Chapter 7", "Appendices"
    ]
    for i in range(3, len(doc.sections)):
        s = doc.sections[i]
        name = section_names[i - 3] if (i - 3) < len(section_names) else f"Section {i}"
        configure_section_numbering(s, is_roman=False, start_num=None, suppress_first_page=True)
        print(f"Section {i} ({name}): Arabic continuous, First page suppressed")

    # Save to Copy file
    output_path = doc_path
    try:
        doc.save(output_path)
        print(f"SUCCESS: Saved changes directly to {output_path}")
    except PermissionError:
        alt_path = 'AiSOC_BTech_Mini_Project_Report - Copy_Numbered.docx'
        doc.save(alt_path)
        print(f"NOTICE: '{output_path}' is currently open in Microsoft Word and locked.")
        print(f"SUCCESS: Saved updated numbered document to '{alt_path}'.")
        print(f"Please close Word to allow overwriting, or open '{alt_path}' directly!")

if __name__ == '__main__':
    main()
