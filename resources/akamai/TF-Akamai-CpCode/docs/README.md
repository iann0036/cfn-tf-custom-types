# TF::Akamai::CpCode

~> **Note** Version 1.0.0 of the Akamai Terraform Provider is now available for the Provisioning module. To upgrade to the new version, you have to update this resource. See the [migration guide](../guides/1.0_migration.md) for details. 

The `akamai_cp_code` resource lets you create or reuse content provider (CP) codes.  CP codes track web traffic handled by Akamai servers. Akamai gives you a CP code when you purchase a product. You need this code when you activate associated properties. 

You can create additional CP codes to support more detailed billing and reporting functions.

By default, the Akamai Provider uses your existing CP code instead of creating a new one.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Akamai::CpCode",
    "Properties" : {
        "<a href="#contract" title="Contract">Contract</a>" : <i>String</i>,
        "<a href="#contractid" title="ContractId">ContractId</a>" : <i>String</i>,
        "<a href="#group" title="Group">Group</a>" : <i>String</i>,
        "<a href="#groupid" title="GroupId">GroupId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#product" title="Product">Product</a>" : <i>String</i>,
        "<a href="#productid" title="ProductId">ProductId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Akamai::CpCode
Properties:
    <a href="#contract" title="Contract">Contract</a>: <i>String</i>
    <a href="#contractid" title="ContractId">ContractId</a>: <i>String</i>
    <a href="#group" title="Group">Group</a>: <i>String</i>
    <a href="#groupid" title="GroupId">GroupId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#product" title="Product">Product</a>: <i>String</i>
    <a href="#productid" title="ProductId">ProductId</a>: <i>String</i>
</pre>

## Properties

#### Contract

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContractId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Group

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Product

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProductId

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

