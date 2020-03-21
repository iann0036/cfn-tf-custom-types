# Terraform::AzureRM::ApiManagementApiOperation Request

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#header" title="Header">Header</a>" : <i>[ <a href="request-header.md">Header</a>, ... ]</i>,
    "<a href="#queryparameter" title="QueryParameter">QueryParameter</a>" : <i>[ <a href="request-queryparameter.md">QueryParameter</a>, ... ]</i>,
    "<a href="#representation" title="Representation">Representation</a>" : <i>[ <a href="request-representation.md">Representation</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#header" title="Header">Header</a>: <i>
      - <a href="request-header.md">Header</a></i>
<a href="#queryparameter" title="QueryParameter">QueryParameter</a>: <i>
      - <a href="request-queryparameter.md">QueryParameter</a></i>
<a href="#representation" title="Representation">Representation</a>: <i>
      - <a href="request-representation.md">Representation</a></i>
</pre>

## Properties

#### Description

A description of the HTTP Request, which may include HTML tags.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Header

_Required_: No

_Type_: List of <a href="request-header.md">Header</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryParameter

_Required_: No

_Type_: List of <a href="request-queryparameter.md">QueryParameter</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Representation

_Required_: No

_Type_: List of <a href="request-representation.md">Representation</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

