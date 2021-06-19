# TF::AzureRM::DnsMxRecord RecordDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#exchange" title="Exchange">Exchange</a>" : <i>String</i>,
    "<a href="#preference" title="Preference">Preference</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#exchange" title="Exchange">Exchange</a>: <i>String</i>
<a href="#preference" title="Preference">Preference</a>: <i>String</i>
</pre>

## Properties

#### Exchange

The mail server responsible for the domain covered by the MX record.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Preference

String representing the "preference” value of the MX records. Records with lower preference value take priority.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

