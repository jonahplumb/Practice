package main

import (
	"context"
	"crypto/sha256"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"log"
	"math/rand"
	"os"
	"strings"
	"time"

	amqp "github.com/rabbitmq/amqp091-go"
)

const (
	charset    = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	charsetLen = len(charset)
)

type HelloData struct {
	TechName   string `json:"Technology-Name"`
	Action     string `json:"Action-Name"`
	ActionId   string `json:"Action-Id"`
	DatabaseId string `json:"Database-Id"`
}

// / Method to generate random id for our actions
// / This will be the id used in lookup calls in my /action call
func GenerateRandomID() string {
	// Set the seed for the random number generator
	rand.Seed(time.Now().UnixNano())

	// Initialize a byte slice to store the random characters
	idBytes := make([]byte, 19) // 4 * 4 characters + 3 hyphens

	// Generate random characters and hyphens directly in the byte slice
	for i := range idBytes {
		// Add hyphen after each segment except the last one
		if i%5 == 4 && i != 18 {
			idBytes[i] = '-'
		} else {
			// Generate a random index within the charset
			randIndex := rand.Intn(charsetLen)
			// Assign the random character to the byte slice
			idBytes[i] = charset[randIndex]
		}
	}

	// Return the byte slice as a string
	return string(idBytes)
}

// / Method to generate random hash for our database
func GenerateSHA256Hash(input string) string {
	// Convert the string to bytes
	data := []byte(input)

	// Initialize the SHA-256 hash algorithm
	hasher := sha256.New()

	// Write the data to the hasher
	hasher.Write(data)

	// Calculate the SHA-256 hash
	hashBytes := hasher.Sum(nil)

	// Convert the hash bytes to a hexadecimal string
	hashString := hex.EncodeToString(hashBytes)

	return hashString
}

//////////// End of Support Methods

func failOnError(err error, msg string) {
	if err != nil {
		log.Panicf("%s: %s", msg, err)
	}
}

func bodyFrom(args []string) string {
	var s string
	if len(args) < 2 || os.Args[1] == "" {
		s = "hello"
	} else {
		s = strings.Join(args[1:], " ")
	}
	return s
}

func main() {
	// 	This is code from the previous hello world module
	randomID := GenerateRandomID()
	input := "Hello, world!"
	hash := GenerateSHA256Hash(input)
	fmt.Println(hash)
	helloData := HelloData{
		Action:     "get-user",
		TechName:   "entra-id",
		ActionId:   randomID,
		DatabaseId: hash, // Just for testing, wont have this value in the real code
	}

	jsonData, err := json.Marshal(helloData)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	conn, err := amqp.Dial("amqp://guest:guest@localhost:5672/")
	failOnError(err, "Failed to connect to RabbitMQ")
	defer conn.Close()

	ch, err := conn.Channel()
	failOnError(err, "Failed to open a channel")
	defer ch.Close()

	q, err := ch.QueueDeclare(
		"task_queue", // name
		true,         // durable
		false,        // delete when unused
		false,        // exclusive
		false,        // no-wait
		nil,          // arguments
	)
	failOnError(err, "Failed to declare a queue")
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	body := bodyFrom(os.Args)
	err = ch.PublishWithContext(ctx,
		"",     // exchange
		q.Name, // routing key
		false,  // mandatory
		false,
		amqp.Publishing{
			DeliveryMode: amqp.Persistent,
			ContentType:  "application/json",
			Body:         jsonData,
		})
	failOnError(err, "Failed to publish a message")
	log.Printf(" [x] Sent %s", body)
}
