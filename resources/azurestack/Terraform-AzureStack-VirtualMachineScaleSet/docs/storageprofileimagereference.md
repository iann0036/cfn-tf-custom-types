# Terraform::AzureStack::VirtualMachineScaleSet StorageProfileImageReference

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#offer" title="Offer">Offer</a>" : <i>String</i>,
    "<a href="#publisher" title="Publisher">Publisher</a>" : <i>String</i>,
    "<a href="#sku" title="Sku">Sku</a>" : <i>String</i>,
    "<a href="#version" title="Version">Version</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#offer" title="Offer">Offer</a>: <i>String</i>
<a href="#publisher" title="Publisher">Publisher</a>: <i>String</i>
<a href="#sku" title="Sku">Sku</a>: <i>String</i>
<a href="#version" title="Version">Version</a>: <i>String</i>
</pre>

## Properties

#### Id

Specifies the ID of the (custom) image to use to create the virtual
machine scale set, as in the [example below](#example-of-storage_profile_image_reference-with-id).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Offer

Specifies the offer of the image used to create the virtual machines.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Publisher

Specifies the publisher of the image used to create the virtual machines.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sku

Specifies the SKU of the image used to create the virtual machines.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

Specifies the version of the image used to create the virtual machines.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

