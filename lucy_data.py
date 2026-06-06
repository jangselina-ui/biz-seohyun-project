# -*- coding: utf-8 -*-
import pandas as pd

# 1. 멤버 데이터
MEMBERS = [
    {
        "id": "yechan",
        "name": "신예찬 (Shin Yechan)",
        "birth": "1992년 6월 13일",
        "role": "리더, 바이올린 (Leader, Violin)",
        "namu_url": "https://namu.wiki/w/%EC%8B%A0%EC%98%88%EC%B0%AC",
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
        "youtube_url": "https://youtu.be/2-P-NIiLiQc?si=OLFcmvN4U9Yi4JBJ",
        "theme_color": "rgba(6, 182, 212, 0.1)",
        "tracks": ["1. INTRO", "2. 개화 (Flowering) [TITLE]"],
        "info": "누군가에게 건네는 편지의 첫 말머리인 ‘DEAR.'는 리스너에게 건네는 첫인사이자, LUCY만의 음악세계로 초대하는 편지의 의미를 담고 있다. 스트링이 돋보이는 유니크한 스타일의 밴드팝 음악을 통해 그들의 메시지를 전한다."
    },
    {
        "id": "panorama",
        "title": "PANORAMA",
        "type": "미니 1집",
        "date": "2020.08.13",
        "title_song": "조깅 (Jogging)",
        "youtube_url": "https://youtu.be/dh684FWByO4?si=0d38Fut-jpSVg-4T",
        "theme_color": "rgba(16, 185, 129, 0.1)",
        "tracks": ["1. 조깅 [TITLE]", "2. 수박깨러가", "3. Straight Line", "4. Missing Call (Feat. 수란)", "5. 충분히", "6. Flare"],
        "info": "시간의 흐름에 따라 혹은 다양한 풍경을 하나의 프레임 안에 담아낸 '파노라마' 사진처럼, LUCY Mini Album 'PANORAMA' 속 6개의 트랙 안에 다양한 여름의 단상들을 담아냈다. \n\n 여름날 아침의 싱그럽고 푸른 하늘을 연상케 하는 타이틀곡 '조깅'부터 한여름 밤 페스티벌의 열기를 담은 'Flare'까지 시간의 흐름을 읽을 수 있는 배열을 통해 점점 더 짙어지는 여름의 농도를 느낄 수 있도록 펼쳐 냈다."
    },
    {
        "id": "snooze",
        "title": "선잠",
        "type": "싱글 2집",
        "date": "2020.11.12",
        "title_song": "선잠 (Snooze)",
        "youtube_url": "https://youtu.be/MR9tD-dkqXI?si=21wTNwQ4BajDZHtp",
        "theme_color": "rgba(245, 158, 11, 0.1)",
        "tracks": ["1. 선잠 (Snooze) [TITLE]", "2. Farther and Farther"],
        "info": "머금고 있지만 느끼지 못했던 기억들과, 이미 흘러가 버린 기억들에 대해"
    },
    {
        "id": "inside",
        "title": "INSIDE",
        "type": "싱글 3집",
        "date": "2021.02.16",
        "title_song": "히어로 (Hero)",
        "youtube_url": "https://youtu.be/V-eHkQ_YABo?si=fFl1whzr9mx8VUY5",
        "theme_color": "rgba(99, 102, 241, 0.1)",
        "tracks": ["1. 히어로 [TITLE]", "2. 난로", "3. Outro (뒤돌아보면)"],
        "info": "겉으로 드러나지 않은 따스한 내면의 이야기를 담은 앨범, 루시가 지난해 봄부터 달려온 사계절 서사를 완성하는 작품이다. 사랑하는 사람 앞에서만큼은 히어로가 되고 싶은 마음을 담은 타이틀곡 '히어로'를 통해 루시표 사랑의 메시지를 전한다. 내 자신이 보잘것없어 보여도 나를 사랑해 주는 사람을 통해 스스로의 가치를 깨닫고, 힘들 때 곁에 있어 주겠다는 따뜻한 위로를 노래한다."
    },
    {
        "id": "gatcha",
        "title": "Gatcha!",
        "type": "싱글 4집",
        "date": "2021.06.16",
        "title_song": "I Got U",
        "youtube_url": "https://youtu.be/p_DczUl8x60?si=J6EYhPU6H1FfxnwG",
        "theme_color": "rgba(236, 72, 153, 0.1)",
        "tracks": ["1. I Got U [TITLE]", "2. One by One", "3. Buddy", "4. 봄인지 여름인지"],
        "info": "무엇이 나올지 모르는 뽑기 기계처럼 인생은 늘 미지의 새로운 하루를 내어준다. 어떤 하루든 Gatcha! 하고 집어 들고는 게임처럼 하루를 즐길 수 있는 사람이 될 수 있을까?\n\n뽑기가 내어준 당신의 하루가 So BAD 일 때도 So NICE 일 때도 LUCY는 늘 당신의 곁에서 하루를 채워주는 응원의 에너지를 건네고 싶은 마음을 담았다."
    },
    {
        "id": "dong",
        "title": "동문서답",
        "type": "디지털 싱글",
        "date": "2021.08.20",
        "title_song": "동문서답",
        "youtube_url": "https://youtu.be/rYwRr0mV5UY?si=51PjB88AqoTBi0lG",
        "theme_color": "rgba(236, 72, 153, 0.1)",
        "tracks": ["1. 동문서답 [TITLE]", "2. 동문서답 (Inst.)"],
        "info": "<동문서답>은 사랑하는 사람의 대답이 듣고 싶어 전전긍긍하는 어리고 조급한 마음이 잘 드러나는 곡으로, 밴드 LUCY 특유의 청량함이 잘 담겨있다."
    },
    {
        "id": "blue",
        "title": "BLUE",
        "type": "미니 2집",
        "date": "2021.12.07",
        "title_song": "떼굴떼굴",
        "youtube_url": "https://youtu.be/zak9lL2EHho?si=s_vnnOCcaY4sEH8E",
        "theme_color": "rgba(59, 130, 246, 0.1)",
        "tracks": ["1. 떼굴떼굴 [TITLE]", "2. 맞네", "3. 해가 뜨는 밤", "4. 꿈", "5. 놓지 않을게", "6. 결국 아무것도 알 수 없었지만"],
        "info": "LUCY의 2nd EP 《BLUE》는 밴드 LUCY 자체를 테마화하여, 멤버 개개인의 음악적 감성과 풍부한 표현력을 조명하는 동시에, 이들이 하나가 되었을 때 일으키는 조화로운 시너지를 담아냈다. \n\n \"서로 다른 채도와 온도의 BLUE를 지녔지만, 함께일 때 우리는 가장 따뜻한 BLUE가 된다\""
    },
    {
        "id": "childhood",
        "title": "Childhood",
        "type": "정규 1집",
        "date": "2022.08.17",
        "title_song": "놀이 (PLAY)",
        "youtube_url": "https://youtu.be/wFJxzoljf10?si=WQ5TQ41VZgwLlUqA",
        "theme_color": "rgba(139, 92, 246, 0.1)",
        "tracks": ["1. Knowhow", "2. MP3", "3. 놀이 [TITLE]", "4. 10sec", "5. 넌 혹시, 난 괜히", "6. Domino (Feat.디핵)", "7. 파울", "8. 내 쓸쓸함은 차갑지 않아요", "9. 이미 다 알고 있었지만", "10. 이 밤을 잊지 말아요", "11. 무색", "12. Opening", "13. Ending", "14. We Will Fly Away (Feat. 송은혜)", "15. 나는 너야"],
        "info": "자유이자 동심 그리고 순수한 마음을 지닌 유년기를 뜻하는 'Childhood'는 이 모든 것을 잃지 않고자 하는 LUCY의 염원이 담긴 그들의 모토이자 아이덴티티이며, 초심 같은 단어이다. \n\n이번 앨범에서 그들은 장르에 국한되거나 규정되지 않은 다양한 시도를 통하여 자유로움과 에너지를 표현하며, 그들만의 꾸밈없고 현실적이고도 따뜻한 가사들이 이를 뒷받침 한다."
    },
    {
        "id": "insert_coin",
        "title": "INSERT COIN",
        "type": "미니 3집",
        "date": "2023.02.23",
        "title_song": "아니 근데 진짜",
        "youtube_url": "https://youtu.be/KcLQhPR-a2w?si=lXmuz_Mit8pabsh3",
        "theme_color": "rgba(220, 38, 38, 0.1)",
        "tracks": ["1. 아니 근데 진짜 (Unbelievable) [TITLE]", "2. 바쁘거든", "3. Never in Vain", "4. 채워"],
        "info": "게임 오버의 상황에서 <INSERT COIN>을 통해 새로운 목숨을 부여하고, 새로운 도전을 나아가는 것처럼, 그들의 음악이 누군가에게 새로운 불씨가 되길 바라고 있다."
    },
    {
        "id": "yeol",
        "title": "열",
        "type": "미니 4집",
        "date": "2023.08.17",
        "title_song": "아지랑이",
        "youtube_url": "https://youtu.be/uSW1iY2iacc?si=PQPmjY5O46_wWq_I",
        "theme_color": "rgba(79, 70, 229, 0.1)",
        "tracks": ["1. 뜨거", "2. 아지랑이 [TITLE]", "3. Magic", "4. 내버려"],
        "info": "누구에게나 열병의 시기들은 어김없이 찾아오고, 때로는 버거움에 무너지기도 한다.\n버텨낸 열병이 휩쓸고 간 자리에는 상처와 함께 조금 더 성숙해진 자신이 남는다.\n이 앨범에 담긴 음악을 통해 열병을 이겨내고 있는 이들에게는 견뎌낼 수 있는 힘을,\n열병을 겪은 이에게는 위로와 불시에 찾아올지 모를 다음 열병을 이겨낼 수 있는 용기를 얻기를 바라는 마음을 담았다."
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
        "info": "어두운 밤 나타나 누군가의 발목을 움켜쥐고는 옷장 속으로 끌고 가는 Boogie Man\n우리는 이 존재가 나를 선택하고, 나를 찾아온 이유를 나로부터 찾고자 하였다.\n\n내 마음속 작은 욕망의 위시리스트가 모여, 옷장 속 내가 그린 또 다른 세계로 나를 데려가 주길 바라며 Boogie Man을 불러온 것이 아닐까."
    },
    {
        "id": "mot",
        "title": "못 죽는 기사와 비단 요람",
        "type": "싱글 7집",
        "date": "2024.03.20",
        "title_song": "못 죽는 기사와 비단 요람",
        "youtube_url": "https://youtu.be/y7jrpS8GHxs?si=eIu6ng1aYofHJBgC",
        "theme_color": "rgba(139, 92, 246, 0.1)",
        "tracks": ["1. 못 죽는 기사와 비단 요람 [TITLE]", "2. 못 죽는 기사와 비단 요람 (Inst.)"],
        "info": "기존 LUCY의 시그니처인 따뜻하고 청량한 무드에서 벗어나, 이번 DS은 다크하고 판타지적인 요소가 가미된 얼터너티브 팝 락 장르의 곡이다.\n\nLUCY는 불사조의 기사가 아닌 자신이 지키고자 하는 것에 대한 사명감으로 끊임없이 달려가는 그야말로 '못 죽는 기사'를 통해 그들이 지켜온 음악적 신념과 리스너에 대한 자신들의 사명감을 드러내고 있다. 빠른 성장세로 인기를 얻고 있는 밴드 LUCY에게는 다시 한번 그들의 원동력을 다지는 다짐과도 같은 곡이다."
    },
    {
        "id": "from",
        "title": "FROM.",
        "type": "미니 5집",
        "date": "2024.08.14",
        "title_song": "빌런 / 못난이",
        "youtube_url": "https://youtu.be/K25eYCAXknQ",
        "theme_color": "rgba(234, 88, 12, 0.1)",
        "tracks": ["1. 빌런 [TITLE]", "2. 못난이 [TITLE]", "3. 도깨비춤", "4. 남김없이", "5. 낙화"],
        "info": "애정을 담아 보내는 편지의 서문인 ‘DEAR.’를 통해 파랗게 개화한 LUCY가 신보 <FROM.>으로 함께 피워낸 꽃의 마지막 장면을 담아내었다.\n만개 후 흩날리는 꽃잎은 소명을 다하고 지는 것처럼 보이지만 다시 아름답게 피워낼 날을 기약하는 약속의 순환이다.\n지는 순간까지도 아름다워 보이는 꽃잎들도 저마다의 시련을 이겨내고 다시 싹을 피워내는 것처럼 누구에게나 아름답고 어두운 양면의 시기들이 존재한다.\n흔히 빛을 희망에 빗대어 이야기하지만 어둠 또한 또 다른 희망을 의미하기에 <FROM.>은 가장 어두운 나를 조명하며, 다시 찾아내고 피워낼 아름다움을 이야기한다."
    },
    {
        "id": "wajangchang",
        "title": "와장창",
        "type": "미니 6집",
        "date": "2025.04.23",
        "title_song": "잠깨 / 하마",
        "youtube_url": "https://youtu.be/POxUDjkMTPY?si=FpblrMlomnxzKNlT",
        "theme_color": "rgba(16, 185, 129, 0.1)",
        "tracks": ["1. 잠깨 [TITLE]", "2. 하마 [TITLE]", "3. 내가 더", "4. 뚝딱", "5. 미워하지 않아도 될 수많은 이유", "6. bleu"],
        "info": "무언가 깨부수고 새롭게 피우려 하는 소리를 “와장창”으로 표현하여 각 곡마다 메시지를 담았다.\n세상 밖으로 나오기 위해 껍질을 깨는 소리, 얼음이 온기를 만나 깨지는 소리, 새로운 시작 앞을 가로막고 있던 벽을 부수는 소리 “와장창”.\n\n이제 우리 모두 “와장창” 소리를 내며 또다시 피울 시간이다."
    },
    {
        "id": "sun",
        "title": "선",
        "type": "미니 7집",
        "date": "2025.10.30",
        "title_song": "사랑은 어쩌고 / 다급해져",
        "youtube_url": "https://youtu.be/hv4odztpC3U?si=JQJDnFgPRuJpBXX3",
        "theme_color": "rgba(245, 158, 11, 0.1)",
        "tracks": ["1. 사랑은 어쩌고 [TITLE]", "2. EIO", "3. 다급해져 (Feat. 원슈타인) [TITLE]", "4. 사랑한 영원"],
        "info": "LUCY의 일곱 번째 EP 은 정의할 수 없는 사랑의 다양한 모습을 LUCY만의 감각으로 담아낸 앨범이다.\n\n같은 선이어도 연결된 방식과 매듭에 따라 각각의 모양을 지니게 되는데, 이처럼 사랑도 누군가와 맺어지고 어떻게 표현하는지에 따라 다양한 형태를 갖게 된다.\n\n그래서 우리는 알아야 한다.\n우리의 매듭이 서로 다른 모습을 하고 있어도 결국 사랑이라는 것을."
    },
    {
        "id": "childish",
        "title": "Childish",
        "type": "정규 2집",
        "date": "2026.04.29",
        "title_song": "전체관람가",
        "youtube_url": "https://youtu.be/mMr52FVf6qk?si=1O45IEcEmM2yJbc1",
        "theme_color": "rgba(99, 102, 241, 0.1)",
        "tracks": ["1. 발아", "2. 전체관람가 [TITLE]", "3. 카멜레온", "4. 하마 (Childish ver.)", "5. 사랑은 어쩌고 (Childish ver.)", "6. EIO (Childish ver.)", "7. Porch Light (Feat. 남제현)", "8. bleu", "9. 미워하지 않아도 될 수많은 이유 (Childish ver.)", "10. 구구절절", "11. 잠깨 (Childish ver.)", "12. 다급해져 (Feat. 원슈타인) (Childish ver.)", "13. 뚝딱 (Childish ver.)", "14. 내가 더 (Childish ver.)", "15. 사랑한 영원"],
        "info": "쉴 새 없이 돌아가는 삭막한 현실 속에서, 한없이 유치하고 순수했던 나를 찾아 헤매다.\n\n우리는 본연에 깃든, 유치하고 순수한 자신을 발견하지 못하고, 어른의 모습으로 버거워하며 살아간다.\n삭막한 현실에서 나다움을 지켜내며, 지루하지 않고 즐겁게 살아갈 방법은 우리 모두에게 내재된 ‘동심’을 찾아내어 마주하는 것이다. 그때 비로소 우리는 진짜 현실을 살아가게 될 것이다."
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
        "lyric": "\"반대로 내가 가고 싶은 대로만 간다면\n\n그저 틀린 길은 아닐 걸\"",
        "description": "속도감 있는 빠른 드럼 비트와 청량하게 터지는 신예찬의 바이올린 솔로가 당신의 심장박동을 높여줄 것입니다. 러닝이나 맑은 날 드라이브에 완벽히 어울립니다.",
        "youtube_url": "https://youtu.be/dh684FWByO4?si=-C-OiRpEzjGSmikh"
    },
    {
        "id": "comfort",
        "option_text": "☕ 지친 하루의 끝, 따뜻하고 포근한 위로가 필요할 때",
        "song": "선잠 (Snooze)",
        "album": "선잠 (싱글 2집)",
        "lyric": "\"너의 마음에 작은 온기를 불어넣을 선잠을 빌려줄게\"",
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
        "lyric": "\"아니 근데 진짜 너 예쁘다니까\n\n새벽을 깨우는 환한 햇살같아\"",
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
