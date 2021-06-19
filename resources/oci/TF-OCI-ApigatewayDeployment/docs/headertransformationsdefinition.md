# TF::OCI::ApigatewayDeployment HeaderTransformationsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#filterheaders" title="FilterHeaders">FilterHeaders</a>" : <i>[ <a href="filterheadersdefinition.md">FilterHeadersDefinition</a>, ... ]</i>,
    "<a href="#renameheaders" title="RenameHeaders">RenameHeaders</a>" : <i>[ <a href="renameheadersdefinition.md">RenameHeadersDefinition</a>, ... ]</i>,
    "<a href="#setheaders" title="SetHeaders">SetHeaders</a>" : <i>[ <a href="setheadersdefinition.md">SetHeadersDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#filterheaders" title="FilterHeaders">FilterHeaders</a>: <i>
      - <a href="filterheadersdefinition.md">FilterHeadersDefinition</a></i>
<a href="#renameheaders" title="RenameHeaders">RenameHeaders</a>: <i>
      - <a href="renameheadersdefinition.md">RenameHeadersDefinition</a></i>
<a href="#setheaders" title="SetHeaders">SetHeaders</a>: <i>
      - <a href="setheadersdefinition.md">SetHeadersDefinition</a></i>
</pre>

## Properties

#### FilterHeaders

_Required_: No

_Type_: List of <a href="filterheadersdefinition.md">FilterHeadersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RenameHeaders

_Required_: No

_Type_: List of <a href="renameheadersdefinition.md">RenameHeadersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetHeaders

_Required_: No

_Type_: List of <a href="setheadersdefinition.md">SetHeadersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

