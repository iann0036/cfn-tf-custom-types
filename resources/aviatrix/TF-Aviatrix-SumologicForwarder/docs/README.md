# TF::Aviatrix::SumologicForwarder

The **aviatrix_sumologic_forwarder** resource allows the enabling and disabling of sumologic forwarder.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::SumologicForwarder",
    "Properties" : {
        "<a href="#accessid" title="AccessId">AccessId</a>" : <i>String</i>,
        "<a href="#accesskey" title="AccessKey">AccessKey</a>" : <i>String</i>,
        "<a href="#customconfiguration" title="CustomConfiguration">CustomConfiguration</a>" : <i>String</i>,
        "<a href="#excludedgateways" title="ExcludedGateways">ExcludedGateways</a>" : <i>[ String, ... ]</i>,
        "<a href="#sourcecategory" title="SourceCategory">SourceCategory</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::SumologicForwarder
Properties:
    <a href="#accessid" title="AccessId">AccessId</a>: <i>String</i>
    <a href="#accesskey" title="AccessKey">AccessKey</a>: <i>String</i>
    <a href="#customconfiguration" title="CustomConfiguration">CustomConfiguration</a>: <i>String</i>
    <a href="#excludedgateways" title="ExcludedGateways">ExcludedGateways</a>: <i>
      - String</i>
    <a href="#sourcecategory" title="SourceCategory">SourceCategory</a>: <i>String</i>
</pre>

## Properties

#### AccessId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessKey

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomConfiguration

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludedGateways

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceCategory

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

#### Status

Returns the <code>Status</code> value.

