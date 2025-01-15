package routes

import (
	"calculator-app/utils"
	"html/template"
	"net/http"
	"os"
)

var users = map[string]string{}

func Init() {
	adminPassword := os.Getenv("ADMIN_PASSWORD")
	if adminPassword == "" {
		adminPassword = "admin"
	}
	users["admin"] = adminPassword
}

func SignupPageHandler(w http.ResponseWriter, r *http.Request) {
	tmpl := template.Must(template.ParseFiles("templates/signup.html"))
	tmpl.Execute(w, nil)
}

func SignupHandler(w http.ResponseWriter, r *http.Request) {
	var creds struct {
		Username string `json:"username"`
		Password string `json:"password"`
	}

	creds.Username = r.FormValue("username")
	creds.Password = r.FormValue("password")

	if _, exists := users[creds.Username]; exists {
		utils.RespondWithError(w, http.StatusConflict, "User already exists")
		return
	}

	users[creds.Username] = creds.Password
	http.Redirect(w, r, "/login", http.StatusSeeOther)
}

func LoginPageHandler(w http.ResponseWriter, r *http.Request) {
	tmpl := template.Must(template.ParseFiles("templates/login.html"))
	tmpl.Execute(w, nil)
}

func LoginHandler(w http.ResponseWriter, r *http.Request) {
	var creds struct {
		Username string `json:"username"`
		Password string `json:"password"`
	}

	creds.Username = r.FormValue("username")
	creds.Password = r.FormValue("password")

	if password, exists := users[creds.Username]; !exists || password != creds.Password {
		utils.RespondWithError(w, http.StatusUnauthorized, "Invalid credentials")
		return
	}

	token, err := utils.GenerateJWT(creds.Username)
	if err != nil {
		utils.RespondWithError(w, http.StatusInternalServerError, "Error generating token")
		return
	}

	http.SetCookie(w, &http.Cookie{
		Name:     "token",
		Value:    token,
		HttpOnly: true,
		SameSite: http.SameSiteStrictMode,
	})

	http.Redirect(w, r, "/normal", http.StatusSeeOther)
}
