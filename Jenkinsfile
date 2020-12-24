pipeline {
  agent any
  stages{
    stage('commitlogger') {
      steps {
	sh 'echo $GIT_MESSAGE'
        sh 'printenv'
        sh 'python3 ./commitLogger.py'
      }
    }
    stage('printCommit') {
      steps {
        sh 'python3 ./printCommit.py'
      }
    }
  }
}
