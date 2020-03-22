# Terraform::VCD::Vapp

Provides a vCloud Director vApp resource. This can be used to create, modify, and delete vApps.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::VCD::Vapp",
    "Properties" : {
        "<a href="#acceptalleulas" title="AcceptAllEulas">AcceptAllEulas</a>" : <i>Boolean</i>,
        "<a href="#catalogname" title="CatalogName">CatalogName</a>" : <i>String</i>,
        "<a href="#cpus" title="Cpus">Cpus</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#guestproperties" title="GuestProperties">GuestProperties</a>" : <i>[ <a href="guestproperties.md">GuestProperties</a>, ... ]</i>,
        "<a href="#initscript" title="Initscript">Initscript</a>" : <i>String</i>,
        "<a href="#ip" title="Ip">Ip</a>" : <i>String</i>,
        "<a href="#memory" title="Memory">Memory</a>" : <i>Double</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadata.md">Metadata</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networkname" title="NetworkName">NetworkName</a>" : <i>String</i>,
        "<a href="#org" title="Org">Org</a>" : <i>String</i>,
        "<a href="#ovf" title="Ovf">Ovf</a>" : <i>[ <a href="ovf.md">Ovf</a>, ... ]</i>,
        "<a href="#poweron" title="PowerOn">PowerOn</a>" : <i>Boolean</i>,
        "<a href="#storageprofile" title="StorageProfile">StorageProfile</a>" : <i>String</i>,
        "<a href="#templatename" title="TemplateName">TemplateName</a>" : <i>String</i>,
        "<a href="#vdc" title="Vdc">Vdc</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::VCD::Vapp
Properties:
    <a href="#acceptalleulas" title="AcceptAllEulas">AcceptAllEulas</a>: <i>Boolean</i>
    <a href="#catalogname" title="CatalogName">CatalogName</a>: <i>String</i>
    <a href="#cpus" title="Cpus">Cpus</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#guestproperties" title="GuestProperties">GuestProperties</a>: <i>
      - <a href="guestproperties.md">GuestProperties</a></i>
    <a href="#initscript" title="Initscript">Initscript</a>: <i>String</i>
    <a href="#ip" title="Ip">Ip</a>: <i>String</i>
    <a href="#memory" title="Memory">Memory</a>: <i>Double</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadata.md">Metadata</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networkname" title="NetworkName">NetworkName</a>: <i>String</i>
    <a href="#org" title="Org">Org</a>: <i>String</i>
    <a href="#ovf" title="Ovf">Ovf</a>: <i>
      - <a href="ovf.md">Ovf</a></i>
    <a href="#poweron" title="PowerOn">PowerOn</a>: <i>Boolean</i>
    <a href="#storageprofile" title="StorageProfile">StorageProfile</a>: <i>String</i>
    <a href="#templatename" title="TemplateName">TemplateName</a>: <i>String</i>
    <a href="#vdc" title="Vdc">Vdc</a>: <i>String</i>
</pre>

## Properties

#### AcceptAllEulas

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CatalogName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cpus

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuestProperties

Key value map of vApp guest properties.

_Required_: No

_Type_: List of <a href="guestproperties.md">GuestProperties</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Initscript

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Memory

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

Key value map of metadata to assign to this vApp. Key and value can be any string. (Since *v2.2+* metadata is added directly to vApp instead of first VM in vApp).

_Required_: No

_Type_: List of <a href="metadata.md">Metadata</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A unique name for the vApp.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Org

The name of organization to use, optional if defined at provider level. Useful when connected as sysadmin working across different organisations.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ovf

_Required_: No

_Type_: List of <a href="ovf.md">Ovf</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PowerOn

A boolean value stating if this vApp should be powered on. Default is `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageProfile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdc

The name of VDC to use, optional if defined at provider level.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Href

The vApp Hyper Reference.

#### Id

Returns the <code>Id</code> value.

#### Status

The vApp status as a numeric code.

#### StatusText

The vApp status as text.

