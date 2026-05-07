from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.units import inch
from content import CV_DATA
import os

def generate_cv_pdf(lang: str, output_path: str, user_name: str = "Client"):
    """Generates an Executive Business Profile PDF."""
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
    c_primary = colors.HexColor("#0f172a") # Dark Slate
    c_accent = colors.HexColor("#6366f1")  # Indigo
    c_text = colors.HexColor("#334155")    # Slate 700
    c_dim = colors.HexColor("#64748b")     # Slate 500
    
    # --- PROFESSIONAL STYLES ---
    st_header = ParagraphStyle('Header', fontSize=32, textColor=c_primary, fontName='Helvetica-Bold', spaceAfter=2)
    st_title = ParagraphStyle('Title', fontSize=14, textColor=c_accent, fontName='Helvetica-Bold', spaceAfter=14, letterSpacing=2)
    st_section = ParagraphStyle('Section', fontSize=15, textColor=c_primary, fontName='Helvetica-Bold', spaceBefore=25, spaceAfter=12)
    st_body = ParagraphStyle('Body', fontSize=11, leading=16, textColor=c_text, fontName='Helvetica')
    st_philosophy = ParagraphStyle('Phil', parent=st_body, italic=True, textColor=c_accent, leftIndent=20, borderPadding=10)
    st_review = ParagraphStyle('Review', fontSize=10, leading=14, textColor=c_dim, italic=True, spaceBefore=10)
    st_client = ParagraphStyle('Client', fontSize=9, fontName='Helvetica-Bold', textColor=c_primary, leftIndent=10)
    
    elements = []
    
    # --- HEADER ---
    elements.append(Paragraph(CV_DATA["name"].upper(), st_header))
    elements.append(Paragraph(CV_DATA["title"].upper(), st_title))
    
    # Quick Info
    contacts = CV_DATA.get("contacts", {})
    info = [[
        f"📍 Tashkent, UZ",
        f"📱 {contacts.get('telegram', '@abdulloh_ai')}",
        f"🌐 @upgcard"
    ]]
    t_info = Table(info, colWidths=[2.2*inch, 2.2*inch, 2.2*inch])
    t_info.setStyle(TableStyle([('FONTSIZE', (0,0), (-1,-1), 10), ('TEXTCOLOR', (0,0), (-1,-1), c_dim)]))
    elements.append(t_info)
    elements.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#e2e8f0"), spaceBefore=15, spaceAfter=20))
    
    # --- STRATEGIC PHILOSOPHY ---
    elements.append(Paragraph("EXECUTIVE SUMMARY", st_section))
    elements.append(Paragraph(CV_DATA["philosophy"].get(lang, CV_DATA["philosophy"]["en"]), st_philosophy))
    elements.append(Spacer(1, 15))
    
    # --- EXPERTISE ---
    elements.append(Paragraph("CORE EXPERTISE", st_section))
    for exp in CV_DATA["experience"]:
        elements.append(Paragraph(f"<b>{exp['title']}</b>", st_body))
        elements.append(Paragraph(exp['desc'].get(lang, exp['desc']['en']), ParagraphStyle('Desc', parent=st_body, fontSize=10, spaceAfter=8, textColor=c_text)))
    
    # --- TESTIMONIALS ---
    elements.append(Paragraph("CLIENT TESTIMONIALS", st_section))
    for rev in CV_DATA["reviews"]:
        elements.append(Paragraph(f"\"{rev['text'].get(lang, rev['text']['en'])}\"", st_review))
        elements.append(Paragraph(f"— {rev['client']}", st_client))
        elements.append(Spacer(1, 5))
        
    # --- STRATEGIC VALUES ---
    elements.append(Paragraph("STRATEGIC VALUES", st_section))
    values = f"◈ <b>Precision:</b> AI-driven efficiency for 0% error margin.<br/>" \
             f"◈ <b>Emotion:</b> Cinematic storytelling for 40%+ conversion rates.<br/>" \
             f"◈ <b>Discipline:</b> Fast execution with Taekwondo-forged focus."
    elements.append(Paragraph(values, st_body))

    # --- CALL TO ACTION ---
    elements.append(Spacer(1, 50))
    # Removed unsupported 'align' argument from HRFlowable
    elements.append(HRFlowable(width="40%", thickness=2, color=c_accent, hAlign='LEFT'))
    cta_text = f"<i>Prepared exclusively for {user_name}.</i><br/>" \
               f"<b>Scan or visit to discuss your project: t.me/AbdullohCvbot</b>"
    elements.append(Paragraph(cta_text, ParagraphStyle('CTA', parent=st_body, textColor=c_accent, spaceBefore=10)))
    
    try:
        doc.build(elements)
        return True
    except Exception as e:
        print(f"PDF Error: {e}")
        return False
