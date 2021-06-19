# TF::OpsGenie::NotificationRule ContactDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#method" title="Method">Method</a>" : <i>String</i>,
    "<a href="#to" title="To">To</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#method" title="Method">Method</a>: <i>String</i>
<a href="#to" title="To">To</a>: <i>String</i>
</pre>

## Properties

#### Method

Contact method. Possible values: `email`, `sms`, `voice`, `mobile`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### To

Address of a given method (eg. email address for `email`, phone number for `sms`/`voice` or mobile application name for `mobile`).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

