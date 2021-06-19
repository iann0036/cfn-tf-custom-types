# TF::Volterra::AwsVpcSite StorageClassesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#defaultstorageclass" title="DefaultStorageClass">DefaultStorageClass</a>" : <i>Boolean</i>,
    "<a href="#storageclassname" title="StorageClassName">StorageClassName</a>" : <i>String</i>,
    "<a href="#openebsenterprise" title="OpenebsEnterprise">OpenebsEnterprise</a>" : <i>[ <a href="openebsenterprisedefinition.md">OpenebsEnterpriseDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#defaultstorageclass" title="DefaultStorageClass">DefaultStorageClass</a>: <i>Boolean</i>
<a href="#storageclassname" title="StorageClassName">StorageClassName</a>: <i>String</i>
<a href="#openebsenterprise" title="OpenebsEnterprise">OpenebsEnterprise</a>: <i>
      - <a href="openebsenterprisedefinition.md">OpenebsEnterpriseDefinition</a></i>
</pre>

## Properties

#### DefaultStorageClass

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageClassName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenebsEnterprise

_Required_: No

_Type_: List of <a href="openebsenterprisedefinition.md">OpenebsEnterpriseDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

