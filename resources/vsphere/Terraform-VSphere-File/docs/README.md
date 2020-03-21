# Terraform::VSphere::File

CloudFormation equivalent of vsphere_file

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

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Datacenter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Datastore

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationFile

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceDatacenter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceDatastore

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceFile

_Required_: Yes

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

