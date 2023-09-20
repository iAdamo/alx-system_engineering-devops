## **Command_Line_For_The_Win**
**`Bash`** **`Scripting`**

**`sftp`** — OpenSSH secure file transfer
- `sftp` is a file transfer program, similar to ftp(1), which performs all operations over an encrypted ssh(1) transport. It may also use many features of ssh, such as public key authentication and compression.
- The destination may be specified either as `[user@]host[:path]` or as a URI in the form `sftp://[user@]host[:port][/path]`.
#### **For full documentation on the `sftp` command line tool, kindly enter `man sftp` on your command line or visit [SFTP](https://man.openbsd.org/sftp)**

### **Tasks**
[CMD CHALLENGE](https://cmdchallenge.com/) is a pretty cool game challenging you on Bash skills. Everything is done via the command line and the questions are becoming increasingly complicated. It’s a good training to improve your command line skills!

Using `sftp` command line to tranfer files (screenshots) from the `local machine` to a `remote srver`. Once the screenshots are transferred, you can proceed to push the screenshots to `GitHub`.

### **Usage:**
How To Use `SFTP` to Securely Transfer Files with a `Remote Server`...
```
1) Ready your files that are to be transferred, in this case we transferred screenshots. Files can be anywhere in your local machine.

2) Get your client remote server username, hostname and password ready for SFTP via ssh connection user@host.

3) Open your local machine terminal and enter your remote server sftp command (sftp username@hostname), It will ask for an option, enter yes and input your server password to connect, then you will begin with a sftp prompt.

4) Use the "put" command to uppload your file to the server, e.g put <file pathname> <srver destination pathname>. server dest pathname can be nothing if you are on the current working directory.

5) You can use the "get" command to download files from the server

6) Use the "exit" command to end the process.
```
`sftp` commands are like shell commands, (`ls`, `pwd`, `cd`, etc..), you can also navigate your local machine by prefixing the command with "!" (`!ls`, `!pwd`, `!cd`, etc), and to use `exit` to exit the local machine back to your sftp prompt.

Enjoy... It's fun...

##### **Author: Adam Sanusi Babatunde**
