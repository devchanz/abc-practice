# ai.py

from openai import OpenAI

def get_personality_analysis_stream(face_desc: str): #-> str: 
    """
    인자로 얼굴 설명을 받아, OpenAI LLM API를 활용하여 성격과 미래를 스트리밍 방식으로 분석합니다.
    각 청크를 즉시 반환하여 실시간 응답을 가능하게 합니다.
    """
    # doc String
   
   # 인자로 얼굴 설명을 받아, OpenAI LLM API를 활용하여 성격과 미래를 분석합니다.

    # 원하는 어떠한 형태로든 지시문 문자열을 생성하실 수 있습니다.
    prompt = "당신은 전문 관상가입니다. "
    prompt += "사람들의 얼굴 특징을 보고 성격과 미래를 친근하게 분석해주세요."
    prompt += "\n 얼굴 특징 : " + face_desc

    client = OpenAI()  # OPENAI_API_KEY 환경변수 지정이 필요

    # 스트리밍 모드 활성화: stream=True
    # Chat Completions API 사용으로 변경
    stream = client.chat.completions.create(
        model="gpt-4o",  # 사용할 두뇌 지정
        messages=[{'role':'user', 'content':prompt}], # 메시지 형식 변경
        stream=True,
    )
    # 응답을 스트리밍으로 받아서 처리
    for chunk in stream:
        # 각 청크에서 실제 텍스트 내용을 추출
        # delta.content에 텍스트가 있을 경우에만 반환
        if chunk.choices[0].delta.content is not None:
            yield chunk.choices[0].delta.content # 청크를 즉시 반환 (yield 사용)