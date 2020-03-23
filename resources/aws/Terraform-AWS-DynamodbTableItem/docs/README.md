# Terraform::AWS::DynamodbTableItem

Provides a DynamoDB table item resource

-> **Note:** This resource is not meant to be used for managing large amounts of data in your table, it is not designed to scale.
  You should perform **regular backups** of all data in the table, see [AWS docs for more](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BackupRestore.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::DynamodbTableItem",
    "Properties" : {
        "<a href="#hashkey" title="HashKey">HashKey</a>" : <i>String</i>,
        "<a href="#item" title="Item">Item</a>" : <i>String</i>,
        "<a href="#rangekey" title="RangeKey">RangeKey</a>" : <i>String</i>,
        "<a href="#tablename" title="TableName">TableName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::DynamodbTableItem
Properties:
    <a href="#hashkey" title="HashKey">HashKey</a>: <i>String</i>
    <a href="#item" title="Item">Item</a>: <i>String</i>
    <a href="#rangekey" title="RangeKey">RangeKey</a>: <i>String</i>
    <a href="#tablename" title="TableName">TableName</a>: <i>String</i>
</pre>

## Properties

#### HashKey

Hash key to use for lookups and identification of the item.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Item

JSON representation of a map of attribute name/value pairs, one for each attribute.
Only the primary key attributes are required; you can optionally provide other attribute name-value pairs for the item.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RangeKey

Range key to use for lookups and identification of the item. Required if there is range key defined in the table.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TableName

The name of the table to contain the item.

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

