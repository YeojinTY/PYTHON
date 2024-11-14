import mysql.connector

def main():
    # MySQL 연결 설정
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='eoe6536jj',
        database='taskdb'
    )
    cursor = conn.cursor()
    
    # SELECT: 고객 테이블에서 성이 '김'씨인 고객 정보 조회
    select_query = """
        SELECT 고객아이디, 고객이름, 나이, 등급, 적립금
        FROM 고객
        WHERE 고객이름 LIKE '김%'
    """
    cursor.execute(select_query)
    select_results = cursor.fetchall()
    print("SELECT 결과:")
    for row in select_results:
        print(row)
    
    # INSERT: 제품 테이블에 새 제품 정보 삽입
    insert_query = """
        INSERT INTO 제품 (제품번호, 제품명, 재고량, 단가, 제조업체)
        VALUES (%s, %s, %s, %s, %s)
    """
    insert_data = ('p08', '빼빼로', 5000, 1200, '롯데')
    cursor.execute(insert_query, insert_data)
    conn.commit()
    print("\nINSERT 결과:")
    print("새 제품 정보가 삽입되었습니다:", insert_data)
    
    # DELETE: 주문 테이블에서 주문 고객이 'pear'인 주문 내역 삭제
    delete_query = """
        DELETE FROM 주문
        WHERE 주문고객 = %s
    """
    delete_data = ('pear',)
    cursor.execute(delete_query, delete_data)
    conn.commit()
    print("\nDELETE 결과:")
    print("'pear' 고객의 주문 내역이 삭제되었습니다.")
    
    # 연결 종료
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
