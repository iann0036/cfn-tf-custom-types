# TF::FortiOS::ReportSetting

Report setting configuration.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::ReportSetting",
    "Properties" : {
        "<a href="#fortiview" title="Fortiview">Fortiview</a>" : <i>String</i>,
        "<a href="#pdfreport" title="PdfReport">PdfReport</a>" : <i>String</i>,
        "<a href="#reportsource" title="ReportSource">ReportSource</a>" : <i>String</i>,
        "<a href="#topn" title="TopN">TopN</a>" : <i>Double</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#webbrowsingthreshold" title="WebBrowsingThreshold">WebBrowsingThreshold</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::ReportSetting
Properties:
    <a href="#fortiview" title="Fortiview">Fortiview</a>: <i>String</i>
    <a href="#pdfreport" title="PdfReport">PdfReport</a>: <i>String</i>
    <a href="#reportsource" title="ReportSource">ReportSource</a>: <i>String</i>
    <a href="#topn" title="TopN">TopN</a>: <i>Double</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#webbrowsingthreshold" title="WebBrowsingThreshold">WebBrowsingThreshold</a>: <i>Double</i>
</pre>

## Properties

#### Fortiview

Enable/disable historical FortiView. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PdfReport

Enable/disable PDF report. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReportSource

Report log source. Valid values: `forward-traffic`, `sniffer-traffic`, `local-deny-traffic`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TopN

Number of items to populate (100 - 4000).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebBrowsingThreshold

Web browsing time calculation threshold (3 - 15 min).

_Required_: No

_Type_: Double

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

