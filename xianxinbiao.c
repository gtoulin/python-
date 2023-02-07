int fch(char c){   //判断字符是否为字母字符 
	if((c>='a'&&c<='z')||(c>='A'&&c<='Z')){
		return 1;
	}
	else	return 0;
}
int fnum(char c){ //判断字符是否为数字字符 
	if(c>='0'&&c<='9'){
		return 1;
	}
	else	return 0;
}
void Sort_Letter(PSeqList R){
	int low=0;
	int high=R->length-1;
	int temp; 
	while(low<high){
		while((low<high)&&fch(R->data[low])){      //找到第一个非字母字符 
			low++;
		}
		while((low<high)&&!(fch(R->data[high]))){  //找到第一个字母字符 
			high--;
		}
		if(low<high){        //交换 
			temp=R->data[low];
			R->data[low]=R->data[high];
			R->data[high]=temp;
		}
	}  //while循环结束时，字母字符全在表的前面，（low之前全是字母字符） ，其他字符和数字字符全在表后 
	high=R->length-1;
	while(low<high){  //处理后面的数字字符和其他字符 
		while((low<high)&&fnum (R->data[low])){     //找到第一个非数字字符 
			low++;
		}
		while((low<high)&&!(fnum(R->data[high]))){  //找到第一个数字字符 
			high--;
		}
		if(low<high){    //交换 
			temp=R->data[low];
			R->data[low]=R->data[high];
			R->data[high]=temp;
		}
	}	 
}