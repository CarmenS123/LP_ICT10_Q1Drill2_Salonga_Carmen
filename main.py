from pyscript import when, display, document

@when("click", "#submit-btn")
def show_message(event):
    name = document.querySelector("#name").value
    age = document.querySelector("#age").value
    interest = document.querySelector("#interest").value
    school = document.querySelector("#school").value

    document.querySelector("#output").innerText = ""

    message = f"""👤 Student Profile
    Name : {name}
    Age  : {age}
    Interest  : {interest}
    School : {school}

    📓 Notes:
    {name} is currently {age} years old. They love {interest}, and study at {school}.✏️
    This information was gathered through input fields and displayed using
    a multiline string in Python via PyScript.
    """

    display(message, target="output")

