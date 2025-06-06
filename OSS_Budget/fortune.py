#test commit
import random

def get_fortune(name):
    """
    사용자 이름을 입력받아 오늘의 운세를 무작위로 생성해주는 함수.
    """
    if not isinstance(name, str) or not name.strip():
        return "이름을 정확히 입력하세요."

    fortunes = [
        "오늘은 기분 좋은 일이 생길 거예요!",
        "생각지 못한 돈이 들어올 수 있어요!",
        "친구와의 갈등을 조심하세요.",
        "무리한 투자는 피하는 것이 좋아요.",
        "오늘은 자신을 믿고 행동해보세요.",
        "기회는 생각보다 가까이 있어요!",
        "뜻밖의 연락이 찾아올 수 있어요.",
        "오늘은 조용히 쉬는 것이 좋겠어요.",
    ]

    fortune = random.choice(fortunes)
    return f"{name}님의 오늘의 운세 🌟: {fortune}"