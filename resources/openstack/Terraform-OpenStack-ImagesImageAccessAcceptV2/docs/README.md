# Terraform::OpenStack::ImagesImageAccessAcceptV2

Manages memberships status for the shared OpenStack Glance V2 Image within the
destination project, which has a member proposal.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenStack::ImagesImageAccessAcceptV2",
    "Properties" : {
        "<a href="#imageid" title="ImageId">ImageId</a>" : <i>String</i>,
        "<a href="#memberid" title="MemberId">MemberId</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenStack::ImagesImageAccessAcceptV2
Properties:
    <a href="#imageid" title="ImageId">ImageId</a>: <i>String</i>
    <a href="#memberid" title="MemberId">MemberId</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
</pre>

## Properties

#### ImageId

The proposed image ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemberId

The member ID, e.g. the target project ID. Optional
for admin accounts. Defaults to the current scope project ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region in which to obtain the V2 Glance client.
A Glance client is needed to manage Image memberships. If omitted, the
`region` argument of the provider is used. Changing this creates a new
membership.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

The membership proposal status. Can either be
`accepted`, `rejected` or `pending`.

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

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### Schema

Returns the <code>Schema</code> value.

#### UpdatedAt

Returns the <code>UpdatedAt</code> value.

