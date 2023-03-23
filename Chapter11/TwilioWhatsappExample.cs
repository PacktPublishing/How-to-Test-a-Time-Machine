private static void whatsAppMessage(Uri[] mediaUrl, String accountSid, String authToken, String toPhone, String fromPhone) {
    TwilioClient.Init(accountSid, authToken);
    MessageResource.Create(mediaUrl: mediaUrl,
    from: new Twilio.Types.PhoneNumber(fromPhone),
    to: new Twilio.Types.PhoneNumber(toPhone));
}