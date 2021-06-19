# TF::AzureRM::ApiManagementApiOperation ResponseDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#statuscode" title="StatusCode">StatusCode</a>" : <i>Double</i>,
    "<a href="#header" title="Header">Header</a>" : <i>[ <a href="headerdefinition.md">HeaderDefinition</a>, ... ]</i>,
    "<a href="#representation" title="Representation">Representation</a>" : <i>[ <a href="representationdefinition.md">RepresentationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#statuscode" title="StatusCode">StatusCode</a>: <i>Double</i>
<a href="#header" title="Header">Header</a>: <i>
      - <a href="headerdefinition.md">HeaderDefinition</a></i>
<a href="#representation" title="Representation">Representation</a>: <i>
      - <a href="representationdefinition.md">RepresentationDefinition</a></i>
</pre>

## Properties

#### Description

A description of the HTTP Response, which may include HTML tags.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatusCode

The HTTP Status Code.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Header

_Required_: No

_Type_: List of <a href="headerdefinition.md">HeaderDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Representation

_Required_: No

_Type_: List of <a href="representationdefinition.md">RepresentationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

