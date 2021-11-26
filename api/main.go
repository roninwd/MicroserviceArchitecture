package main

import (
	"encoding/json"
	"fmt"
	"github.com/gorilla/mux"
	"log"
	"net/http"
)

type HealthMessage struct {
	Status string `json:"status"`
}

type Message struct {
	Message string `json:"message"`
}

func main() {
	r := mux.NewRouter()
	r.HandleFunc("/otusapp/{name}", namePage)
	r.HandleFunc("/health", healthPage)
	r.HandleFunc("/", homePage)
	http.Handle("/", r)
	log.Fatal(http.ListenAndServe(":8000", nil))
}

func namePage(writer http.ResponseWriter, request *http.Request) {
	initHeaders(writer)
	vars := mux.Vars(request)
	json.NewEncoder(writer).Encode(Message{Message: fmt.Sprintf("home page %s", vars["name"])})
}

func homePage(w http.ResponseWriter, r *http.Request) {
	initHeaders(w)
	json.NewEncoder(w).Encode(Message{Message: "home page"})
}

func healthPage(w http.ResponseWriter, r *http.Request) {
	initHeaders(w)
	json.NewEncoder(w).Encode(HealthMessage{Status: "ok"})
}

func initHeaders(writer http.ResponseWriter) {
	writer.Header().Set("Content-Type", "application/json")
}
