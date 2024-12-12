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
