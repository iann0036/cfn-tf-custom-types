# TF::AzureRM::ServiceFabricMeshApplication ServiceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#ostype" title="OsType">OsType</a>" : <i>String</i>,
    "<a href="#codepackage" title="CodePackage">CodePackage</a>" : <i>[ <a href="codepackagedefinition.md">CodePackageDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#ostype" title="OsType">OsType</a>: <i>String</i>
<a href="#codepackage" title="CodePackage">CodePackage</a>: <i>
      - <a href="codepackagedefinition.md">CodePackageDefinition</a></i>
</pre>

## Properties

#### Name

The name of the service resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsType

The operating system required by the code in service. Valid values are `Linux` or `Windows`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CodePackage

_Required_: No

_Type_: List of <a href="codepackagedefinition.md">CodePackageDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

