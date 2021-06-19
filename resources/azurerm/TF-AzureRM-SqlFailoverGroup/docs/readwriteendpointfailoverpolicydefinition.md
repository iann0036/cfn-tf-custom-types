# TF::AzureRM::SqlFailoverGroup ReadWriteEndpointFailoverPolicyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#graceminutes" title="GraceMinutes">GraceMinutes</a>" : <i>Double</i>,
    "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#graceminutes" title="GraceMinutes">GraceMinutes</a>: <i>Double</i>
<a href="#mode" title="Mode">Mode</a>: <i>String</i>
</pre>

## Properties

#### GraceMinutes

Applies only if `mode` is `Automatic`. The grace period in minutes before failover with data loss is attempted.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

the failover mode. Possible values are `Manual`, `Automatic`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

