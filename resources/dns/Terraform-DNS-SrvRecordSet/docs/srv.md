# Terraform::DNS::SrvRecordSet Srv

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
    "<a href="#target" title="Target">Target</a>" : <i>String</i>,
    "<a href="#weight" title="Weight">Weight</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#priority" title="Priority">Priority</a>: <i>Double</i>
<a href="#target" title="Target">Target</a>: <i>String</i>
<a href="#weight" title="Weight">Weight</a>: <i>Double</i>
</pre>

## Properties

#### Port

The port for the service on the target.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

The priority for the record.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Target

The FQDN of the target, include the trailing dot.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Weight

The weight for the record.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

