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

Node* BinaryTree(){
     int x;
     cin >> x;
    if(x==-1){
        return NULL;
    }
    Node* temp = new Node(x);
    cout << "Enter the left child" << x << ":";
    temp -> left = BinaryTree();
    cout << "Enter the Right child" << x << ":";
    temp -> right = BinaryTree();
}

bool toCheck(Node*root1 , Node*root2){
    if(!root1 && !root2) return 1;
    if((!root1&&root2)||(root1 && !root2)) return 0;
    if(root1->data != root2->data) return 0;
    return toCheck(root1->left,root2->left) &&toCheck(root1->right,root2->right);
}

int main(){
    cout << "Enter the Root for 1st tree: " ;
    Node* root1 =BinaryTree();
    cout << "Enter the Root for 2nd tree : " ;
    Node* root2 =BinaryTree();
    cout << toCheck(root1,root2);
}