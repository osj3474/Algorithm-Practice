-- -- 코드를 입력하세요
-- SELECT ID, NAME, (CASE
--                      WHEN CNT IS NULL
--                      THEN 0
--                      ELSE CNT
--                     END) AS "개수"
-- FROM
-- (SELECT LT.ID, LT.NAME, RT.CNT
-- FROM PLACES AS LT
-- LEFT JOIN
-- (SELECT PL.ID, COUNT(RW.COMMENTS) AS CNT FROM PLACES AS PL
-- JOIN PLACE_REVIEWS AS RW
-- ON PL.ID = RW.PLACE_ID
-- GROUP BY PL.ID) AS RT
-- ON LT.ID = RT.ID) AS FINAL
-- ORDER BY ID

SELECT P.ID as PLACE_ID, P.NAME as NAME, COUNT(PR.ID) as 개수
FROM PLACES as P
LEFT JOIN PLACE_REVIEWS as PR
ON P.ID = PR.PLACE_ID
GROUP BY P.ID
ORDER BY P.ID

