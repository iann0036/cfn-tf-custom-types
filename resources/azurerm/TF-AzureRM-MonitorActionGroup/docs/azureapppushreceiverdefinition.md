# TF::AzureRM::MonitorActionGroup AzureAppPushReceiverDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#emailaddress" title="EmailAddress">EmailAddress</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#emailaddress" title="EmailAddress">EmailAddress</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### EmailAddress

The email address of the user signed into the mobile app who will receive push notifications from this receiver.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Azure app push receiver.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

