# TF::AWS::ImagebuilderDistributionConfiguration AmiDistributionConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#amitags" title="AmiTags">AmiTags</a>" : <i>[ <a href="amitagsdefinition.md">AmiTagsDefinition</a>, ... ]</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#targetaccountids" title="TargetAccountIds">TargetAccountIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#launchpermission" title="LaunchPermission">LaunchPermission</a>" : <i>[ <a href="launchpermissiondefinition.md">LaunchPermissionDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#amitags" title="AmiTags">AmiTags</a>: <i>
      - <a href="amitagsdefinition.md">AmiTagsDefinition</a></i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#targetaccountids" title="TargetAccountIds">TargetAccountIds</a>: <i>
      - String</i>
<a href="#launchpermission" title="LaunchPermission">LaunchPermission</a>: <i>
      - <a href="launchpermissiondefinition.md">LaunchPermissionDefinition</a></i>
</pre>

## Properties

#### AmiTags

_Required_: No

_Type_: List of <a href="amitagsdefinition.md">AmiTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKeyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetAccountIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchPermission

_Required_: No

_Type_: List of <a href="launchpermissiondefinition.md">LaunchPermissionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

