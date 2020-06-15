pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
    }

  }
  stages {
    stage('Build') {
      steps {
        sh 'make build'
      }
    }

    stage('Unit Tests') {
      steps {
        sh 'make unit-test'
        junit '.pytest_cache/unit_test_report.xml'
      }
    }

    stage('Performance Tests') {
      steps {
        sh 'make performance-test'
      }
    }

  }
}