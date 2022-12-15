terraform {
  required_version = ">= 1.0"
}

provider "aws" {
  region = "us-east-1"

}
resource "aws_instance" "app" {
  instance_type = "t2.micro"
  ami = "ami-083654bd07b5da81d"
  source_dest_check = false
  tags = {
    "Name" : "our app",
    "GDPR" : "no"

  }
}