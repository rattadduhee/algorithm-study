-- truncate 함수를 활용한 가격대 나누기
-- truncate(1234.123, 1) = 1234.1
-- truncate(1234.123, -1) = 1230
-- 가격대 나눈 값에 따른 groupby

-- 코드를 입력하세요
SELECT TRUNCATE(PRICE, -4) AS PRICE_GROUP, COUNT(PRODUCT_ID) AS PRODUCTS
FROM PRODUCT
GROUP BY PRICE_GROUP
ORDER BY PRICE_GROUP