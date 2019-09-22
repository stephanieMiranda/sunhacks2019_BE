'''
test: https://github.com/flasgger/flasgger
'''

user_dict = {
  "parameters": [
    {
      "name": "user_email",
      "in": "path",
      "type": "string",
    }
  ],
  "definitions": {
    "User": {
      "type": "object",
      "properties": {
        "user_email": {
          "type": "object",
          "items": {
            "$ref": "#/definitions/User"
          }
        }
      }
    },
    "Name": {
      "type": "string"
    },
    "Email": {
      "type": "string"
    },
    "Favorite_Color": {
      "type": "string"
    },
    "Power": {
      "type": "string"
    },
    "Field": {
      "type": "string"
    },
    "Favorite_Hobby": {
      "type": "string"
    }
  },
  "responses": {
    "200": {
      "description": "A users public information",
      "schema": {
        "$ref": "#/definitions/User"
      },
      "examples": {
        "User" : {
      	 "Email": "test@donut.derp",
 		     "Favorite_Color": "FF8017",
 		     "Favorite_Hobby": "Pancakes",
 		     "Field": "Software Engineering",
 		     "Name": "Jacob Wallert",
 		     "Nametag": "test@donut.derp.nametag",
 		     "Superpower": "Overthinking"
 		}
 		}
    }
  }
}


products = {
  "tags": [
    "users"
  ],
  "parameters": [
    {
      "name": "body",
      "in": "body",
      "required": True,
      "schema": {
        "id": "User",
        "required": [
          "Email",
          "Favorite_Color",
          "Favorite_Hobby",
          "Field",
          "Name",
          "Nametag",
          "Superpower",
        ],
        "properties": {
          "username": {
            "type": "string",
            "description": "The user name.",
            "default": "Sirius Black"
          },
          "age": {
            "type": "integer",
            "description": "The user age (should be integer)",
            "default": "180"
          },
          "tags": {
            "type": "array",
            "description": "optional list of tags",
            "default": [
              "wizard",
              "hogwarts",
              "dead"
            ],
            "items": {
              "type": "string"
            }
          }
        }
      }
    }
  ],
  "responses": {
    "200": {
      "description": "A single user item",
      "schema": {
        "$ref": "#/definitions/User"
      }
    }
  }
}
