# TF::CloudSigma::Acl

Provides a CloudSigma ACL resource. Access Control Lists (ACLs) can be used to
grant permissions to another user to manage your resources. Permissions can be
granted on servers, drives, network resources, and firewall policies.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::CloudSigma::Acl",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourceuri" title="ResourceUri">ResourceUri</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::CloudSigma::Acl
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourceuri" title="ResourceUri">ResourceUri</a>: <i>String</i>
</pre>

## Properties

#### Name

The name of the ACL.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceUri

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

