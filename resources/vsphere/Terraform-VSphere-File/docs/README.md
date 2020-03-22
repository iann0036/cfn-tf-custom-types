# Terraform::VSphere::File

The `vsphere_file` resource can be used to upload files (such as virtual disk
files) from the host machine that Terraform is running on to a target
datastore.  The resource can also be used to copy files between datastores, or
from one location to another on the same datastore.

Updates to destination parameters such as `datacenter`, `datastore`, or
`destination_file` will move the managed file a new destination based on the
values of the new settings.  If any source parameter is changed, such as
`source_datastore`, `source_datacenter` or `source_file`), the resource will be
re-created. Depending on if destination parameters are being changed as well,
this may result in the destination file either being overwritten or deleted at
the old location.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::VSphere::File",
    "Properties" : {
        "<a href="#createdirectories" title="CreateDirectories">CreateDirectories</a>" : <i>Boolean</i>,
        "<a href="#datacenter" title="Datacenter">Datacenter</a>" : <i>String</i>,
        "<a href="#datastore" title="Datastore">Datastore</a>" : <i>String</i>,
        "<a href="#destinationfile" title="DestinationFile">DestinationFile</a>" : <i>String</i>,
        "<a href="#sourcedatacenter" title="SourceDatacenter">SourceDatacenter</a>" : <i>String</i>,
        "<a href="#sourcedatastore" title="SourceDatastore">SourceDatastore</a>" : <i>String</i>,
        "<a href="#sourcefile" title="SourceFile">SourceFile</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::VSphere::File
Properties:
    <a href="#createdirectories" title="CreateDirectories">CreateDirectories</a>: <i>Boolean</i>
    <a href="#datacenter" title="Datacenter">Datacenter</a>: <i>String</i>
    <a href="#datastore" title="Datastore">Datastore</a>: <i>String</i>
    <a href="#destinationfile" title="DestinationFile">DestinationFile</a>: <i>String</i>
    <a href="#sourcedatacenter" title="SourceDatacenter">SourceDatacenter</a>: <i>String</i>
    <a href="#sourcedatastore" title="SourceDatastore">SourceDatastore</a>: <i>String</i>
    <a href="#sourcefile" title="SourceFile">SourceFile</a>: <i>String</i>
</pre>

## Properties

#### CreateDirectories

Create directories in `destination_file`
path parameter if any missing for copy operation.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Datacenter

The name of a datacenter in which the file will be
uploaded to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Datastore

The name of the datastore in which to upload the
file to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationFile

The path to where the file should be uploaded
or copied to on vSphere.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceDatacenter

The name of a datacenter in which the file
will be copied from. Forces a new resource if changed.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceDatastore

The name of the datastore in which file will
be copied from. Forces a new resource if changed.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceFile

The path to the file being uploaded from the
Terraform host to vSphere or copied within vSphere. Forces a new resource if
changed.

_Required_: Yes

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

#### Id

Returns the <code>Id</code> value.

