# TF::Thunder::WriteMemory

`thunder_write_memory` Provides details about thunder write memory

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::WriteMemory",
    "Properties" : {
        "<a href="#destination" title="Destination">Destination</a>" : <i>String</i>,
        "<a href="#partition" title="Partition">Partition</a>" : <i>String</i>,
        "<a href="#profile" title="Profile">Profile</a>" : <i>String</i>,
        "<a href="#specifiedpartition" title="SpecifiedPartition">SpecifiedPartition</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::WriteMemory
Properties:
    <a href="#destination" title="Destination">Destination</a>: <i>String</i>
    <a href="#partition" title="Partition">Partition</a>: <i>String</i>
    <a href="#profile" title="Profile">Profile</a>: <i>String</i>
    <a href="#specifiedpartition" title="SpecifiedPartition">SpecifiedPartition</a>: <i>String</i>
</pre>

## Properties

#### Destination

‘primary’: Write to default Primary Configuration; ‘secondary’: Write to default Secondary Configuration; ‘local’: Local Configuration Profile Name;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Partition

‘all’: All partition configurations; ‘shared’: Shared partition; ‘specified’: Specified partition;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Profile

Local Configuration Profile Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpecifiedPartition

Specified partition.

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

#### Id

Returns the <code>Id</code> value.

