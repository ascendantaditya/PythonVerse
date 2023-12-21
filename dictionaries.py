##Dictionary : Its a special structure in python which allows us to store information in what are called "Key Value"
monthConversions = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December"
}
#for using keys we can use "[]" ~ 1st Method
print(monthConversions["Apr"])
#for using keys we can use ".get"() ~ 2nd Method
print(monthConversions.get("Adi"))
#if you want to add a default value to dictionary keys we can use sep"
print(monthConversions.get("Lund" , "Not a Valid Key"))