# Terraform::AzureRM::DevTestLinuxVirtualMachine GalleryImageReference

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#offer" title="Offer">Offer</a>" : <i>String</i>,
    "<a href="#publisher" title="Publisher">Publisher</a>" : <i>String</i>,
    "<a href="#sku" title="Sku">Sku</a>" : <i>String</i>,
    "<a href="#version" title="Version">Version</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#offer" title="Offer">Offer</a>: <i>String</i>
<a href="#publisher" title="Publisher">Publisher</a>: <i>String</i>
<a href="#sku" title="Sku">Sku</a>: <i>String</i>
<a href="#version" title="Version">Version</a>: <i>String</i>
</pre>

## Properties

#### Offer

The Offer of the Gallery Image. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Publisher

The Publisher of the Gallery Image. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sku

The SKU of the Gallery Image. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

The Version of the Gallery Image. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

