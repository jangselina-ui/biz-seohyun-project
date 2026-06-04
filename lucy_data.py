# -*- coding: utf-8 -*-
import pandas as pd

# 1. 멤버 데이터
MEMBERS = [
    {
        "id": "yechan",
        "name": "신예찬 (Shin Yechan)",
        "birth": "1992년 6월 13일",
        "role": "리더, 바이올린 (Leader, Violin)",
        "namu_url": "https://namu.wiki/w/%EC%8B%A0%EC%98%88%EC%B0%AC(LUCY)",
        "image_path": "assets/yechan.png",
        "color": "#06B6D4",  # Cyan
        "description": "무대 위에서 날아다니는 열정적인 연주와 끊어질 듯한 활이 시그니처인 귀여운 맏내 리더! 클래식 바이올린과 버스킹 경험을 바탕으로 루시의 독창적인 바이올린 리드 사운드를 담당합니다."
    },
    {
        "id": "sangyeop",
        "name": "최상엽 (Choi Sangyeop)",
        "birth": "1994년 2월 27일",
        "role": "보컬, 기타 (Vocal, Guitar)",
        "namu_url": "https://namu.wiki/w/%EC%B5%9C%EC%83%81%EC%97%BD",
        "image_path": "assets/sangyeop.png",
        "color": "#10B981",  # Emerald / Green
        "description": "맑고 맑은 은쟁반에 옥구슬 굴러가는 청량 보이스부터 락킹하고 폭발적인 보컬까지 폭넓게 넘나드는 보컬리스트. 특유의 따뜻하고 힘찬 목소리로 청춘을 노래합니다."
    },
    {
        "id": "wonsang",
        "name": "조원상 (Cho Wonsang)",
        "birth": "1996년 8월 15일",
        "role": "프로듀서, 베이스 (Producer, Bass)",
        "namu_url": "https://namu.wiki/w/%EC%A1%B0%EC%9B%90%EC%83%81",
        "image_path": "assets/wonsang.png",
        "color": "#6366F1",  # Indigo
        "description": "루시의 정체성인 '청량함'과 '하이브리드 팝락' 사운드를 만들어내는 천재 프로듀서이자 베이시스트. 화려한 베이스 슬랩과 더불어 바람 소리, 빗소리 같은 엠비언스(Ambience) 사운드를 적극 활용하는 사운드 디자인의 마술사입니다."
    },
    {
        "id": "gwangil",
        "name": "신광일 (Shin Gwangil)",
        "birth": "1997년 5월 25일",
        "role": "드럼, 보컬 (Drum, Vocal)",
        "namu_url": "https://namu.wiki/w/%EC%8B%A0%EA%B4%91%EC%9D%BC",
        "image_path": "assets/gwangil.png",
        "color": "#F59E0B",  # Amber / Orange
        "description": "흔들림 없는 드러밍을 소화하면서 동시에 감미롭고 부드러운 목소리로 서브 보컬 및 화음을 넣어주는 사운드의 든든한 대들보. 페루 유학파 출신으로 다국어에 능통한 매력 만점 막내입니다."
    }
]

# 2. 앨범 데이터 (나무위키 공식 소개글 반영)
ALBUMS = [
    {
        "id": "dear",
        "title": "DEAR.",
        "type": "데뷔 싱글 1집",
        "date": "2020.05.08",
        "title_song": "개화 (Flowering)",
        "youtube_url": "https://www.youtube.com/watch?v=rR_AVo1RaNw",
        "theme_color": "rgba(6, 182, 212, 0.1)",
        "tracks": ["1. INTRO", "2. 개화 (Flowering) [TITLE]"],
        "info": "머금고 있지만 느끼지 못했던 기억들과, 이미 흘러가 버린 기억들에 대해."
    },
    {
        "id": "panorama",
        "title": "PANORAMA",
        "type": "미니 1집",
        "date": "2020.08.13",
        "title_song": "조깅 (Jogging)",
        "youtube_url": "https://www.youtube.com/watch?v=h6W6c1Y-X2g",
        "theme_color": "rgba(16, 185, 129, 0.1)",
        "tracks": ["1. 조깅 [TITLE]", "2. 수박 (Watermelon)", "3. Straight Line", "4. Missing Call (Feat. 수란)", "5. 충분히 (Enough)", "6. Flare"],
        "info": "시간의 흐름에 따라 혹은 다양한 풍경을 하나의 프레임 안에 담아낸 '파노라마' 사진처럼, LUCY Mini Album 'PANORAMA' 속 6개의 트랙 안에 다양한 여름의 단상들을 담아냈다. 여름날 아침의 싱그럽고 푸른 하늘을 연상케 하는 타이틀곡 '조깅'부터 한여름 밤 페스티벌의 열기를 담은 'Flare'까지, 트랙이 진행됨에 따라 점차 짙어지는 여름의 농도를 느낄 수 있도록 구성되었다."
    },
    {
        "id": "snooze",
        "title": "선잠",
        "type": "싱글 2집",
        "date": "2020.11.12",
        "title_song": "선잠 (Snooze)",
        "youtube_url": "https://www.youtube.com/watch?v=i90vB5g9ZtI",
        "theme_color": "rgba(245, 158, 11, 0.1)",
        "tracks": ["1. 선잠 (Snooze) [TITLE]", "2. 멀리 (Farther and Farther)"],
        "info": "\"머금고 있지만 느끼지 못했던 기억들과, 이미 흘러가 버린 기억들에 대해\" 노래한 앨범이다. 몸만 커버린 어른이 되어버린 우리들이 잊고 살았던 순수한 시절의 기억을 되새기고, 낮보다 밤을 기다리게 된 회색빛의 사람들에게 잃어버린 기억과 평안을 찾길 바라는 마음을 담았다."
    },
    {
        "id": "inside",
        "title": "INSIDE",
        "type": "싱글 3집",
        "date": "2021.02.16",
        "title_song": "히어로 (Hero)",
        "youtube_url": "https://www.youtube.com/watch?v=eD5iJ-7S65E",
        "theme_color": "rgba(99, 102, 241, 0.1)",
        "tracks": ["1. 히어로 [TITLE]", "2. 난로 (Stove)", "3. Outro (뒤돌아보면)"],
        "info": "겉으로 드러나지 않은 따스한 내면의 이야기를 담은 앨범으로, 루시가 지난해 봄부터 달려온 사계절 서사를 완성하는 작품이다. 사랑하는 사람 앞에서만큼은 히어로가 되고 싶은 마음을 담은 타이틀곡 '히어로'를 통해 루시표 사랑의 메시지를 전한다. 내 자신이 보잘것없어 보여도 나를 사랑해 주는 사람을 통해 스스로의 가치를 깨닫고, 힘들 때 곁에 있어 주겠다는 따뜻한 위로를 노래한다."
    },
    {
        "id": "gatcha",
        "title": "Gatcha!",
        "type": "싱글 4집",
        "date": "2021.06.16",
        "title_song": "I Got U (아지랑이)",
        "youtube_url": "https://www.youtube.com/watch?v=Jm5yN5-kG_g",
        "theme_color": "rgba(236, 72, 153, 0.1)",
        "tracks": ["1. I Got U [TITLE]", "2. 어이쿠 (One by One)", "3. Buddy", "4. 봄인지 여름인지 (Wonder)"],
        "info": "\"무엇이 나올지 모르는 뽑기 기계처럼 인생은 늘 미지의 새로운 하루를 내어준다\"는 의미를 담고 있다. 어떤 하루든 'Gatcha!'하고 집어 들어 게임처럼 즐길 수 있기를 바라는 응원의 메시지를 담았다. 뽑기가 내어준 당신의 하루가 So BAD일 때도, So NICE일 때도 늘 곁에서 힘이 되어주고 싶다는 루시의 응원 에너지가 담겨 있다."
    },
    {
        "id": "blue",
        "title": "BLUE",
        "type": "미니 2집",
        "date": "2021.12.07",
        "title_song": "떼굴떼굴",
        "youtube_url": "https://www.youtube.com/watch?v=zS1Q4c1-s5A",
        "theme_color": "rgba(59, 130, 246, 0.1)",
        "tracks": ["1. 떼굴떼굴 [TITLE]", "2. 맞네 (You're Right)", "3. 해가 뜨는 밤 (Eclipse)", "4. 꿈 (Dream)", "5. 놓지 않을게 (Hug)", "6. 결국 아무것도 알 수 없었지만 (Sad Ending)"],
        "info": "LUCY의 2nd EP 《BLUE》는 밴드 LUCY 자체를 테마화하여, 멤버 개개인의 음악적 감성과 풍부한 표현력을 조명하는 동시에, 이들이 하나가 되었을 때 일으키는 조화로운 시너지를 담아낸 앨범이다. \"네 가지 BLUE로 그려낸 단 하나의 'BLUE'\"를 슬로건으로 내세우며 \"서로 다른 채도와 온도의 BLUE를 지녔지만, 함께일 때 우리는 가장 따뜻한 BLUE가 된다\"는 메시지를 전한다."
    },
    {
        "id": "childhood",
        "title": "Childhood",
        "type": "정규 1집",
        "date": "2022.08.17",
        "title_song": "놀이 (PLAY)",
        "youtube_url": "https://www.youtube.com/watch?v=kYJvM99T73k",
        "theme_color": "rgba(139, 92, 246, 0.1)",
        "tracks": ["1. Know Knows", "2. 놀이 [TITLE]", "3. 우동 (U DONG)", "4. 도라희 (DOH)", "5. 채워 (Prequel)", "6. 지레 (Ji-rae)", "7. 이 밤을 잃고 싶지 않아", "8. 무색 (Colorless)", "9. Opening", "10. Ending", "11. We Will Fly Away (Feat. 송은혜)", "12. 나는 너고 너는 나야 (You Are My Light)", "13. 드라이브 (Drive)", "14. 세이브 미 (Save Me)", "15. 아지랑이 (Haze) - CD Only"],
        "info": "LUCY가 데뷔 2년 만에 발매한 첫 번째 정규 앨범이다. 'Childhood'는 자유, 동심, 순수한 마음을 지닌 유년기를 뜻하며, 이를 잃지 않고자 하는 LUCY의 염원이 담긴 모토이자 아이덴티티이다. 장르에 국한되지 않는 다양한 시도를 통해 자유로움과 에너지를 표현했으며, LUCY 특유의 꾸밈없고 현실적이면서도 따뜻한 가사들이 돋보인다."
    },
    {
        "id": "insert_coin",
        "title": "INSERT COIN",
        "type": "미니 3집",
        "date": "2023.02.23",
        "title_song": "아니 근데 진짜",
        "youtube_url": "https://www.youtube.com/watch?v=k4U-3f8_4Gg",
        "theme_color": "rgba(220, 38, 38, 0.1)",
        "tracks": ["1. 바쁘거든 (Intro)", "2. 아니 근데 진짜 (Unbelievable) [TITLE]", "3. 띠띡 (Never in Vain)", "4. 채워 (Forget About It)", "5. 내버려둬 (Leave Me Alone)"],
        "info": "게임에서 목숨을 다했을 때 다시 시작할 기회를 얻는 'INSERT COIN'을 테마로 한 앨범으로, LUCY의 음악이 누군가에게 새로운 불씨가 되기를 바라는 희망적인 메시지를 담았다. LUCY 특유의 청량하고 따뜻한 곡들과 그동안 보여준 적 없는 강렬한 사운드의 곡들이 공존하며, 마치 동전의 양면처럼 반전 넘치는 구성을 보여준다. 멤버 조원상이 전곡 작사, 작곡, 프로듀싱에 참여했다."
    },
    {
        "id": "yeol",
        "title": "열 (10)",
        "type": "미니 4집",
        "date": "2023.08.17",
        "title_song": "아지랑이 (Haze)",
        "youtube_url": "https://www.youtube.com/watch?v=uSW1iY2iacc",
        "theme_color": "rgba(79, 70, 229, 0.1)",
        "tracks": ["1. 뜨거 (Hot!)", "2. 아지랑이 (Haze) [TITLE]", "3. Magic", "4. 내 가슴속에 들어온 낙엽은"],
        "info": "누구나 겪게 되는 '열병'의 시기를 관통하며 한층 더 성숙해진 청춘의 모습을 담은 앨범이다. 열병을 이겨내고 있는 이들에게는 견뎌낼 힘을, 이미 겪은 이들에게는 위로와 다음 열병을 이겨낼 용기를 전하고자 하는 마음을 담았다. 타이틀곡 '아지랑이'를 비롯해 여름의 열기를 표현한 EDM, 강렬한 록 사운드 등 다양한 장르의 곡들이 수록되어 있으며, 멤버 전원이 작업에 참여해 완성도를 높였다."
    },
    {
        "id": "boogie_man",
        "title": "Boogie Man",
        "type": "싱글 6집",
        "date": "2023.12.05",
        "title_song": "Boogie Man",
        "youtube_url": "https://youtu.be/MjMVg4sBEr8?si=flfyV1oCD03H1jww",
        "theme_color": "rgba(139, 92, 246, 0.1)",
        "tracks": ["1. Boogie Man [TITLE]", "2. Over The Christmas"],
        "info": "LUCY의 염원이 담긴 모토이자 아이덴티티이다. 장르에 국한되지 않는 다양한 시도를 통해 자유로움과 에너지를 표현했으며, LUCY 특유의 꾸밈없고 현실적이면서도 따뜻한 가사들이 돋보인다."
    }
]

# 3. 성장 데이터
CONCERT_GROWTH = pd.DataFrame([
    {"시기": "2021년 6월", "공연명": "LUCY ISLAND (첫 단독)", "관객수": 1700},
    {"시기": "2022년 3월", "공연명": "Childhood (첫 정규)", "관객수": 3000},
    {"시기": "2023년 8월", "공연명": "열, 장충체육관 (다섯 번째)", "관객수": 7600},
    {"시기": "2026년 5월", "공연명": "Childish, 체조경기장 (KSPO DOME)", "관객수": 15000}
])

ALBUM_SALES_GROWTH = pd.DataFrame([
    {"시기": "2020년 8월", "앨범명": "PANORAMA (미니 1집)", "판매량": 850},
    {"시기": "2022년 8월", "앨범명": "Childhood (정규 1집)", "판매량": 24000},
    {"시기": "2023년 8월", "앨범명": "열 (미니 4집)", "판매량": 64000},
    {"시기": "2026년 4월", "앨범명": "Childish (정규 2집)", "판매량": 103562}
])

# 4. 감정/상황별 노래 추천 데이터
MOOD_RECOMMENDATIONS = [
    {
        "id": "running",
        "option_text": "🏃 찌푸린 하늘을 벗어나 벅차오르게 달리고 싶을 때!",
        "song": "조깅 (Jogging)",
        "album": "PANORAMA (미니 1집)",
        "lyric": "“머리 위로 쏟아지는 뜨거운 해를 피해 힘껏 뛰어봐”",
        "description": "속도감 있는 빠른 드럼 비트와 청량하게 터지는 신예찬의 바이올린 솔로가 당신의 심장박동을 높여줄 것입니다. 러닝이나 맑은 날 드라이브에 완벽히 어울립니다.",
        "youtube_url": "https://www.youtube.com/watch?v=h6W6c1Y-X2g"
    },
    {
        "id": "comfort",
        "option_text": "☕ 지친 하루의 끝, 따뜻하고 포근한 위로가 필요할 때",
        "song": "선잠 (Snooze)",
        "album": "선잠 (싱글 2집)",
        "lyric": "“너의 마음에 작은 온기를 불어넣을 선잠을 빌려줄게”",
        "description": "바쁜 일상 속에 지친 마음에 달콤한 쪽잠 같은 위로를 안겨주는 곡입니다. 아기자기한 시계 태엽 소리와 조원상의 부드러운 베이스, 멤버들의 따뜻한 음색이 포근하게 감싸줍니다.",
        "youtube_url": "https://www.youtube.com/watch?v=i90vB5g9ZtI"
    },
    {
        "id": "energy",
        "option_text": "🔥 무기력함에서 탈출하여 자신감을 얻고 싶을 때",
        "song": "히어로 (Hero)",
        "album": "INSIDE (싱글 3집)",
        "lyric": "“지구는 내가 지킬게, 네 걱정은 하지 마!”",
        "description": "한 편의 열혈 애니메이션 주제가를 듣는 듯한 밝은 멜로디와 희망찬 가사가 특징입니다. 최상엽의 시원한 보컬과 역동적인 드럼비트가 에너지를 충전해 줍니다.",
        "youtube_url": "https://www.youtube.com/watch?v=eD5iJ-7S65E"
    },
    {
        "id": "healing",
        "option_text": "🌸 봄날의 꽃밭 속을 걷는 듯한 화사한 설렘을 느끼고 싶을 때",
        "song": "개화 (Flowering)",
        "album": "DEAR. (데뷔 싱글)",
        "lyric": "“내게 찾아온 봄처럼 너의 마음에 꽃을 피워줄게”",
        "description": "루시의 탄생이자 정체성이 담긴 명곡. 겨울을 이겨낸 꽃망울처럼 화사하고 아름다운 바이올린 선율이 흘러나오며, 새로운 시작을 앞둔 분들에게 강력한 희망을 전합니다.",
        "youtube_url": "https://www.youtube.com/watch?v=rR_AVo1RaNw"
    },
    {
        "id": "sweet",
        "option_text": "🧸 짝사랑의 몽글몽글하고 귀여운 설렘을 느끼고 싶을 때",
        "song": "아니 근데 진짜 (Unbelievable)",
        "album": "INSERT COIN (미니 3집)",
        "lyric": "“아니 근데 진짜 너 엄청 예쁘다니까!”",
        "description": "귀여운 게임 8비트 사운드와 대화체를 차용한 사랑스러운 가사가 매력적입니다. 듣는 내내 미소를 짓게 만드는 연인 혹은 썸타는 연인들의 대표 추천곡입니다.",
        "youtube_url": "https://www.youtube.com/watch?v=k4U-3f8_4Gg"
    },
    {
        "id": "sentimental",
        "option_text": "🍂 울적하거나 아련하게 마음 깊은 곳을 터치하고 싶을 때",
        "song": "아지랑이 (Haze)",
        "album": "열 (미니 4집)",
        "lyric": "“아직 서툰 청춘이라 그래, 우리 흔들려도 괜찮아”",
        "description": "성장의 통통을 겪는 모든 서툰 청춘들에게 건네는 루시의 담담하지만 묵직한 고백입니다. 신예찬의 애절하고 묵직한 바이올린 현소리가 가슴을 뭉클하게 만듭니다.",
        "youtube_url": "https://www.youtube.com/watch?v=uSW1iY2iacc"
    }
]
