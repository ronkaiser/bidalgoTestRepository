pipeline {
  agent any
  stages{
    stage('commitlogger') {
      steps {
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
