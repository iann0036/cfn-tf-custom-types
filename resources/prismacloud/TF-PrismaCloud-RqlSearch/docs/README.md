# TF::PrismaCloud::RqlSearch

Manage a RQL search on the Prisma Cloud Platform.

NOTE:  Prisma Cloud does not currently support deleting RQL searches, so
`terraform destroy` is a noop.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::PrismaCloud::RqlSearch",
    "Properties" : {
        "<a href="#limit" title="Limit">Limit</a>" : <i>Double</i>,
        "<a href="#query" title="Query">Query</a>" : <i>String</i>,
        "<a href="#searchtype" title="SearchType">SearchType</a>" : <i>String</i>,
        "<a href="#timerange" title="TimeRange">TimeRange</a>" : <i>[ <a href="timerangedefinition.md">TimeRangeDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::PrismaCloud::RqlSearch
Properties:
    <a href="#limit" title="Limit">Limit</a>: <i>Double</i>
    <a href="#query" title="Query">Query</a>: <i>String</i>
    <a href="#searchtype" title="SearchType">SearchType</a>: <i>String</i>
    <a href="#timerange" title="TimeRange">TimeRange</a>: <i>
      - <a href="timerangedefinition.md">TimeRangeDefinition</a></i>
</pre>

## Properties

#### Limit

Limit rules (default: `10`).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Query

The RQL query.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SearchType

The search type.  Valid values are `config`
(default) and `event`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeRange

_Required_: No

_Type_: List of <a href="timerangedefinition.md">TimeRangeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CloudType

Returns the <code>CloudType</code> value.

#### ConfigData

Returns the <code>ConfigData</code> value.

#### Description

Returns the <code>Description</code> value.

#### EventData

Returns the <code>EventData</code> value.

#### GroupBy

Returns the <code>GroupBy</code> value.

#### Id

Returns the <code>Id</code> value.

#### Name

Returns the <code>Name</code> value.

#### SearchId

Returns the <code>SearchId</code> value.

