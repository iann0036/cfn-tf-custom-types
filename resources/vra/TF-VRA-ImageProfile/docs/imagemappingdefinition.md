# TF::VRA::ImageProfile ImageMappingDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cloudconfig" title="CloudConfig">CloudConfig</a>" : <i>String</i>,
    "<a href="#imageid" title="ImageId">ImageId</a>" : <i>String</i>,
    "<a href="#imagename" title="ImageName">ImageName</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#constraints" title="Constraints">Constraints</a>" : <i>[ <a href="constraintsdefinition.md">ConstraintsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cloudconfig" title="CloudConfig">CloudConfig</a>: <i>String</i>
<a href="#imageid" title="ImageId">ImageId</a>: <i>String</i>
<a href="#imagename" title="ImageName">ImageName</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#constraints" title="Constraints">Constraints</a>: <i>
      - <a href="constraintsdefinition.md">ConstraintsDefinition</a></i>
</pre>

## Properties

#### CloudConfig

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Constraints

_Required_: No

_Type_: List of <a href="constraintsdefinition.md">ConstraintsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

