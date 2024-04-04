def main():
  # Create an empty arraylist to hold the user's favorite Ninja Turtles
  favorite_turtles =[]

  # Get input from the user for their favorite Ninja Turtles
  print("Enter your favorite Ninja Turtles (seperated by spaces):")
  turtles_input = input().split()

  # Add the entered turtles to the array list
  favorite_turtles.extend(turtles_input)

  # Check if Donnie is in the list of favorite turtles
  if 'Donnie' in favorite_turtles:
    print("Great Choices! Donnie is awesome.")
    
    # Print the user's favorite with an asterik next to Donnie
    print("Your favorites:")
    for turtle in favorite_turtles:
      if turtle == 'Donnie':
        print(f"* {turtle}")
      else:
        print(f" {turtle}")

    # Additional message
    print("One of my favorites too.")
  else:
    # Print the user's favorites without any modification
    print("Your favorites")
    for turtle in favorite_turtle:
      print(f" {turtle}")


if __name__ == "__main__":
  main()