# python-tools

format text to xml

Execute
$echo '<note><to>Tove</to><from>Jani</from><heading>Reminder</heading><body>Dont forget me this weekend!</body></note>' | python formatxml.py

output
<note>
	<to>Tove</to>
	<from>Jani</from>
	<heading>Reminder</heading>
	<body>Dont forget me this weekend!</body>
</note>

