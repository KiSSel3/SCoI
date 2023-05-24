from SerilizerKiselev import JsonSerializer
serializer_xml = JsonSerializer()
with open("test1.json", "w") as file:
        serializer_xml.dump(5, file)

