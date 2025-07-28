# 03-cli.py

# from dotenv import load_dotenv
from ai import get_personality_analysis_stream

print('# 안녕하세요 AI 관상가입니다. 얼굴 특징을 입력해주시면 성격과 미래를 알려드릴게요.')
line = input("얼굴 특징: ").strip()

if not line:
    print('오류! 얼굴 특징을 입력하지 않으셨습니다.')
else:
    print('입력하신 얼굴 특징 : ', line)
    print('분석 중 ...')
    print('분석 결과:') # 결과가 바로 나오기 시작할 것이므로 메시지 변경
    for chunk in get_personality_analysis_stream(line):
        print(chunk, end='', flush=True) # 청크를 바로 출력하고, 버퍼를 비워줌
    print('분석 완료')