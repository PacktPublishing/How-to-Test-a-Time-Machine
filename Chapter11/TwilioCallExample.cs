private static void callOnCall(int issueNumber, String accountSid, String authToken, String toPhone, String fromPhone) {
TwilioClient.Init(accountSid, authToken);
CallResource.Create(twiml: "<Response><Say>Dear person on Call!"
        + "We have found an issue "+ issueNumber +" that needs immediate"
        + " attention. Some other instructions...</Say></Response>",
    to: new Twilio.Types.PhoneNumber(toPhone),
    from: new Twilio.Types.PhoneNumber(fromPhone));
}