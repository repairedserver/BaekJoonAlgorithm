#include <stdio.h>
#include <stdlib.h>
typedef struct {
	int age;
	int idx;
	char name[101];
}member;

int compare(const void* first, const void* second) {
	member* a = (member*)first;
	member* b = (member*)second;
	if (a->age < b->age)
		return -1;
	else if (a->age > b->age)
		return 1;
	else {
		if (a->idx < b->idx)
			return -1;
		else
			return 1;
	}
	return 0;
}
int main() {
	int i, n;
	member* list;
	scanf("%d", &n);
	list = (member*)malloc(n * sizeof(member));
	for (i = 0; i < n; i++) {
		scanf(" %d %s", &list[i].age, list[i].name);
		list[i].idx = i;
	}
	qsort(list, n, sizeof(list[0]), compare);
	for (i = 0; i < n; i++) {
		printf("%d %s\n", list[i].age, list[i].name);
	}
	return 0;
}