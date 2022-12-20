// Just some simple API interaction practice using GO and Alpha Vantage API for stock data
// https://www.alphavantage.co/documentation/#

package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)

func main() {
	symbol := "IBM"
	// url := fmt.Sprintf("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=%s&interval=60min&apikey=xxxxxxx", symbol)
	// resp, err := http.Get(url)

	// resp, err := weeklychart(symbol)
	resp, err := intraday(symbol)

	if err != nil {
		log.Fatalln(err)
	}
	//Read the response body on the line below.
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatalln(err)
	}
	//Convert the body to type string
	sb := string(body)
	log.Printf(sb)
}

func intraday(symbol string) (*http.Response, error) {
	url := fmt.Sprintf("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=%s&interval=60min&apikey=xxxxxxxxx", symbol)
	resp, err := http.Get(url)
	return resp, err
}

func weeklychart(symbol string) (*http.Response, error) {
	url := fmt.Sprintf("https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=%s&apikey=xxxxxxx", symbol)
	resp, err := http.Get(url)
	return resp, err
}
