# Terraform::HuaweiCloud::ApiGatewayApi RequestParameter

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#default" title="Default">Default</a>" : <i>String</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#location" title="Location">Location</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#required" title="Required">Required</a>" : <i>Boolean</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#default" title="Default">Default</a>: <i>String</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#location" title="Location">Location</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#required" title="Required">Required</a>: <i>Boolean</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### Default

Specifies the default value when the parameter is optional.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Specifies the description of the parameter. The description cannot exceed 255 characters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

Specifies the input parameter location, which can be 'PATH', 'QUERY' or 'HEADER'.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the input parameter name. A parameter name consists of 1–32 characters, starting with a letter.
Only letters, digits, periods (.), hyphens (-), and underscores (_) are allowed.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Required

Specifies whether the parameter is mandatory or not.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Specifies the input parameter type, which can be 'STRING' or 'NUMBER'.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

