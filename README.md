# WebhookUtilsV3
Little script I use to disrupt malicious discord webhook

### configuration
All that's important is to:
- own Python
- Install requirement with:
```
pip install requests
```

And you're all set

<img width="1259" height="553" alt="image" src="https://github.com/user-attachments/assets/22fe95d0-44b0-4995-84b0-8b2ec273a280" />


Remove Webhook functionality can also be achieved easily via DevTools' console on any website using this snippet:
```js
let z = 'webhookrul';
fetch(z, { method: 'DELETE' }).catch(() => {});
```
