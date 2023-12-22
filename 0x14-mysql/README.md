### **MySQL**
**`DevOps`** **`SysAdmin`** **`MySQL`**

#### Concept
- [Database administration](https://www.techtarget.com/searchdatamanagement/definition/database)
- [Web stack debugging]()
- [How to] Install mysql 5.7

#### Learning Objectives
**What is the main role of a database:**
The main role of a database is to store, manage, and organize data in a structured and efficient manner. Databases provide a mechanism for storing and retrieving data, ensuring data integrity, and supporting data manipulation operations. They serve as a central repository for applications to access and manage information, facilitating data-driven decision-making.

**What is a database replica:**
A database replica is a copy of a database that is created and maintained to provide redundancy and improve availability and performance. Replication involves creating and maintaining one or more copies (replicas) of the original or primary database. These replicas are kept synchronized with the primary database to ensure consistency.

**What is the purpose of a database replica:**
The purpose of a database replica is primarily to enhance system reliability, fault tolerance, and performance. Key purposes include:
1. **High Availability:** Database replicas provide failover capabilities. If the primary database goes offline due to hardware failure, maintenance, or other issues, one of the replicas can take over to minimize downtime.
2. **Load Balancing:** Replicas can be used to distribute read queries, reducing the load on the primary database and improving overall system performance.
3. **Disaster Recovery:** In the event of a catastrophic failure or disaster affecting the primary database, replicas can serve as a backup to restore data and services.

**Why database backups need to be stored in different physical locations:**
Storing database backups in different physical locations is essential for ensuring data resilience and protection against various risks. The reasons include:
1. **Disaster Recovery:** If a natural disaster, fire, or other catastrophic event occurs at one location, backups stored in a different location remain unaffected, allowing for recovery.
2. **Data Redundancy:** Multiple copies of backups provide an additional layer of redundancy, reducing the risk of data loss due to hardware failures or corruption.
3. **Security:** Different physical locations enhance security by mitigating the risk of simultaneous data loss at all locations, whether due to theft, vandalism, or other security breaches.

**What operation should you regularly perform to make sure that your database backup strategy actually works:**
Regularly performing a **backup restoration test** is crucial to ensure that your database backup strategy is effective. This involves:
1. **Restoring Backups:** Periodically restore backups to a test environment or a separate server.
2. **Verification:** Verify that the restored database is consistent, and data is accurate.
3. **Test Scenarios:** Conduct test scenarios to simulate common recovery situations, such as restoring from different types of backups (full, incremental), and ensure the database behaves as expected.
4. **Automation Check:** If backup processes are automated, ensure that scheduled backups are completing successfully and monitor any automated alerts or logs.

Regular testing helps identify and address issues with the backup and recovery process, ensuring that the organization can rely on its backup strategy in real-world scenarios.


#### **[How to] Install mysql 5.7**
[Copy the key here to your clipboard](https://dev.mysql.com/doc/refman/5.7/en/checking-gpg-signature.html)

Save it in a file on your machine i.e. signature.key and then
```
sudo apt-key add signature.key
```
add the apt repo
```
sudo sh -c 'echo "deb http://repo.mysql.com/apt/ubuntu bionic mysql-5.7" >> /etc/apt/sources.list.d/mysql.list'
```
update apt
```
sudo apt-get update
```
now check your available versions:
```
vagrant@ubuntu-focal:/vagrant$ sudo apt-cache policy mysql-server
mysql-server:
  Installed: (none)
  Candidate: 8.0.27-0ubuntu0.20.04.1
  Version table:
     8.0.27-0ubuntu0.20.04.1 500
        500 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 Packages
        500 http://security.ubuntu.com/ubuntu focal-security/main amd64 Packages
     8.0.19-0ubuntu5 500
        500 http://archive.ubuntu.com/ubuntu focal/main amd64 Packages
     5.7.37-1ubuntu18.04 500
        500 http://repo.mysql.com/apt/ubuntu bionic/mysql-5.7 amd64 Packages
```
Now install mysql 5.7
```
sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*
```

### **Tasks**
#### **0. Install MySQL**

First things first, let’s get MySQL installed on both your web-01 and web-02 servers.
- MySQL distribution must be 5.7.x
Example:
```
ubuntu@229-web-01:~$ mysql --version
mysql  Ver 14.14 Distrib 5.7.25, for Linux (x86_64) using  EditLine wrapper
ubuntu@229-web-01:~$
```

In order for us to verify that your servers are properly configured, we need you to create a user and password for both MySQL databases which will allow the checker access to them.

- Create a MySQL user named `holberton_user` on both `web-01` and `web-02` with the host name set to `localhost` and the password `projectcorrection280hbtn`. This will allow us to access the replication status on both servers.
- Make sure that `holberton_user` has permission to check the primary/replica status of your databases.

Example:
```
ubuntu@229-web-01:~$ mysql -uholberton_user -p -e "SHOW GRANTS FOR 'holberton_user'@'localhost'"
Enter password:
+-----------------------------------------------------------------+
| Grants for holberton_user@localhost                             |
+-----------------------------------------------------------------+
| GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost' |
+-----------------------------------------------------------------+
ubuntu@229-web-01:~$
```

In order for you to set up replication, you’ll need to have a database with at least one table and one row in your primary MySQL server (web-01) to replicate from.

- Create a `database` named `tyrell_corp`.
- Within the `tyrell_corp` database create a table named `nexus6` and add at least one entry to it.
- Make sure that `holberton_user` has `SELECT` permissions on your table so that we can check that the table exists and is not empty.
```
ubuntu@229-web-01:~$ mysql -uholberton_user -p -e "use tyrell_corp; select * from nexus6"
Enter password:
+----+-------+
| id | name  |
+----+-------+
|  1 | Leon  |
+----+-------+
ubuntu@229-web-01:~$
```

Before you get started with your primary-replica synchronization, you need one more thing in place. On your primary MySQL server (web-01), create a new user for the replica server.

- The name of the new user should be `replica_user`, with the host name set to `%`, and can have whatever password you’d like.
replica_user must have the appropriate permissions to replicate your primary MySQL server.
- `holberton_user` will need SELECT privileges on the `mysql.user` table in order to check that `replica_user` was created with the correct permissions.
```
ubuntu@229-web-01:~$ mysql -uholberton_user -p -e 'SELECT user, Repl_slave_priv FROM mysql.user'
+------------------+-----------------+
| user             | Repl_slave_priv |
+------------------+-----------------+
| root             | Y               |
| mysql.session    | N               |
| mysql.sys        | N               |
| debian-sys-maint | Y               |
| holberton_user   | N               |
| replica_user     | Y               |
+------------------+-----------------+
ubuntu@229-web-01:~$
```


#### Author: **`Adam Sanusi Babatunde`**
