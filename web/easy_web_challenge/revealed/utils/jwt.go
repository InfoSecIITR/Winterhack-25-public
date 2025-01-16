package utils

import (
	"fmt"
	"os"
	"time"

	"github.com/golang-jwt/jwt/v5"
)

var publicKeyData []byte
var privateKeyData []byte

func LoadKeys(privateKeyPath, publicKeyPath string) error {
	data, err := os.ReadFile(privateKeyPath)
	if err != nil {
		return fmt.Errorf("failed to read private key file: %v", err)
	}
	privateKeyData = data

	data, err = os.ReadFile(publicKeyPath)
	if err != nil {
		return fmt.Errorf("failed to read public key file: %v", err)
	}
	publicKeyData = data

	fmt.Println("RSA keys successfully loaded")
	return nil
}

func GenerateJWT(username string) (string, error) {
	rsaPrivateKey, err := jwt.ParseRSAPrivateKeyFromPEM(privateKeyData)
	if err != nil {
		return "", fmt.Errorf("failed to parse RSA private key: %v", err)
	}
	claims := &jwt.RegisteredClaims{
		Subject:   username,
		ExpiresAt: jwt.NewNumericDate(time.Now().Add(24 * time.Hour)),
	}
	token := jwt.NewWithClaims(jwt.SigningMethodRS256, claims)
	return token.SignedString(rsaPrivateKey)
}

func ValidateJWT(tokenStr string) bool {

	token, err := jwt.Parse(tokenStr, func(token *jwt.Token) (interface{}, error) {
		if _, ok := token.Method.(*jwt.SigningMethodHMAC); ok {
			return publicKeyData, nil
		}

		rsaPublicKey, _ := jwt.ParseRSAPublicKeyFromPEM(publicKeyData)
		return rsaPublicKey, nil
	})

	return err == nil && token.Valid
}

func ValidateAdminJWT(tokenStr string) bool {
	token, err := jwt.Parse(tokenStr, func(token *jwt.Token) (interface{}, error) {
		if _, ok := token.Method.(*jwt.SigningMethodHMAC); ok {
			return publicKeyData, nil
		}

		rsaPublicKey, _ := jwt.ParseRSAPublicKeyFromPEM(publicKeyData)
		return rsaPublicKey, nil
	})

	if err != nil || !token.Valid {
		return false
	}

	claims, ok := token.Claims.(jwt.MapClaims)
	if !ok {
		return false
	}

	if claims["sub"] == "admin" {
		return true
	}

	return false
}
