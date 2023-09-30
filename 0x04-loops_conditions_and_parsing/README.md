### **Loops, conditions and parsing**
**`DevOps`** **`Shell`** **`Bash`** **`Scripting`**

## Tasks
#### **0. Create a SSH RSA key pair**

*Run the following command to create an SSH key pair. You can leave the passphrase blank if you do not wish to `unlock` your key each time you use it:*

`ssh-keygen -t rsa`
The output will be similar to this

```
Generating public/private rsa key pair.
Enter file in which to save the key (/home/a/.ssh/id_rsa): 
Created directory '/home/a/.ssh'.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/a/.ssh/id_rsa.
Your public key has been saved in /home/a/.ssh/id_rsa.pub.
The key fingerprint is:
3e:4f:05:79:3a:9f:96:7c:3b:ad:e9:58:37:bc:37:e4 a@A
```
Then you'll need to copy the new key to your server.

After copying the SSH keys you can log into your machine without a password.

