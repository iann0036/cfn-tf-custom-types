# TF::Dome9::OrganizationalUnit

CloudFormation equivalent of dome9_organizational_unit

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Dome9::OrganizationalUnit",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#parentid" title="ParentId">ParentId</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Dome9::OrganizationalUnit
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#parentid" title="ParentId">ParentId</a>: <i>String</i>
</pre>

## Properties

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParentId

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

#### AccountId

Returns the <code>AccountId</code> value.

#### AwsAggregateCloudAccountsCount

Returns the <code>AwsAggregateCloudAccountsCount</code> value.

#### AwsCloudAccountsCount

Returns the <code>AwsCloudAccountsCount</code> value.

#### AzureAggregateCloudAccountsCount

Returns the <code>AzureAggregateCloudAccountsCount</code> value.

#### AzureCloudAccountsCount

Returns the <code>AzureCloudAccountsCount</code> value.

#### Created

Returns the <code>Created</code> value.

#### GoogleAggregateCloudAccountsCount

Returns the <code>GoogleAggregateCloudAccountsCount</code> value.

#### GoogleCloudAccountsCount

Returns the <code>GoogleCloudAccountsCount</code> value.

#### Id

Returns the <code>Id</code> value.

#### IsParentRoot

Returns the <code>IsParentRoot</code> value.

#### IsRoot

Returns the <code>IsRoot</code> value.

#### Path

Returns the <code>Path</code> value.

#### PathStr

Returns the <code>PathStr</code> value.

#### SubOrganizationalUnitsCount

Returns the <code>SubOrganizationalUnitsCount</code> value.

#### Updated

Returns the <code>Updated</code> value.

