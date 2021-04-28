# [python-client](#)
A Python library to easy the integration with the Beem Africa SMS Gateway 

[![Downloads](https://pepy.tech/badge/beem-africa)](https://pepy.tech/project/beem-africa)
[![Downloads](https://pepy.tech/badge/beem-africa/month)](https://pepy.tech/project/beem-africa)
[![Downloads](https://pepy.tech/badge/beem-africa/week)](https://pepy.tech/project/beem-africa)


## Features to be Implemented 

- [x] Airtime 
- [x] OTP
- [x] SMS 
- [ ] Two way SMS
- [ ] USSD
- [ ] Bpay


## Getting started

To get started with exploring beem-africa you can either clone the repository or install directly from pip (pre-release is already deployed)

### Installing from pip

```bash
pip install beem-africa
```

### Installing directly from github

```bash
git clone https://github.com/beem-africa/python-client
cd python-client
python setup.py install
```

### Authentication

The first thing you need to do before calling module in the beem-africa app is authorize our app with access key and secret key which can be obtained as you signup for beem-official website.

#### Do this to Authenticate !!

```python3
>>> from BeemAfrica import Authorize, AirTime, OTP, SMS
>>> Authorize('access-key', 'secret-key')
```

### Sending SMS with BeemAfrica

To send SMS with beem africa now made easy, you can use single method to send single and multiple messages at once.

Here how you would send a single SMS with beem-africa, Note that I'm assuming you have already entered the correct access-key and secret-key

```python
>>> SMS.send_sms('hello pythonista', '255xxxxxxxxxx')
{'successful': True, 'request_id': 35918915, 'code': 100, 'message': 'Message Submitted Successfully', 'valid': 1, 'invalid': 0, 'duplicates': 0}
```

The above example is that I'm assuming you're using default BeemAfrica sender ID to use yours just do this instead;

```python
>>> SMS.send_sms(
        'You\'re now verified',
        '255xxxxxxxxx', 
        sender_id='new-sender-id'
        )

{'successful': True, 'request_id': 35918915, 'code': 100, 'message': 'Message Submitted Successfully', 'valid': 1, 'invalid': 0, 'duplicates': 0}
```

You can also schedule message to be sent after a certain time or at a specific time to do that together with new sender_id, do this instead !!

```python
>>> SMS.send_sms(
        'You have won a 10 Million', 
        '2557xxxxxxxxx', 
        sender_id='new-sender-d', 
        schedule_time='scheduled time'
    )
{'successful': True, 'request_id': 35918915, 'code': 100, 'message': 'Message Submitted Successfully', 'valid': 1, 'invalid': 0, 'duplicates': 0}
```

Also instead of sending to one recipient per time you can send an SMS to Multiple clients at Once you just have to twist the send_sms() to look like this;

```python
>>> SMS.send_sms('my-message', ['2557xxxxxx', '2557xxxxxx'])
```

## Verifying One Time password with BeemAfrica

Apart from just sending SMS, Beem also provides OTP Services for One Time password verification system that is expected to be expired after a certain time that has been specified.

You can also use OTP to do 2-factor-authentication system to your app/website, Beem will generate a random OTP for you and provide you an endpoint to verify it.

Here how to send OTP with Beem !!

```python
>>> OTP.send_otp('2557xxxxxx')
{'data': {'pinId': '4a5c2141-c965-4a9d-aca4-54f58063e831', 'message': {'code': 100, 'message': 'SMS sent successfully'}}}
```

To verify the OTP send to user do this !!
 
Note:  Use pin_id from response you just recieve while sending an OTP and the PIN sent to user phone to verify the OTP, its going to look like this !!


```python
>>> OTP.verify(pin_id='4a5c2141-c965-4a9d-aca4-54f58063e831', pin='122496')
{'data': {'message': {'code': 117, 'message': 'Valid Pin'}}}
```


## AirTime

BeemAfrica also provide interface to interact with AirTime allowing you to easily transfer AirTime from BeemAfrica Credit to customer mobile !!

Here how to Transfer AirTime to customer mobile with Beem Africa !!

```python
>>> AirTime.transfer_airtime('255757294146', 100)
{'code': 200, 'transaction_id': 1619484193194, 'message': 'Disbursement is in progress'}
```

By doing that now after few seconds check AirTime balance on mobile and it going to increase by +100 .

You can also check balance of remaining credit balance by doing this

```python
>>> AirTime.get_credit_balance()
{'data': {'credit_bal': '708.0357'}}
```

Well these are the only implemented features by now !


## Issues

Are you facing any issue with the integration of beem-africa libray, please raise an Issue so as we can fix as soon as we can !!

## Contribution ?

Would you like to contribute to beem-africa python-client, Contributions of any kind is really welcomed, just fork it .. you can also reach me direct if you face any issue with contributing at isaaackeinstein(at)gmail(dot)com.

## Give it star ?

Was this repository useful to you in any means, well then give it a star so as more people can get to know it.


## Credits

All the credits to [kalebu](https://github.com/kalebu) and all the future contributors