package routes

import (
	"calculator-app/utils"
	"net/http"
)

func JWTMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		token, err := r.Cookie("token")
		if err != nil {
			utils.RespondWithError(w, http.StatusUnauthorized, "Invalid or missing token")
			return
		}
		if token.Value == "" || !utils.ValidateJWT(token.Value) {
			utils.RespondWithError(w, http.StatusUnauthorized, "Invalid or missing token")
			return
		}
		next.ServeHTTP(w, r)
	})
}

func JWTAdminMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		token, err := r.Cookie("token")
		if err != nil {
			utils.RespondWithError(w, http.StatusUnauthorized, "Invalid or missing token")
			return
		}

		if token.Value == "" || !utils.ValidateJWT(token.Value) {
			utils.RespondWithError(w, http.StatusUnauthorized, "Invalid or missing token")
			return
		}

		if !utils.ValidateAdminJWT(token.Value) {
			utils.RespondWithError(w, http.StatusUnauthorized, "You need admin privileges to access the special calculator!!")
			return
		}
		next.ServeHTTP(w, r)
	})
}
