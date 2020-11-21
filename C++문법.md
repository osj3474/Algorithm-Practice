# 파이썬 -> C++ 

지금까지 알고리즘 풀이에 파이썬을 이용했으나, C++도 해볼까 해서..



```c++
#include <iostream>
#include<algorithm>
#include <queue>
#include<stack>
#include<map>
#include<vector>
```



모든 경우는 

```c++
using namespace std;
```

가 있다고 가정하고 예시를 적었습니다.



# ✅ 자료형

### 1.list

: c++에서는 **vector**가 이 역할을 대신한다.

#### [ vector ]

헤더파일은 다음과 같다.

```c++
#include <vector>
```



0. initialization & length

     ```c++
     vector<int> v;    // 벡터 1개
     vector<int> v(5); // 벡터 5개
     
     // length
     v.size();
     v.empty();
     v.assign(5,1);          // 1,1,1,1,1으로 초기화
     vector<vector<int> > v; // 2차원 벡터 생성
     ```

     

1. append

   ```c++
   v.push_back(value);
   v.emplace_back(value);  // 이것이 성능이 더 좋다고 합니다~
   ```

   

2. pop

   ```c++
   v.pop_back(value);
   v.erase(int idx);                    // 인덱스로 원소를 지운다. 
   v.erase(int start, int end);     // 해당하는 범위의 원소를 지운다. start는 포함하고, end는 포함하지 않는다. 
   ```

   

3. insert

   ```c++
   v.insert(int idx, value);    // idx에 value를 넣는다.
   ```

   

4. slice indexing

   ```c++
   // for문으로 해야하는가,,,
   ```

   

5. list concatenate

    ```c++
    v1.insert(v1.end(), v2.begin(), v2.end());  // v1벡터와 v2벡터가 합쳐짐.
    ```

    

6. swap

   ```c++
   v1.swap(v2)          // v1과 v2 swap
   ```

   

7. sort

   ```c++
   sort(v.begin(), v.end());                   // 오름차순 정렬
   sort(v.begin(), v.end(), greater<int>());   // 내림차순 정렬
   ```




8. 그 외

   ```c++
   v.at(int idx);       // idx 번째 원소
   v.front();           // 첫번째 원소
   v.back();            // 마지막 원소
   v.begin();           // 첫번째 원소 iterator
   v.end();             // 마지막 원소 다음⭐️ iterator
   
   vactor<int>::iterator iter;
   for(iter=v.begin(); iter!=v.end(); iter++) {
   	cout << *iter << endl;
   }
   ```





### 2. dictionary

: c++에서는 **unordered_map**이이 역할을 대신한다. 그 전에, **pair**에 대해서 알고 가자.

#### [ pair ]

 먼저 헤더는 utility이다.

```c++
#include <utility>
```



초기화 방법은,

```c++
pair<string, int> p1 = make_pair("one", 1);    
```

혹은, 변수 생성 없이 바로 인자로 넘겨주는 경우에는 다음처럼도 사용할 수 있다.

```c++
pair<string, int>("one", 1);
```

혹은, 복사를 할 수도 있다.

```c++
pair<string, int> p2(p1);
```



element **접근**은 다음과 같으며, **할당**도 가능하다.

```c++
p1.first    // 첫번째 element
p1.second   // 두번째 element
```



#### [ unordered_map ]

0. initialization & length

   ```c++
   #include <map>
   
   map<string, int> m;
   
   m.insert(pair<string, int>("one", 1));
   m.insert(make_pair("one", 1));
   m["one"] = 1;
   
   // length확인
   cout << m.size() << endl;
   ```

   

1. key로 value 찾기

   ```c++
   string key = "one";
   cout << m[key] << endl;
   ```

   혹은,

   ```c++
   map<string, int>::iterator it;
   it = m.find(key);
   cout << it->first << " " << it->second << endl;
   ```

   만약, 없는 key라면, value로 (에러 없이) 0을 반환. 

   

2. value로 key 찾기

   ```cpp
   // for문으로 밖에 없는강,,,
   ```

   

3. key에 value 삽입

   ```cpp
   map<string, int> m;
   m.insert(make_pair("one", 1));
   ```

   만약, 기존에 있는 key에 대해 insert를 할 시, 아무런 변화 없음.



4. key에 해당되는 원소 삭제

   ```c++
   m.erase(key)
   ```

   

5. map의 모든 원소 삭제

   ```c++
   m.clear()
   ```



6. value를 vector로 가지기

   ```c++
   map<string, vector<int> > m;
   vector<int> v;
   m.insert(pair<string, vector<int> >("one", v));
   ```





### 3. set vs unordered_set

0. **Use set when**

   - We need ordered data.

   - We would have to print/access the data (in sorted order).

   - We need predecessor/successor of elements.

   - ###### Since set is ordered, we can use functions like [binary_search(), lower_bound() and upper_bound()](https://www.geeksforgeeks.org/binary-search-functions-in-c-stl-binary_search-lower_bound-and-upper_bound/) on set elements. These functions cannot be used on unordered_set().

   **Use unordered_set when**

   - We need to keep a set of distinct elements and no ordering is required.
   - We need single element access i.e. no traversal.

1. initialization & length

   ```cpp
   #include <unordered_set>
   #include <set>
   
   // unordered_set
   unordered_set<std::string> first;                                // empty
   unordered_set<std::string> second ( {"red","green","blue"} );    // init list
   unordered_set<std::string> third ( {"orange","pink","yellow"} ); // init list
   unordered_set<std::string> fourth ( second );                    // copy
   
   // set
   set<int> s; 
   set<int> first;                           // empty set of ints
   int myints[]= {10,20,30,40,50};
   set<int> second (myints,myints+5);        // range
   ```

   

2. insert

   ```cpp
   s.insert(1);
   ```

3. erase & clear

   ```c++
   s.erase(1); // remove an element
   s.clear(); // remove all elements
   ```

4. insert

   ```cpp
   s.insert(1);
   ```

5. size(==length)

   ```cpp
   s.size();
   ```

6. empty

   ```
   s.empty();
   ```

7. max_size

   ```c++
   s.max_size(); // Returns the maximum number of elements that the set container can hold.
   while(s.max_size() > 1000) // example
   ```

8. find

   ```c++
   it=myset.find(20); //An iterator to the element, if val is found, or set::end otherwise.
   myset.erase (it);
   myset.erase (myset.find(40));
   ```

9. count

   ```c++
   myset.count(1); // 1 if the container contains an element equivalent to val, or zero otherwise.
   if (myset.count(i)!=0)
   ```

   

10. equal_range

    ```c++
    set.equal_range(x) : pair형 리턴
    set.eqaul_range(x).first : lower_bound(x)   // x이하이므로 x를 리턴
    set.eqaul_range(x).second : upper_bound(x) // x다음걸 리턴
    set<int> Set = { 1,3,5,7,9,11 };
    pair<set<int>::iterator, set<int>::iterator> Pair = Set.equal_range(3); 
    cout << *Pair.first << "  " << *Pair.second << endl;// output: 3, 5
    ```





### 4. stack

0. initialization & length

   ```cpp
   #include <stack>          // std::stack
   
   std::stack<int> first;                    // empty stack
   std::stack<int> second (mydeque);         // stack initialized to copy of dequ
   
   // 참고
   Queue: you can insert only in one end and remove from the other.
   Deque: you can insert and remove from both ends.
   Deque is short for "Double ended queue".
   ```

   

1. empty

   ```cpp
   mystack.empty();
   while (!mystack.empty())
   {
     sum += mystack.top();
     mystack.pop();
   }
   ```

   

2. push & pop

   ```
   myints.push(i);
   myints.pop();
   ```

```
   
3. size

```

   myints.size();

```
4. top

   ```c++
   mystack.top(); //Returns a reference to the top element in the stack.
```

   

### 5. queue

0. initialization & length

   ```cpp
   #include <deque>          // std::deque
   #include <queue>          // std::queue
   
   deque<int> mydeck (3,100);        // deque with 3 elements
   queue<int> first;                 // empty queue
   queue<int> second (mydeck);       // queue initialized to copy of deque
   ```

1. empty

   ```cpp
   mystack.empty();
   while (!mystack.empty())
   {
     sum += mystack.top();
     mystack.pop();
   }
   ```

   

2. push & pop

   ```
   myints.push(i);
   myints.pop();
   ```

3. size

   ```
   myints.size();
   ```

4. front

   ```c++
   myqueue.front(); // Returns a reference to the next element in the queue.
   ```

5. back

   ```c++
   myqueue.back(); // Returns a reference to the last element in the queue.
   ```





### 5. heap

**c++ reference**

0. code

    ```cpp
    // range heap example
    #include <iostream>     // std::cout
    #include <algorithm>    // std::make_heap, std::pop_heap, std::push_heap, std::sort_heap
    #include <vector>       // std::vector
    
    int main () {
      int myints[] = {10,20,30,5,15};
      std::vector<int> v(myints,myints+5);
    
      std::make_heap (v.begin(),v.end());
      std::cout << "initial max heap   : " << v.front() << '\n';
    
      std::pop_heap (v.begin(),v.end()); v.pop_back();
      std::cout << "max heap after pop : " << v.front() << '\n';
    
      v.push_back(99); std::push_heap (v.begin(),v.end());
      std::cout << "max heap after push: " << v.front() << '\n';
    
      std::sort_heap (v.begin(),v.end());
    
      std::cout << "final sorted range :";
      for (unsigned i=0; i<v.size(); i++)
        std::cout << ' ' << v[i];
    
      std::cout << '\n';
    
      return 0;
    }
    ```








# ✅ 추가 Tips

1. 네이밍 컨벤션







# ✅ 궁금한 점

0. 효율적인 입력 받기

   ```c++
   #include <iostream>
   
   // stdin
   cin >> i;
   cin >> a >> b >> c ;
   
   // stdout
   cout << " and its double is " << i*2 << ".\n"; // '\n' 또는 endl 쓰면 new line char의 역활
   
   // get a word (without space)
   string mystring;
   cin >> mystring; // always get a single word not a string since (빈칸을 기준으로 받기 때문)
   
   // get a line (with space)
   getline (cin, mystr);
   ```

1. 동적할당은 언제 하는가?

2. 정규표현식 사용 방법은?

   ```c++
   std::regex_match 를 이용해서 정규 표현식으로 전체 문자열 패턴 매칭하기.
   std::regex_search 를 이용해서 정규 표현식으로 문자열 검색하기
   std::regex_replace 를 이용해서 정규 표현식으로 문자열 치환하기
   
   #include <regex>
    
   // C++ 에서 정규 표현식을 사용하기 위해서는 먼저 위와 같이 정규 표현식 객체를 정의해야 합니다. 
   std::regex re("db-\\d*-log\\.txt");
   for (const auto &file_name : file_names) {
     // std::boolalpha 는 bool 을 0 과 1 대신에 false, true 로 표현하게 해줍니다.
     std::cout << file_name << ": " << std::boolalpha
       << std::regex_match(file_name, re) << '\n';
   }
   
   std::regex re("[01]{3}-(\\d{3,4})-\\d{4}"); // () 로 원하는 부분을 감싸게 된다면 해당 부분에 매칭된 문자열을 얻을 수 있게 됩니다.
   
   std::regex re("[01]{3}-(\\d{3,4})-\\d{4}");
   std::smatch match;  // 매칭된 결과를 string 으로 보관
   for (const auto &number : phone_numbers) {
     if (std::regex_match(number, match, re)) {
       for (size_t i = 0; i < match.size(); i++) {
         std::cout << "Match : " << match[i].str() << std::endl;
       }
       std::cout << "-----------------------\n";
     }
   }
   ```

3. 2진수, 16진수 표현 및 비트 연산하는 방법?

4. max, min, sort함수?

5. 나누기, 몫과 나머지?

6. global 변수 명시적 선언?

7. deep copy, shallow copy?

8. split을 대체할 무언가?

9. DFS & BFS

```c++
// DFS
#include <iostream>
#include <stack>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <queue>

using namespace std;


// stack에 들어가면 방문한거로 판단
// 해당 위치를 true로 해준다.
void dfs(int start, vector<int> graph[], bool check[]){

	stack<int> s;
	s.push(start);
	check[start] = true;
	printf("%d ",start);

	while(!s.empty()){

		int current_node = s.top();
		s.pop();
		for(int i=0; i<graph[current_node].size(); i++){

			int next_node = graph[current_node][i];

			if(check[next_node]==false){
				printf("%d ", next_node);
				check[next_node] = true;
				// pop()을 했었기 때문에 현재 current_node도 넣어줘야한다.
				s.push(current_node);
				s.push(next_node);
				break;
			}
		}
	}

}

// BFS
#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

void bfs(int start, vector<int> graph[], bool check[]){
	queue<int> q;

	q.push(start);
	check[start] = true;

	while(!q.empty()){
		int tmp = q.front();
		q.pop();
		printf("%d ",tmp);
		for(int i=0; i<graph[tmp].size(); i++){

			// 방문하지 않았다면
			if(check[graph[tmp][i]] == false){
				// 큐에 넣어주고 방문했음을 표시한다.
				q.push(graph[tmp][i]);
				check[graph[tmp][i]] = true;
			}
		}
	}

}
```

1. Combination

   ```c++
   #include <iostream>
   #include <algorithm>
   #include <vector>
   
   int main() {
      int n, r;
      std::cin >> n;
      std::cin >> r;
   
      std::vector<bool> v(n);
      std::fill(v.begin(), v.begin() + r, true);
   
      do {
          for (int i = 0; i < n; ++i) {
              if (v[i]) {
                  std::cout << (i + 1) << " ";
              }
          }
          std::cout << "\n";
      } while (std::prev_permutation(v.begin(), v.end()));
      return 0;
   }
   
   ```

2. Permutation

   ```c++
   // C++ program to display all permutations 
   // of an array using STL in C++ 
     
   #include <bits/stdc++.h> 
   using namespace std; 
     
   // Function to display the array 
   void display(int a[], int n) 
   { 
       for (int i = 0; i < n; i++) { 
           cout << a[i] << "  "; 
       } 
       cout << endl; 
   } 
     
   // Function to find the permutations 
   void findPermutations(int a[], int n) 
   { 
       // Sort the given array 
       sort(a, a + n); 
     
       // Find all possible permutations 
       cout << "Possible permutations are:\n"; 
       do { 
           display(a, n); 
       } while (next_permutation(a, a + n)); 
   } 
     
   // Driver code 
   int main() 
   { 
       int a[] = { 10, 20, 30, 40 }; 
       int n = sizeof(a) / sizeof(a[0]); 
       findPermutations(a, n); 
       return 0; 
   } 
   ```

   

