# TF::ECL::SssTenantV1

Manages a V1 tenant resource within Enterprise Cloud.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ECL::SssTenantV1",
    "Properties" : {
        "<a href="#contractid" title="ContractId">ContractId</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#tenantname" title="TenantName">TenantName</a>" : <i>String</i>,
        "<a href="#tenantregion" title="TenantRegion">TenantRegion</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ECL::SssTenantV1
Properties:
    <a href="#contractid" title="ContractId">ContractId</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#tenantname" title="TenantName">TenantName</a>: <i>String</i>
    <a href="#tenantregion" title="TenantRegion">TenantRegion</a>: <i>String</i>
</pre>

## Properties

#### ContractId

Contract which new tenant belongs to.
If this parameter is not designated, API user's contract
implicitly designated.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description for this tenant.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantName

Name of new tenant.
This name need to be unique globally.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRegion

Region this tenant belongs to.

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

#### StartTime

Returns the <code>StartTime</code> value.

#### TenantId

Returns the <code>TenantId</code> value.

