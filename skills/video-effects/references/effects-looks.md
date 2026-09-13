# 화면 스타일·재질 효과 — 33개

[선택 색인](effect-selection.md)에서 필요한 항목만 읽는다. [공식 카탈로그](https://higgsfield.ai/effects)의 짧은 설명에서 시각 특성을 요약했다. 개별 식별자는 [스냅샷](catalog-snapshot.json)에 있다. **아래 시간 과정·동작 문장은 새 각색**이며 원본 영상에서 확인된 전환 방식이 아니다. 스타일만 요청하면 전체 숏에 일정하게 적용해도 된다. 그림 속 인물을 실사로 재현하는 유형은 제외했지만 잉크·캔버스·색감 등 화면 처리는 유지한다. 얼굴·제품·공간 중 어떤 표면에 입힐지 먼저 선택한다. 영화·광고·뮤직비디오에 공통 적용하며, 완전한 최종 프롬프트에는 사용자 장면과 카메라·끝 상태를 추가한다.

<a id="ink-riot"></a>
## Ink Riot

- 시각 특성: 여러 매체를 겹친 밀도 높은 잉크·혼합재료 화면.
- 시간 과정 각색: 주제의 실루엣 주위로 잉크와 잘린 질감을 단계적으로 겹치고 중심은 남긴다.
- 분리·보완: 얼굴·제품 라벨을 가리는 면적을 제한한다.
- 핵심 문장: “Layers of ink marks and mixed-media textures build around the subject while its central silhouette stays readable.”

<a id="comic"></a>
## Comic

- 시각 특성: 그래픽 만화식 선과 색면.
- 시간 과정 각색: 외곽선이 먼저 잡히고 음영을 색면으로 정리한 뒤 만화 화면을 유지한다.
- 분리·보완: 말풍선·만화 분할·슈퍼히어로 동작은 별도 요청 때만 더한다.
- 핵심 문장: “Clean illustrated contours form around the subject as the shading simplifies into graphic comic color planes.”

<a id="cold-vision"></a>
## Cold vision

- 시각 특성: 차가운 네온과 짙은 그림자.
- 시간 과정 각색: 기존 구도에서 차가운 가장자리 빛이 강해지고 후경의 네온이 나타난다.
- 분리·보완: 온도감·조명 효과이며 열화상 센서라고 단정하지 않는다.
- 핵심 문장: “Cool neon edge light grows around the subject while the background falls into deep blue shadow.”

<a id="particles"></a>
## Particles

- 시각 특성: 움직이는 발광 입자.
- 시간 과정 각색: 입자의 발생 위치·흐름·소멸 지점을 정해 피사체 주변으로 한 번 흐르게 한다.
- 분리·보완: 몸의 입자 분해는 별도 변형 요청일 때만 적용한다.
- 핵심 문장: “Luminous particles emerge behind the subject, stream along a curved path, and fade before crossing the face.”

<a id="windows"></a>
## Windows

- 시각 특성: 겹쳐진 디지털 인터페이스 창.
- 시간 과정 각색: 후경에서 창이 열리고 깊이별로 겹친 뒤 중심 창 하나에 정착한다.
- 분리·보완: 실제 OS나 읽을 수 있는 UI 문구를 자동 가정하지 않는다.
- 핵심 문장: “Translucent interface windows open at different depths around the subject and settle into a layered digital composition.”

<a id="canvas"></a>
## Canvas

- 시각 특성: 손으로 그린 캔버스 질감.
- 시간 과정 각색: 현재 장면에 직물 결·붓 질감을 입히며 구도를 유지한다.
- 분리·보완: 그림 속 사람을 실제 사람으로 바꾸는 재현 장면과 구분한다.
- 핵심 문장: “Canvas grain and hand-drawn pigment texture spread across the existing scene while its composition remains fixed.”

<a id="tracking"></a>
## Tracking

- 시각 특성: 물체를 추적하는 선형 그래픽.
- 시간 과정 각색: 대상 특징점을 정해 선과 경계가 움직임을 따라가도록 한다.
- 분리·보완: 추적 카메라 이동이 아니다. 그래픽 오버레이와 카메라 지시를 분리한다.
- 핵심 문장: “Thin tracking lines lock onto the moving object and update their positions as it crosses the frame; the camera remains fixed.”

<a id="lsd"></a>
## LSD

- 시각 특성: 환각적인 색 파동.
- 시간 과정 각색: 후경의 색이 파동으로 번졌다 잦아들며 실루엣을 남긴다.
- 분리·보완: 명칭은 색 처리 참고다. 약물 사용이나 인물 행동을 추가하지 않는다.
- 핵심 문장: “Waves of saturated color roll through the background while the subject's outline stays coherent, then settle into a stable palette.”

<a id="palette"></a>
## Palette

- 시각 특성: 손으로 칠한 색채 구성.
- 시간 과정 각색: 큰 색 덩어리를 먼저 두고 선택한 부분에 붓질을 채워 마감한다.
- 분리·보완: 명화 재현이나 고정 화가 모방을 자동 추가하지 않는다.
- 핵심 문장: “Broad painted color fields appear behind the subject, followed by smaller brush marks that complete the composition.”

<a id="fragments"></a>
## Fragments

- 시각 특성: 추상적인 시각 조각의 중첩.
- 시간 과정 각색: 조각이 깊이별로 들어와 한 구도를 구성하고 안정된다.
- 분리·보완: 신체 훼손으로 해석하지 않는다. 분리되는 것은 시각 레이어다.
- 핵심 문장: “Abstract visual fragments drift onto separate planes around the intact subject and settle into a layered frame.”

<a id="overexposed"></a>
## Overexposed

- 시각 특성: 극단적으로 밝은 노출 처리.
- 시간 과정 각색: 하이라이트가 번져 프레임 일부를 덮은 뒤 주요 윤곽을 다시 드러낸다.
- 분리·보완: 제품 식별이 필요하면 노출 회복 구간을 둔다. 시간 변화는 각색이다.
- 핵심 문장: “Highlights bloom toward white around the subject, then recede enough to reveal the defining contours again.”

<a id="multiverse"></a>
## Multiverse

- 시각 특성: 여러 현실 레이어의 충돌.
- 시간 과정 각색: 서로 다른 공간을 겹치고 경계를 교차시킨 뒤 선택한 현실로 정착한다.
- 분리·보완: 각 현실의 기준점과 최종 공간을 지정한다.
- 핵심 문장: “Several versions of the location overlap on translucent planes, slide across one another, and resolve into the selected final world.”

<a id="noir"></a>
## Noir

- 시각 특성: 명암 대비가 큰 누아르 조명.
- 시간 과정 각색: 측면 빛으로 얼굴 일부를 드러내고 배경 그림자를 깊게 유지한다.
- 분리·보완: 흑백·비·범죄 서사는 요청 없으면 필수가 아니다.
- 핵심 문장: “A narrow side light reveals one plane of the face while the opposite side and background remain in deep cinematic shadow.”

<a id="ocean"></a>
## Ocean

- 시각 특성: 바다 색의 유동적 오버레이.
- 시간 과정 각색: 청록·남색 반사가 화면을 따라 흐르고 끝에 잦아든다.
- 분리·보완: 실제 바다 침수 효과로 바꾸지 않는다.
- 핵심 문장: “Fluid blue and teal color reflections wash across the scene as an overlay while the physical space remains unchanged.”

<a id="sketch"></a>
## Sketch

- 시각 특성: 손으로 그린 선과 거친 결.
- 시간 과정 각색: 윤곽을 선으로 단순화하고 필요한 음영에 해칭을 더한다.
- 분리·보완: 정체성에 중요한 얼굴 비율·제품 구조를 남긴다.
- 핵심 문장: “The image resolves into textured hand-drawn outlines with selective hatching while preserving the subject's proportions.”

<a id="akrill"></a>
## Akrill

- 시각 특성: 아크릴처럼 겹친 색 덩어리.
- 시간 과정 각색: 불투명한 색 블록을 겹쳐 입체감과 가장자리를 구성한다.
- 분리·보완: 실제 액체 아크릴의 물리적 유출과 구분한다.
- 핵심 문장: “Opaque acrylic-like color blocks layer across the background and selected surfaces, leaving crisp gaps around the subject.”

<a id="magazine"></a>
## Magazine

- 시각 특성: 인쇄 잡지의 시각 질감.
- 시간 과정 각색: 사진에 인쇄 결·편집 여백을 더해 지면 같은 화면으로 정착한다.
- 분리·보완: 필수 텍스트·표지 문구는 별도 지정하고 실제 글자 작업은 후반 대안으로 둔다.
- 핵심 문장: “The portrait settles into a printed editorial composition with paper grain, deliberate margins, and restrained ink texture.”

<a id="cannabis"></a>
## Cannabis

- 시각 특성: 연기 같은 사이키델릭 포스터 처리.
- 시간 과정 각색: 추상적인 연기 층과 색 대비를 후경에 배치한다.
- 분리·보완: 섭취·흡연 장면을 자동 추가하지 않는다.
- 핵심 문장: “Soft smoke-like graphic layers curl behind the subject and settle into a psychedelic poster composition.”

<a id="bubbles"></a>
## Bubbles

- 시각 특성: 몽환적인 비눗방울 질감.
- 시간 과정 각색: 방울이 다른 깊이로 떠오르고 가장자리를 지나 사라진다.
- 분리·보완: 얼굴 앞의 왜곡 면적과 제품 가림을 조절한다.
- 핵심 문장: “Translucent soap bubbles rise through different depth planes, carrying soft reflections as they drift out of frame.”

<a id="acid"></a>
## Acid

- 시각 특성: 강한 네온색 왜곡.
- 시간 과정 각색: 배경부터 색 분리가 커졌다 선택한 색으로 안정된다.
- 분리·보완: LSD와 가까운 색 처리 계열이다. 별개 물리 사건으로 과장하지 않는다.
- 핵심 문장: “Neon color channels distort across the background, pulse once, and align into a stable high-contrast image.”

<a id="flash-comic"></a>
## Flash comic

- 시각 특성: 강한 에너지가 있는 만화 그래픽.
- 시간 과정 각색: 짧은 그래픽 강조 후 굵은 선과 색면을 유지한다.
- 분리·보완: 실제 섬광·효과음은 별도 지시다. 사용자 음향을 보존한다.
- 핵심 문장: “A brief graphic burst accents the pose, then resolves into bold comic outlines and high-energy color shapes.”

<a id="paper"></a>
## Paper

- 시각 특성: 수공예 종이 질감.
- 시간 과정 각색: 종이 결과 접힌 가장자리를 선택 영역에 입힌다.
- 분리·보완: Cutout처럼 공간 분리를 자동 포함하지 않는다.
- 핵심 문장: “Handcrafted paper texture appears across the set surfaces, with subtle folded edges and the original spatial layout intact.”

<a id="random-glow"></a>
## Random Glow

- 시각 특성: 짧은 설명의 불규칙 발광 처리.
- 시간 과정 각색: 빛의 위치를 소수 지점으로 제한하고 약하게 켜졌다 꺼지게 각색한다.
- 분리·보완: 카탈로그 설명이 짧아 색·빈도·범위를 공식 동작으로 주장하지 않는다.
- 핵심 문장: “Small areas of soft glow appear at irregular positions around the subject, brighten gently, and fade without obscuring the face.”

<a id="toxic"></a>
## Toxic

- 시각 특성: 방사성 이미지를 연상시키는 강렬한 네온색.
- 시간 과정 각색: 선택한 배경·외곽에 독특한 네온 색을 입힌다.
- 분리·보완: 실제 독성 사건이나 신체 손상을 의미하지 않는다.
- 핵심 문장: “Intense radioactive-green graphic light spreads through the background while the intact subject remains clearly outlined.”

<a id="broken-mirror"></a>
## Broken mirror

- 시각 특성: 깨진 거울의 반사 분할.
- 시간 과정 각색: 조각별 반사 각도를 어긋나게 했다가 최종 분할 구도로 고정한다.
- 분리·보완: 반사된 얼굴을 다른 정체성으로 만들지 않는다. 실제 유리 파열 동작은 별도 각색이다.
- 핵심 문장: “The reflection separates into angled mirror fragments, each retaining a coherent portion of the same subject.”

<a id="hand-paint"></a>
## Hand paint

- 시각 특성: 자유로운 손 붓질 표현.
- 시간 과정 각색: 큰 붓질을 배경부터 올리고 작은 흔적으로 마무리한다.
- 분리·보완: Palette와 유사한 색 표현 계열이며 인물화 실사 재현은 포함하지 않는다.
- 핵심 문장: “Freeform hand-painted strokes sweep across the background and selected contours, then hold as a textured finished image.”

<a id="lava"></a>
## Lava

- 시각 특성: 용암색의 유동적 움직임.
- 시간 과정 각색: 검정·적색·주황이 점성 있게 흘렀다 고이는 그래픽을 만든다.
- 분리·보완: 물리적 용암 분출이나 인물 연소를 자동 추가하지 않는다.
- 핵심 문장: “Viscous red-orange color flows through dark graphic channels around the subject and gathers into slow luminous pools.”

<a id="marble"></a>
## Marble

- 시각 특성: 조각된 대리석 같은 표면.
- 시간 과정 각색: 정한 대상에 돌의 결·미세 반사·조각 음영을 입힌다.
- 분리·보완: 몸을 석화할지 표면만 바꿀지는 별도 선택한다. 제품 라벨 보호를 구체화한다.
- 핵심 문장: “Fine marble veins and sculpted stone shading develop across the chosen surface while its silhouette remains stable.”

<a id="modern"></a>
## Modern

- 시각 특성: 정돈된 기하학적 미니멀 화면.
- 시간 과정 각색: 몇 개 도형과 여백으로 배경을 재구성하고 정지한다.
- 분리·보완: 큰 VFX 사건이 아닌 구성 스타일로 추천한다.
- 핵심 문장: “A few clean geometric planes arrange behind the subject, leaving generous negative space and a restrained minimal composition.”

<a id="origami"></a>
## Origami

- 시각 특성: 각이 뚜렷한 종이접기 기하 형태.
- 시간 과정 각색: 선택 영역을 접힌 면으로 분할해 기하 구조를 만든다.
- 분리·보완: 원자료 설명이 짧고 일부 잘려 있어 접히는 시간 과정은 새 각색이다.
- 핵심 문장: “The selected object resolves into crisp folded-paper planes, with clear creases and a stable recognizable silhouette.”

<a id="two-color"></a>
## Two color

- 시각 특성: 대비가 큰 두 가지 색 구성.
- 시간 과정 각색: 지정한 두 색으로 화면을 분리하고 중요한 윤곽을 보존한다.
- 분리·보완: 색 두 개를 사용자 브랜드/장면에 맞게 정한다. 자동 깜빡임은 없다.
- 핵심 문장: “The scene simplifies into two contrasting colors, preserving the subject's essential contours and holding the final graphic composition.”

<a id="ultraviolet"></a>
## Ultraviolet

- 시각 특성: 자외선 느낌의 네온 발광.
- 시간 과정 각색: 보라·청색 계열 외곽광을 조절해 어둠에서 형태를 드러낸다.
- 분리·보완: 실제 UV 물리 시뮬레이션이라고 주장하지 않는다.
- 핵심 문장: “Violet and blue neon edge glow reveals the subject against a dark background, then stabilizes at a restrained intensity.”

<a id="vintage"></a>
## Vintage

- 시각 특성: 손으로 잉크를 입힌 삽화 스타일.
- 시간 과정 각색: 윤곽·음영을 잉크 선과 인쇄 결로 정리한다.
- 분리·보완: 이 카탈로그의 설명은 손 잉크 삽화다. 이름만 보고 세피아·VHS·필름 손상을 강제하지 않는다.
- 핵심 문장: “Hand-inked contours and printed illustration texture replace the smooth shading while the original composition remains recognizable.”
