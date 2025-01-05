wkn=input("Enter your week name :")

match(wkn.lower()):
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday" | "mon" | "tue" | "wed" | "thu" | "fri":
        print("{} is working day".format(wkn))

    case "saturday" | "sat" :
        print("{} is weekend".format(wkn))

    case "sunday" | "sun" :
        print("{} is holiday".format(wkn))

    case _ :
        print("{} is not weekday".format(wkn))