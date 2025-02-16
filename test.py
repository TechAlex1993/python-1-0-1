provisioner "remote-exec" {
    inline = [
        "sudo apt-get update",
        "sudo apt-get install -y nginx",
        "echo \"Hello World from $(hostname -f)\" | sudo tee /var/www/html/index.html"
    ]
}




