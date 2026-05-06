from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.units import inch
from content import CV_DATA
import os

def generate_cv_pdf(lang: str, output_path: str, user_name: str = "Foydalanuvchi"):
    """Generates an Elite Level professional PDF CV with Case Studies."""
    doc = SimpleDocTemplate(
        output_path, 
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )
    styles = getSampleStyleSheet()
    
    # Professional Palette
    primary_color = colors.HexColor("#0f172a") # Darker Slate
    accent_color = colors.HexColor("#2563eb") # Clear Blue
    text_color = colors.HexColor("#334155")
    
    # Custom Styles
    name_style = ParagraphStyle('Name', fontSize=26, textColor=primary_color, fontName='Helvetica-Bold', spaceAfter=2)
    sub_style = ParagraphStyle('Sub', fontSize=12, textColor=accent_color, fontName='Helvetica-Bold', spaceAfter=12)
    sec_style = ParagraphStyle('Sec', fontSize=14, textColor=primary_color, fontName='Helvetica-Bold', spaceBefore=18, spaceAfter=10, borderPadding=(0,0,2,0), borderColor=accent_color, borderWidth=1)
    body_style = ParagraphStyle('Body', fontSize=10, leading=14, textColor=text_color)
    case_style = ParagraphStyle('Case', fontSize=9, leading=12, textColor=text_color, leftIndent=15)
    
    elements = []
    
    # --- HEADER ---
    elements.append(Paragraph(CV_DATA["name"].upper(), name_style))
    elements.append(Paragraph("CREATIVE DIRECTOR | DEVELOPER | AI ENGINEER", sub_style))
    
    contact = f"📍 {CV_DATA['location']}  |  💬 {CV_DATA['contacts']['telegram']}  |  📷 @{CV_DATA['contacts']['instagram']}"
    elements.append(Paragraph(contact, body_style))
    elements.append(Spacer(1, 15))
    
    # --- SUMMARY ---
    elements.append(Paragraph("PROFESSIONAL PROFILE", sec_style))
    summary = {
        "uz": "Innovatsion yechimlar yaratuvchi va vizual san'at orqali bizneslarga qiymat qo'shuvchi mutaxassis.",
        "ru": "Специалист, создающий инновационные решения и приносящий пользу бизнесу через визуальное искусство.",
        "en": "Specialist creating innovative solutions and adding value to businesses through visual arts."
    }
    elements.append(Paragraph(summary[lang], body_style))
    
    # --- CASE STUDIES (The "Perfection" part) ---
    elements.append(Paragraph("SELECTED CASE STUDIES", sec_style))
    for proj in CV_DATA["projects"]:
        elements.append(Paragraph(f"<b>{proj['name']}</b> ({proj['type']})", body_style))
        elements.append(Paragraph(proj[lang], case_style))
        elements.append(Spacer(1, 8))
        
    # --- EXPERIENCE ---
    elements.append(Paragraph("EXPERIENCE", sec_style))
    for exp in CV_DATA["experience"]:
        elements.append(Paragraph(f"<b>{exp['title']}</b> — {exp['duration']}", body_style))
    
    # --- SKILLS & EDUCATION ---
    elements.append(Paragraph("CORE SKILLS", sec_style))
    elements.append(Paragraph(", ".join(CV_DATA["skills"]["technical"]), body_style))
    
    elements.append(Paragraph("EDUCATION", sec_style))
    edu = f"{CV_DATA['education']['university']} - {CV_DATA['education']['major']}"
    elements.append(Paragraph(edu, body_style))
    
    # --- CALL TO ACTION ---
    elements.append(Spacer(1, 30))
    cta_style = ParagraphStyle('CTA', parent=body_style, alignment=1, textColor=accent_color, fontName='Helvetica-Bold')
    elements.append(Paragraph("🔗 VISIT MY DIGITAL ECOSYSTEM", cta_style))
    elements.append(Paragraph("https://t.me/AbdullohCvbot", ParagraphStyle('Link', parent=body_style, alignment=1, fontSize=8)))
    
    # --- FOOTER ---
    elements.append(Spacer(1, 20))
    footer = f"<i>Eksklyuziv ravishda {user_name} uchun tayyorlandi | © 2024 Abdulloh Portfolio</i>"
    elements.append(Paragraph(footer, ParagraphStyle('Footer', parent=body_style, alignment=1, fontSize=8, textColor=colors.grey)))
    
    try:
        doc.build(elements)
        return True
    except Exception:
        return False
