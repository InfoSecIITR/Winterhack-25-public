package main

import (
	"calculator-app/routes"
	"calculator-app/utils"
	"log"
	"net/http"
	"os"

	"github.com/go-chi/chi/v5"
	"github.com/go-chi/chi/v5/middleware"
)

func main() {
	err := utils.LoadKeys("keys/private.key", "keys/public.key")
	if err != nil {
		log.Fatalf("Error loading RSA keys: %v", err)
	}

	r := chi.NewRouter()

	r.Use(middleware.Logger)
	r.Use(middleware.StripSlashes)
	r.Use(middleware.NoCache)

	fs := http.FileServer(http.Dir("static/"))
	r.Handle("/static/*", http.StripPrefix("/static/", fs))

	r.Group(func(r chi.Router) {
		r.Post("/login", routes.LoginHandler)
		r.Post("/signup", routes.SignupHandler)
		r.Get("/login", routes.LoginPageHandler)
		r.Get("/signup", routes.SignupPageHandler)
	})

	r.Group(func(r chi.Router) {
		r.Use(routes.JWTMiddleware)
		r.Get("/normal", routes.NormalHandler)
		r.Post("/add", routes.AddHandler)
		r.Post("/subtract", routes.SubtractHandler)
	})

	r.Group(func(r chi.Router) {
		r.Use(routes.JWTAdminMiddleware)
		r.Post("/calculate", routes.CalculateHandler)
		r.Get("/calculate", routes.GetCalculateHandler)
	})

	routes.Init()

	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}
	log.Printf("Server running on port %s", port)
	log.Fatal(http.ListenAndServe(":"+port, r))
}
