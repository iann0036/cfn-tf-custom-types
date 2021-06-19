# TF::CheckPoint::ManagementWhereUsed

This command resource allows you to execute Check Point Where Used.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::CheckPoint::ManagementWhereUsed",
    "Properties" : {
        "<a href="#dereferencegroupmembers" title="DereferenceGroupMembers">DereferenceGroupMembers</a>" : <i>Boolean</i>,
        "<a href="#indirect" title="Indirect">Indirect</a>" : <i>Boolean</i>,
        "<a href="#indirectmaxdepth" title="IndirectMaxDepth">IndirectMaxDepth</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#showmembership" title="ShowMembership">ShowMembership</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::CheckPoint::ManagementWhereUsed
Properties:
    <a href="#dereferencegroupmembers" title="DereferenceGroupMembers">DereferenceGroupMembers</a>: <i>Boolean</i>
    <a href="#indirect" title="Indirect">Indirect</a>: <i>Boolean</i>
    <a href="#indirectmaxdepth" title="IndirectMaxDepth">IndirectMaxDepth</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#showmembership" title="ShowMembership">ShowMembership</a>: <i>Boolean</i>
</pre>

## Properties

#### DereferenceGroupMembers

Indicates whether to dereference "members" field by details level for every object in reply.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Indirect

Search for indirect usage.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IndirectMaxDepth

Maximum nesting level during indirect usage search.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Object name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShowMembership

Indicates whether to calculate and show "groups" field for every object in reply.

_Required_: No

_Type_: Boolean

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

