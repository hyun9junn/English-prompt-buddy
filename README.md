# English Prompt Buddy

영어 표현이 익숙하지 않은 한국어 사용자가 Codex, Claude Code 같은 AI 코딩 도구에 더 자연스러운 영어로 요청하도록 도와주고, 이를 통해 사용자가 자연스러운 영어 표현을 익힐 수 있게 돕는 Agent Skill입니다.

실제 작업 흐름을 방해하지 않도록 짧고 자연스러운 영어 프롬프트로 다듬고, 재사용하기 좋은 표현 하나만 알려준 뒤 원래 작업을 계속 진행하게 합니다.

## 토큰 사용이 걱정된다면

한국어 요청은 영어보다 토큰이 더 많이 사용되는 경우가 많습니다. 그래서 처음부터 영어로 요청하는 습관을 들이면, 장기적으로는 한글로 길게 설명하는 것보다 더 토큰 친화적인 작업 흐름을 만들 수 있습니다.

또한, English Prompt Buddy는 짧은 개선 프롬프트와 한 가지 표현 팁만 제공하도록 설계되어 있어 작업 흐름과 토큰 사용 부담을 최대한 줄입니다.

## 이런 사람에게 좋아요

- AI 코딩 도구를 영어로 쓰고 싶은데 표현이 자주 막히는 사람
- 한국어로 먼저 생각한 요청을 자연스러운 영어 작업 지시로 바꾸고 싶은 사람
- 문법 설명보다 바로 써먹는 개발 요청 표현을 배우고 싶은 사람
- Codex나 Claude에게 더 명확하고 안전한 영어 프롬프트를 주고 싶은 사람

## 설치: Claude Code

모든 프로젝트에서 쓸 수 있게 전역으로 설치하려면:

```bash
curl -fsSL https://raw.githubusercontent.com/hyun9junn/English-prompt-buddy/main/setup.sh | bash
```

현재 프로젝트에서만 쓰고 싶다면 프로젝트 루트에서:

```bash
curl -fsSL https://raw.githubusercontent.com/hyun9junn/English-prompt-buddy/main/setup.sh | bash -s -- --project
```

설치 후에는 Claude Code를 재시작해야 새 skill이 인식됩니다.

## 설치: Codex

Codex에서는 `$skill-installer`를 사용해 GitHub repo에서 설치할 수 있습니다.

Codex에 아래처럼 요청하세요.

```text
Use $skill-installer to install the skill from:
https://github.com/hyun9junn/English-prompt-buddy/tree/main/english-prompt-buddy
```

설치 후에는 Codex를 재시작해야 새 skill이 인식됩니다.

## 사용법

Claude Code에서는 `/english-prompt-buddy`로 직접 실행하거나, `hey buddy`처럼 skill 설명과 맞는 요청을 하면 자동으로 사용될 수 있습니다.

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

실제 skill 패키지는 아래 `english-prompt-buddy/` 폴더입니다.

```text
english-prompt-buddy/
├── SKILL.md
└── agents/
    └── openai.yaml
```
