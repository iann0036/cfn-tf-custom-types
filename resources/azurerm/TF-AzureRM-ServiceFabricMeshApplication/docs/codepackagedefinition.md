# TF::AzureRM::ServiceFabricMeshApplication CodePackageDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#imagename" title="ImageName">ImageName</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#resources" title="Resources">Resources</a>" : <i>[ <a href="resourcesdefinition.md">ResourcesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#imagename" title="ImageName">ImageName</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#resources" title="Resources">Resources</a>: <i>
      - <a href="resourcesdefinition.md">ResourcesDefinition</a></i>
</pre>

## Properties

#### ImageName

The Container image the code package will use.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the code package.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resources

_Required_: No

_Type_: List of <a href="resourcesdefinition.md">ResourcesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

