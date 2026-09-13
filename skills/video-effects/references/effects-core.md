# 기존 핵심 효과 — 14개

Higgsfield의 [공개 Effects](https://higgsfield.ai/effects)와 아래 상세 설명을 2026-09-12에 확인해 시각 원리를 정리했다. 동작 요약의 근거는 공개 텍스트이며 영상을 직접 분석했다고 주장하지 않는다. 아래 장면 설계·프롬프트는 새로 작성한 각색으로, 공식 내부 프롬프트나 다른 모델에서 검증된 프리셋이 아니다.

이 파일만으로 범용 프롬프트를 작성할 수 있다. 최신 목록 요청이나 불명확한 특정 효과 확인에만 추가 조회를 한다. 각 항목의 영어 문장은 핵심 동작 예시이며 최종 결과에는 사용자 장면, 시작 상태, 카메라, 마지막 상태를 함께 채운다.

<a id="floating-fall"></a>
## 1. 공중 정지와 낙하 재개 — Floating fall

[동작 출처](https://higgsfield.ai/effects/examples/floating-fall): 낙하 중 소지품이 떠 있고 제품 클로즈업을 거쳐 낙하가 이어지는 구조.
- 설계: 떨어질 대상이 보임 → 중력의 영향이 잠시 멈춤 → 카메라가 정지한 대상에 접근 → 낙하 재개 또는 요청한 공중 정지 구도로 종료.
- 분리: 정지할 물체와 계속 움직일 배경·카메라를 지정한다. 제품만 요청하면 인물 낙하 없이 병의 상승·체공·착지로 각색한다.
- 핵심 문장: “The falling objects stop at different heights in midair. The camera glides between them, then their downward motion resumes.”
- 제작 보완: 라벨이 중요한 제품 숏은 회전을 줄이고 끝에 정면을 남긴다. 핵심이 낙하 재개라면 임의로 정지 엔딩으로 바꾸지 않는다.

<a id="cutout"></a>
## 2. 공간을 레이어로 분리 — Cutout

[동작 출처](https://higgsfield.ai/effects/examples/cutout): 주변이 오려낸 레이어로 분리돼 흰 공간을 드러낸 뒤 복귀.
- 설계: 인물/제품과 배경이 함께 보임 → 배경 경계를 따라 층이 갈라짐 → 층들이 서로 다른 깊이로 벌어짐 → 다시 맞물림.
- 분리: 보호할 피사체의 윤곽과 분리할 배경을 구별한다. 종이·사진·얇은 건축판 등 원하는 재질을 선택한다.
- 핵심 문장: “The background separates into thin cut-paper layers and drifts outward at different depths, exposing a white void around the intact subject. The layers slide back into alignment.”
- 제작 보완: 원테이크라면 층의 이동을 연결하고 하드컷을 추가하지 않는다. 흰 공간을 다른 색으로 바꾸면 선택한 변주로 표시한다.

<a id="eyes-in"></a>
## 3. 눈을 통과하는 장면 연결 — Eyes in

[동작 출처](https://higgsfield.ai/effects/examples/eyes-in): 눈동자 안으로 카메라가 들어가 다른 공간으로 연결.
- 설계: 얼굴에서 한쪽 눈으로 접근 → 홍채가 프레임을 채움 → 동공의 어둠을 통과 → 목적지 공간이 열림.
- 분리: 눈 안에 비친 영상인지 실제 통과하는 환상 전환인지 정한다. 목적지와 전환 뒤 시점을 구체화한다.
- 핵심 문장: “The camera moves toward one eye until the iris fills the frame, passes through the dark pupil, and emerges into the remembered room.”
- 제작 보완: 실제 무편집 요구라면 연속된 시각적 통로로 설계한다. 암전 뒤 컷을 쓰는 방식은 편집 대안으로 구분한다.

<a id="bullet-time"></a>
## 4. 시간 정지 속 카메라 회전 — Bullet time

[동작 출처](https://higgsfield.ai/effects/examples/bullet-time): 흩어진 물체와 인물이 멈춘 동안 카메라가 회전하고 상태가 정리됨.
- 설계: 행동 발생 → 인물·물체의 운동 정지 → 카메라만 호를 그리며 이동 → 시간 재개 또는 합의한 복귀.
- 분리: 카메라 궤도와 피사체 회전을 구별한다. 회전 각도는 장면에 맞추며 완전한 360도는 사용자가 원할 때 보존한다.
- 핵심 문장: “The performer and suspended droplets remain motionless in world space while the camera travels in an arc around them. Motion resumes as the camera settles.”
- 제작 보완: 원본에서 보이지 않는 뒤쪽은 모델이 추정할 수 있다. 재현이 부족하면 짧은 회전이나 다각도 참고를 대안으로 제안한다.

<a id="clones"></a>
## 5. 같은 인물의 증식 — Clones

[동작 출처](https://higgsfield.ai/effects/examples/clones): 같은 인물들이 등장해 움직임을 반복.
- 설계: 원본 인물 → 정해진 위치에 복제 인물 등장 → 동작의 동시성 또는 시차 반복 → 하나로 수렴하거나 군무로 종료.
- 분리: 복제 수·배치·등장 순서를 지정하고 서로 다른 인물로 바뀌지 않도록 특징을 연결한다.
- 핵심 문장: “Two identical copies appear one after the other beside the central performer, repeating the same gesture with a slight delay.”
- 제작 보완: 숫자가 중요하면 레이어 합성도 대안이다. “인물 복제 금지” 같은 일관성 문장을 함께 넣지 않는다.

<a id="vanish"></a>
## 6. 몸의 소멸과 남은 옷 — Vanish

[동작 출처](https://higgsfield.ai/effects/examples/vanish): 몸이 사라진 직후 빈 옷이 바닥에 떨어짐.
- 설계: 사람의 존재와 의상을 보여줌 → 몸 소멸 → 지지를 잃은 의상이 접히며 낙하 → 빈 공간을 유지.
- 분리: 남길 옷·소품과 사라질 몸을 지정한다. 효과 뒤 반응이나 정적의 길이가 장면의 정서를 만든다.
- 핵심 문장: “The person's body disappears instantly. Their now-empty coat loses its support, folds inward, and drops to the floor.”
- 제작 보완: 용해나 연기 소멸을 추가하면 다른 변주가 된다. 제품 소멸에 쓰면 옷 낙하를 그대로 복사하지 않는다.

<a id="world-morphing"></a>
## 7. 세계가 안으로 접힘 — World morphing

[동작 출처](https://higgsfield.ai/effects/examples/world-morphing): 중심 피사체 주변의 풍경이 들리고 접혀 공간을 에워쌈.
- 설계: 넓은 공간 → 외곽이 들림 → 양옆/먼 풍경이 중심을 향해 접힘 → 거대한 포위 공간 형성.
- 분리: 피사체 아래 지면을 유지할지 함께 움직일지 명시한다. 세계가 접히는 것과 카메라 롤을 혼동하지 않는다.
- 핵심 문장: “The distant street and buildings lift from their outer edges and fold inward around the stationary figure, forming an enormous enclosure.”
- 제작 보완: 배경 변화가 주효과이면 카메라 이동을 절제해 변형을 읽을 시간을 준다.

<a id="architecture-wave"></a>
## 8. 건축물의 파동 — Architecture wave

[동작 출처](https://higgsfield.ai/effects/examples/architecture-wave): 전경의 자연스러운 행동 뒤로 건물들이 유체처럼 휘어짐.
- 설계: 견고한 건물 → 한쪽에서 휨 발생 → 파동이 건물군을 통과 → 잔물결이 가라앉음.
- 분리: 전경 인물의 보행과 후경 건물 변형을 독립시킨다. 구조물이 액체가 되는지, 고체 표면인 채 휘는지 선택한다.
- 핵심 문장: “A broad deformation wave travels through the buildings behind the walking figure, bending their façades while the foreground pavement stays stable.”
- 제작 보완: 건물이 인물에 겹쳐 녹는 문제가 나면 거리와 보호 영역을 보강한다.

<a id="melting"></a>
## 9. 물성의 용해 — Melting

[동작 출처](https://higgsfield.ai/effects/examples/melting): 대상과 부속물이 늘어지며 액체 웅덩이로 변함.
- 설계: 원형 인지 → 특정 부분부터 처짐 → 끈적한 흐름이 아래로 이동 → 바닥에 모임.
- 분리: 용해할 재질과 보호할 요소를 정한다. 제품 형태를 유지해야 하는 광고라면 주변 세트/외피만 녹이는 변주를 선택한다.
- 핵심 문장: “The sculpted surface softens from the top, stretches into thick liquid strands, and gathers into a glossy pool at its base.”
- 제작 보완: “모든 형태 유지”와 “대상 용해”를 동시에 지시하지 않는다. 인지 단계와 변형 단계를 나눈다.

<a id="earth-zoom"></a>
## 10. 우주에서 장소로 진입 — Earth zoom

[동작 출처](https://higgsfield.ai/effects/examples/earth-zoom-exported): 궤도에서 구름·도시를 지나 지상으로 접근.
- 설계: 지구/궤도 → 대기·구름 → 지역의 거리 구조 → 목적지와 인물/제품.
- 분리: 마지막 목적지를 먼저 정해 시선 축을 연결한다. 지상에서 우주로 후퇴하는 요청이면 역방향 각색임을 명시한다.
- 핵심 문장: “The viewpoint descends from orbit through cloud layers toward the city grid, decelerating into the final street-level view.”
- 제작 보완: 여러 스케일을 한 번에 유지하기 어렵다면 구름 등 가림 지점의 편집을 대안으로 제시한다. 실제 무편집 요구에는 그 대안을 몰래 적용하지 않는다.

<a id="selfception"></a>
## 11. 프레임 안의 재귀 — Selfception

[동작 출처](https://higgsfield.ai/effects/examples/selfception): 작은 동일 인물 안으로 계속 접근하는 중첩 구조.
- 설계: 큰 장면 안의 작은 동일 장면 → 작은 장면으로 접근 → 그것이 새 전체 구도가 됨 → 반복.
- 분리: 반복 횟수, 중심점, 프레임의 대응 형태를 고정한다. 무한 루프는 유한 생성 구간과 편집상 연결 목표로 구분한다.
- 핵심 문장: “The camera pushes toward the miniature scene held in the hands until it becomes the full frame, revealing the same composition at the next scale.”
- 제작 보완: 정확한 루프에는 시작·끝 구도 맞춤이나 후반 합성이 필요할 수 있다.

<a id="incline"></a>
## 12. 중력 방향의 기울어짐 — Incline

[동작 출처](https://higgsfield.ai/effects/examples/incline): 중심 인물 주변 세계가 기울며 느슨한 물체가 이동.
- 설계: 기준 수평 → 환경의 기울기 변화 → 소품이 새 중력 방향으로 미끄러짐 → 새 균형 또는 복귀.
- 분리: 인물의 축, 환경의 축, 카메라의 축 중 무엇이 유지되는지 지정한다.
- 핵심 문장: “The room tilts around the upright figure. Loose objects slide toward its lowered side while the camera maintains the figure's vertical alignment.”
- 제작 보완: 단순 화면 회전만으로 처리되지 않도록 소품의 물리적 반응과 공간 관계를 적는다.

<a id="wild-ride"></a>
## 13. 역동적인 궤도 이동 — Wild ride

[동작 출처](https://higgsfield.ai/effects/examples/wild-ride): 회전·드리프트하는 중심 동작을 따라 높은 시점과 낮은 시점 사이로 움직이는 카메라.
- 설계: 중심 동작 인지 → 대상 주위를 이동 → 연결된 경로로 높이 변화 → 동작의 끝과 함께 안정.
- 분리: 피사체의 이동과 카메라의 궤도를 각각 쓴다. 빠른 이동 자체가 목적이 아니라 동작의 힘과 공간을 보여 주는지 판단한다.
- 핵심 문장: “The camera arcs around the drifting car, descends along a continuous curved path, and settles near wheel height as the car straightens.”
- 제작 보완: 좁은 공간이면 요청에 맞는 짧은 호를 사용한다. 갑작스러운 위치 점프를 원테이크라고 쓰지 않는다.

<a id="act-natural"></a>
## 14. 국소 시간 정지 — Act natural

[동작 출처](https://higgsfield.ai/effects/examples/act-natural): 중심 인물과 일부 물체가 정지해도 나머지 세계의 시간은 흐름.
- 설계: 일상 동작 → 선택된 인물/물체만 멈춤 → 주변 행동이 이어짐 → 정지 해제 또는 대비를 남김.
- 분리: 시간 그룹을 정확히 지정한다. 영상 전체 일시정지나 슬로모션과 구분한다.
- 핵심 문장: “The central figure and the cup beside them freeze mid-action while pedestrians continue walking through the background at normal speed.”
- 제작 보완: 음악·대사도 정지한다고 자동 가정하지 않는다. 움직이는 군중이 주피사체를 가리는 구간은 필요한 경우 줄인다.


전체 선택은 [효과 색인](effect-selection.md)을 참조한다. 그림을 실제 인물로 재현하는 유형은 제외한다.
