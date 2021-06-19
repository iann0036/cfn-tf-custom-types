# TF::FortiOS::EmailfilterProfile MsnHotmailDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#log" title="Log">Log</a>" : <i>String</i>,
    "<a href="#logall" title="LogAll">LogAll</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#log" title="Log">Log</a>: <i>String</i>
<a href="#logall" title="LogAll">LogAll</a>: <i>String</i>
</pre>

## Properties

#### Log

Enable/disable logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogAll

Enable/disable logging of all email traffic. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

