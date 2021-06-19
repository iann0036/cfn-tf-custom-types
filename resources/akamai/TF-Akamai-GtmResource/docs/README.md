# TF::Akamai::GtmResource

The `akamai_gtm_resource` lets you create, configure, and import a GTM resource. In GTM, a resource is anything you can measure whose scarcity affects load balancing. Examples of resources include bandwidth, CPU load average, database queries per second, or disk operations per second. 

~> **Note** Import requires an ID with this format: `existing_domain_name`:
`existing_resource_name`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Akamai::GtmResource",
    "Properties" : {
        "<a href="#aggregationtype" title="AggregationType">AggregationType</a>" : <i>String</i>,
        "<a href="#constrainedproperty" title="ConstrainedProperty">ConstrainedProperty</a>" : <i>String</i>,
        "<a href="#decayrate" title="DecayRate">DecayRate</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#hostheader" title="HostHeader">HostHeader</a>" : <i>String</i>,
        "<a href="#leaderstring" title="LeaderString">LeaderString</a>" : <i>String</i>,
        "<a href="#leastsquaresdecay" title="LeastSquaresDecay">LeastSquaresDecay</a>" : <i>Double</i>,
        "<a href="#loadimbalancepercentage" title="LoadImbalancePercentage">LoadImbalancePercentage</a>" : <i>Double</i>,
        "<a href="#maxumultiplicativeincrement" title="MaxUMultiplicativeIncrement">MaxUMultiplicativeIncrement</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#upperbound" title="UpperBound">UpperBound</a>" : <i>Double</i>,
        "<a href="#waitoncomplete" title="WaitOnComplete">WaitOnComplete</a>" : <i>Boolean</i>,
        "<a href="#resourceinstance" title="ResourceInstance">ResourceInstance</a>" : <i>[ <a href="resourceinstancedefinition.md">ResourceInstanceDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Akamai::GtmResource
Properties:
    <a href="#aggregationtype" title="AggregationType">AggregationType</a>: <i>String</i>
    <a href="#constrainedproperty" title="ConstrainedProperty">ConstrainedProperty</a>: <i>String</i>
    <a href="#decayrate" title="DecayRate">DecayRate</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#hostheader" title="HostHeader">HostHeader</a>: <i>String</i>
    <a href="#leaderstring" title="LeaderString">LeaderString</a>: <i>String</i>
    <a href="#leastsquaresdecay" title="LeastSquaresDecay">LeastSquaresDecay</a>: <i>Double</i>
    <a href="#loadimbalancepercentage" title="LoadImbalancePercentage">LoadImbalancePercentage</a>: <i>Double</i>
    <a href="#maxumultiplicativeincrement" title="MaxUMultiplicativeIncrement">MaxUMultiplicativeIncrement</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#upperbound" title="UpperBound">UpperBound</a>: <i>Double</i>
    <a href="#waitoncomplete" title="WaitOnComplete">WaitOnComplete</a>: <i>Boolean</i>
    <a href="#resourceinstance" title="ResourceInstance">ResourceInstance</a>: <i>
      - <a href="resourceinstancedefinition.md">ResourceInstanceDefinition</a></i>
</pre>

## Properties

#### AggregationType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConstrainedProperty

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DecayRate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostHeader

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LeaderString

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LeastSquaresDecay

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadImbalancePercentage

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxUMultiplicativeIncrement

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpperBound

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitOnComplete

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceInstance

_Required_: No

_Type_: List of <a href="resourceinstancedefinition.md">ResourceInstanceDefinition</a>

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

