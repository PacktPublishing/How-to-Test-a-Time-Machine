private static void sendGmail(int failedTests) {
    String userName = "yourEmail";
    String password = "yourPassword";
    String toEmail = "toEmail";
    String fromEmail = "yourEmail"; // likely same as userName
    SmtpClient client = new SmtpClient("smtp.gmail.com", 587);
    MailMessage message = new MailMessage(
            new MailAddress(fromEmail, "Your name"),
            new MailAddress(toEmail));
    message.IsBodyHtml = true;
    message.Subject = "We found some failed tests";
    message.Body = "<html><head></head><body><p>Hi!</p><br>"
        + <p><font size=\"3\" color=\"red\">We found "
        + failedTests +" failed tests. Please"
        + "verify.</font></p></body></html>";
    client.EnableSsl = true;
    client.Credentials = new NetworkCredential(userName, password);
    client.Send(message);
}