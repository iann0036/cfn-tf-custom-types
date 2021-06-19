# TF::SumoLogic::Partition

Provides a [Sumologic Partition][1].

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::SumoLogic::Partition",
    "Properties" : {
        "<a href="#analyticstier" title="AnalyticsTier">AnalyticsTier</a>" : <i>String</i>,
        "<a href="#iscompliant" title="IsCompliant">IsCompliant</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#reduceretentionperiodimmediately" title="ReduceRetentionPeriodImmediately">ReduceRetentionPeriodImmediately</a>" : <i>Boolean</i>,
        "<a href="#retentionperiod" title="RetentionPeriod">RetentionPeriod</a>" : <i>Double</i>,
        "<a href="#routingexpression" title="RoutingExpression">RoutingExpression</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::SumoLogic::Partition
Properties:
    <a href="#analyticstier" title="AnalyticsTier">AnalyticsTier</a>: <i>String</i>
    <a href="#iscompliant" title="IsCompliant">IsCompliant</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#reduceretentionperiodimmediately" title="ReduceRetentionPeriodImmediately">ReduceRetentionPeriodImmediately</a>: <i>Boolean</i>
    <a href="#retentionperiod" title="RetentionPeriod">RetentionPeriod</a>: <i>Double</i>
    <a href="#routingexpression" title="RoutingExpression">RoutingExpression</a>: <i>String</i>
</pre>

## Properties

#### AnalyticsTier

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsCompliant

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReduceRetentionPeriodImmediately

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionPeriod

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoutingExpression

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

#### DataForwardingId

Returns the <code>DataForwardingId</code> value.

#### Id

Returns the <code>Id</code> value.

#### IndexType

Returns the <code>IndexType</code> value.

#### IsActive

Returns the <code>IsActive</code> value.

#### TotalBytes

Returns the <code>TotalBytes</code> value.

