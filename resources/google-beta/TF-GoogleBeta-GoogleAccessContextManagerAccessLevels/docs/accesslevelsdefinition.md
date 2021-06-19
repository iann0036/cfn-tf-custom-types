# TF::GoogleBeta::GoogleAccessContextManagerAccessLevels AccessLevelsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#title" title="Title">Title</a>" : <i>String</i>,
    "<a href="#basic" title="Basic">Basic</a>" : <i>[ <a href="basicdefinition.md">BasicDefinition</a>, ... ]</i>,
    "<a href="#custom" title="Custom">Custom</a>" : <i>[ <a href="customdefinition.md">CustomDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#title" title="Title">Title</a>: <i>String</i>
<a href="#basic" title="Basic">Basic</a>: <i>
      - <a href="basicdefinition.md">BasicDefinition</a></i>
<a href="#custom" title="Custom">Custom</a>: <i>
      - <a href="customdefinition.md">CustomDefinition</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Basic

_Required_: No

_Type_: List of <a href="basicdefinition.md">BasicDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Custom

_Required_: No

_Type_: List of <a href="customdefinition.md">CustomDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

