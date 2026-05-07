from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.units import inch
from content import CV_DATA
import os

def generate_cv_pdf(lang: str, output_path: str, user_name: str = "Client"):
    """Generates an Elite Business Profile PDF for Abdulloh Muhammadjonov."""
    doc = SimpleDocTemplate(
        output_path, 
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )
    styles = getSampleStyleSheet()
    
    # --- EXECUTIVE DESIGN SYSTEM ---
    c_primary = colors.HexColor("#1e1b4b") # Deep Indigo
    c_accent = colors.HexColor("#4f46e5")  # Indigo 600
    c_text = colors.HexColor("#1f2937")    # Gray 800
    c_dim = colors.HexColor("#6b7280")     # Gray 500
    
    # --- PROFESSIONAL STYLES ---
    st_header = ParagraphStyle('Header', fontSize=28, textColor=c_primary, fontName='Helvetica-Bold', spaceAfter=2)
    st_title = ParagraphStyle('Title', fontSize=12, textColor=c_accent, fontName='Helvetica-Bold', spaceAfter=14, letterSpacing=1.5)
    st_section = ParagraphStyle('Section', fontSize=14, textColor=c_primary, fontName='Helvetica-Bold', spaceBefore=20, spaceAfter=10, borderPadding=5)
    st_body = ParagraphStyle('Body', fontSize=10, leading=14, textColor=c_text, fontName='Helvetica')
    st_label = ParagraphStyle('Label', fontSize=9, fontName='Helvetica-Bold', textColor=c_primary)
    
    elements = []
    
    # --- HEADER ---
    elements.append(Paragraph(CV_DATA["name"].upper(), st_header))
    elements.append(Paragraph(CV_DATA["title"].upper(), st_title))
    
    # Contact Info Table
    contacts = CV_DATA.get("contacts", {})
    info = [
        [f"📍 {CV_DATA['location']}", f"📱 {contacts.get('phone')}"],
        [f"📧 {contacts.get('email')}", f"🌐 {contacts.get('domain')}"]
    ]
    t_info = Table(info, colWidths=[3.2*inch, 3.2*inch])
    t_info.setStyle(TableStyle([('FONTSIZE', (0,0), (-1,-1), 9), ('TEXTCOLOR', (0,0), (-1,-1), c_dim)]))
    elements.append(t_info)
    elements.append(HRFlowable(width="100%", thickness=1.5, color=c_primary, spaceBefore=10, spaceAfter=15))
    
    # --- SUMMARY ---
    elements.append(Paragraph("PROFESSIONAL SUMMARY", st_section))
    elements.append(Paragraph(CV_DATA["philosophy"].get(lang, CV_DATA["philosophy"]["en"]), st_body))
    
    # --- EXPERIENCE ---
    elements.append(Paragraph("WORK EXPERIENCE", st_section))
    for exp in CV_DATA["experience"]:
        elements.append(Paragraph(f"<b>{exp['title']}</b>", st_body))
        elements.append(Paragraph(f"<font color='#6b7280'>{exp['duration']}</font>", st_body))
        elements.append(Paragraph(exp['desc'].get(lang, exp['desc']['en']), ParagraphStyle('Desc', parent=st_body, leftIndent=10, spaceBefore=4, spaceAfter=8)))
    
    # --- EDUCATION & CERTIFICATES ---
    elements.append(Paragraph("EDUCATION & CERTIFICATIONS", st_section))
    for edu in CV_DATA["education"]:
        elements.append(Paragraph(f"<b>{edu['institution']}</b> — {edu['major']}", st_body))
        elements.append(Paragraph(f"<font color='#6b7280'>{edu['period']}</font>", st_body))
        elements.append(Paragraph(edu['details'], ParagraphStyle('EduDet', parent=st_body, fontSize=9, leftIndent=10, spaceAfter=6)))

    # Certificates & Sports
    ach = CV_DATA.get("achievements", {})
    elements.append(Spacer(1, 5))
    elements.append(Paragraph(f"<b>Key Achievements:</b> {ach.get('sports')}", st_body))
    elements.append(Paragraph(f"<b>Certificates:</b> {', '.join(ach.get('certs', []))}", st_body))

    # --- SKILLS ---
    elements.append(Paragraph("CORE SKILLS", st_section))
    skills = CV_DATA.get("skills", {})
    skill_text = f"<b>Creative:</b> {', '.join(skills.get('visual', []))}<br/>" \
                 f"<b>Technical:</b> {', '.join(skills.get('tech', []))}<br/>" \
                 f"<b>AI Tools:</b> {', '.join(skills.get('ai', []))}<br/>" \
                 f"<b>SMM:</b> {', '.join(skills.get('smm', []))}"
    elements.append(Paragraph(skill_text, st_body))

    # --- FOOTER ---
    elements.append(Spacer(1, 40))
    elements.append(HRFlowable(width="100%", thickness=0.5, color=c_dim))
    footer_text = f"<center><i>This document was generated automatically for {user_name}. View online at {contacts.get('domain')}</i></center>"
    elements.append(Paragraph(footer_text, ParagraphStyle('Footer', parent=st_body, fontSize=8, textColor=c_dim, spaceBefore=10)))
    
    try:
        doc.build(elements)
        return True
    except Exception as e:
        print(f"PDF Error: {e}")
        return False
