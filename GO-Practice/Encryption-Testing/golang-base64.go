package main

import (
	"encoding/base64"
	"fmt"
)

func main() {
	Name := " Cornelius Napolean"
	fmt.Printf("Current Name is:%s.\n", Name)
	encryption(Name)
}

func encryption(name string) {
	cipherText := base64.StdEncoding.EncodeToString([]byte(name))
	fmt.Printf("Encrypted Name in base64 is: %s.\n", string(cipherText))
	decryption(cipherText)
}

func decryption(cipherText string) {
	plaintext, _ := base64.StdEncoding.DecodeString(cipherText)
	fmt.Printf("The plaintext name is:%s", plaintext)
}
