# TF::TencentCloud::ApiGatewayApi RequestParametersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#defaultvalue" title="DefaultValue">DefaultValue</a>" : <i>String</i>,
    "<a href="#desc" title="Desc">Desc</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#position" title="Position">Position</a>" : <i>String</i>,
    "<a href="#required" title="Required">Required</a>" : <i>Boolean</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#defaultvalue" title="DefaultValue">DefaultValue</a>: <i>String</i>
<a href="#desc" title="Desc">Desc</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#position" title="Position">Position</a>: <i>String</i>
<a href="#required" title="Required">Required</a>: <i>Boolean</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### DefaultValue

Parameter default value.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Desc

Parameter description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Parameter name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Position

Parameter location.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Required

If this parameter required. Default value: `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Parameter type.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

