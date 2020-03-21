# Terraform::VCD::IndependentDisk

Provides a vCloud Director independent disk resource. This can be used to create and delete independent disks.

Supported in provider *v2.1+*

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::VCD::IndependentDisk",
    "Properties" : {
        "<a href="#bussubtype" title="BusSubType">BusSubType</a>" : <i>String</i>,
        "<a href="#bustype" title="BusType">BusType</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#org" title="Org">Org</a>" : <i>String</i>,
        "<a href="#size" title="Size">Size</a>" : <i>Double</i>,
        "<a href="#storageprofile" title="StorageProfile">StorageProfile</a>" : <i>String</i>,
        "<a href="#vdc" title="Vdc">Vdc</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::VCD::IndependentDisk
Properties:
    <a href="#bussubtype" title="BusSubType">BusSubType</a>: <i>String</i>
    <a href="#bustype" title="BusType">BusType</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#org" title="Org">Org</a>: <i>String</i>
    <a href="#size" title="Size">Size</a>: <i>Double</i>
    <a href="#storageprofile" title="StorageProfile">StorageProfile</a>: <i>String</i>
    <a href="#vdc" title="Vdc">Vdc</a>: <i>String</i>
</pre>

## Properties

#### BusSubType

Disk bus subtype. Values can be: `buslogic`, `lsilogic`, `lsilogicsas`, `VirtualSCSI` for `SCSI` and `ahci` for `SATA`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BusType

Disk bus type. Values can be: `IDE`, `SCSI`, `SATA`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Disk name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Org

The name of organization to use, optional if defined at provider level. Useful when connected as sysadmin working across different organisations.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

Size of disk in MB. On read this values isn't refreshed.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageProfile

The name of storage profile where disk will be created.

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

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### DatastoreName

Returns the <code>DatastoreName</code> value.

#### Iops

Returns the <code>Iops</code> value.

#### IsAttached

Returns the <code>IsAttached</code> value.

#### OwnerName

Returns the <code>OwnerName</code> value.

