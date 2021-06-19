# TF::AzureAD::GroupMember

Manages a single Group Membership within Azure Active Directory.

-> **NOTE:** Do not use this resource at the same time as `azuread_group.members`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureAD::GroupMember",
    "Properties" : {
        "<a href="#groupobjectid" title="GroupObjectId">GroupObjectId</a>" : <i>String</i>,
        "<a href="#memberobjectid" title="MemberObjectId">MemberObjectId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureAD::GroupMember
Properties:
    <a href="#groupobjectid" title="GroupObjectId">GroupObjectId</a>: <i>String</i>
    <a href="#memberobjectid" title="MemberObjectId">MemberObjectId</a>: <i>String</i>
</pre>

## Properties

#### GroupObjectId

The Object ID of the Azure AD Group you want to add the Member to.  Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemberObjectId

The Object ID of the Azure AD Object you want to add as a Member to the Group. Supported Object types are Users, Groups or Service Principals. Changing this forces a new resource to be created.

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

#### Id

Returns the <code>Id</code> value.

