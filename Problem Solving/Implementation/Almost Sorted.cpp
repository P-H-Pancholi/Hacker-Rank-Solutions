#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
	
	
	int n;
	int arr[100000];
	int sorted_arr[100000];
	
	scanf("%d", &n);
	
	for(int i=0; i<n; i++){
		scanf("%d",&arr[i]);
	}
	
	for(int i=0; i<n; i++){
		sorted_arr[i] = arr[i];
	}
	
	sort(sorted_arr,sorted_arr+n);
	
	//for(int i=0; i<n; i++){
		//printf("%d ",sorted_arr[i]);
	//}
	
	int cnt = 0;
	int first = 0;
	int last = 0;
	bool first_cmp = true;
	
	for(int i = 0; i<n; i++){
		if(arr[i] != sorted_arr[i] && first_cmp){
			cnt += 1;
			first = i+1;
			first_cmp = false;
		}
		else if(arr[i] != sorted_arr[i] && !first_cmp){
			cnt += 1;
			last = i+1;
		}
		else{
			continue;
		}
	}
	
	int sub_arr[last - first + 1];
	int sorted_sub_arr[last - first + 1];
	
	for(int i=0; i<last - first + 1; i++){
		sub_arr[i] = arr[i + first - 1];
		sorted_sub_arr[i] = sorted_arr[i + first - 1];
	}
	
	//sort(sub_arr,sub_arr + last - first + 1);
	
	//printf("\nSub array \n");
	
	//for(int i=0; i<last - first + 1; i++){
		//printf("%d ",sub_arr[i]);
	//}
	
	
	//printf("\nSorted Sub array\n");
	
	//for(int i=0; i<last - first + 1; i++){
		//printf("%d ",sorted_sub_arr[i]);
	//}
	
	bool reverse = false;
	
	for(int i = 0; i<last - first + 1; i++){
		if(sub_arr[last - i - 2] == sorted_sub_arr[i]){
			reverse = true;
		}
		else{
			reverse = false;
			break;
		}
	}
	
	
	
	if(cnt == 0){
		printf("yes");
	}
	else if(cnt == 2){
		printf("yes\n");
		printf("swap %d %d", first, last);
	}
	else{
		if(abs(first - last) + 1 == cnt && reverse){
			printf("yes\n");
			printf("reverse %d %d", first, last);
		}
		else{
			printf("no");
		}
	}
		
	return 0;
	
	
}
