# TF::AzureRM::MonitorActionGroup SmsReceiverDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#countrycode" title="CountryCode">CountryCode</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#phonenumber" title="PhoneNumber">PhoneNumber</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#countrycode" title="CountryCode">CountryCode</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#phonenumber" title="PhoneNumber">PhoneNumber</a>: <i>String</i>
</pre>

## Properties

#### CountryCode

The country code of the SMS receiver.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the SMS receiver. Names must be unique (case-insensitive) across all receivers within an action group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PhoneNumber

The phone number of the SMS receiver.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

