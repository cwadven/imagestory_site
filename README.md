## 이미지스토리 (IMAGESTORY)

이미지에 이야기를 남기고, 그 때의 기억을 회상 시킬 수 있는 서비스!

<p>
<img alt="imagestory" src=""/>
</p>

---

## 서비스 주소
**주소**
https://www.imagestory.shop/

**이미지스토리 서비스 설명 및 튜토리얼 :**<br>
https://www.imagestory.shop/tutorial/

## 개발자

**👤 이창우**

- Github : https://github.com/cwadven
- Backend : Django
- Service : SQLite, Pythonanywhere
- Server : Pythonanywhere 호스팅
- 기술스택 : Django, JQuery, Imagemapster

## 환경 구축

~~~
1. python -m venv myvenv (가상환경 생성)
2. python source myvenv/Script/activates (가상환경 실행)
3. pip install -r requirements.txt (의존성 모듈 설치)
4. python manage.py collectstatic (static 파일 생성)
5. python manage.py makemigrations account
6. python manage.py makemigrations category
7. python manage.py makemigrations board
8. python manage.py migrate (테이블 생성)
9. python manage.py createsuper (관리자 id 생성)
10. python manage.py runserver
~~~

## 기능

- 이미지에 영역을 남여 메모를 기록하기
- 협업을 통한 이미지 영역 추가