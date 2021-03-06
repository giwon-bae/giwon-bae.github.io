---
layout: single
title: "쿠키런:킹덤 - 게임분석1"
excerpt: "게임분석 연습 - 개요, 게임구성과 시스템"

categories:
  - Game
tags:
  - game
  - analysis
---

## **Part1. 개요, 게임구성과 시스템**

![image](https://user-images.githubusercontent.com/79121621/109123599-5ed45580-778d-11eb-895e-e49cd921e9cf.png)
### **1. 기본 정보**
이름 : 쿠키런 킹덤  
장르 : 소셜 RPG  
소개 : 데브시스터즈의 쿠키런 스핀오프 게임으로 건물 건설과 쿠키 성장의 두 가지 재미 요소를 느낄 수 있다.  

### **2. 게임 구성과 시스템**
#### **2.1. Basic flow chart**
![BasicFlowChart](https://user-images.githubusercontent.com/79121621/109597040-cc4fff80-7b5a-11eb-9446-0d786f6d61e7.PNG)

#### **2.2. 핵심 컨텐츠**
1 ) 마을  
• 건물 관리 : 마을에서 자원을 얻고 이를 이용하여 다시 건물을 짓는 컨텐츠  
• 소원나무 : 건물에서 획득한 자원을 소모하여 코인을 얻는 컨텐츠  
• 곰젤리 열기구 : 필드 탐험 모드에서 클리어한 월드에 쿠키들을 탐사 보내서 자원을 얻는 컨텐츠  
• 곰젤리 열차 : 건물에서 획득한 자원을 소모하여 희귀한 자원을 얻는 컨텐츠  

2 ) 게임 플레이  
• 필드 탐험 : 스테이지로 이루어져 있고 모든 몬스터를 제거하는 컨텐츠  
• 오늘의 현상수배 : 필드 탐험과 같은 방식으로 진행되지만 요일에 따라서 다른 보스와 보상이 나오는 컨텐츠  
• 킹덤 아레나 : PVP 모드. 상대를 선택해서 자동으로 대결하게 하는 컨텐츠  

#### **2.3. 모드 별 보상과 Motivation**
1 ) 마을
![게임 플레이 보상_로비](https://user-images.githubusercontent.com/79121621/109253530-5c2c3b80-7833-11eb-8372-fd35f54a17fe.PNG)
• 건물 관리 : 마을에서 사용되는 거의 모든 자원을 생산한다.  
• 소원나무 : 자원을 만드는데 드는 코인보다 더 많은 코인을 준다. (코인 수급의 주체) 또한 일일 보상으로 희귀 자원들도 획득 가능하다.  
• 곰젤리 열기구 : 토핑 수급의 주체가 되는 컨텐츠이다.  
• 곰젤리 열차 : 희귀 재료 수급의 주체가 되는 컨텐츠이다.  

2 ) 게임 플레이
![게임 플레이 보상](https://user-images.githubusercontent.com/79121621/109253528-5afb0e80-7833-11eb-9afd-8063ac94aee6.PNG)
• 필드 탐험 : 최초 한 번 별의 개수에 따라 크리스탈을 얻을 수 있다. 게임 초반 크리스탈 수급을 통해 쿠키를 얻는데 도움이 된다.  
• 오늘의 현상수배 : 사실상 파우더를 얻을 수 있는 주 컨텐츠이다.  
• 킹덤 아레나 : 승리의 메달을 이용하여 쿠키 영혼석, 뽑기권, 별사탕 등으로 교환 가능하다.  

#### **2.4. 게임 플레이 loop**
앞서 정리한 자료에 유저의 행동을 추가하여 표현하면 아래와 같은 loop로 표현할 수 있다.  
마을에서의 loop는 너무 얽혀있어 보기 복잡하고 게임 플레이에서의 loop와 유사하므로 따로 표기하지 않고 Simple game loop에서 간단하게 보여주겠다.  

1 ) Game Loop
![game_loop](https://user-images.githubusercontent.com/79121621/109597046-d07c1d00-7b5a-11eb-973f-a6fd5a20d603.PNG)
1) 필드 탐험을 통해 크리스탈을 수급하고 이를 이용해 쿠키와 보물을 뽑는다.  
2) 필드 탐험과 현상수배를 통해 쿠키 레벨업 및 스킬 강화, 토핑 강화를 해서 스펙업을 한다.  
3) 킹덤 아레나를 통해 승리의 메달을 얻고 다시 스펙업을 한다.  

2 ) Simple Game Loop
![simple_game_loop](https://user-images.githubusercontent.com/79121621/109602507-9105fe80-7b63-11eb-8722-d1933f90cc3f.PNG)

• 마을에서 얻는 보상은 스펙업에 사용되거나 다시 마을에 사용된다(건물 건설, 건물 레벨업 등)  

• 컨텐츠의 흐름은 PVE->PVP로 최종 컨텐츠는 킹덤 아레나에서 높은 랭킹을 기록하는 것이다. 
사실상 필드 탐험의 자원 획득 효율은 다른 컨텐츠에 비해 좋지 않은 편이어서 크리스탈 획득과 게임 스토리 진행만이 주목적이다.

### p.s. 자동 전투에 대한 생각
PVE(필드 탐험, 오늘의 현상수배)에서는 자동전투를 선택할 수 있고 PVP(킹덤 아레나)는 무조건 자동전투로 진행된다. 이 자동전투에 대해서 유사한 게임인 세븐나이츠와 비교하여 설명해보겠다.  
세븐나이츠 같은 경우 턴제로 스킬을 사용하고 각 캐릭터가 여러 개의 스킬을 가지고 있는 경우가 대부분이어서 모든 스킬이 콜타임이어서 스킬을 못 쓰는 경우는 잘 없다. (상대의 스킬쿨 증가 공격을 맞은 경우 제외)  
하지만 쿠키런 킹덤은 쿠키마다 하나씩의 스킬만 가지고 있고 턴제가 아니므로 자동전투를 돌리면 5초 만에 모든 스킬을 사용하고 스킬 쿨 동안 평타를 때리는 경우가 보인다.  
PVP에서는 상대도 자동전투로 진행되기에 크게 상관없지만 PVE에서는 자동전투가 그리 좋지 않다고 생각한다. 특히 스펙(전투력)이 비슷한 곳에서는 그게 더 크게 느껴진다.

이 포스트는 [참고 블로그](https://hiprock.tistory.com/169)를 참고하였습니다.  
이 포스트는 게임분석 공부를 위해 쓰여진 글이므로 오류나 오타에 대한 피드백은 언제든 환영입니다:)