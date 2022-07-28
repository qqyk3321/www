#include <iostream>
#include <stdlib.h>
#include <string.h>
 
const  std::string ENV[]=
{
	"SERVER_NAME",
	"SERVER_SOFTWARE",
	"GATEWAY_INTERFACE",
	"SERVER_PROTOCOL",
	"SERVER_PORT",
	"REQUEST_METHOD",
	"HTTP_ACCEPT",
	"HTTP_USER_AGENT",
	"HTTP_REFERER",
	"PATH_INFO",
	"PATH_TRANSLATED",
	"SCRIPT_NAME",
	"QUERY_STRING",
	"REMOTE_HOST",
	"REMOTE_ADDR",
	"REMOTE_USER",
	"REMOTE_IDENT",
	"CONTENT_TYPE",
	"CONTENT_LENGTH",
	"DEBUG"
};
 
int get_cgi_env()
{
	int i = 0;
	std::cout<<"Content-type:text/html\r\n\r\n";
	std::cout<<"<html>\n";
	
	std::cout<<"<head>\n";
	std::cout<<"<title> CGI Envrionment  Variables</title>\n";
	std::cout<<"</head>\n";
 
	std::cout<<"<body>\n";
	//std::cout<<"<h2>Hello World ! This is my first CGI program </h2>\n";
 
	std::cout<<"<table border =\"0\" cellspacing=\"2\">";
	for(i=0;i< sizeof(ENV)/sizeof(ENV[0]);i++)
	{
		std::cout<<"<tr>";
		std::cout<<"<td>" <<ENV[i]<<"</td>";
		std::cout<<"<td>";
		char *value = getenv(ENV[i].c_str());
		if(NULL != value)
		{
			std::cout<< value;
		}
		else
		{
			std::cout<<"Environment variable does not exist.";
		}
		std::cout<<"</td>";
		std::cout<<"</tr>\n";
	}
	std::cout<<"</table>";
	std::cout<<"</body>\n";
	std::cout<<"</html>\n";
	//std::cout<<"</head>\n";
 
 
	
	return 0;
}
 
int main()
{
     get_cgi_env();
	return 0;
}
 
