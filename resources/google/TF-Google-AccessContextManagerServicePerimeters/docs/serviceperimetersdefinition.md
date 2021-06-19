# TF::Google::AccessContextManagerServicePerimeters ServicePerimetersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#perimetertype" title="PerimeterType">PerimeterType</a>" : <i>String</i>,
    "<a href="#title" title="Title">Title</a>" : <i>String</i>,
    "<a href="#useexplicitdryrunspec" title="UseExplicitDryRunSpec">UseExplicitDryRunSpec</a>" : <i>Boolean</i>,
    "<a href="#spec" title="Spec">Spec</a>" : <i>[ <a href="specdefinition.md">SpecDefinition</a>, ... ]</i>,
    "<a href="#status" title="Status">Status</a>" : <i>[ <a href="statusdefinition.md">StatusDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#perimetertype" title="PerimeterType">PerimeterType</a>: <i>String</i>
<a href="#title" title="Title">Title</a>: <i>String</i>
<a href="#useexplicitdryrunspec" title="UseExplicitDryRunSpec">UseExplicitDryRunSpec</a>: <i>Boolean</i>
<a href="#spec" title="Spec">Spec</a>: <i>
      - <a href="specdefinition.md">SpecDefinition</a></i>
<a href="#status" title="Status">Status</a>: <i>
      - <a href="statusdefinition.md">StatusDefinition</a></i>
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

#### PerimeterType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseExplicitDryRunSpec

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Spec

_Required_: No

_Type_: List of <a href="specdefinition.md">SpecDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: No

_Type_: List of <a href="statusdefinition.md">StatusDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

