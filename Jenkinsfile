pipeline {
    agent any

    stages {
        stage('Dev Dummmy code') {
            steps {
                echo 'Building the code.............'
                bat "mvn clean"
            }
        }
        stage('Test') {
            steps {
                echo 'Testing the code.............'
                bat "mvn test"
            }
        }
        stage('Compile') {
            steps {
                echo 'complilng the code..........'
                bat "mvn compile"
            }
        }
        stage('Release') {
            steps {
                echo 'Released'
            }
        }
    }
}
