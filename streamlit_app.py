import streamlit as st
import io
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

st.set_page_config(page_title="개념기반 탐구 수업 설계", layout="wide")
st.title("📘 개념기반 탐구 수업 설계 Web App")

st.markdown("""
### 🧭 1단계: 바람직한 학습 결과
교육과정을 분석하고, 개념적으로 재구성하여 단원의 핵심을 도출합니다.
""")

with st.expander("📝 교육과정 입력 및 개념 재구성"):
    core_idea = st.text_area("핵심 아이디어", help="교육과정에서 추출한 핵심 개념 또는 메시지를 입력하세요.")
    standard = st.text_area("성취 기준", help="교육과정 성취 기준을 입력하세요.")
    knowledge = st.text_area("내용 요소 - 지식·이해", help="개념 이해에 필요한 지식 요소를 정리하세요.")
    skills = st.text_area("내용 요소 - 과정·기능", help="탐구 및 실천과 관련된 기능 요소를 정리하세요.")
    values = st.text_area("내용 요소 - 가치·태도", help="학습자가 갖추어야 할 태도 및 가치 요소를 정리하세요.")

    concept_lens = st.multiselect(
        "개념 렌즈 선택",
        options=["미학", "변화", "의사소통", "공동체", "연결", "창의성", "문화", "개발",
                 "형식", "세계적 상호작용", "정체성", "논리", "관점", "관계", "시스템", "시간", "장소 및 공간"]
    )

    driving_concept = st.text_input("단원의 주도개념", help="이 단원에서 중심이 되는 개념을 입력하세요.")

st.markdown("""
---
### 🧪 2단계: 총괄평가 설계
""")

with st.expander("📊 평가 요소 설계"):
    eval_goal = st.text_area("학습 목표 평가 관점에서의 재진술", help="학습자가 무엇을 보여주어야 하는지 명확히 합니다.")
    eval_type = st.selectbox("평가 유형 선택", ["GRASPS 과제", "서술형 문항", "객관식 평가", "프로젝트 기반 평가"])
    eval_task = st.text_area("평가 과제 설명", help="학생이 수행할 과제 또는 문항을 구체적으로 서술하세요.")

st.markdown("""
---
### 🧑‍🏫 3단계: 교수-학습 계획
""")

with st.expander("📚 수업 흐름 구성"):
    intro = st.text_area("도입 활동", help="학생의 흥미를 유발하고 배경지식을 활성화할 수 있는 활동")
    inquiry = st.text_area("탐구 활동", help="학생이 주도적으로 참여하는 개념 탐구 또는 실험")
    reflection = st.text_area("정리 및 반성 활동", help="학습 내용을 정리하고 자기 성찰을 유도하는 활동")
    support = st.text_area("학습 지원 전략", help="개별화, 피드백, 협력학습 등의 지원 방안")

st.success("설계가 완료되었습니다. 필요시 저장 기능을 추가하세요.")

# PDF 생성 함수
def create_pdf():
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    
    # 한글 스타일 설정
    korean_style = ParagraphStyle(
        'Korean',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
    )
    
    title_style = ParagraphStyle(
        'KoreanTitle',
        parent=styles['Title'],
        fontName='Helvetica',
        fontSize=16,
        leading=20,
    )
    
    story = []
    
    # 제목
    story.append(Paragraph("개념기반 탐구 수업 설계", title_style))
    story.append(Spacer(1, 20))
    
    # 1단계
    story.append(Paragraph("1단계: 바람직한 학습 결과", korean_style))
    story.append(Spacer(1, 10))
    story.append(Paragraph(f"핵심 아이디어: {core_idea}", korean_style))
    story.append(Paragraph(f"성취 기준: {standard}", korean_style))
    story.append(Paragraph(f"지식·이해: {knowledge}", korean_style))
    story.append(Paragraph(f"과정·기능: {skills}", korean_style))
    story.append(Paragraph(f"가치·태도: {values}", korean_style))
    story.append(Paragraph(f"개념 렌즈: {', '.join(concept_lens)}", korean_style))
    story.append(Paragraph(f"주도 개념: {driving_concept}", korean_style))
    story.append(Spacer(1, 20))
    
    # 2단계
    story.append(Paragraph("2단계: 총괄평가", korean_style))
    story.append(Spacer(1, 10))
    story.append(Paragraph(f"학습 목표 재진술: {eval_goal}", korean_style))
    story.append(Paragraph(f"평가 유형: {eval_type}", korean_style))
    story.append(Paragraph(f"과제 설명: {eval_task}", korean_style))
    story.append(Spacer(1, 20))
    
    # 3단계
    story.append(Paragraph("3단계: 교수학습계획", korean_style))
    story.append(Spacer(1, 10))
    story.append(Paragraph(f"도입 활동: {intro}", korean_style))
    story.append(Paragraph(f"탐구 활동: {inquiry}", korean_style))
    story.append(Paragraph(f"정리 및 반성 활동: {reflection}", korean_style))
    story.append(Paragraph(f"학습 지원 전략: {support}", korean_style))
    
    doc.build(story)
    buffer.seek(0)
    return buffer

# PDF 다운로드 버튼
if st.button("📄 PDF로 내보내기"):
    try:
        pdf_buffer = create_pdf()
        st.download_button(
            label="📥 PDF 다운로드",
            data=pdf_buffer,
            file_name="lesson_plan.pdf",
            mime="application/pdf"
        )
        st.success("PDF가 생성되었습니다!")
    except Exception as e:
        st.error(f"PDF 생성 중 오류가 발생했습니다: {str(e)}")
        st.info("대신 텍스트 파일로 다운로드할 수 있습니다.")
        
        # 텍스트 파일 대안
        text_content = f"""📘 개념기반 탐구 수업 설계

[1단계: 바람직한 학습 결과]
핵심 아이디어: {core_idea}
성취 기준: {standard}
지식·이해: {knowledge}
과정·기능: {skills}
가치·태도: {values}
개념 렌즈: {', '.join(concept_lens)}
주도 개념: {driving_concept}

[2단계: 총괄평가]
학습 목표 재진술: {eval_goal}
평가 유형: {eval_type}
과제 설명: {eval_task}

[3단계: 교수학습계획]
도입 활동: {intro}
탐구 활동: {inquiry}
정리 및 반성 활동: {reflection}
학습 지원 전략: {support}
"""
        
        st.download_button(
            label="📄 텍스트 파일 다운로드",
            data=text_content,
            file_name="lesson_plan.txt",
            mime="text/plain"
        )