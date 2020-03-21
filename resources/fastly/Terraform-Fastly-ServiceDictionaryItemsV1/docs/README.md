# Terraform::Fastly::ServiceDictionaryItemsV1

CloudFormation equivalent of fastly_service_dictionary_items_v1

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Fastly::ServiceDictionaryItemsV1",
    "Properties" : {
        "<a href="#dictionaryid" title="DictionaryId">DictionaryId</a>" : <i>String</i>,
        "<a href="#items" title="Items">Items</a>" : <i>[ <a href="items.md">Items</a>, ... ]</i>,
        "<a href="#serviceid" title="ServiceId">ServiceId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Fastly::ServiceDictionaryItemsV1
Properties:
    <a href="#dictionaryid" title="DictionaryId">DictionaryId</a>: <i>String</i>
    <a href="#items" title="Items">Items</a>: <i>
      - <a href="items.md">Items</a></i>
    <a href="#serviceid" title="ServiceId">ServiceId</a>: <i>String</i>
</pre>

## Properties

#### DictionaryId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Items

_Required_: No

_Type_: List of <a href="items.md">Items</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceId

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

