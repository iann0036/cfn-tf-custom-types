# Terraform::AzureRM::EventgridDomain InputMappingFields

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dataversion" title="DataVersion">DataVersion</a>" : <i>String</i>,
    "<a href="#eventtime" title="EventTime">EventTime</a>" : <i>String</i>,
    "<a href="#eventtype" title="EventType">EventType</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#subject" title="Subject">Subject</a>" : <i>String</i>,
    "<a href="#topic" title="Topic">Topic</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#dataversion" title="DataVersion">DataVersion</a>: <i>String</i>
<a href="#eventtime" title="EventTime">EventTime</a>: <i>String</i>
<a href="#eventtype" title="EventType">EventType</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#subject" title="Subject">Subject</a>: <i>String</i>
<a href="#topic" title="Topic">Topic</a>: <i>String</i>
</pre>

## Properties

#### DataVersion

Specifies the data version of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventTime

Specifies the event time of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventType

Specifies the event type of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

Specifies the id of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subject

Specifies the subject of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Topic

Specifies the topic of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

