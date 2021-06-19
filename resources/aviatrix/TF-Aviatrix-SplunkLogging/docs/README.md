# TF::Aviatrix::SplunkLogging

The **aviatrix_splunk_logging** resource allows the enabling and disabling of splunk logging.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::SplunkLogging",
    "Properties" : {
        "<a href="#custominputconfig" title="CustomInputConfig">CustomInputConfig</a>" : <i>String</i>,
        "<a href="#customoutputconfigfile" title="CustomOutputConfigFile">CustomOutputConfigFile</a>" : <i>String</i>,
        "<a href="#excludedgateways" title="ExcludedGateways">ExcludedGateways</a>" : <i>[ String, ... ]</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#server" title="Server">Server</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::SplunkLogging
Properties:
    <a href="#custominputconfig" title="CustomInputConfig">CustomInputConfig</a>: <i>String</i>
    <a href="#customoutputconfigfile" title="CustomOutputConfigFile">CustomOutputConfigFile</a>: <i>String</i>
    <a href="#excludedgateways" title="ExcludedGateways">ExcludedGateways</a>: <i>
      - String</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#server" title="Server">Server</a>: <i>String</i>
</pre>

## Properties

#### CustomInputConfig

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomOutputConfigFile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludedGateways

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Server

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

