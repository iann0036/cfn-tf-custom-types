# TF::Dome9::CloudaccountKubernetes

This resource used to onboard kubernetes cloud accounts to Dome9. This is the first and pre-requisite step in order to apply Dome9 kubernetes features on the account.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Dome9::CloudaccountKubernetes",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#organizationalunitid" title="OrganizationalUnitId">OrganizationalUnitId</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Dome9::CloudaccountKubernetes
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#organizationalunitid" title="OrganizationalUnitId">OrganizationalUnitId</a>: <i>String</i>
</pre>

## Properties

#### Name

The name of the kubernetes cluster as it will appear in Dome9 kubernetes cloud account.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrganizationalUnitId

The Organizational Unit this cloud account will be attached to.

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

#### ClusterVersion

Returns the <code>ClusterVersion</code> value.

#### CreationDate

Returns the <code>CreationDate</code> value.

#### Id

Returns the <code>Id</code> value.

#### OrganizationalUnitName

Returns the <code>OrganizationalUnitName</code> value.

#### OrganizationalUnitPath

Returns the <code>OrganizationalUnitPath</code> value.

#### Vendor

Returns the <code>Vendor</code> value.

