# Terraform::OCI::FileStorageExportSet

This resource provides the Export Set resource in Oracle Cloud Infrastructure File Storage service.

The export set resource can neither be directly created, nor destroyed.

An export set is created by the service automatically when a mount target is created.
When a mount target is deleted, the export set associated with it is also deleted automatically.

However, export sets expose a few attributes that can be updated.

Hence we provide this resource for managing the already created export set from within Terraform.
Only one export set resource should be created per mount target.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::FileStorageExportSet",
    "Properties" : {
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#maxfsstatbytes" title="MaxFsStatBytes">MaxFsStatBytes</a>" : <i>String</i>,
        "<a href="#maxfsstatfiles" title="MaxFsStatFiles">MaxFsStatFiles</a>" : <i>String</i>,
        "<a href="#mounttargetid" title="MountTargetId">MountTargetId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::FileStorageExportSet
Properties:
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#maxfsstatbytes" title="MaxFsStatBytes">MaxFsStatBytes</a>: <i>String</i>
    <a href="#maxfsstatfiles" title="MaxFsStatFiles">MaxFsStatFiles</a>: <i>String</i>
    <a href="#mounttargetid" title="MountTargetId">MountTargetId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### DisplayName

(Updatable) A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information.  Example: `My export set`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxFsStatBytes

(Updatable) Controls the maximum `tbytes`, `fbytes`, and `abytes`, values reported by `NFS FSSTAT` calls through any associated mount targets. This is an advanced feature. For most applications, use the default value. The `tbytes` value reported by `FSSTAT` will be `maxFsStatBytes`. The value of `fbytes` and `abytes` will be `maxFsStatBytes` minus the metered size of the file system. If the metered size is larger than `maxFsStatBytes`, then `fbytes` and `abytes` will both be '0'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxFsStatFiles

(Updatable) Controls the maximum `tfiles`, `ffiles`, and `afiles` values reported by `NFS FSSTAT` calls through any associated mount targets. This is an advanced feature. For most applications, use the default value. The `tfiles` value reported by `FSSTAT` will be `maxFsStatFiles`. The value of `ffiles` and `afiles` will be `maxFsStatFiles` minus the metered size of the file system. If the metered size is larger than `maxFsStatFiles`, then `ffiles` and `afiles` will both be '0'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MountTargetId

(Updatable) The OCID of the mount target that the export set is associated with.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AvailabilityDomain

Returns the <code>AvailabilityDomain</code> value.

#### CompartmentId

Returns the <code>CompartmentId</code> value.

#### Id

Returns the <code>Id</code> value.

#### State

Returns the <code>State</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

#### VcnId

Returns the <code>VcnId</code> value.

