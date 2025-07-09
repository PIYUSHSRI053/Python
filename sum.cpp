#include<iostream>
#include<queue>
using namespace std;

class Node{
    public:
    int data;
    Node* left,*right;
    Node(int value){
        data=value;
        left=right=NULL;
    }
};

Node* Binary_tree(){
    int x;
    cin >> x;
    if(x==-1){
        return NULL;
    }
    Node* temp=new Node(x);
    cout << "Enter the left child" << x << ":";
    temp->left=Binary_tree();
    cout << "Enter the Right child" << x << ":";
    temp->right=Binary_tree();
}

int sum(Node* root,int &s){
    if(root==NULL) {
        return 0;
    }
    s=root->data;
    sum(root->left,s);
    sum(root->right,s);
}   

int total(Node* root) {
    if (root == NULL) {
        return 0;
    }
    return root->data + total(root->left) + total(root->right); // Return the total sum
}

int main (){
    cout << "Enter the root : " ;
    Node* root=Binary_tree();
    int s=total(root);
    cout << s;
}