from kafka import KafkaConsumer

consumer = KafkaConsumer('order_details', bootstrap_servers='localhost:29092')

print("Gonna start listening")
while True:
    for message in consumer:
        print("Here is a message..")
        print (message)