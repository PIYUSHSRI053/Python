#include<iostream>
#include<queue>
using namespace std;

class Node{
    public:
    int data;
    Node *left,*right;

    Node(int value){
        data=value;
        left=right-NULL;
    }
};

Node* BinaryTree(){
    int x;
    cin >> x;
    if(x==-1){
        return NULL;
    }

    Node* temp =new Node(x);
    cout << "Enter the left child " <<" " <<x <<":";
    temp->left = BinaryTree(); // left side create
    cout << "Enter the Right child " <<" " <<x<< ":";
    temp->right = BinaryTree();//right side create
    return temp;
}
int pathsum(Node* root ,int x){
    if(root==NULL) return 0;
    if(!root->left && !root->right){
        return root->data;
    }
    int a;
    a=(root->data+pathsum(root->left)+pathsum(root->right));
    if(x==a) {
        return 1;
    }
    else return 0 ;
}
int main(){
    int x;
    cin >> x;
    cout <<"Enter the root node";
    Node* root;
    root=BinaryTree();
     cout << pathsum(root,x);

}