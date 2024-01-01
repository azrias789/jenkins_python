podTemplate(containers: [
  containerTemplate(
    name: 'python', 
    image: 'jenkins/inbound-agent-python:latest', 
    command: 'sleep', 
    args: '30d')
]) 
{
  node(POD_LABEL)
  {
    stage('Get a Python Project')
    {
      container('python')
      {
          stage('Checkout Code')
          {
            sh 'pwd'
            sh 'ls -la'
            sh 'python -V'
            sh 'hostname'
            sh 'git clone https://github.com/azrias789/jenkins_python'
            sh 'ls -la jenkins_python'
            sh 'python jenkins_python/cal.py'
          }
          stage(' Installing packages')
          {
            sh 'pwd'
            sh 'ls -la'
            sh 'python -V'
	    sh 'git clone https://github.com/azrias789/jenkins_python'
            sh 'apt install -y pip'
            sh 'pip install requests'
            sh 'python jenkins_python/cal.py'
          }
          stage('Static Code Check')
          {
            sh 'pwd'
            sh 'ls -la'
            sh 'python -V'
            sh 'git clone https://github.com/azrias789/jenkins_python'
            sh 'ls -la jenkins_python'
            sh 'python jenkins_python/cal.py'
          }
          stage('Unit Test Check')
          {
            python3 -m unittest check_os.py          
          }
        
      }
    }
  }
}
