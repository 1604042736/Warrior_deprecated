#include<iostream>
#include<string>
#include<vector>
#include<windows.h>
#include<cstdlib>
#include<ctime>
#include<cmath>
#include<fstream>
#include<sys/types.h>
#include<sys/stat.h>
#include<direct.h>
using namespace std;

#define THINGSLEN 6
#define SALELEN 28
#define BUYLEN 28
#define SPOILSLEN 28
#define CHANTLEN 15

struct Index
{
	int now;
	int max;
};

struct Things
{
	string name;
	int attack;
	int defense;
	string ench;
};

struct Bag
{
	string name;
	int num;
	int attack;
	int defense;
	string ench;
};

struct Sale
{
	string name;
	int money;
	int attack;
	int defense;
	string ench;
}sale[SALELEN]=
{
	{"Wooden sword",100,10,0,"nothing"},
	{"Iron sword",200,20,0,"nothing"},
	{"Golden sword",300,30,0,"nothing"},
	{"Bronze sword",400,40,0,"nothing"},
	{"Diamond sword",500,50,0,"nothing"},
	{"Leather Helmet",100,0,10,"nothing"},
	{"Leather Armor",100,0,13,"nothing"},
	{"Leather shinguard",100,0,16,"nothing"},
	{"Leather Boots",100,0,19,"nothing"},
	{"Iron helmet",200,0,20,"nothing"},
	{"Iron armor",200,0,23,"nothing"},
	{"Iron shinguard",200,0,26,"nothing"},
	{"Iron boots",200,0,29,"nothing"},
	{"Gold helmet",300,0,30,"nothing"},
	{"Gold armor",300,0,33,"nothing"},
	{"Gold shinguard",300,0,36,"nothing"},
	{"Golden boots",300,0,39,"nothing"},
	{"Bronze Helmet",400,0,40,"nothing"},
	{"Bronze armor",400,0,43,"nothing"},
	{"Bronze shinguard",400,0,46,"nothing"},
	{"Bronze boots",400,0,49,"nothing"},
	{"Diamond helmet",500,0,50,"nothing"},
	{"Diamond armor",500,0,53,"nothing"},
	{"Diamond Leggings",500,0,56,"nothing"},
	{"Diamond Boots",500,0,59,"nothing"},
	{"A rch",300,30,0,"nothing"},
	{"S hield",300,0,100,"nothing"},
	{"A rrow",1,0,0,"nothing"}
},buy[BUYLEN]=
{
	{"Wooden-sword",100,10,0,"nothing"},
	{"Iron-sword",200,20,0,"nothing"},
	{"Golden-sword",300,30,0,"nothing"},
	{"Bronze-sword",400,40,0,"nothing"},
	{"Diamond-sword",500,50,0,"nothing"},
	{"Leather-Helmet",100,0,10,"nothing"},
	{"Leather-Armor",100,0,13,"nothing"},
	{"Leather-shinguard",100,0,16,"nothing"},
	{"Leather-Boots",100,0,19,"nothing"},
	{"Iron-helmet",200,0,20,"nothing"},
	{"Iron-armor",200,0,23,"nothing"},
	{"Iron-shinguard",200,0,26,"nothing"},
	{"Iron-boots",200,0,29,"nothing"},
	{"Gold-helmet",300,0,30,"nothing"},
	{"Gold-armor",300,0,33,"nothing"},
	{"Gold-shinguard",300,0,36,"nothing"},
	{"Golden-boots",300,0,39,"nothing"},
	{"Bronze-Helmet",400,0,40,"nothing"},
	{"Bronze-armor",400,0,43,"nothing"},
	{"Bronze-shinguard",400,0,46,"nothing"},
	{"Bronze-boots",400,0,49,"nothing"},
	{"Diamond-helmet",500,0,50,"nothing"},
	{"Diamond-armor",500,0,53,"nothing"},
	{"Diamond-Leggings",500,0,56,"nothing"},
	{"Diamond-Boots",500,0,59,"nothing"},
	{"A-rch",300,30,0,"nothing"},
	{"S-hield",300,0,100,"nothing"},
	{"A-rrow",1,0,0,"nothing"}
},spoils[SPOILSLEN]=
{
	{"Wooden sword",100,10,0,"nothing"},
	{"Iron sword",200,20,0,"nothing"},
	{"Golden sword",300,30,0,"nothing"},
	{"Bronze sword",400,40,0,"nothing"},
	{"Diamond sword",500,50,0,"nothing"},
	{"Leather Helmet",100,0,10,"nothing"},
	{"Leather Armor",100,0,13,"nothing"},
	{"Leather shinguard",100,0,16,"nothing"},
	{"Leather Boots",100,0,19,"nothing"},
	{"Iron helmet",200,0,20,"nothing"},
	{"Iron armor",200,0,23,"nothing"},
	{"Iron shinguard",200,0,26,"nothing"},
	{"Iron boots",200,0,29,"nothing"},
	{"Gold helmet",300,0,30,"nothing"},
	{"Gold armor",300,0,33,"nothing"},
	{"Gold shinguard",300,0,36,"nothing"},
	{"Golden boots",300,0,39,"nothing"},
	{"Bronze Helmet",400,0,40,"nothing"},
	{"Bronze armor",400,0,43,"nothing"},
	{"Bronze shinguard",400,0,46,"nothing"},
	{"Bronze boots",400,0,49,"nothing"},
	{"Diamond helmet",500,0,50,"nothing"},
	{"Diamond armor",500,0,53,"nothing"},
	{"Diamond Leggings",500,0,56,"nothing"},
	{"Diamond Boots",500,0,59,"nothing"},
	{"Arch",300,30,0,"nothing"},
	{"Shield",300,0,100,"nothing"},
	{"Arrow",1,0,0,"nothing"}
},chant[CHANTLEN]=
{
	{"Damage increased(1)",100,10,0},
	{"Damage increased(2)",120,30,0},
	{"Damage increased(3)",140,50,0},
	{"Damage increased(4)",160,70,0},
	{"Damage increased(5)",180,90,0},
	{"Increased defense(1)",100,0,10},
	{"Increased defense(2)",120,0,30},
	{"Increased defense(3)",140,0,50},
	{"Increased defense(4)",160,0,70},
	{"Increased defense(5)",180,0,90},
	{"Comprehensive improvement(1)",1000,20,20},
	{"Comprehensive improvement(2)",2000,40,40},
	{"Comprehensive improvement(3)",3000,60,60},
	{"Comprehensive improvement(4)",4000,80,80},
	{"Comprehensive improvement(5)",5000,100,100} 
};

FILE* file;

struct Player
{
	string playername;
	int money;
	int lvl;
	Index heart;
	Index defense;
	Index attack;
	Things things[THINGSLEN];
	int thing;
	vector<Bag> bag;
}player;

bool ClearSpaces(string s)
{
	for(int i=0;i<s.length();i++)
	{
		if(s[i]!='\t'&&s[i]!=' ')
		{
			return true;
		}
	}
	return false;
}

int clrscr() 
{ 
  	HANDLE hndl = GetStdHandle(STD_OUTPUT_HANDLE); 
  	CONSOLE_SCREEN_BUFFER_INFO csbi; 
  	GetConsoleScreenBufferInfo(hndl, &csbi); 
  	DWORD written; 
  	DWORD N = csbi.dwSize.X * csbi.dwCursorPosition.Y + csbi.dwCursorPosition.X + 1; 
  	COORD curhome = {0,0}; 
	
	FillConsoleOutputCharacter(hndl, ' ', N, curhome, &written); 
	csbi.srWindow.Bottom -= csbi.srWindow.Top; 
  	csbi.srWindow.Top = 0; 
  	SetConsoleWindowInfo(hndl, TRUE, &csbi.srWindow); 
  	SetConsoleCursorPosition(hndl, curhome); 

  	return 0;
}

string getTrue(string s)
{
	string str;
	for(int i=0;i<s.length();i++)
	{
		if(s[i]!=' ')
		{
			str+=s[i];
		}
		else
		{
			str+="-";
		}
	}
	return str;
}

void ColorChoose(int color)
{
    switch(color)
    {
        case 1:	//sky blue
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),FOREGROUND_INTENSITY|FOREGROUND_GREEN|FOREGROUND_BLUE);
            break;
        case 2:	//green
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),FOREGROUND_INTENSITY|FOREGROUND_GREEN);    
            break;
        case 3:	//yellow
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),FOREGROUND_INTENSITY|FOREGROUND_RED|FOREGROUND_GREEN);
            break;
        case 4:	//red
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),FOREGROUND_INTENSITY|FOREGROUND_RED);
            break;
        case 5:	//purple
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),FOREGROUND_INTENSITY|FOREGROUND_RED|FOREGROUND_BLUE);
            break;
        case 6:	//white
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),FOREGROUND_INTENSITY|FOREGROUND_RED|FOREGROUND_BLUE|FOREGROUND_GREEN);
            break;
        case 7:	//dark blue
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),FOREGROUND_INTENSITY|FOREGROUND_BLUE);
            break;
    }
}

string input(string s)
{
	cout<<s;
	string str;
	getline(cin,str);
	return str;
}

int random(int a,int b)
{
	return a + (int)b * rand() / (RAND_MAX + 1);
}

int getEnch(string s)
{
	for(int i=0;i<CHANTLEN;i++)
	{
		if(s==chant[i].name)
		{
			return i;
		}
	}
	return -1;
}

class Equip
{
public:
	void help()
	{
		ColorChoose(5);
		cout<<"help\tOutput this list\n";
		cout<<"return\tReturn\n";
		cout<<"Please input the equipment directly\n";
		cout<<"Note: when equipping things, the middle of the items is a space. When unloading, you need to change the space to '-'\n";
		ColorChoose(6);
	}
	
	bool get(string s)
	{
		for(int i=0;i<player.bag.size();i++)
		{
			if(s==player.bag[i].name)
			{
				ColorChoose(3);
				if(player.thing<THINGSLEN)
				{
					player.things[player.thing].name=player.bag[i].name;
					player.things[player.thing].attack=player.bag[i].attack;
					player.things[player.thing].defense=player.bag[i].defense;
					player.things[player.thing].ench=player.bag[i].ench;
					player.thing++;
					player.bag[i].num--;
					int a=getEnch(player.bag[i].ench);
					if(a!=-1)
					{
						player.defense.now+=(player.bag[i].defense+chant[a].defense);
						player.attack.now+=(player.bag[i].attack+chant[a].attack);
					}
					else
					{
						player.defense.now+=(player.bag[i].defense);
						player.attack.now+=(player.bag[i].attack);
					}
					if(player.bag[i].num==0)
					{
						player.bag.erase(player.bag.begin()+i);
					}
					cout<<"Equipped with "<<s<<endl;
				}
				else
				{
					cout<<"Gear bar full\n";
				}
				ColorChoose(6);
				return false;
			}
		}
		for(int i=0;i<THINGSLEN;i++)
		{
			if(s==getTrue(player.things[i].name))
			{
				ColorChoose(3);
				bool b=true;
				player.thing--;
				for(int j=0;j<player.bag.size();j++)
				{
					if(player.bag[j].name==player.things[player.thing].name)
					{
						int a=getEnch(player.bag[j].ench);
						player.bag[j].num++;
						if(a!=-1)
						{
							player.defense.now-=(player.bag[j].defense+chant[a].defense);
							player.attack.now-=(player.bag[j].attack+chant[a].attack);
						}
						else
						{
							player.defense.now-=(player.bag[j].defense);
							player.attack.now-=(player.bag[j].attack);
						}
						player.things[player.thing].name=player.things[player.thing].ench="nothing";
						player.things[player.thing].attack=player.things[player.thing].defense=0;
						b=false;
						cout<<"Unloading completed\n";
						break;
					}
				}
				if(b)
				{
					Bag bag;
					bag.name=player.things[player.thing].name;
					bag.num=1;
					bag.attack=player.things[player.thing].attack;
					bag.defense=player.things[player.thing].defense;
					bag.ench=player.things[player.thing].ench;
					player.bag.push_back(bag);
					player.attack.now-=player.things[player.thing].attack;
					player.defense.now-=player.things[player.thing].defense;
					player.things[player.thing].name=player.things[player.thing].ench="nothing";
					player.things[player.thing].attack=player.things[player.thing].defense=0;
					cout<<"Unloading completed\n";
				}
				ColorChoose(6);
				return false;
			}
		}
		return true;
	}
	
	bool docommand(string s)
	{
		if(s=="return")
		{
			return false;
		}
		else if(s=="cls")
		{
			clrscr();
		}
		else if(s=="help")
		{
			help();
		}
		else if(get(s)&&ClearSpaces(s))
		{
			ColorChoose(4);
			cout<<"There is no definition for "<<"'"<<s<<"', Please type help for help\n";
			ColorChoose(6);
		}
		return true;
	}
	
	void play()
	{
		bool bl=true;
		while(bl)
		{
			string s=input("Equip> ");
			bl=docommand(s);
		}
	}
};

class Shop
{
public:
	void help()
	{
		ColorChoose(5);
		cout<<"cls\tClear screen\n";
		cout<<"help\tOutput this list\n";
		cout<<"list\tShow product list\n";
		cout<<"return\tReturn\n";
		cout<<"Please input the item name directly when shopping\n";
		cout<<"Note: there is a space in the middle of the item when shopping. You need to change the space to '-' when shopping\n";
		ColorChoose(6);
	}
	
	void list()
	{
		ColorChoose(7);
		cout<<"\nSell:\n";
		for(int i=0;i<SALELEN;i++)
		{
			cout<<"Name: "<<sale[i].name;
			cout<<"\tMoney: "<<sale[i].money;
			cout<<"\tAttack: "<<sale[i].attack;
			cout<<"\tDefense: "<<sale[i].defense;
			cout<<"\tEnchant: "<<sale[i].ench<<endl;
		}
		cout<<"\nRecovery:\n";
		for(int i=0;i<BUYLEN;i++)
		{
			cout<<"Name: "<<buy[i].name;
			cout<<"\tMoney: "<<buy[i].money;
			cout<<"\tAttack: "<<buy[i].attack;
			cout<<"\tDefense: "<<buy[i].defense;
			cout<<"\tEnchant: "<<buy[i].ench<<endl;
		}
		cout<<endl;
		ColorChoose(6);
	}
	
	bool get(string s)
	{
		for(int i=0;i<SALELEN;i++)
		{
			if(sale[i].name==s)
			{
				ColorChoose(3);
				if(sale[i].money<=player.money)
				{
					bool b=true;
					player.money-=sale[i].money;
					for(int j=0;j<player.bag.size();i++)
					{
						if(s==player.bag[i].name)
						{
							b=false;
							player.bag[i].num+=1;
							break;
						}
					}
					if(b)
					{
						Bag bag;
						bag.name=sale[i].name;
						bag.num=1;
						bag.attack=sale[i].attack;
						bag.defense=sale[i].defense;
						bag.ench=sale[i].ench;
						player.bag.push_back(bag);
					}
					cout<<"You have bought "<<s<<endl;
				}
				else
				{
					cout<<"You can't buy a "<<s<<" because you don't have enough money\n";
				}
				ColorChoose(6);
				return false;
			}
		}
		for(int i=0;i<BUYLEN;i++)
		{
			if(buy[i].name==s)
			{
				ColorChoose(3);
				bool b=true;
				for(int i=0;i<player.bag.size();i++)
				{
					if(s==getTrue(player.bag[i].name))
					{
						b=false;
						player.money+=buy[i].money;
						player.bag[i].num-=1;
						if(player.bag[i].num==0)
						{
							player.bag.erase(player.bag.begin()+i);
						}
						cout<<"Successful sale of "<<s<<endl;
						break;
					}
				}
				if(b)
				{
					cout<<"Can't find the "<<s<<endl;
				}
				ColorChoose(6);
				return false;
			}
		}
		return true;
	}
	
	bool docommand(string s)
	{
		if(s=="return")
		{
			return false;
		}
		else if(s=="cls")
		{
			clrscr();
		}
		else if(s=="help")
		{
			help();
		}
		else if(s=="list")
		{
			list();
		}
		else if(get(s)&&ClearSpaces(s))
		{
			ColorChoose(4);
			cout<<"There is no definition for "<<"'"<<s<<"', Please type help for help\n";
			ColorChoose(6);
		}
		return true;
	}
	
	void play()
	{
		bool bl=true;
		while(bl)
		{
			string s=input("Shop> ");
			bl=docommand(s);
		}
	}
};

class Attack
{
private:
	struct Enemy
	{
		int lvl;
		Index heart;
		Index defense;
		Index attack; 
	}enemy;
	
public:
	Attack()
	{
		enemy.lvl=player.lvl;
		enemy.heart.now=enemy.heart.max=enemy.attack.max=enemy.defense.max=100;
		enemy.attack.now=enemy.defense.now=random(0,(player.attack.now+player.defense.now)/2);
	}
	
	void help()
	{
		ColorChoose(5);
		cout<<"attack\tAttack\n";
		cout<<"blood\tBlood return\n";
		cout<<"help\tOutput this list\n";
		cout<<"return\tReturn\n";
		cout<<"state\tShow you and the enemy\n";
		ColorChoose(6);
	}
	
	bool attack()
	{
		ColorChoose(3);
		cout<<"You attacked the enemy\n";
		ColorChoose(6);
		enemy.heart.now-=(abs(player.attack.now-enemy.defense.now));
		bool b=true;
		for(int i=0;i<THINGSLEN;i++)
		{
			if(player.things[i].name=="Arch")
			{
				if(random(0,player.lvl))
				{
					
					for(int j=0;j<player.bag.size();j++)
					{
						if(player.bag[i].name=="Arrow")
						{
							b=false;
							player.bag[i].num--;
							if(player.bag[i].num==0)
							{
								player.bag.erase(player.bag.begin()+i);
							}
							if(random(0,player.lvl/2))
							{
								ColorChoose(3);
								cout<<"The enemy attacked you\n";
								ColorChoose(6);
								player.heart.now-=(abs(enemy.attack.now-player.defense.now));
								if(player.heart.now<=0)
								{
									ColorChoose(3);
									cout<<"Your fail!\n";
									ColorChoose(6);
									return false;
								}
							}
							break;
						}
					}
				}
				break;
			}
		}
		if(enemy.heart.now<=0)
		{
			ColorChoose(3);
			cout<<"Your win!\n";
			ColorChoose(6);
			player.money+=random(0,100);
			int a;
			a=random(0,player.lvl/10);
			for(int i=0;i<SPOILSLEN;i++)
			{
				if(i==a)
				{
					bool b=true;
					for(int j=0;j<player.bag.size();j++)
					{
						if(player.bag[j].name==spoils[i].name)
						{
							b=false;
							player.bag[j].num++;
							break;
						}
					}
					if(b)
					{
						Bag bag;
						bag.name=spoils[i].name;
						bag.num=1;
						bag.attack=spoils[i].attack;
						bag.defense=spoils[i].defense;
						bag.ench=spoils[i].ench;
						player.bag.push_back(bag);
					}
					break;
				} 
			}
			player.lvl+=1;
			return false;
		}
		if(b)
		{
			ColorChoose(3);
			cout<<"The enemy attacked you\n";
			ColorChoose(6);
			player.heart.now-=(abs(enemy.attack.now-player.defense.now));
			if(player.heart.now<=0)
			{
				ColorChoose(3);
				cout<<"Your fail!\n";
				ColorChoose(6);
				return false;
			}
		}
		return true;
	}
	
	void blood()
	{
		if(player.money>=player.lvl)
		{
			ColorChoose(3);
			cout<<"Successfully recovered blood\n";
			ColorChoose(6);
			player.heart.now+=player.lvl;
			player.money-=player.lvl;
		}
		else
		{
			ColorChoose(3);
			cout<<"You can't get your blood back, because there's not enough money\n";
			ColorChoose(6);
		}
		if(random(0,player.lvl))
		{
			ColorChoose(3);
			cout<<"The enemy's back\n";
			ColorChoose(6);
			enemy.heart.now+=enemy.lvl;
		}
	}
	
	void state()
	{
		ColorChoose(1);
		cout<<"\nYours\n";
		cout<<"Lvl: "<<player.lvl<<endl;
		cout<<"Heart: "<<player.heart.now<<"/"<<player.heart.max<<endl;
		cout<<"Defense: "<<player.defense.now<<"/"<<player.defense.max<<endl;
		cout<<"Attack: "<<player.attack.now<<"/"<<player.attack.max<<endl;
		cout<<"\nEnemy\n";
		cout<<"Lvl: "<<enemy.lvl<<endl;
		cout<<"Heart: "<<enemy.heart.now<<"/"<<enemy.heart.max<<endl;
		cout<<"Defense: "<<enemy.defense.now<<"/"<<enemy.defense.max<<endl;
		cout<<"Attack: "<<enemy.attack.now<<"/"<<enemy.attack.max<<endl;
		cout<<endl;
		ColorChoose(6);
	}
	
	bool docommand(string s)
	{
		if(s=="return")
		{
			return false;
		}
		else if(s=="attack")
		{
			return attack();
		}
		else if(s=="blood")
		{
			blood();
		}
		else if(s=="cls")
		{
			clrscr();
		}
		else if(s=="help")
		{
			help();
		}
		else if(s=="state")
		{
			state();
		}
		else if(ClearSpaces(s))
		{
			ColorChoose(4);
			cout<<"There is no definition for "<<"'"<<s<<"', Please type help for help\n";
			ColorChoose(6);
		}
		return true;
	}
	
	void play()
	{
		bool bl=true;
		while(bl)
		{
			string s=input("Attack> ");
			bl=docommand(s);
		}
	}
};

class Place
{
public:
	void help()
	{
		ColorChoose(5);
		cout<<"attack\tAttack something\n";
		cout<<"help\tOutput this list\n";
		cout<<"return\tReturn\n";
		cout<<"search\tSearch for supplies\n";
		ColorChoose(6);
	}
	
	void search()
	{
		ColorChoose(3);
		cout<<"Searching...";
		ColorChoose(6);
		if(random(0,player.lvl))
		{
			ColorChoose(3);
			cout<<"You met an enemy in the search\n";
			ColorChoose(6);
			Attack attack;
			attack.play();
		}
		else
		{
			ColorChoose(3);
			Sleep(random(0,100)*10);
			cout<<"\nSearch complete\n";
			player.money+=random(0,100);
			ColorChoose(6);
		}
	}
	
	bool docommand(string s)
	{
		if(s=="return")
		{
			return false;
		}
		else if(s=="attack")
		{
			Attack attack;
			attack.play();
		}
		else if(s=="cls")
		{
			clrscr();
		}
		else if(s=="help")
		{
			help();
		}
		else if(s=="search")
		{
			search();
		}
		else if(ClearSpaces(s))
		{
			ColorChoose(4);
			cout<<"There is no definition for "<<"'"<<s<<"', Please type help for help\n";
			ColorChoose(6);
		}
		return true;
	}
	
	void play()
	{
		bool bl=true;
		while(bl)
		{
			string s=input("Place> ");
			bl=docommand(s);
		}
	}
};

class Enchant
{
public:
	void help()
	{
		ColorChoose(5);
		cout<<"help\tOutput this list\n";
		cout<<"list\tOutput enchant list\n";
		cout<<"return\tReturn\n";
		cout<<"Please input \"name+enchant name\" directly for Enchant\n";
		ColorChoose(6);
	}
	
	void list()
	{
		ColorChoose(7);
		for(int i=0;i<CHANTLEN;i++)
		{
			cout<<"Name: "<<chant[i].name;
			cout<<"\tMoney: "<<chant[i].money;
			cout<<"\tAttack: "<<chant[i].attack;
			cout<<"\tDefense: "<<chant[i].defense<<endl;
		}
		ColorChoose(6);
	}
	
	string get_one(string s)
	{
		string str;
		for(int i=0;i<s.length();i++)
		{
			if(s[i]!='+')
			{
				str+=s[i];
			}
			else
			  break;
		}
		return str;
	}
	
	string get_two(string s)
	{
		string str;
		for(int i=0;i<s.length();i++)
		{
			if(s[i]=='+')
			{
				str="";
			}
			else
			  str+=s[i];
		}
		return str;
	}
	
	bool get(string s)
	{
		string one=get_one(s);
		string two=get_two(s);
		int a=getEnch(two);
		if(a!=-1)
		{
			if(player.money>=chant[a].money)
			{
				bool b=true;
				for(int i=0;i<player.bag.size();i++)
				{
					if(player.bag[i].name==one)
					{
						b=false;
						player.money-=chant[a].money;
						player.bag[i].ench=two;
						break;
					}
				}
				if(b)
				{
					ColorChoose(3);
					cout<<"Can't find the "<<one<<endl;
					ColorChoose(6);
				}
				else
				{
					ColorChoose(3);
					cout<<"Enchanted '"<<two<<"'\n";
					ColorChoose(6);
				}
				return false;
			}
			else
			{
				ColorChoose(3);
				cout<<"You don't have enough money!\n";
				ColorChoose(6);
				return false;
			}
		}
		else
		{
			ColorChoose(3);
			cout<<"Can't find the "<<two<<endl;
			ColorChoose(6);
			return false;
		}
		return true;
	}
	
	bool docommand(string s)
	{
		if(s=="return")
		{
			return false;
		}
		else if(s=="cls")
		{
			clrscr();
		}
		else if(s=="list")
		{
			list();
		}
		else if(s=="help")
		{
			help();
		}
		else if(ClearSpaces(s)&&get(s))
		{
			ColorChoose(4);
			cout<<"There is no definition for "<<"'"<<s<<"', Please type help for help\n";
			ColorChoose(6);
		}
		return true;
	}
	
	void play()
	{
		bool bl=true;
		while(bl)
		{
			string s=input("Enchant> ");
			bl=docommand(s);
		}
	}
};

class Main
{
public:
	void help()
	{
		ColorChoose(5);
		cout<<"blood\tBlood return\n";
		cout<<"cls\tClear screen\n";
		cout<<"enchant\tEnchant items\n";
		cout<<"equip\tEquip some items\n";
		cout<<"exit\tExit\n";
		cout<<"help\tOutputs this list\n";
		cout<<"place\tGo to some places\n";
		cout<<"shop\tEnter the store\n";
		cout<<"state\tState\n";
		ColorChoose(6);
	}
	
	void blood()
	{
		if(player.money>=player.lvl)
		{
			ColorChoose(3);
			cout<<"Successfully recovered blood\n";
			ColorChoose(6);
			player.heart.now+=player.lvl;
			player.money-=player.lvl;
		}
		else
		{
			ColorChoose(3);
			cout<<"You can't get your blood back, because there's not enough money\n";
			ColorChoose(6);
		}
	}
	
	void state()
	{
		ColorChoose(1);
		cout<<"\nPlayer name: "<<player.playername<<endl;
		cout<<"\nMoney: "<<player.money<<endl;
		cout<<"Lvl: "<<player.lvl<<endl;
		cout<<"Heart: "<<player.heart.now<<"/"<<player.heart.max<<endl;
		cout<<"Defense: "<<player.defense.now<<"/"<<player.defense.max<<endl;
		cout<<"Attack: "<<player.attack.now<<"/"<<player.attack.max<<endl;
		
		cout<<"\nThings:\n";
		for(int i=0;i<THINGSLEN;i++)
		{
			cout<<"Name: "<<player.things[i].name;
			cout<<"\tAttack: "<<player.things[i].attack;
			cout<<"\tDefense: "<<player.things[i].defense;
			cout<<"\tEnchant: "<<player.things[i].ench<<endl;
		}
		
		cout<<"\nBag:\n";
		for(int i=0;i<player.bag.size();i++)
		{
			cout<<"Name: "<<player.bag[i].name;
			cout<<"\tNum: "<<player.bag[i].num;
			cout<<"\tAttack: "<<player.bag[i].attack;
			cout<<"\tDefense: "<<player.bag[i].defense;
			cout<<"\tEnchant: "<<player.bag[i].ench<<endl;
		}
		cout<<endl;
		ColorChoose(6);
	}
	
	bool docommand(string s)
	{
		if(s=="exit")
		{
			return false;
		}
		else if(s=="blood")
		{
			blood();
		}
		else if(s=="cls")
		{
			clrscr();
		}
		else if(s=="enchant")
		{
			Enchant enchant;
			enchant.play();
		}
		else if(s=="equip")
		{
			Equip equip;
			equip.play();
		}
		else if(s=="help")
		{
			help();
		}
		else if(s=="place")
		{
			Place place;
			place.play();
		}
		else if(s=="shop")
		{
			Shop shop;
			shop.play();
		}
		else if(s=="state")
		{
			state();
		}
		else if(ClearSpaces(s))
		{
			ColorChoose(4);
			cout<<"There is no definition for "<<"'"<<s<<"', Please type help for help\n";
			ColorChoose(6);
		}
		return true;
	}
	
	void play()
	{
		bool bl=true;
		while(bl)
		{
			string s=input("Main-city> ");
			bl=docommand(s);
		}
	}	
};

char* StringtoChar(string s)
{
	static char str[1024];
	int i=0;
	for(;i<s.length();i++)
	{
		str[i]=s[i];
		str[i+1]='\0';
	}
	return str;
}

string getChar()
{
	char buf[1024];
	if(!fgets(buf,1024,file))
	{
		return "\0";
	}
	string str;
	for(int i=0;i<strlen(buf);i++)
	{
		if(buf[i]!='\n')
		  str+=buf[i];
	}
	return str;
}

char* _getChar()
{
	static char buf[1024];
	fgets(buf,1024,file);
	return buf;
}

char* InttoChar(int n)
{
	static char buf[1024];
	sprintf(buf,"%d\0",n);
	return buf;
}

void readin()
{
	cout<<"Reading file...";
	char buf[1024];
	sprintf(buf,"data/%s.txt",StringtoChar(player.playername));
	
	file=fopen(buf,"r+");
	
	if(!file)
	{
		char buff[1024];
		sprintf(buff,"cd.>\"%s\"",buf);
		system(buff);
		player.money=100;
		player.lvl=0;
		player.heart.now=player.heart.max=player.defense.max=player.attack.max=100;
		player.defense.now=player.attack.now=1;
		for(int i=0;i<THINGSLEN;i++)
		{
			player.things[i].name=player.things[i].ench="nothing";
			player.things[i].defense=player.things[i].attack=0;
		}
		player.thing=0;
	}
	else
	{
		player.money=atoi(_getChar());
		player.lvl=atoi(_getChar());
		player.heart.now=atoi(_getChar());
		player.heart.max=atoi(_getChar());
		player.defense.now=atoi(_getChar());
		player.defense.max=atoi(_getChar());
		player.attack.now=atoi(_getChar());
		player.attack.max=atoi(_getChar());
		for(int i=0;i<THINGSLEN;i++)
		{
			player.things[i].name=getChar();
			player.things[i].defense=atoi(_getChar());
			player.things[i].attack=atoi(_getChar());
			player.things[i].ench=getChar();
		}
		player.thing=atoi(_getChar());
		string s;
		s=getChar();
		while(s!="\0")
		{
			Bag bag;
			bag.name=s;
			bag.num=atoi(_getChar());
			bag.defense=atoi(_getChar());
			bag.attack=atoi(_getChar());
			bag.ench=getChar();
			s=getChar();
			player.bag.push_back(bag);
		}
	}
	
	fclose(file);
	clrscr();
}

void writein()
{
	cout<<"Writing file...";
	char buf[1024];
	sprintf(buf,"data/%s.txt",StringtoChar(player.playername));
	
	file=fopen(buf,"r+");
	
	fprintf(file,"%s\n",InttoChar(player.money));
	fprintf(file,"%s\n",InttoChar(player.lvl));
	fprintf(file,"%s\n",InttoChar(player.heart.now));
	fprintf(file,"%s\n",InttoChar(player.heart.max));
	fprintf(file,"%s\n",InttoChar(player.defense.now));
	fprintf(file,"%s\n",InttoChar(player.defense.max));
	fprintf(file,"%s\n",InttoChar(player.attack.now));
	fprintf(file,"%s\n",InttoChar(player.heart.max));
	for(int i=0;i<THINGSLEN;i++)
	{
		fprintf(file,"%s\n",StringtoChar(player.things[i].name));
		fprintf(file,"%s\n",InttoChar(player.things[i].defense));
		fprintf(file,"%s\n",InttoChar(player.things[i].attack));
		fprintf(file,"%s\n",StringtoChar(player.things[i].ench));
	}
	fprintf(file,"%s\n",InttoChar(player.thing));
	for(int i=0;i<player.bag.size();i++)
	{
		fprintf(file,"%s\n",StringtoChar(player.bag[i].name));
		fprintf(file,"%s\n",InttoChar(player.bag[i].num));
		fprintf(file,"%s\n",InttoChar(player.bag[i].defense));
		fprintf(file,"%s\n",InttoChar(player.bag[i].attack));
		fprintf(file,"%s\n",StringtoChar(player.bag[i].ench));
	}
	
	fclose(file);
	clrscr();
}

void init()
{
	srand((int)time(NULL));
	player.playername=input("Please enter your player-name: ");
	readin();
}

int main()
{
	ColorChoose(6);
	init();
	ColorChoose(2);
	cout<<"Welcome to Warrior Game!\n";
	cout<<"Producer: Wang Yongjian [Edition 16.16.15.1]\n";
	cout<<"Warm tip: if you want to save the progress, please exit by entering exit. Do not close the program directly\n";
	cout<<"If you find a bug, please feedback\n";
	cout<<"Hava a good time!\n\n";
	ColorChoose(6);
	
	Main main;
	main.play();
	
	writein();
	return 0;
}
