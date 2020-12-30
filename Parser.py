from scanner import Scanner
import os

os.environ['PATH'] = os.environ['PATH']+';'+r"C:\\Program Files\\Graphviz\\bin"

import pygraphviz as pgv
class Parser():
	def __init__(self):
		self.Graph=pgv.AGraph()
		self.count=0
		self.scanner=Scanner()

	def addCode(self,tiny):
		self.tinyCode=tiny
	
	def ConnectHorizontal(self,firstNode,secondNode):
		self.Graph.subgraph(nbunch=[firstNode,secondNode],rank= 'same')
		self.Graph.add_edge(firstNode,secondNode)


	def stmt_seq(self):
		temp=self.statment()
		temp1 = temp
		token=self.scanner.getToken(self.tinyCode)
		while token[0]== "SEMICOLON":
			temp2 = self.statment()
			self.ConnectHorizontal(temp1,temp2)
			temp1 = temp2
			token=self.scanner.getToken(self.tinyCode)
			if(token==None):
				break
		self.scanner.tkpointer-=1
		return temp 





	def statment(self):
		token=self.scanner.getToken(self.tinyCode)

		if token[0] =="IF":
			t=self.if_stmt()
		elif token[0] =="Repeat":
			t=self.repeat()
		elif token[0] == "IDENTIFIER":
			t=self.assign(token[1])
		elif token[0] == "READ":
			t=self.read()
		elif token[0] == "WRITE":
			t=self.write()
		else:
			print("not a valid token")
			return 
		return t



	def if_stmt(self):
		self.Graph.add_node(self.count,label = 'if',shape='rectangle')
		parentnode= self.Graph.get_node(self.count)
		self.count +=1
		left=self.exp()
		self.Graph.subgraph(nbunch=[left],rank= 'same')
		token=self.scanner.getToken(self.tinyCode)
		if token[0]!="THEN":
			print("error333")
		right=self.stmt_seq()
		self.Graph.subgraph(nbunch=[left,right],rank= 'same')
		self.Graph.add_edge(left,right,color='white')
		self.Graph.add_edge(parentnode,left)
		self.Graph.add_edge(parentnode,right)
		token=self.scanner.getToken(self.tinyCode)
		if token[0]=="ELSE":
			elsechild = self.stmt_seq()
			self.Graph.add_edge(parentnode,elsechild)
			token=self.scanner.getToken(self.tinyCode)
			if token[0]!="END":
				print("error444")
		elif token[0]!="END":
			print("error555")
		return parentnode




	def repeat(self):
		self.Graph.add_node(self.count,label = "repeat",shape='rectangle' )
		parentnode = self.Graph.get_node(self.count)
		self.count+=1
		left = self.stmt_seq()
		token=self.scanner.getToken(self.tinyCode)
		if token[0]!="UNTIL":
			print("error666")
		right = self.exp()
		self.Graph.subgraph(nbunch=[right],rank = 'same')
		self.Graph.add_edge(parentnode,left)
		self.Graph.add_edge(parentnode,right)
		return parentnode

	def assign(self,token_value):
		self.Graph.add_node(self.count,label = "assign \\n"+ token_value,shape='rectangle' )
		parentnode = self.Graph.get_node(self.count)
		self.count+=1
		token = self.scanner.getToken(self.tinyCode)
		if token[0]!="ASSIGN":
			print("error777")
		right= self.exp()
		self.Graph.add_edge(parentnode,right)
		return parentnode
	def read(self):
		token=self.scanner.getToken(self.tinyCode)
		if token[0]!="IDENTIFIER":
			print("error88888888")
		self.Graph.add_node(self.count,label = 'read \\n'+token[1],shape='rectangle')
		parentnode = self.Graph.get_node(self.count)
		self.count+=1
		return parentnode
	def write(self):
		t = self.exp()
		self.Graph.add_node(self.count,label = "write",shape='rectangle')
		parentnode = self.Graph.get_node(self.count)
		self.count+=1
		self.Graph.add_edge(parentnode,t)
		return parentnode
	def exp(self):
		t1=self.simple_exp()
		token = self.scanner.getToken(self.tinyCode)
		if(token==None):
			return t1
		if token[0]=="LESSTHAN" or token[0]=="EQUAL" :
			self.Graph.add_node(self.count,label = token[1])
			parentnode = self.Graph.get_node(self.count)
			self.count+=1
			left = t1
			right = self.exp()
			self.Graph.add_edge(parentnode,left)
			self.Graph.add_edge(parentnode,right)
			return parentnode
		self.scanner.tkpointer -= 1
		return t1
	def simple_exp(self):
		t1=self.term()
		token= self.scanner.getToken(self.tinyCode)
		if(token==None):
			return t1
		while token[0]=="PLUS" or token[0]=="MINUS":
			self.Graph.add_node(self.count,label = token[1])
			parentnode = self.Graph.get_node(self.count)
			self.count+=1
			self.Graph.add_edge(parentnode,t1)
			self.Graph.add_edge(parentnode,self.term()) 
			t1 = parentnode
			token = self.scanner.getToken(self.tinyCode)
		self.scanner.tkpointer -= 1
		return t1

	def term(self):
		t1=self.factor()
		token= self.scanner.getToken(self.tinyCode)
		if(token==None):
			return t1
		while token[0]=="MULT" or token[0]=="DIV":
			self.Graph.add_node(self.count,label = token[1])
			parentnode = self.Graph.get_node(self.count)
			self.count+=1
			self.Graph.add_edge(parentnode,t1)
			self.Graph.add_edge(parentnode,self.factor()) 
			token = self.scanner.getToken(self.tinyCode)
			t1 = parentnode
		self.scanner.tkpointer-=1
		return t1

	def factor(self):
		token=self.scanner.getToken(self.tinyCode)
		if token[0]=="NUMBER":
			self.Graph.add_node(self.count,label = token[1])
			ret = self.Graph.get_node(self.count)
			self.count+=1
			return ret
		elif token[0] == "IDENTIFIER":
			self.Graph.add_node(self.count,label = token[1])
			ret = self.Graph.get_node(self.count)
			self.count+=1
			return ret
		elif token[0]=="OPENBRACKET":
			t1=self.exp()
			token = self.scanner.getToken(self.tinyCode)
			if token[0]!="CLOSEBRACKET":
				print("error101010")
			return t1
		else:
			print("error kokokokokoko")

