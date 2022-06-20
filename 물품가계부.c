#include<stdio.h>

int i;

struct product {
	int barcode; //��ǰ ���ڵ� ������ ���� ����
	char name[100]; //��ǰ �̸� ���� �迭 ����(ũ�� 100)
	int count; //��ǰ ���� ������ ���� ����
}list[100] = { 0 };

void input() {
	printf("\n��ǰ ���ڵ� ��ȣ : ");
	scanf("%d", &list[i].barcode); //��ǰ ���ڵ� ��ȣ �Է�
	printf("��ǰ �̸� : ");
	scanf("%s", &list[i].name); //��ǰ �̸� �Է�
	printf("��ǰ ���� : ");
	scanf("%d", &list[i].count); //��ǰ ���� �Է�
	printf("\n");
	i++;
}

void show() {
	printf("\n��ǰ ���ڵ� ��ȣ	��ǰ �̸�	��ǰ ����\n");
	for (int j = 0; j < i ; j++) { //�ݺ��� ����(����� ��ǰ ���� ����� �� �ֵ��� �ݺ��� ��)
		printf("%16d %16s %15d\n", list[j].barcode, list[j].name, list[j].count);
	}
	printf("\n");
}

void sold() {
	int code, cnt;
	printf("\n�Ǹ��� ��ǰ ���ڵ� ��ȣ �Է� : ");
	scanf("%d", &code);
	printf("�Ǹ��� ��ǰ�� ���� �Է� : ");
	scanf("%d", &cnt);

	for (int j = 0; j < i; j++) {
		if (code == list[j].barcode) {
			if (cnt > list[j].count) {//if�� �ۼ�
				printf("��� �����մϴ�.\n\n");
			}
			else {
				list[j].count -= cnt; //���� ������ �ִ� ��ǰ �������� �Ǹ��� ��ǰ ���� ����
				printf("%d\t%s\t%d\n\n", list[j].barcode, list[j].name, list[j].count);
				break;
			}
		}
	}
}

int main() {
	int n;
	int* p = &n;
	while (1) {
		printf("1. ��ǰ �߰�\t2. ��ǰ �����ֱ�\t3. �Ǹ��� ��ǰ\t0. ����\n");
		scanf_s("%d", p);
		if (1 == *p) {
			input(); //��ǰ �߰� �Լ� ȣ��
		}
		else if (2 == *p) {
			show(); //��ǰ �����ֱ� �Լ� ȣ��
		}
		else if (3 == *p) {
			sold(); //�Ǹ��� ��ǰ �Լ� ȣ��
		}
		else if (0 == *p) {
		printf("���α׷� ����\n\n");
		break;
		}
		else {
		printf("��ȣ�� �����ϴ�. �ٽ� �Է��ϼ���.\n\n");
		}
	}
	return 0;
}