# # SPARK Chat

## 1. Overall
 `SPARK Chat`은 SPARK의 첫 미니 프로젝트로써 구현된 간단한 채팅 서비스이다.  
웹페이지 구동은 Flask를 이용하였으며, 채팅 동작은 socket을 이용한 통신으로 구현하였다.
총 두 페이지로 구성되어 있으며 첫 페이지에서 유저가 개인의 id로써 사용될 user name을 입력하고, 개인의 icon으로 사용될 user icon을 10가지 캐릭터 중 선택해서 채팅방으로 입장한다. 채팅방으로 입장 시 채팅창에는 입장한 유저의 name, icon과 함께 새로운 유저가 입장했다는 메세지가 뜨고, 채팅 시 유저의 이름과 함께 유저가 입력한 메세지가 함께 올라간다. 채팅방의 오른쪽에는 현재 입장해있는 모든 유저들의 user name이 표시된다.
- - - -
## 2. Version Update Timeline
	- [2019.01.13] v0.0.1 감마버전(Local용) 완성
- - - -
## 3. Version Detail
#### 1) v0.0.1 감마버전(Local용) [2019.01.13]

- **index.html**  

	1. user name, user icon 선택시 변수로 저장
	2. user name은 input box에서 직접 입력, user icon은 dropdown toggle bar 로 선택
	3. `GO!` 버튼 클릭 시, user name과 user icon값을 저장한 채로 채팅 페이지로 이동



- **chat.html**  

	1. 새로운 유저 입장 시, user name, user icon과 함께 입장했다는 메세지 표시
	2. 오른쪽 `Current Users` 칸에 접속한 모든 유저의 user name 표시
	3. 대화 시 input box에 메세지 입력 후 `Send 버튼 클릭` or `Enter 키 입력` 시 메세지 전송
	4. 메세지가 많아져서 채팅창의 기본 크기를 넘어서는 경우 스크롤 생성, 내려서 확인 가능



- **::Todo List::**
	- 첫 페이지에서  `GO!` 버튼 위치, 디자인 개선
	- 채팅창 스크롤 생성시 자동으로 항상 맨 밑부분을 보여주도록 개선
	- 현재는 유저 입장 시 아이콘이 뜨지 않고 아이콘의 파일명만 뜨지만, 이미지가 뜰 수 있도록 개선
	- 현재 영어로만 채팅 가능, 한글도 가능하도록 개선
	- aws서버에 파일을 올려서 local뿐만아니라 공용서버에서 채팅 가능하도록 개선
	- chat.html에 SPARK로고 표시, 프론트엔드 쪽 디자인 개선
