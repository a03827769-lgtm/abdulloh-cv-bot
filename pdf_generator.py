from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.units import inch
from content import CV_DATA
import os

def generate_cv_pdf(lang: str, output_path: str, user_name: str = "Foydalanuvchi"):
    """Generates an Agency-Grade professional PDF CV."""
    doc = SimpleDocTemplate(
        output_path, 
        pagesize=A4,
        rightMargin=45,
        leftMargin=45,
        topMargin=45,
        bottomMargin=45
    )
    styles = getSampleStyleSheet()
    
    # --- DESIGN SYSTEM ---
    c_primary = colors.HexColor("#0f172a") # Midnight
    c_accent = colors.HexColor("#3b82f6")  # Electric Blue
    c_text = colors.HexColor("#475569")    # Slate
    
    # --- STYLES ---
    st_name = ParagraphStyle('Name', fontSize=28, textColor=c_primary, fontName='Helvetica-Bold', spaceAfter=2)
    st_title = ParagraphStyle('Title', fontSize=12, textColor=c_accent, fontName='Helvetica-Bold', spaceAfter=14, letterSpacing=1)
    st_section = ParagraphStyle('Sec', fontSize=14, textColor=c_primary, fontName='Helvetica-Bold', spaceBefore=20, spaceAfter=10, borderPadding=(0,0,3,0), borderColor=c_accent, borderWidth=0, leading=20)
    st_body = ParagraphStyle('Body', fontSize=10, leading=15, textColor=c_text, fontName='Helvetica')
    st_case_title = ParagraphStyle('CaseT', fontSize=11, fontName='Helvetica-Bold', textColor=c_primary, spaceBefore=8)
    st_case_body = ParagraphStyle('CaseB', fontSize=9, leading=13, textColor=c_text, leftIndent=12, spaceAfter=8)
    
    elements = []
    
    # --- HEADER ---
    elements.append(Paragraph(CV_DATA["name"].upper(), st_name))
    elements.append(Paragraph("CREATIVE DIRECTOR | FULL-STACK DEVELOPER | AI SPECIALIST", st_title))
    
    contact_data = [
        [f"📍 {CV_DATA['location']}", f"📱 {CV_DATA['contacts']['telegram']}", f"✉️ {CV_DATA['contacts']['instagram']}"]
    ]
    t_contact = Table(contact_data, colWidths=[2*inch, 2*inch, 2*inch])
    t_contact.setStyle(TableStyle([
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('TEXTCOLOR', (0,0), (-1,-1), c_text),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ]))
    elements.append(t_contact)
    elements.append(Spacer(1, 10))
    elements.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#e2e8f0"), spaceBefore=10, spaceAfter=10))
    
    # --- ABOUT ---
    elements.append(Paragraph("PROFESSIONAL PROFILE", st_section))
    about_text = {
        "uz": "Innovatsion texnologiyalar va vizual san'at uyg'unligida bizneslar uchun yuqori natijali yechimlar yaratuvchi mutaxassis. Nordic University talabasi va 5 yillik professional Taekwondo tajribasiga ega intizomli lider.",
        "ru": "Специалист, создающий высокоэффективные решения на стыке инновационных технологий и визуального искусства. Студент Nordic University и дисциплинированный лидер с 5-летним опытом в Тхэквондо.",
        "en": "Specialist creating high-performance solutions at the intersection of innovative technologies and visual arts. Nordic University student and a disciplined leader with 5 years of professional Taekwondo experience."
    }
    elements.append(Paragraph(about_text[lang], st_body))
    
    # --- CASE STUDIES ---
    elements.append(Paragraph("STRATEGIC PROJECTS & CASE STUDIES", st_section))
    for proj in CV_DATA["projects"]:
        elements.append(Paragraph(proj['name'], st_case_title))
        elements.append(Paragraph(proj[lang], st_case_body))
    
    # --- SKILLS & EXPERIENCE (Two Column Layout) ---
    elements.append(Paragraph("EXPERTISE & SKILLS", st_section))
    skills_text = f"<b>Technical:</b> {', '.join(CV_DATA['skills']['technical'])}<br/><b>Soft Skills:</b> {', '.join(CV_DATA['skills']['soft'])}"
    elements.append(Paragraph(skills_text, st_body))
    
    elements.append(Paragraph("PROFESSIONAL EXPERIENCE", st_section))
    for exp in CV_DATA["experience"]:
        elements.append(Paragraph(f"<b>{exp['title']}</b> — {exp['duration']}", st_body))
        elements.append(Paragraph(exp['desc'][lang], st_case_body))

    # --- CALL TO ACTION ---
    elements.append(Spacer(1, 40))
    elements.append(HRFlowable(width="30%", thickness=2, color=c_accent, align='CENTER'))
    elements.append(Spacer(1, 10))
    cta_text = f"<i>This CV was generated exclusively for {user_name} by Abdulloh's AI Bot.</i><br/><b>Scan to see full Interactive Portfolio: t.me/AbdullohCvbot</b>"
    elements.append(Paragraph(cta_text, ParagraphStyle('CTA', parent=st_body, alignment=1, textColor=c_accent)))
    
    try:
        doc.build(elements)
        return True
    except Exception as e:
        print(f"PDF Error: {e}")
        return False
