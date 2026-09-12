# Seedance 2.5 Prompting v2

스토리·이미지를 읽고 장면, 카메라, 연기, 음향을 씨댄스 2.5용 전체 프롬프트로 작성하는 배포용 Codex 스킬 묶음입니다. **v2 / 2.0.0은 이 스킬 묶음의 버전**이며, 대상 영상 모델은 Seedance 2.5입니다.

기존 `seedance-2-5-prompting` 저장소와 분리한 독립 v2 공개 저장소입니다. 로그인이나 초대 없이 열람하고 내려받을 수 있습니다.

## 포함된 스킬

| 폴더 | 역할 |
| --- | --- |
| [seedance-2-5-prompting](skills/seedance-2-5-prompting/SKILL.md) | 입력 해석, 레퍼런스 역할, 타임라인, 카메라·음향, 전체 프롬프트 작성·수정 |
| [seedance-25-cinematic](skills/seedance-25-cinematic/SKILL.md) | 영화 같은 사건·연기·조명·대사·원테이크 연출 |
| [eyecandy-visual-development](skills/eyecandy-visual-development/SKILL.md) | 장면의 감정과 공간에 맞는 구도·무빙·전환 선택 |

GODSTOUCH 액션 카메라, NO-BGM, 스토리·이미지 해석, 2.5 작성법 5팁은 기본 스킬의 참고자료에 포함됩니다. 아이캔디의 장면 연결용 모티프 참고자료도 함께 들어 있어 특정 개인 PC의 HERA 설치 경로에 의존하지 않습니다.

## v2에서 할 수 있는 일

- 스토리만, 이미지만, 둘 다 받아 어울리는 장면을 구성합니다.
- 얼굴·의상·공간·행동·카메라·음향 참조의 역할과 우선순위를 분리합니다.
- 장면에 맞는 렌즈, 고정 또는 주 이동, 경로·속도·초점·끝 구도를 씁니다.
- 영화 같은 반응을 신체 부위·행동·횟수/속도로 구체화하고 접촉을 인과 순서로 연결합니다.
- 요청한 원샷·컷 정책·길이를 유지하며 추격·충격·등장 장면의 카메라를 보강합니다.
- NO-BGM, 완전 무음, 현장음, 무반주 보컬, 첨부 음원 전용을 구분합니다.
- 첫 실패부터 결과나 설명을 보고 수정한 전체 프롬프트를 반환합니다. 고정된 실패 횟수나 다른 테이크의 자동 채택을 적용하지 않습니다.
- 정확한 문자 수와 충돌을 점검합니다. 기본 2.5 작성 상한은 5,000자이며 초과 시 간체 중국어로 압축합니다. 사용자가 언어를 고정하면 그 언어를 유지합니다.

이 수치와 작성법은 스킬의 제작 규칙입니다. 모델의 공식 한도나 생성 성공을 보장하지 않습니다. 실제 생성 모드·오디오 전이·출력 설정은 사용하는 UI에서 확인합니다. 영상 생성은 별도로 요청된 제작 작업에서만 실행합니다.

## 설치

1. GitHub에서 ZIP으로 내려받거나 Git으로 복제합니다:

   ```bash
   git clone https://github.com/babicat4242-svg/seedance-2-5-prompting-v2.git
   ```

2. `skills` 안의 세 폴더를 사용 중인 Codex의 개인 스킬 디렉터리에 나란히 복사합니다. 이 묶음에서 사용하는 기본 위치는 Windows의 `%USERPROFILE%/.codex/skills`, macOS/Linux의 `~/.codex/skills`입니다. 이미 같은 이름의 스킬이 있으면 해당 폴더를 백업한 뒤 교체합니다.

설치 후 디렉터리 구조:

```text
.codex/skills/
  seedance-2-5-prompting/
    SKILL.md
    references/
    scripts/
  seedance-25-cinematic/
    SKILL.md
    references/
  eyecandy-visual-development/
    SKILL.md
    references/
    techniques/
```

저장소 루트 자체를 스킬 하나로 설치하지 말고, 위 세 폴더를 함께 설치합니다. 내부 스킬 이름은 연결 호환성을 위해 유지했습니다. 기존 공개 저장소의 원격 주소를 이 저장소로 변경할 필요는 없습니다.

## 사용 예시

```text
이 이미지와 스토리로 씨댄스 2.5용 20초 원샷 프롬프트를 써줘.
영화 같은 분위기로, 인물 반응이 읽히는 카메라를 골라줘.
대사는 없고 발소리만 허용하는 NO-BGM이야.
```

```text
첫 결과에서 원치 않는 줌과 음악이 들어갔어.
인물과 사건은 유지하고 카메라 고정과 현장음만 남도록 수정해줘.
현재 지시만 담은 전체 프롬프트를 다시 작성해줘.
```

## 검증

저장소 루트에서 Python과 pytest를 사용할 수 있을 때:

```bash
python -m pytest skills/seedance-2-5-prompting/tests -q
python skills/eyecandy-visual-development/tests/test_technique_contract.py
```

배포 점검 기록은 [VALIDATION.md](VALIDATION.md), 버전별 변경은 [CHANGELOG.md](CHANGELOG.md)에 있습니다. 프롬프트 작성 사례 점검은 실제 영상 생성 성공률 측정과 구분합니다.

## 자료와 라이선스

스킬 본문에 원자료의 출처와 작성 관찰/공식 사양의 구분을 유지했습니다. 원본 강의 ZIP·PDF·이미지·영상과 개인 작업 파일은 배포에 포함하지 않습니다. 기존 코드·문서의 라이선스 고지는 [LICENSE](LICENSE)에 보존했습니다.
