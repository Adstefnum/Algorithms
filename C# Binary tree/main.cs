using System;
using System.Collections.Generic;

namespace BinaryTree{

class Program{

  
  static void Main(string [] args){
    Root binaryTree = new Root();
    Console.WriteLine("Binary Tree\n Enter space separated integer values");
    string input = Console.ReadLine();
     List<int> branches = new List<int>(Array.ConvertAll(input.Split(' '), int.Parse));

     for(int i=0;i<branches.Count;i++){
       binaryTree.Insert(branches[i]);
     }
      Console.WriteLine($"The depth is{binaryTree.Depth()}");

  }
  
  }


}