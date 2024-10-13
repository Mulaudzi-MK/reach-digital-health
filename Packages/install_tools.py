import os
import subprocess

def install_docker():
    print("\nInstalling Docker...")
    commands = [
        "sudo apt-get update",
        "sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common",
        "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -",
        "sudo add-apt-repository 'deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable'",
        "sudo apt-get update",
        "sudo apt-get install -y docker-ce",
        "sudo systemctl enable docker",
        "sudo systemctl start docker",
        "sudo usermod -aG docker $USER"
    ]
    for command in commands:
        subprocess.run(command, shell=True, check=True)

def install_terraform():
    print("\nInstalling Terraform...")
    commands = [
        "sudo apt-get update && sudo apt-get install -y gnupg software-properties-common curl",
        "curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -",
        "sudo apt-add-repository 'deb [arch=amd64] https://apt.releases.hashicorp.com focal main'",
        "sudo apt-get update && sudo apt-get install -y terraform"
    ]
    for command in commands:
        subprocess.run(command, shell=True, check=True)

def install_flask():
    print("\nInstalling Flask...")
    subprocess.run("pip install flask", shell=True, check=True)

def install_git():
    print("\nInstalling Git...")
    subprocess.run("sudo apt-get update && sudo apt-get install -y git", shell=True, check=True)

def install_jenkins():
    print("\nInstalling Jenkins...")
    commands = [
        "sudo apt-get update",
        "sudo apt-get install -y openjdk-11-jdk",
        "curl -fsSL https://pkg.jenkins.io/debian/jenkins.io.key | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null",
        "echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null",
        "sudo apt-get update",
        "sudo apt-get install -y jenkins",
        "sudo systemctl enable jenkins",
        "sudo systemctl start jenkins"
    ]
    for command in commands:
        subprocess.run(command, shell=True, check=True)

def install_trivy():
    print("\nInstalling Trivy...")
    commands = [
        "sudo apt-get update",
        "sudo apt-get install -y wget",
        "wget https://github.com/aquasecurity/trivy/releases/latest/download/trivy_0.44.0_Linux-64bit.deb",
        "sudo dpkg -i trivy_0.44.0_Linux-64bit.deb"
    ]
    for command in commands:
        subprocess.run(command, shell=True, check=True)

def main():
    try:
        install_docker()
        install_terraform()
        install_flask()
        install_git()
        install_jenkins()
        install_trivy()
        print("\nAll tools installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
