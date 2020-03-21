# Terraform::AzureRM::ApiManagementApiOperation Response

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#statuscode" title="StatusCode">StatusCode</a>" : <i>Double</i>,
    "<a href="#header" title="Header">Header</a>" : <i>[ <a href="response-header.md">Header</a>, ... ]</i>,
    "<a href="#representation" title="Representation">Representation</a>" : <i>[ <a href="response-representation.md">Representation</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#statuscode" title="StatusCode">StatusCode</a>: <i>Double</i>
<a href="#header" title="Header">Header</a>: <i>
      - <a href="response-header.md">Header</a></i>
<a href="#representation" title="Representation">Representation</a>: <i>
      - <a href="response-representation.md">Representation</a></i>
</pre>

## Properties

#### Description

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatusCode

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Header

_Required_: No
_Type_: List of <a href="response-header.md">Header</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Representation

_Required_: No
_Type_: List of <a href="response-representation.md">Representation</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

