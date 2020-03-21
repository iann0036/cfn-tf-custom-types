# Terraform::AzureRM::StorageAccount BlobProperties

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#corsrule" title="CorsRule">CorsRule</a>" : <i>[ <a href="blobproperties-corsrule.md">CorsRule</a>, ... ]</i>,
    "<a href="#deleteretentionpolicy" title="DeleteRetentionPolicy">DeleteRetentionPolicy</a>" : <i>[ <a href="blobproperties-deleteretentionpolicy.md">DeleteRetentionPolicy</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#corsrule" title="CorsRule">CorsRule</a>: <i>
      - <a href="blobproperties-corsrule.md">CorsRule</a></i>
<a href="#deleteretentionpolicy" title="DeleteRetentionPolicy">DeleteRetentionPolicy</a>: <i>
      - <a href="blobproperties-deleteretentionpolicy.md">DeleteRetentionPolicy</a></i>
</pre>

## Properties

#### CorsRule

_Required_: No
_Type_: List of <a href="blobproperties-corsrule.md">CorsRule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteRetentionPolicy

_Required_: No
_Type_: List of <a href="blobproperties-deleteretentionpolicy.md">DeleteRetentionPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

