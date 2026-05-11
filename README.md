# English Prompt Buddy

영어가 약한 한국어 사용자가 Codex, Claude Code 같은 AI 코딩 도구에 더 자연스러운 영어로 요청하도록 도와주고, 이를 통해 사용자가 자연스러운 영어 표현을 익힐 수 있게 돕는 Agent Skill입니다.

이 skill은 사용자의 요청을 영어 수업처럼 길게 고치지 않습니다. 대신 실제 작업 흐름을 방해하지 않도록 짧고 자연스러운 영어 프롬프트로 다듬고, 재사용하기 좋은 표현 하나만 알려준 뒤 원래 작업을 계속 진행하게 합니다.

## 이런 사람에게 좋아요

- AI 코딩 도구를 영어로 쓰고 싶은데 표현이 자주 막히는 사람
- 한국어로 먼저 생각한 요청을 자연스러운 영어 작업 지시로 바꾸고 싶은 사람
- 문법 설명보다 바로 써먹는 개발 요청 표현을 배우고 싶은 사람
- Codex나 Claude에게 더 명확하고 안전한 영어 프롬프트를 주고 싶은 사람

## 설치: Codex

Codex에서 GitHub repo 경로로 설치할 수 있습니다.

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo hyun9junn/English-prompt-buddy \
  --path english-prompt-buddy
```

수동으로 설치하려면 이 저장소의 `english-prompt-buddy` 폴더를 `~/.codex/skills/` 아래에 복사하면 됩니다.

```bash
mkdir -p ~/.codex/skills
cp -R english-prompt-buddy ~/.codex/skills/
```

설치 후에는 Codex를 재시작해야 새 skill이 인식됩니다.

## 설치: Claude Code

Claude Code도 같은 `SKILL.md` 기반 skill 구조를 사용합니다. 이 저장소의 `english-prompt-buddy` 폴더를 Claude Code의 personal skills 폴더인 `~/.claude/skills/` 아래에 넣으면 모든 프로젝트에서 사용할 수 있습니다.

GitHub에 올린 뒤 설치하려면 이렇게 받을 수 있습니다.

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/hyun9junn/English-prompt-buddy.git /tmp/English-prompt-buddy
cp -R /tmp/English-prompt-buddy/english-prompt-buddy ~/.claude/skills/
```

이미 저장소를 내려받았다면 이렇게 복사하면 됩니다.

```bash
mkdir -p ~/.claude/skills
cp -R english-prompt-buddy ~/.claude/skills/
```

특정 프로젝트에서만 쓰고 싶다면 프로젝트 루트에 `.claude/skills/` 폴더를 만들고 그 아래에 복사하세요.

```bash
mkdir -p .claude/skills
cp -R english-prompt-buddy .claude/skills/
```

Claude Code에서는 `/english-prompt-buddy`로 직접 실행하거나, `hey buddy`처럼 skill 설명과 맞는 요청을 하면 자동으로 사용될 수 있습니다. Claude Code가 이미 실행 중이면 새 skill 폴더를 감지하지 못할 수 있으니, 처음 설치한 뒤에는 Claude Code를 다시 시작하는 것이 가장 확실합니다.

## 사용법

Buddy를 켜려면 이렇게 말하면 됩니다.

```text
hey buddy
```

그 다음부터는 같은 대화 안에서 영어 코칭이 가볍게 적용됩니다.

예시:

```text
이 함수 동작은 그대로 두고 더 깔끔하게 바꿔줘.
```

Buddy는 이런 식으로 도와줍니다.

```text
English Prompt Buddy
Natural prompt:
"Could you refactor this function to make it cleaner while keeping the behavior the same?"

Tiny note:
"While keeping the behavior the same" is useful for safe refactoring.

------------
Now I'll refactor it.
```

끄려면 이렇게 말하면 됩니다.

```text
goodbye buddy
```

이번 한 번만 영어 코칭을 건너뛰려면 이렇게 말하면 됩니다.

```text
skip buddy
```

특정 문장을 조금 더 자세히 배우고 싶으면 이렇게 말하면 됩니다.

```text
teach me this: Can you make this function more clean without change behavior?
```

## 파일 구조

```text
English-prompt-buddy/
├── README.md
├── LICENSE
└── english-prompt-buddy/
    ├── SKILL.md
    └── agents/
        └── openai.yaml
```

설치할 때는 `english-prompt-buddy/` 폴더 전체를 각 도구의 skills 폴더 아래에 넣으면 됩니다.

```text
english-prompt-buddy/
├── SKILL.md
└── agents/
    └── openai.yaml
```

`SKILL.md`는 skill의 실제 동작 지침입니다. `agents/openai.yaml`은 Codex UI에서 보일 이름과 설명을 담는 파일이고, Claude Code에서는 없어도 되지만 있어도 문제 없는 보조 metadata입니다.
