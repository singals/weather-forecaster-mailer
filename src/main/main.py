import emailer;
import weather;

def main():
    emails = emailer.get_emails()
    weather_forecast = weather.get_weather_forecast()
    emailer.send_emails(emails, weather_forecast)

main()