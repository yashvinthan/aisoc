import os
import shutil
import win32com.client

preview_dir = os.path.abspath('docs/ppt_preview')
if os.path.exists(preview_dir):
    shutil.rmtree(preview_dir)
os.makedirs(preview_dir, exist_ok=True)

ppt_path = os.path.abspath('AiSOC_Mini_Project_Presentation_Master.pptx')
ppt = win32com.client.Dispatch('PowerPoint.Application')
pres = ppt.Presentations.Open(ppt_path, WithWindow=False)
out_path = os.path.join(preview_dir, 'Slide.PNG')
pres.SaveAs(out_path, 17) # 17 = ppSaveAsPNG
pres.Close()
ppt.Quit()
print("All slides successfully exported to docs/ppt_preview/")
