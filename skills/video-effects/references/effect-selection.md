# 효과 선택 색인 — 81개

2026-09-12 확인한 [Higgsfield Effects](https://higgsfield.ai/effects) 공개 갤러리 45개와 공식 카탈로그의 고유 항목 87개를 대조했다. 갤러리 45개는 카탈로그 87개에 포함된다. 사용자 요청으로 **그림·명화를 실제 인물로 재현하는 6개 유형을 제외해 81개**를 제공한다. 기존 14개에 67개를 추가했다. 원자료의 87개 전부가 독립적인 시간 변화 VFX인 것은 아니며 장면·카메라·그래픽 스타일도 포함한다. 목록은 확인일 스냅샷이다.

원본 영상 81개의 12시점 표본 분석과 장면별 완성 프롬프트를 각 항목에 연결했다. 예전 설명 중심의 묶음 문서는 개념 참고이며, 실제 원본과의 차이는 아래 개별 분석 카드의 관찰 기록을 따른다.

## 선택 규칙

1. 장면의 감정·사건·제품 정보·퍼포먼스에 필요한 변화부터 정한다. 효과가 필요 없으면 추가하지 않는다.
2. 아래 색인에서 관련 항목만 열어 시작·발동·변화·카메라·끝·연결을 사용자 장면으로 재작성한다. 81개 문서를 모두 읽을 필요가 없다.
3. **근거 요약과 새 연출 각색을 구분한다.** 공개 텍스트를 읽은 항목을 영상 분석했다고 쓰지 않는다. 스타일의 시간 변화는 각색이며 필수가 아니다.
4. Stop world는 주변 정지/주인공 이동, Act natural·Frozen in motion은 주인공 정지/주변 이동이다. Tracking은 추적 그래픽, Moonwalk는 천체 모형을 밟는 무대 같은 장면, Lidar transition은 점군→실사다. 이름만으로 동작을 추측하지 않는다.
5. 그림을 실제 인물로 재현하는 유형은 추천하지 않는다. 그림 질감·잉크·종이·색감은 별도 범주로 유지한다. 제외 항목은 [자료 대조 기록](catalog-snapshot.json)에만 남기며 실행 레시피로 제공하지 않는다.

계정·플러그인·실시간 조회 없이 이 자료로 완전한 범용 프롬프트를 작성한다. 특정 모델에서는 해당 모델의 참조 태그·길이·컷·음향·출력 계약을 우선한다. 여기 있는 이름이나 원본 ID는 생성 명령이 아니다.

## 기존 핵심 효과 — 14개

| 항목 | 시각 원리 |
| --- | --- |
| [Floating fall](prompt-library/higgsfield/floating-fall.md) | 공중 정지와 낙하 재개 |
| [Cutout](prompt-library/higgsfield/cutout.md) | 배경 레이어 분리와 복귀 |
| [Eyes in](prompt-library/higgsfield/eyes-in.md) | 눈을 통과하는 공간 연결 |
| [Bullet time](prompt-library/higgsfield/bullet-time.md) | 정지한 사건 주위의 카메라 궤도 |
| [Clones](prompt-library/higgsfield/clones.md) | 동일 인물의 증식 |
| [Vanish](prompt-library/higgsfield/vanish.md) | 몸 소멸 뒤 빈 옷 낙하 |
| [World morphing](prompt-library/higgsfield/world-morphing.md) | 풍경이 안으로 접히는 공간 변형 |
| [Architecture wave](prompt-library/higgsfield/architecture-wave.md) | 건축물에 전파되는 휨 |
| [Melting](prompt-library/higgsfield/melting.md) | 고체가 액체로 용해 |
| [Earth zoom](prompt-library/higgsfield/earth-zoom.md) | 궤도에서 지상으로 진입 |
| [Selfception](prompt-library/higgsfield/selfception.md) | 동일 장면으로 들어가는 재귀 |
| [Incline](prompt-library/higgsfield/incline.md) | 세계의 기울기와 중력 반응 |
| [Wild ride](prompt-library/higgsfield/wild-ride.md) | 동작 주위의 역동적인 카메라 경로 |
| [Act natural](prompt-library/higgsfield/act-natural.md) | 선택된 대상만 정지 |

## 추가 장면·동작 — 34개

| 항목 | 시각 원리 |
| --- | --- |
| [Studio slide](prompt-library/higgsfield/studio-slide.md) | 크기·각도·깊이가 다른 동일 인물 레이어가 단색 공간에서 교차한다. |
| [Smash and grab](prompt-library/higgsfield/smash-and-grab.md) | 차창 안 제품을 보여준 뒤 유리를 깨고 가져가는 동작에서 도주 추적 숏으로 이어진다. |
| [High flip](prompt-library/higgsfield/high-flip.md) | 카메라가 인물 위로 올라가 뒤집히며 반대편 인물·공간을 공개한다. |
| [Street colossus](prompt-library/higgsfield/street-colossus.md) | 도심 속 인물을 거대하게 배치하는 규모 대비다. |
| [Lacewalker](prompt-library/higgsfield/lacewalker.md) | 작은 인물이 거대한 자신을 지나 대형 가방 사이의 얇은 스트랩을 건넌다. |
| [Burning man](prompt-library/higgsfield/burning-man.md) | 불꽃으로 된 분신이 등장해 원래 인물에게 악수를 내민다. |
| [boarding pass](prompt-library/higgsfield/boarding-pass.md) | 거대한 항공권을 통과할 때마다 의상과 장소가 바뀐다. |
| [Monster dab](prompt-library/higgsfield/monster-dab.md) | 거대한 판타지 생물이 주인공 뒤로 내려와 존재감을 드러낸다. |
| [Lidar transition](prompt-library/higgsfield/lidar-transition.md) | 청록색 깊이 점군으로 보이는 식물 공간을 이동하다 인물 가까이에서 실사 색과 질감으로 해소된다. |
| [Scrapbook collage](prompt-library/higgsfield/scrapbook-collage.md) | 중앙 전신과 주변 상세 프레임이 한 화면에서 함께 보이는 스크랩북 구성이다. |
| [Stop world](prompt-library/higgsfield/stop-world.md) | 중앙 인물이 손으로 신호를 보낸 뒤 주변 보행자들이 멈추고 인물은 앞으로 움직인다. |
| [Agamemnon](prompt-library/higgsfield/agamemnon.md) | 영화 스크린에서 인물이 밖으로 나오고 갑옷 입은 전사들이 극장으로 들어온다. |
| [Infinite clones](prompt-library/higgsfield/infinite-clones.md) | 작은 차에서 동일 인물들이 계속 나와 서로 다른 방향으로 달린다. |
| [Frozen in motion](prompt-library/higgsfield/frozen-in-motion.md) | 중심 인물은 공중 동작에서 멈추고 보행자와 차량은 계속 움직인다. |
| [Mighty fighter](prompt-library/higgsfield/mighty-fighter.md) | 안개와 붉은 양귀비 들판 속 지친 기사의 장면이다. |
| [Pigeons](prompt-library/higgsfield/pigeons.md) | 도시에서 발밑 비둘기를 스케이트처럼 타고 떠서 이동하는 초현실 장면이다. |
| [Fairytale castle](prompt-library/higgsfield/fairytale-castle.md) | 어스름 들판이 빛나는 성·개울·불꽃놀이의 동화 풍경으로 전환된다. |
| [Superstar](prompt-library/higgsfield/superstar.md) | 관중의 휴대폰·경기장 조명·대형 화면 속 얼굴로 스타의 규모를 보여준다. |
| [Skatedog](prompt-library/higgsfield/skatedog.md) | 닥스훈트 위를 스케이트보드처럼 타며 도로를 질주하는 판타지 장면이다. |
| [Blue depth](prompt-library/higgsfield/blue-depth.md) | 어두운 물의 벽이 프레임을 채우며 물고기만 느리게 움직이는 정적 장면이다. |
| [Moonwalk](prompt-library/higgsfield/moonwalk.md) | 왕관 쓴 우주 여행자가 달·태양·지구의 세계를 이동한다. |
| [Knight's diary](prompt-library/higgsfield/knight-s-diary.md) | 알프스 위 쉬는 기사가 고양이와 함께 일기를 쓰는 휴식 장면이다. |
| [2000's paparazzi](prompt-library/higgsfield/2000-s-paparazzi.md) | 2000년대 의상·VHS 감각의 인물이 호텔 회전문에서 나와 플래시 속 검은 차로 이동한다. |
| [Dolphin ride](prompt-library/higgsfield/dolphin-ride.md) | 돌고래를 보드처럼 타는 초현실 서핑 장면이다. |
| [Sticker peel](prompt-library/higgsfield/sticker-peel.md) | 거대한 손이 벽 속 인물을 스티커처럼 떼고 다시 붙인다. |
| [Casual monster slayer](prompt-library/higgsfield/casual-monster-slayer.md) | 일상 인물이 사이버 갑옷으로 바뀌고 불타는 거인이 세탁소에 충돌한 뒤 일상으로 복귀한다. |
| [Selfie twin](prompt-library/higgsfield/selfie-twin.md) | 동일 인물이 들어와 옆에 앉아 셀피를 찍은 뒤 사라진다. |
| [Penguin ride](prompt-library/higgsfield/penguin-ride.md) | 눈 위에서 배로 미끄러지는 펭귄 한 마리에 올라 눈 언덕을 타고 이동한다. |
| [3D render](prompt-library/higgsfield/3d-render.md) | 캐릭터 모델의 소프트웨어 쇼케이스처럼 궤도 카메라·빠른 확대·회전 조명을 사용한다. |
| [Action figure](prompt-library/higgsfield/action-figure.md) | 손이 인물을 딱딱한 피규어로 들어 올려 장난감 리뷰처럼 회전시킨다. |
| [Orbit 360](prompt-library/higgsfield/orbit-360.md) | 피사체 주위를 카메라가 부드럽게 한 바퀴 도는 운동이다. |
| [Orbital presence](prompt-library/higgsfield/orbital-presence.md) | 거대한 우주 인물이 지구의 소용돌이를 손끝으로 펴고 지구에 앉는다. |
| [Race track](prompt-library/higgsfield/race-track.md) | 트랙 위 셀피 보행 중 지나가는 경주차의 바람이 머리·옷·카메라에 전달된다. |
| [Puffin ride](prompt-library/higgsfield/puffin-ride.md) | 발밑 퍼핀을 스케이트처럼 타고 도시 위로 떠서 이동한다. |

## 화면 스타일·재질 — 33개

| 항목 | 시각 원리 |
| --- | --- |
| [Ink Riot](prompt-library/higgsfield/ink-riot.md) | 여러 매체를 겹친 밀도 높은 잉크·혼합재료 화면 |
| [Comic](prompt-library/higgsfield/comic.md) | 그래픽 만화식 선과 색면 |
| [Cold vision](prompt-library/higgsfield/cold-vision.md) | 차가운 네온과 짙은 그림자 |
| [Particles](prompt-library/higgsfield/particles.md) | 움직이는 발광 입자 |
| [Windows](prompt-library/higgsfield/windows.md) | 겹쳐진 디지털 인터페이스 창 |
| [Canvas](prompt-library/higgsfield/canvas.md) | 손으로 그린 캔버스 질감 |
| [Tracking](prompt-library/higgsfield/tracking.md) | 물체를 추적하는 선형 그래픽 |
| [LSD](prompt-library/higgsfield/lsd.md) | 환각적인 색 파동 |
| [Palette](prompt-library/higgsfield/palette.md) | 손으로 칠한 색채 구성 |
| [Fragments](prompt-library/higgsfield/fragments.md) | 추상적인 시각 조각의 중첩 |
| [Overexposed](prompt-library/higgsfield/overexposed.md) | 극단적으로 밝은 노출 처리 |
| [Multiverse](prompt-library/higgsfield/multiverse.md) | 여러 현실 레이어의 충돌 |
| [Noir](prompt-library/higgsfield/noir.md) | 명암 대비가 큰 누아르 조명 |
| [Ocean](prompt-library/higgsfield/ocean.md) | 바다 색의 유동적 오버레이 |
| [Sketch](prompt-library/higgsfield/sketch.md) | 손으로 그린 선과 거친 결 |
| [Akrill](prompt-library/higgsfield/akrill.md) | 아크릴처럼 겹친 색 덩어리 |
| [Magazine](prompt-library/higgsfield/magazine.md) | 인쇄 잡지의 시각 질감 |
| [Cannabis](prompt-library/higgsfield/cannabis.md) | 연기 같은 사이키델릭 포스터 처리 |
| [Bubbles](prompt-library/higgsfield/bubbles.md) | 몽환적인 비눗방울 질감 |
| [Acid](prompt-library/higgsfield/acid.md) | 강한 네온색 왜곡 |
| [Flash comic](prompt-library/higgsfield/flash-comic.md) | 강한 에너지가 있는 만화 그래픽 |
| [Paper](prompt-library/higgsfield/paper.md) | 수공예 종이 질감 |
| [Random Glow](prompt-library/higgsfield/random-glow.md) | 짧은 설명의 불규칙 발광 처리 |
| [Toxic](prompt-library/higgsfield/toxic.md) | 방사성 이미지를 연상시키는 강렬한 네온색 |
| [Broken mirror](prompt-library/higgsfield/broken-mirror.md) | 깨진 거울의 반사 분할 |
| [Hand paint](prompt-library/higgsfield/hand-paint.md) | 자유로운 손 붓질 표현 |
| [Lava](prompt-library/higgsfield/lava.md) | 용암색의 유동적 움직임 |
| [Marble](prompt-library/higgsfield/marble.md) | 조각된 대리석 같은 표면 |
| [Modern](prompt-library/higgsfield/modern.md) | 정돈된 기하학적 미니멀 화면 |
| [Origami](prompt-library/higgsfield/origami.md) | 각이 뚜렷한 종이접기 기하 형태 |
| [Two color](prompt-library/higgsfield/two-color.md) | 대비가 큰 두 가지 색 구성 |
| [Ultraviolet](prompt-library/higgsfield/ultraviolet.md) | 자외선 느낌의 네온 발광 |
| [Vintage](prompt-library/higgsfield/vintage.md) | 손으로 잉크를 입힌 삽화 스타일 |

## 출처·확인 범위

카탈로그는 50개와 37개 두 페이지에서 고유 ID 87개를 확인했다. 전체 원본 설명·미디어·내부 프롬프트는 배포하지 않는다. 설명이 비었거나 충돌한 Stop world·Lidar transition·Penguin ride는 공식 미리보기의 10개 시점 프레임을 확인해 구분했다. 전체 영상을 재생하거나 오디오를 분석했다는 뜻이 아니다. Lidar transition의 중복된 기울임 설명은 시각 확인 근거와 분리했다. 모든 카드의 제작 동작·영어 문장은 자체 작성이며 다른 모델에서 생성 성공을 보장하지 않는다.

추가 자료를 받아 새 효과를 넣을 때에도 출처 확인 범위와 각색을 구분하고, 그림 인물 재현 제외 조건을 유지한다.
