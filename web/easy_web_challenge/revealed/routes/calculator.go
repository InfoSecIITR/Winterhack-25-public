package routes

import (
	"calculator-app/utils"
	"encoding/json"
	"html/template"
	"net/http"
	"os"
)

func AddHandler(w http.ResponseWriter, r *http.Request) {
	var numbers struct {
		A float64 `json:"a"`
		B float64 `json:"b"`
	}

	if err := json.NewDecoder(r.Body).Decode(&numbers); err != nil {
		utils.RespondWithError(w, http.StatusBadRequest, "Invalid request payload")
		return
	}

	result := numbers.A + numbers.B
	utils.RespondWithJSON(w, http.StatusOK, map[string]float64{"result": result})
}

func SubtractHandler(w http.ResponseWriter, r *http.Request) {
	var numbers struct {
		A float64 `json:"a"`
		B float64 `json:"b"`
	}

	if err := json.NewDecoder(r.Body).Decode(&numbers); err != nil {
		utils.RespondWithError(w, http.StatusBadRequest, "Invalid request payload")
		return
	}

	result := numbers.A - numbers.B
	utils.RespondWithJSON(w, http.StatusOK, map[string]float64{"result": result})
}

func CalculateHandler(w http.ResponseWriter, r *http.Request) {
	myHTTPClient := &http.Client{}
	local_service := os.Getenv("LOCAL_SERVICE")
	if local_service == "" {
		local_service = "localhost:5000"
	}
	resp, err := myHTTPClient.Post("http://"+local_service+"/calculate", "application/json", r.Body)
	if err != nil {
		utils.RespondWithError(w, http.StatusInternalServerError, "Error calling calculation service")
		return
	}

	var result struct {
		Result string `json:"result"`
	}

	if err := json.NewDecoder(resp.Body).Decode(&result); err != nil {
		utils.RespondWithError(w, http.StatusInternalServerError, "Error decoding response from calculation service")
		return
	}

	utils.RespondWithJSON(w, http.StatusOK, map[string]string{"result": result.Result})
}

func GetCalculateHandler(w http.ResponseWriter, r *http.Request) {
	tmpl := template.Must(template.ParseFiles("templates/advanced.html"))
	tmpl.Execute(w, nil)
}

func NormalHandler(w http.ResponseWriter, r *http.Request) {
	tmpl := template.Must(template.ParseFiles("templates/normal.html"))
	tmpl.Execute(w, nil)
}
