package main

import (
	"encoding/json"
	"log"
	"math/rand" // for test ID number
	"net/http"
	"strconv"

	"github.com/gorilla/mux"
)

// backpack struct (Model)
type Backpack struct {
	ID      string `json:"id"`
	Country string `json:"country"`
	City    string `json:"city"`
	Index   *Index `json:"index"`
}

// Index struct (used in model)
type Index struct {
	Currency string  `json:"currency"`
	score    float32 `json:"score"`
}

// Init backpack var as a slice Backpack struct
var backpacks []Backpack

// Get all backpacks
func getBackpacks(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(backpacks)
}

// Get single backpack
func getBackpack(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	params := mux.Vars(r) // Gets params
	// Loop through backpacks and find one with the id from the params
	for _, item := range backpacks {
		if item.ID == params["id"] {
			json.NewEncoder(w).Encode(item)
			return
		}
	}
	json.NewEncoder(w).Encode(&Backpack{})
}

// Add new backpack
func createBackpack(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	var backpack Backpack
	_ = json.NewDecoder(r.Body).Decode(&backpack)
	backpack.ID = strconv.Itoa(rand.Intn(100000000)) // TEST ID - not safe
	backpacks = append(backpacks, backpack)
	json.NewEncoder(w).Encode(backpack)
}

// Update backpack
func updateBackpack(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	params := mux.Vars(r)
	for index, item := range backpacks {
		if item.ID == params["id"] {
			backpacks = append(backpacks[:index], backpacks[index+1:]...)
			var backpack Backpack
			_ = json.NewDecoder(r.Body).Decode(&backpack)
			backpack.ID = params["id"]
			backpacks = append(backpacks, backpack)
			json.NewEncoder(w).Encode(backpack)
			return
		}
	}
}

// Delete backpack
func deleteBackpack(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	params := mux.Vars(r)
	for index, item := range backpacks {
		if item.ID == params["id"] {
			backpacks = append(backpacks[:index], backpacks[index+1:]...)
			break
		}
	}
	json.NewEncoder(w).Encode(backpacks)
}

// Main function
func main() {
	// Init router
	r := mux.NewRouter()

	// Hardcoded data - @todo: add database
	backpacks = append(backpacks, Backpack{ID: "1", Country: "USA", City: "Little Rock", Index: &Index{Currency: "USD", Score: 1.5}})
	backpacks = append(backpacks, Backpack{ID: "1", Country: "COL", City: "Cartagena", Index: &Index{Currency: "USD", Score: 8.0}})

	// Route handles & endpoints
	r.HandleFunc("/backpacks", getBackpacks).Methods("GET")
	r.HandleFunc("/backpacks/{id}", getBackpack).Methods("GET")
	r.HandleFunc("/backpacks", createBackpack).Methods("POST")
	r.HandleFunc("/backpacks/{id}", updateBackpack).Methods("PUT")
	r.HandleFunc("/backpacks/{id}", deleteBackpack).Methods("DELETE")

	// Start server
	log.Fatal(http.ListenAndServe(":8000", r))
}

// struct sample
// {
// 	"country":"USA",
// 	"city":"New York",
// 	"index":{"currency":"USD","score":1.0}
// }
