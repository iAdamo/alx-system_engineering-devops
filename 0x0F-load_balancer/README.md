### **Load balancer**
**`DevOps`** **`SysAdmin`**

Let’s improve our web stack so that there is `redundancy` for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.

#### **0. Double the number of webservers**

In this first task you need to configure `web-02` to be identical to `web-01`. Fortunately, you built a Bash script during your web server project, and they’ll now come in handy to easily configure `web-02`. Remember, always try to automate your work!

Since we’re placing our web servers behind a load balancer for this project, we want to add a custom Nginx response header. The goal here is to be able to track which web server is answering our HTTP requests, to understand and track the way a load balancer works. More in the coming tasks.

Requirements:

- Configure Nginx so that its HTTP response contains a custom header (on `web-01` and `web-02`)
    - The name of the custom HTTP header must be `X-Served-By`
    - The value of the custom HTTP header must be the hostname of the server Nginx is running on
- Write `0-custom_http_response_header` so that it configures a brand new Ubuntu machine to the requirements asked in this task
    - Ignore SC2154 for `shellcheck`
Example:
```
sylvain@ubuntu$ curl -sI 34.198.248.145 | grep X-Served-By
X-Served-By: 03-web-01
sylvain@ubuntu$ curl -sI 54.89.38.100 | grep X-Served-By
X-Served-By: 03-web-02
sylvain@ubuntu$
```
