# Terraform::Datadog::LogsIndexOrder

Provides a Datadog [Logs Index API](https://docs.datadoghq.com/api/?lang=python#logs-indexes) resource. This can be used to manage the order of Datadog logs indexes.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Datadog::LogsIndexOrder",
    "Properties" : {
        "<a href="#indexes" title="Indexes">Indexes</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Datadog::LogsIndexOrder
Properties:
    <a href="#indexes" title="Indexes">Indexes</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### Indexes

The index resource list. Logs are tested against the query filter of each index one by one following the order of the list.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The unique name of the index order resource.

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

