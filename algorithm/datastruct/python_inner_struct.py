# 1. 리스트: 배열과 유사, 크기 가변적, 다양한 자료형 보관 가능
my_list = []
# 1-1 끝에 요소 추가
my_list.append(1)
# 1-2 다른 리스트나 iterable 객체를 붙임
my_list.extend([6,7])
# 1-3 특정 인덱스에 요소를 삽입
my_list.insert(1,'A')
# 1-4 첫 번째로 나오는 특정 요소를 제거
my_list.remove(1)
# 1-5 인덱스의 요소를 제거하고 반환. 인덱스를 지정하지 않으면 마지막 요소를 제거하고 반환
my_list.pop()
# 1-6 첫 번째로 나오는 요소의 인덱스를 반환
my_list.index(2)
# 1-7 리스트를 오름차순으로 정렬. reverse=True로 지정하면 내림차순으로 정렬
my_list.sort()
# 1-8 리스트에서 특정 요소의 개수를 반환
my_list.count(2)
# 1-9 리스트의 요소 순서를 뒤집음
my_list.reverse()
# 1-10 리스트의 얕은 복사본을 반환
new_list = my_list.copy()
# 1-11 모든 요소를 제거
my_list.clear()


# 2. 튜플: 한 번 생성하면 값을 변경할 수 없음
my_tuple = (3,5,4,5)
# 2-1 튜플에서 특정 요소의 개수를 반환
my_tuple.count(3)
# 2-2 특정 요소의 첫 번째 인덱스를 반환
my_tuple.index(3)

# 3. 딕셔너리: 키-값 쌍을 저장하는 해시 테이블 구조
my_dict = {}
# 3-1 키에 해당하는 값을 반환, 키가 없으면 default 반환
my_dict.get('key1', 'default_value')
# 3-2 딕셔너리의 모든 키를 반환
my_dict.keys()
# 3-3 딕셔너리의 모든 값을 반환
my_dict.values()
# 3-4 딕셔너리의 (키, 값) 쌍을 반환
my_dict.items()
# 3-5 다른 딕셔너리의 키-값 쌍을 추가하거나 덮어씀
my_dict.update({'key2': 'value2'})
# 3-6 특정 키를 제거하고 그 값을 반환. 키가 없으면 default 반환.
my_dict.pop('key1')
# 3-7 마지막 키-값 쌍을 제거하고 반환
my_dict.popitem()
# 3-8 모든 키-값 쌍을 제거
my_dict.clear()
# 3-9 딕셔너리의 얕은 복사본을 반환
new_dict = my_dict.copy()
# 3-10 키가 있으면 값을 반환하고, 없으면 키를 추가하고 기본값을 설정.
my_dict.setdefault('key3', 'default_value')

# 4. 셋: 중복되지 않는 값을 저장하는 집합 구조
my_set = {}
other_set ={}
# 4-1 셋에 요소를 추가
my_set.add(5)
# 4-2 셋에서 특정 요소를 제거, 요소가 없으면 오류 발생
my_set.remove(3)
# 4-3 셋에서 특정 요소를 제거, 요소가 없으면 아무 일도 일어나지 않음
my_set.discard(3)
# 4-4 셋에서 임의의 요소를 제거하고 반환
my_set.pop()
# 4-5 셋의 모든 요소를 제거
my_set.clear()
# 4-6 두 셋의 합집합을 반환
my_set.union(other_set)
# 4-7 두 셋의 교집합을 반환
my_set.intersection(other_set)
# 4-8 두 셋의 차집합을 반환
my_set.difference(other_set)
# 4-9 두 셋의 대칭 차집합을 반환
my_set.symmetric_difference(other_set)
# 4-10 셋이 다른 셋의 부분집합인지 확인
my_set.issubset(other_set)
# 4-11 셋이 다른 셋을 포함하는지 확인
my_set.issuperset(other_set)
# 4-12 셋의 복사본을 반환
new_set = my_set.copy()
