<h1 align="center">이미지스토리 (IMAGESTORY)[현재 사용중 인 실 서비스용은 PRIVATE화] 🖼<br></h1>

<h3>사이트 설명 :</h3>

이미지에 이야기를 남기고, 그 때의 기억을 회상 시킬 수 있는 서비스!

## 홈페이지
<p>
<img alt="imagestory" src="https://github.com/cwadven/imagestory_site/blob/master/asset/imagestory_page.png?raw=true"/>
</p>
<hr>

## 게시글 목록
<p>
<img alt="imagestory" src="https://github.com/cwadven/imagestory_site/blob/master/asset/imagestory_example2.png?raw=true"/>
</p>
<hr>

## 게시글 예제
<p>
<img alt="imagestory" src="https://github.com/cwadven/imagestory_site/blob/master/asset/imagestory_example1.png?raw=true"/>
</p>
<hr>

## 마이페이지
<p>
<img alt="imagestory" src="https://github.com/cwadven/imagestory_site/blob/master/asset/imagestory_example3.png?raw=true"/>
</p>
<hr>

## 데이터베이스 구조
<p>
<img alt="imagestory" src="https://github.com/cwadven/imagestory_site/blob/master/asset/db_schema.png?raw=true"/>
</p>

---

## 서비스 주소
**주소 :**<br>

- Raspberry Pi 4 서버 구축 : https://imstory.shop/


**이미지스토리 서비스 설명 및 튜토리얼 :**<br>

- https://imstory.shop/tutorial/

## 개발자

**👤 이창우**

- Github : https://github.com/cwadven
- Backend : Django
- Service : Mariadb(Mysql), Nginx, uwsgi
- Server : 
    - Pythonanywhere 호스팅 : <br>(2020-11-05 : Hacker/월 5천원.. DB Mysql할 경우 2만원 훌쩍 ㅠㅠ 그래서 SQLite로 유지중...)
    - Raspberry Pi 4 : Mariadb, Nginx, uwsgi (2021-01-08)
    - Pythonanywhere 호스팅 종료 : <br>(2021-02-15 : 비효율적이라고 판단)
- 기술스택 : Django, JQuery, Bootstrap, Imagemapster(오픈라이브러리 : http://www.outsharked.com/imagemapster/)
- 개발기간 : <br>
    - 2020년 6월 29일 ~ 2020 8월 9일 (필수 기능 완성 / 하루에 2시간 씩)
    - 2020년 8월 9일 ~ 지금 (필요에 따른 유지보수)

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
