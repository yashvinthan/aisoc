import os
import win32com.client

docx_path = os.path.abspath(r"AiSOC_BTech_Mini_Project_Report - Copy.docx")
print("Target file:", docx_path)

word = win32com.client.Dispatch("Word.Application")
word.Visible = False

try:
    doc = word.Documents.Open(docx_path)
    print("Opened document. Total paragraphs:", doc.Paragraphs.Count)
    print("Initial sections:", doc.Sections.Count)
    
    # Target headings to insert section breaks before
    target_headings = [
        "ACKNOWLEDGEMENT",
        "CHAPTER 1",
        "CHAPTER 2",
        "CHAPTER 3",
        "CHAPTER 4",
        "CHAPTER 5",
        "CHAPTER 6",
        "CHAPTER 7",
        "APPENDIX A"
    ]
    
    # In Word, wdSectionBreakNextPage = 2
    # wdHeaderFooterPrimary = 1
    # wdHeaderFooterFirstPage = 2
    # wdAlignParagraphRight = 2
    # wdPageNumberStyleArabic = 0
    # wdPageNumberStyleLowerRoman = 2
    
    if doc.Sections.Count == 1:
        for heading in target_headings:
            for p in doc.Paragraphs:
                text = p.Range.Text.strip()
                if text.startswith(heading):
                    rng = p.Range
                    rng.Collapse(1) # wdCollapseStart = 1
                    rng.InsertBreak(2) # 2 = wdSectionBreakNextPage
                    print(f"Inserted section break before: {heading}")
                    break
                
    print("Total sections:", doc.Sections.Count)
    
    cm_to_pt = 28.3465
    for i in range(1, doc.Sections.Count + 1):
        sec = doc.Sections(i)
        ps = sec.PageSetup
        ps.PageWidth = 21.0 * cm_to_pt
        ps.PageHeight = 29.7 * cm_to_pt
        ps.LeftMargin = 2.5 * cm_to_pt
        ps.RightMargin = 2.0 * cm_to_pt
        ps.TopMargin = 2.0 * cm_to_pt
        ps.BottomMargin = 2.0 * cm_to_pt
        
    # Configure Section 1 (Title / Cover, Bonafide, Constraints) - No page numbers
    sec1 = doc.Sections(1)
    sec1.PageSetup.DifferentFirstPageHeaderFooter = True
    sec1.Footers(1).Range.Text = ""
    sec1.Footers(2).Range.Text = ""
    
    # Configure Section 2: Roman numerals starting at i, bottom right
    sec2 = doc.Sections(2)
    sec2.PageSetup.DifferentFirstPageHeaderFooter = False
    sec2.Footers(1).LinkToPrevious = False
    sec2_footer = sec2.Footers(1).Range
    sec2_footer.Text = ""
    sec2_footer.ParagraphFormat.Alignment = 2 # Right
    sec2.Headers(1).PageNumbers.NumberStyle = 2 # lowerRoman
    sec2.Headers(1).PageNumbers.RestartNumberingAtSection = True
    sec2.Headers(1).PageNumbers.StartingNumber = 1
    sec2.Headers(1).PageNumbers.Add(PageNumberAlignment=2, FirstPage=True)
    
    # Configure Body Sections (Chapter 1 onwards): Arabic numbers starting at 1 for Ch1, continuous for rest
    # First page of each chapter must be suppressed!
    for sec_idx in range(3, doc.Sections.Count + 1):
        sec = doc.Sections(sec_idx)
        sec.PageSetup.DifferentFirstPageHeaderFooter = True
        
        # Unlink footers
        sec.Footers(1).LinkToPrevious = False # Primary footer (page 2+)
        sec.Footers(2).LinkToPrevious = False # First page footer
        sec.Footers(2).Range.Text = "" # Suppress first page
        
        sec.Headers(1).PageNumbers.NumberStyle = 0 # Arabic
        if sec_idx == 3:
            sec.Headers(1).PageNumbers.RestartNumberingAtSection = True
            sec.Headers(1).PageNumbers.StartingNumber = 1
        else:
            sec.Headers(1).PageNumbers.RestartNumberingAtSection = False
            
        f_range = sec.Footers(1).Range
        f_range.Text = ""
        f_range.ParagraphFormat.Alignment = 2 # Right
        sec.Headers(1).PageNumbers.Add(PageNumberAlignment=2, FirstPage=False)

    saved_path = docx_path
    try:
        doc.Save()
        print(f"Successfully saved in-place to: {docx_path}")
    except Exception as e:
        alt_path = docx_path.replace(".docx", "_Numbered.docx")
        print(f"File locked by another program. Saving to: {alt_path}")
        doc.SaveAs2(alt_path)
        saved_path = alt_path
        print(f"Successfully saved to: {alt_path}")
        
    doc.Close(False)
finally:
    word.Quit()
