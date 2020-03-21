# Terraform::HuaweiCloud::AsPolicyV1 ScalingPolicyAction

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#instancenumber" title="InstanceNumber">InstanceNumber</a>" : <i>Double</i>,
    "<a href="#operation" title="Operation">Operation</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#instancenumber" title="InstanceNumber">InstanceNumber</a>: <i>Double</i>
<a href="#operation" title="Operation">Operation</a>: <i>String</i>
</pre>

## Properties

#### InstanceNumber

The number of instances to be operated. The default number is 1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Operation

The operation to be performed. The options include `ADD` (default), `REMOVE`,
and `SET`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

