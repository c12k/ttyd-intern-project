## Story A1
* hi
  - utter_hi

## Story A2
* bye
  - utter_bye

## Story G1
* hi
  - utter_hi
* facts{"org":"service" , "fact":"revenue" , "period":"2015"}
  - slot{"fact": "revenue"}
  - slot{"org": "service"}
  - slot{"period": "2015"}
  - get_facts
  - slot{"matches": "revenue is $7m"}
  - suggest
* clarify{"geo":"USA","period":"last 3 years"}
  - slot{"geo":"USA"}
  - slot{"period":"last 3 years"}
  - get_trends
  - suggest
* clarify{"period":"2013","timeunit":"monthly"}
  - slot{"period":"2013"}
  - slot{"timeunit":"monthly"}
  - get_facts
  - suggest
* clarify{"timeunit":"yearly","org":"Finance"}
  - slot{"timeunit":"yearly"}
  - slot{"org":"Finance"}
  - get_facts
  - suggest
* bye
  - utter_bye

## Story G2
* hi
  - utter_hi
* facts{"org":"service" , "fact":"revenue" , "period":"2015"}
  - slot{"fact": "revenue"}
  - slot{"org": "service"}
  - slot{"period": "2015"}
  - get_facts
  - slot{"matches": "revenue is $7m"}
  - suggest
* bye
  - utter_bye

## Story G3
* hi
  - utter_hi
* facts{"org":"service" , "fact":"revenue" , "period":"2015"}
  - slot{"fact": "revenue"}
  - slot{"org": "service"}
  - slot{"period": "2015"}
  - get_facts
  - slot{"matches": "revenue is $7m"}
  - suggest
* clarify{"org":"Finance","period":"2014"}
  - slot{"org":"Finance"}
  - slot{"period":"2014"}
  - get_facts
  - suggest
* clarify{"org":"Sales","timeunit":"monthly"}
  - slot{"org":"Sales"}
  - slot{"timeunit":"monthly"}
  - get_facts
  - suggest
* clarify{"period":"2013","fact":"expense"}
  - slot{"period":"2013"}
  - slot{"fact":"expense"}
  - get_facts
  - suggest
* bye
  - utter_bye

## Story G4
* hi
  - utter_hi
* facts{"org":"service" , "fact":"revenue" , "period":"2015"}
  - slot{"fact": "revenue"}
  - slot{"org": "service"}
  - slot{"period": "2015"}
  - get_facts
  - slot{"matches": "revenue is $7m"}
  - suggest
* bye
  - utter_bye

## Story G5
* hi
  - utter_hi
* facts{"org":"service" , "fact":"revenue" , "period":"2015"}
  - slot{"fact": "revenue"}
  - slot{"org": "service"}
  - slot{"period": "2015"}
  - get_facts
  - slot{"matches": "revenue is $7m"}
  - suggest
* clarify{"geo":"USA","fact":"profit"}
  - slot{"geo":"USA"}
  - slot{"fact":"profit"}
  - get_facts
  - suggest
* clarify{"period":"2013","geo":"Australia"}
  - slot{"period":"2013"}
  - slot{"geo":"Australia"}
  - get_facts
  - suggest
* clarify{"timeunit":"yearly","geo":"USA"}
  - slot{"timeunit":"yearly"}
  - slot{"geo":"USA"}
  - get_facts
  - suggest
* bye
  - utter_bye

## Story G6
* hi
  - utter_hi
* facts{"org":"service" , "fact":"revenue" , "period":"2015"}
  - slot{"fact": "revenue"}
  - slot{"org": "service"}
  - slot{"period": "2015"}
  - get_facts
  - slot{"matches": "revenue is $7m"}
  - suggest
* bye
  - utter_bye

## Story G7
* hi
  - utter_hi
* facts{"org":"service" , "fact":"revenue" , "period":"2015"}
  - slot{"fact": "revenue"}
  - slot{"org": "service"}
  - slot{"period": "2015"}
  - get_facts
  - slot{"matches": "revenue is $7m"}
  - suggest
* clarify{"period":"2014","fact":"profit"}
  - slot{"period":"2014"}
  - slot{"fact":"profit"}
  - get_facts
  - suggest
* clarify{"period":"2014","org":"Sales"}
  - slot{"period":"2014"}
  - slot{"org":"Sales"}
  - get_facts
  - suggest
* clarify{"org":"Finance","period":"last 3 years"}
  - slot{"org":"Finance"}
  - slot{"period":"last 3 years"}
  - get_trends
  - suggest
* bye
  - utter_bye

## Story G8
* hi
  - utter_hi
* facts{"org":"service" , "fact":"revenue" , "period":"2015"}
  - slot{"fact": "revenue"}
  - slot{"org": "service"}
  - slot{"period": "2015"}
  - get_facts
  - slot{"matches": "revenue is $7m"}
  - suggest
* bye
  - utter_bye

## Story G9
* hi
  - utter_hi
* facts{"org":"service" , "fact":"revenue" , "period":"2015"}
  - slot{"fact": "revenue"}
  - slot{"org": "service"}
  - slot{"period": "2015"}
  - get_facts
  - slot{"matches": "revenue is $7m"}
  - suggest
* clarify{"period":"2010","fact":"profit"}
  - slot{"period":"2010"}
  - slot{"fact":"profit"}
  - get_facts
  - suggest
* clarify{"org":"Sales","period":"2013"}
  - slot{"org":"Sales"}
  - slot{"period":"2013"}
  - get_facts
  - suggest
* clarify{"org":"Sales","fact":"expense"}
  - slot{"org":"Sales"}
  - slot{"fact":"expense"}
  - get_facts
  - suggest
* bye
  - utter_bye

## Story G10
* hi
  - utter_hi
* facts{"org":"service" , "fact":"revenue" , "period":"2015"}
  - slot{"fact": "revenue"}
  - slot{"org": "service"}
  - slot{"period": "2015"}
  - get_facts
  - slot{"matches": "revenue is $7m"}
  - suggest
* bye
  - utter_bye

## Story G11
* hi
  - utter_hi
* facts{"org":"service" , "fact":"revenue" , "period":"2015"}
  - slot{"fact": "revenue"}
  - slot{"org": "service"}
  - slot{"period": "2015"}
  - get_facts
  - slot{"matches": "revenue is $7m"}
  - suggest
* clarify{"fact":"revenue","org":"Sales"}
  - slot{"fact":"revenue"}
  - slot{"org":"Sales"}
  - get_facts
  - suggest
* clarify{"period":"2010","period":"2014"}
  - slot{"period":"2010"}
  - slot{"period":"2014"}
  - get_facts
  - suggest
* clarify{"timeunit":"yearly","fact":"profit"}
  - slot{"timeunit":"yearly"}
  - slot{"fact":"profit"}
  - get_facts
  - suggest
* bye
  - utter_bye

## Story G12
* hi
  - utter_hi
* facts{"org":"service" , "fact":"revenue" , "period":"2015"}
  - slot{"fact": "revenue"}
  - slot{"org": "service"}
  - slot{"period": "2015"}
  - get_facts
  - slot{"matches": "revenue is $7m"}
  - suggest
* bye
  - utter_bye

## Story G13
* hi
  - utter_hi
* facts{"org":"service" , "fact":"revenue" , "period":"2015"}
  - slot{"fact": "revenue"}
  - slot{"org": "service"}
  - slot{"period": "2015"}
  - get_facts
  - slot{"matches": "revenue is $7m"}
  - suggest
* clarify{"geo":"USA","timeunit":"yearly"}
  - slot{"geo":"USA"}
  - slot{"timeunit":"yearly"}
  - get_facts
  - suggest
* clarify{"org":"Sales","geo":"USA"}
  - slot{"org":"Sales"}
  - slot{"geo":"USA"}
  - get_facts
  - suggest
* clarify{"period":"2010","period":"2014"}
  - slot{"period":"2010"}
  - slot{"period":"2014"}
  - get_facts
  - suggest
* bye
  - utter_bye

## Story G14
* hi
  - utter_hi
* facts{"org":"service" , "fact":"revenue" , "period":"2015"}
  - slot{"fact": "revenue"}
  - slot{"org": "service"}
  - slot{"period": "2015"}
  - get_facts
  - slot{"matches": "revenue is $7m"}
  - suggest
* bye
  - utter_bye

## Story G15
* hi
  - utter_hi
* facts{"org":"service" , "fact":"revenue" , "period":"2015"}
  - slot{"fact": "revenue"}
  - slot{"org": "service"}
  - slot{"period": "2015"}
  - get_facts
  - slot{"matches": "revenue is $7m"}
  - suggest
* clarify{"org":"Legal","fact":"profit"}
  - slot{"org":"Legal"}
  - slot{"fact":"profit"}
  - get_facts
  - suggest
* clarify{"org":"Finance","period":"2014"}
  - slot{"org":"Finance"}
  - slot{"period":"2014"}
  - get_facts
  - suggest
* clarify{"org":"Finance","period":"2014"}
  - slot{"org":"Finance"}
  - slot{"period":"2014"}
  - get_facts
  - suggest
* bye
  - utter_bye

## Story G16
* hi
  - utter_hi
* facts{"org":"service" , "fact":"revenue" , "period":"2015"}
  - slot{"fact": "revenue"}
  - slot{"org": "service"}
  - slot{"period": "2015"}
  - get_facts
  - slot{"matches": "revenue is $7m"}
  - suggest
* bye
  - utter_bye

## Story G17
* hi
  - utter_hi
* facts{"org":"service" , "fact":"revenue" , "period":"2015"}
  - slot{"fact": "revenue"}
  - slot{"org": "service"}
  - slot{"period": "2015"}
  - get_facts
  - slot{"matches": "revenue is $7m"}
  - suggest
* clarify{"org":"Sales","geo":"USA"}
  - slot{"org":"Sales"}
  - slot{"geo":"USA"}
  - get_facts
  - suggest
* clarify{"geo":"USA","org":"Finance"}
  - slot{"geo":"USA"}
  - slot{"org":"Finance"}
  - get_facts
  - suggest
* clarify{"org":"Finance","fact":"revenue"}
  - slot{"org":"Finance"}
  - slot{"fact":"revenue"}
  - get_facts
  - suggest
* bye
  - utter_bye

## Story G18
* hi
  - utter_hi
* facts{"org":"service" , "fact":"revenue" , "period":"2015"}
  - slot{"fact": "revenue"}
  - slot{"org": "service"}
  - slot{"period": "2015"}
  - get_facts
  - slot{"matches": "revenue is $7m"}
  - suggest
* bye
  - utter_bye

## Story G19
* hi
  - utter_hi
* facts{"org":"service" , "fact":"revenue" , "period":"2015"}
  - slot{"fact": "revenue"}
  - slot{"org": "service"}
  - slot{"period": "2015"}
  - get_facts
  - slot{"matches": "revenue is $7m"}
  - suggest
* clarify{"timeunit":"monthly","period":"2014"}
  - slot{"timeunit":"monthly"}
  - slot{"period":"2014"}
  - get_facts
  - suggest
* clarify{"period":"2014","fact":"eps"}
  - slot{"period":"2014"}
  - slot{"fact":"eps"}
  - get_facts
  - suggest
* clarify{"org":"Sales","geo":"USA"}
  - slot{"org":"Sales"}
  - slot{"geo":"USA"}
  - get_facts
  - suggest
* bye
  - utter_bye

