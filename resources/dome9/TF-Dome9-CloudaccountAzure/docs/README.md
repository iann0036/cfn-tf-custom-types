# TF::Dome9::CloudaccountAzure

This resource is used to onboard Azure cloud accounts to Dome9. This is the first and pre-requisite step in order to apply  Dome9 features, such as compliance testing, on the account.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Dome9::CloudaccountAzure",
    "Properties" : {
        "<a href="#clientid" title="ClientId">ClientId</a>" : <i>String</i>,
        "<a href="#clientpassword" title="ClientPassword">ClientPassword</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#operationmode" title="OperationMode">OperationMode</a>" : <i>String</i>,
        "<a href="#organizationalunitid" title="OrganizationalUnitId">OrganizationalUnitId</a>" : <i>String</i>,
        "<a href="#subscriptionid" title="SubscriptionId">SubscriptionId</a>" : <i>String</i>,
        "<a href="#tenantid" title="TenantId">TenantId</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Dome9::CloudaccountAzure
Properties:
    <a href="#clientid" title="ClientId">ClientId</a>: <i>String</i>
    <a href="#clientpassword" title="ClientPassword">ClientPassword</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#operationmode" title="OperationMode">OperationMode</a>: <i>String</i>
    <a href="#organizationalunitid" title="OrganizationalUnitId">OrganizationalUnitId</a>: <i>String</i>
    <a href="#subscriptionid" title="SubscriptionId">SubscriptionId</a>: <i>String</i>
    <a href="#tenantid" title="TenantId">TenantId</a>: <i>String</i>
</pre>

## Properties

#### ClientId

Azure account id.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientPassword

Password for account*.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Azure account in Dome9.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OperationMode

Dome9 operation mode for the Azure account ("Read-Only" or "Managed").

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrganizationalUnitId

Organizational Unit that this cloud account will be attached to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubscriptionId

The Azure subscription id for account.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantId

The Azure tenant id.

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

