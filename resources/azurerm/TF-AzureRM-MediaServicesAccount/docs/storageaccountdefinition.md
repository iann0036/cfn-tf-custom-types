# TF::AzureRM::MediaServicesAccount StorageAccountDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#isprimary" title="IsPrimary">IsPrimary</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#isprimary" title="IsPrimary">IsPrimary</a>: <i>Boolean</i>
</pre>

## Properties

#### Id

Specifies the ID of the Storage Account that will be associated with the Media Services instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsPrimary

Specifies whether the storage account should be the primary account or not. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

