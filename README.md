# Python-Work

## Setup the Java Environment to Work with Kafka

### Step 1: Install Java (JDK)
Since Kafka is built on Java, we need to ensure Java is installed properly. We will use OpenJDK 11 (a version compatible with Kafka).

#### 1. Download OpenJDK 11:
- Go to the [AdoptOpenJDK](https://adoptopenjdk.net/) website.
- Choose `OpenJDK 11 (LTS)` for your system and download the Windows version.

#### 2. Install OpenJDK 11:
- Run the installer after downloading the `.msi` file.
- Choose the default installation directory or set a custom one (e.g., `C:\Program Files\OpenJDK`).
- Complete the installation steps.

#### 3. Set Environment Variables for Java:
1. Right-click **This PC** > **Properties** > **Advanced system settings** > **Environment Variables**.
2. Under **System variables**, click **New** and add:
   - **Variable Name**: `JAVA_HOME`
   - **Variable Value**: `C:\Program Files\OpenJDK\jdk-11.0.x` (adjust version number as needed)
3. Find the **Path** variable in **System variables** and click **Edit**.
   - Click **New** and add:  
     `C:\Program Files\OpenJDK\jdk-11.0.x\bin`
4. Confirm by clicking **OK**.

#### 4. Verify Java Installation:
- Open Command Prompt and type:
  ```bash
  java -version

### Step 2: Install Apache Kafka

#### 1. Download Kafka:
- Visit the [Apache Kafka download page](https://kafka.apache.org/downloads).
- Choose the latest stable version of Kafka. As of now, the latest stable version is Kafka 3.5.0 (check for the most recent version).
- Download the **Binary downloads for Kafka 3.5.0** (for Windows).

#### 2. Extract Kafka:
- Once the download is complete, extract the `.tgz` file using a tool like 7-Zip or WinRAR to a directory (e.g., `C:\kafka`).

---

### Step 3: Install Zookeeper (Required by Kafka)
Kafka uses Zookeeper for managing and coordinating distributed services. It is bundled with Kafka, so you don't need to install it separately.

---

### Step 4: Start Zookeeper and Kafka Server

#### 1. Start Zookeeper:
- Open Command Prompt and navigate to the Kafka directory:
  ```bash
  cd C:\kafka
#### Run the following command to start Zookeeper:
- Open Command Prompt and navigate to the Kafka directory:
  ```bash
  zookeeper-server-start.bat config\zookeeper.properties
- You should see that logs indicating that Zookeeper has started.
#### Start Kafka Server
- Open another command prompt window
- Navigate to the Kafka directory:
  ```bash
  cd C:\kafka
- Run the following command to start Kafka:
  ```bash
  kafka-server-start.bat config\server.properties
- You should see logs indicating Kafka is running. Keep this window open.

#### Step 4: Install Kafka Python Liabrary
1. Open the Command Prompt or Terminal
2. Type `pip install kafka-python` and press `Enter`. This install a python liabrary that allows you interact with Kafka.

#### Step 5: Set up the SQLite Database
- You don't need to install sqlite separately, because it comes with Python.
- Open Command Prompt and Terminal.
- Type `python` and press `Enter`.
- Type ```import sqlite``` and press `Enter`
### 2. Create a new Python script to set up the SQLite database:
- Create a folder called kafka_project.
- Inside this folder, create a file called database.py using a text editor
like Notepad or Visual Studio Code.

### Run the Script:
- Open Command Prompt or Terminal.
- Navigate to the folder where `database.py` is located by typing ```cd
path_to_folder```.
- Type `python database.py` and press `Enter` to create the database.

#### Step 6: Create Producer (Send Messages to Kafka)
1. Inside the kafka_project folder, create a new file called `producer.py`
using a text editor.

### Run the Producer:
- Open Command Prompt or Terminal.
- Navigate to the kafka_project folder where `producer.py` is
located.
- Type `python producer.py` and press `Enter` to send the messages to
Kafka.

#### Step 7: Create Consumer (Receive Messages from Kafka)
1. Inside the kafka_project folder, create a new file called consumer.py.

### Run the Consumer:
- Open Command Prompt or Terminal.
- Navigate to the kafka_project folder where `consumer.py` is
located.
- Type `python consumer.py` and press `Enter` to send the messages to
Kafka.

#### Step 8: Add Messages to SQLite Database
1. You can now add messages to the SQLite database manually or through Python
code

#### Step 10: Final Test
1. Open two Command Prompt/Terminal windows.
2. In the first window, run the consumer by typing `python consumer.py`.
3. In the second window, run the producer by typing `python producer.py`.
4. Add a message using `add_message.py` or manually insert a message into the
database.
5. Watch as the consumer receives the message in real-time.
Conclusion
Congratulations! You’ve built a simple Kafka-based messaging application that stores
and sends messages using Kafka, Python, and SQLite.
Free Resources:
• Kafka: (Download Kafka)
• SQLite: (SQLite Official Page)

  

  


