#include "wordtree.h"


WordTree::WordTree()
{
	root = new TreeNode;
	root->value = " ";
	root->left = NULL;
	root->right = NULL;
	root->count = 0;
}

void WordTree::addWord(std::string wordToBeAdded)
{
	addWord(root, wordToBeAdded);
}

void WordTree::findWord(std::string wordToFind)
{
	TreeNode * temp = root;
	
	while(wordToFind != temp->value && temp->left != NULL && temp->right!= NULL)
	{
		if(wordToFind < temp->value)
		{
			temp = temp->left;
		}
		
		else if(wordToFind > temp->value)
		{
			temp = temp->right;
		}
	}
	
	if(temp->value==wordToFind)
	{
		std::cout << "The word '" << wordToFind << "' occurs " << temp->count << 
		" time(s) in the text.\n\n";
	}
	else 
		std::cout << "The word '" << wordToFind << "' was not found in the text.\n\n";
}

void WordTree::getCounts(int numberThreshold)
{
	int acc = 0;
	getCounts(root, numberThreshold, acc);
	std::cout << acc << " nodes had words with " << numberThreshold << 
	" or more occurrence(s).\n\n";
}

void WordTree::addWord(TreeNode *& root, std::string wordToBeAdded)
{
	if(root->value == " ")
	{
		root->value = wordToBeAdded;
		root->count++;
	}
	
	else if(wordToBeAdded < root->value)
	{
		if(root->left == NULL)
		{
			TreeNode * temp = new TreeNode;
			temp->count = 1;
			temp->left = NULL;
			temp->right = NULL;
			temp->value = wordToBeAdded;
			root->left = temp;
		}
		
		else
		{
			addWord(root->left, wordToBeAdded);
		}
		
	}
	
	
	else if(wordToBeAdded > root->value)
	{
		if(root->right == NULL)
		{
			TreeNode * temp = new TreeNode;
			temp->count = 1;
			temp->left = NULL;
			temp->right = NULL;
			temp->value = wordToBeAdded;
			root->right = temp;
		}
		
		else
		{
			addWord(root->right, wordToBeAdded);
		}
	}
	
	else if(root->value == wordToBeAdded)
	{
		root->count++;
	}
	
	
}

void WordTree::deleteSubTree(TreeNode* root)
{
	if(root->left!=NULL)
	{
		deleteSubTree(root->left);
	}
	
	if(root->right!=NULL)
	{
		deleteSubTree(root->right);
	}
	
	root->left = NULL;
	root->right = NULL;
	delete root;
}

void WordTree::getCounts(TreeNode* root, int threshold, int& acc) const
{
	
	
	if(root->left!= NULL)
	{
		getCounts(root->left, threshold, acc);
	}
	
	if(root->count >= threshold)
	{
		std::cout << root->value << "(" << root->count << ")\n";
		acc++;
	}
	
	if(root->right!=NULL)
	{
		getCounts(root->right, threshold, acc);
	}
	
	
}

WordTree::~WordTree()
{
	
	deleteSubTree(root);
}


