# TF::AWS::ApprunnerService ImageRepositoryDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#imageidentifier" title="ImageIdentifier">ImageIdentifier</a>" : <i>String</i>,
    "<a href="#imagerepositorytype" title="ImageRepositoryType">ImageRepositoryType</a>" : <i>String</i>,
    "<a href="#imageconfiguration" title="ImageConfiguration">ImageConfiguration</a>" : <i>[ <a href="imageconfigurationdefinition.md">ImageConfigurationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#imageidentifier" title="ImageIdentifier">ImageIdentifier</a>: <i>String</i>
<a href="#imagerepositorytype" title="ImageRepositoryType">ImageRepositoryType</a>: <i>String</i>
<a href="#imageconfiguration" title="ImageConfiguration">ImageConfiguration</a>: <i>
      - <a href="imageconfigurationdefinition.md">ImageConfigurationDefinition</a></i>
</pre>

## Properties

#### ImageIdentifier

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageRepositoryType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageConfiguration

_Required_: No

_Type_: List of <a href="imageconfigurationdefinition.md">ImageConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

