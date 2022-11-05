-- 프로그래머스 groupby 예제
-- date함수 활용- month

-- 코드를 입력하세요
SELECT MCDP_CD AS 진료과코드, COUNT(*) AS 5월예약건수
FROM APPOINTMENT
WHERE MONTH(APNT_YMD) = 5
GROUP BY 진료과코드
ORDER BY 5월예약건수, 진료과코드