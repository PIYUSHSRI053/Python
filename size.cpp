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

void Total(Node* root,int cnt=0){
    if(root==NULL){
        return;
    }
    cnt++;
    Total(root->left,cnt);
    Total(root->right,cnt);
}

int total_node(Node* root){
    if(root==NULL) return 0;
    return(1+total_node(root->left)+total_node(root->right));
}

int main(){
    cout <<"Enter the root:";
    Node* root;
    root=Binary_tree();
    cout<<total_node(root);

}
