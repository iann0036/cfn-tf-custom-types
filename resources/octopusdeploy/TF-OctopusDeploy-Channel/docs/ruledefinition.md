# TF::OctopusDeploy::Channel RuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#tag" title="Tag">Tag</a>" : <i>String</i>,
    "<a href="#versionrange" title="VersionRange">VersionRange</a>" : <i>String</i>,
    "<a href="#actionpackage" title="ActionPackage">ActionPackage</a>" : <i>[ <a href="actionpackagedefinition.md">ActionPackageDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#tag" title="Tag">Tag</a>: <i>String</i>
<a href="#versionrange" title="VersionRange">VersionRange</a>: <i>String</i>
<a href="#actionpackage" title="ActionPackage">ActionPackage</a>: <i>
      - <a href="actionpackagedefinition.md">ActionPackageDefinition</a></i>
</pre>

## Properties

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionRange

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionPackage

_Required_: No

_Type_: List of <a href="actionpackagedefinition.md">ActionPackageDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

