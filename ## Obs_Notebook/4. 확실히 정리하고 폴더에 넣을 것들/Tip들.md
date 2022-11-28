1. 우클릭 컨텍스트 메뉴 전환
- cmd 관리자권한으로 실행 후, 복사하여 실행
  1) windows10 스타일
	reg.exe add "HKCU\Software\Classes\CLSID{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f /ve
	
  2) windows11 스타일
	reg.exe delete "HKCU\Software\Classes\CLSID{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}" /f

2. 윈도11 마우스 우클릭, 윈도10처럼 바꾸기
	https://onna.kr/616