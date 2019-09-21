'''
test: https://github.com/flasgger/flasgger
'''

specs_dict = {
  "parameters": [
    {
      "name": "palette",
      "in": "path",
      "type": "string",
      "enum": [
        "all",
        "rgb",
        "cmyk",
        "hi_mom"
      ],
      "required": "true",
      "default": "all"
    }
  ],
  "definitions": {
    "Palette": {
      "type": "object",
      "properties": {
        "palette_name": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Color"
          }
        }
      }
    },
    "Color": {
      "type": "string"
    }
  },
  "responses": {
    "200": {
      "description": "A list of colors (may be filtered by palette)",
      "schema": {
        "$ref": "#/definitions/Palette"
      },
      "examples": {
        "rgb": [
          "red",
          "green",
          "blue"
        ]
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
          "username",
          "age"
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
