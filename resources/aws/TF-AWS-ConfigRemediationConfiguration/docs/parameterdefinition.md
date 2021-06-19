# TF::AWS::ConfigRemediationConfiguration ParameterDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#resourcevalue" title="ResourceValue">ResourceValue</a>" : <i>String</i>,
    "<a href="#staticvalue" title="StaticValue">StaticValue</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#resourcevalue" title="ResourceValue">ResourceValue</a>: <i>String</i>
<a href="#staticvalue" title="StaticValue">StaticValue</a>: <i>String</i>
</pre>

## Properties

#### Name

The name of the attribute.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceValue

The value is dynamic and changes at run-time.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticValue

The value is static and does not change at run-time.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

