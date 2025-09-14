import subprocess
import sys
import socket
from pathlib import Path

def run_command(command):
    """Run a command and return the result"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def check_module_installed(module_name):
    """Check if a Python module is installed"""
    try:
        __import__(module_name)
        return True
    except ImportError:
        return False

def check_port_available(port):
    """Check if a port is available"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('127.0.0.1', port)) != 0

def create_env_file():
    """Create .env file from env.example if it doesn't exist"""
    env_example = Path("env.example")
    env_file = Path(".env")
    
    if env_example.exists() and not env_file.exists():
        try:
            with open(env_example, 'r') as src, open(env_file, 'w') as dst:
                dst.write(src.read())
            print("✅ Created .env file from env.example")
            return True
        except Exception as e:
            print(f"❌ Failed to create .env file: {e}")
            return False
    elif env_file.exists():
        print("✅ .env file already exists")
        return True
    else:
        print("❌ env.example not found")
        return False

def main():
    print("🔍 Checking your FastAPI development environment...")
    print("=" * 60)
    
    # Check Python version
    success, stdout, stderr = run_command("python --version")
    if success:
        print(f"✅ Python version: {stdout.strip()}")
    else:
        print("❌ Python not found or not in PATH")
    
    # Check for email-validator
    if check_module_installed('email_validator'):
        print("✅ email-validator is installed")
    else:
        print("❌ email-validator is not installed")
        print("   Installing email-validator...")
        success, stdout, stderr = run_command("pip install email-validator")
        if success:
            print("✅ Successfully installed email-validator")
        else:
            print("❌ Failed to install email-validator")
            print(f"   Error: {stderr}")
    
    # Check port availability
    if check_port_available(8000):
        print("✅ Port 8000 is available for Uvicorn")
    else:
        print("❌ Port 8000 is in use")
        print("   Another process might be using this port")
        print("   You can try using a different port with --port 8001")
    
    if check_port_available(3306):
        print("❌ MySQL server is not running on port 3306")
        print("   Make sure your MySQL server is started")
    else:
        print("✅ MySQL server appears to be running on port 3306")
    
    # Check for .env file
    create_env_file()
    
    print("=" * 60)
    print("\n📝 Next steps:")
    print("1. Make sure your MySQL server is running")
    print("2. Verify your database credentials in the .env file")
    print("3. Run your FastAPI application with:")
    print("   uvicorn app.main:app --reload --host 127.0.0.1 --port 8000")
    print("4. Open http://127.0.0.1:8000 in your browser")
    print("5. Check http://127.0.0.1:8000/docs for the API documentation")

if __name__ == "__main__":
    main()