import streamlit as st

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

from fpdf import FPDF

if st.button("📄 PDF로 내보내기"):
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font('NanumGothic', '', 'fonts/NanumGothic.ttf', uni=True)
    pdf.set_font('NanumGothic', size=12)


    # 내용 구성
    pdf.multi_cell(0, 10, f"📘 개념기반 탐구 수업 설계\n", align='L')
    pdf.multi_cell(0, 10, f"[1단계: 바람직한 학습 결과]\n핵심 아이디어: {core_idea}\n성취 기준: {standard}\n\n"
                          f"내용 요소 - 지식: {knowledge}\n과정·기능: {skills}\n가치·태도: {values}\n"
                          f"개념 렌즈: {', '.join(concept_lens)}\n주도 개념: {driving_concept}\n\n", align='L')

    pdf.multi_cell(0, 10, f"[2단계: 총괄평가]\n학습 목표 재진술: {eval_goal}\n평가 유형: {eval_type}\n과제 설명: {eval_task}\n\n", align='L')

    pdf.multi_cell(0, 10, f"[3단계: 교수학습계획]\n도입 활동: {intro}\n탐구 활동: {inquiry}\n"
                          f"정리 및 반성 활동: {reflection}\n학습 지원 전략: {support}", align='L')

    # PDF 저장
    pdf.output("/tmp/lesson_plan.pdf")

    with open("/tmp/lesson_plan.pdf", "rb") as f:
        st.download_button("📥 PDF 다운로드", f, file_name="lesson_plan.pdf", mime="application/pdf")
